#!/usr/bin/env python3
"""Check canonical-pack integrity and emit a resumable checkpoint, not visual QA."""
import argparse
import hashlib
import json
import math
from pathlib import Path
import struct
import sys


def digest(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(',', ':')).encode()).hexdigest()


def design_digest(pack):
    keys = ('id', 'view_id', 'sha256', 'shell_id', 'shell_revision', 'capture')
    refs = [{k: r.get(k) for k in keys} for r in pack.get('references', [])
            if r.get('status') != 'superseded']
    return digest({'required_views': pack.get('required_views'),
                   'shells': pack.get('shells'), 'references': refs})


def image_size(path):
    with path.open('rb') as stream:
        head = stream.read(24)
    if head[:8] == b'\x89PNG\r\n\x1a\n' and head[12:16] == b'IHDR':
        return list(struct.unpack('>II', head[16:24]))
    try:
        from PIL import Image
        with Image.open(path) as im:
            return list(im.size)
    except ImportError as exc:
        raise ValueError('non-PNG format needs Pillow for dimension verification') from exc


def validate(pack, root):
    errors = []

    def need(ok, message):
        if not ok:
            errors.append(message)
        return bool(ok)

    def local_file(value, label):
        if not need(isinstance(value, str) and bool(value), label + ': missing relative path'):
            return None
        path = Path(value)
        resolved = (root / path).resolve()
        if not need(not path.is_absolute() and resolved.is_relative_to(root), label + ': path must stay inside project'):
            return None
        return resolved if need(resolved.is_file(), label + ': file missing: ' + value) else None

    def numbers(value, size, positive=False):
        return (isinstance(value, list) and len(value) == size
                and all(type(n) in (int, float) and math.isfinite(n)
                        and (n > 0 if positive else n >= 0) for n in value))

    for key in ('revision', 'phase', 'required_views', 'shells', 'references', 'decisions', 'queue', 'reviews'):
        need(key in pack, 'durable record missing: ' + key)
    need(isinstance(pack.get('revision'), str) and bool(pack['revision']), 'pack revision required')
    phase = pack.get('phase')
    need(phase in ('shaping', 'review', 'confirmed'), 'invalid phase')
    refs = pack.get('references', [])
    need(isinstance(refs, list) and bool(refs), 'references must be a nonempty list')
    if not isinstance(refs, list):
        return errors
    refs = [r for r in refs if need(isinstance(r, dict), 'reference must be an object')]
    ids = [r.get('id') for r in refs]
    need(all(isinstance(i, str) and i for i in ids) and len(set(ids)) == len(ids), 'reference IDs must be present and unique')
    current = [r for r in refs if r.get('status') != 'superseded']
    files = [r.get('artifact') for r in current]
    need(all(isinstance(f, str) for f in files) and len(set(files)) == len(files), 'current artifact files must be unique')
    required = pack.get('required_views')
    if need(isinstance(required, list) and bool(required) and all(isinstance(v, str) for v in required), 'required_views must list independently inventoried view/role/state IDs'):
        covered = {r.get('view_id') for r in current}
        for view in required:
            need(view in covered, 'uncovered required view: ' + view)
    shells = pack.get('shells', [])
    if not isinstance(shells, list):
        errors.append('shells must be a list')
        shells = []
    by_shell = {}
    for shell in shells:
        key = (shell.get('id'), shell.get('revision'))
        need(all(isinstance(v, str) and v for v in key) and key not in by_shell, 'shell ID/revision missing or duplicated')
        by_shell[key] = shell
        need(shell.get('reference_id') in [r.get('id') for r in current], 'shell anchor must be a current reference')
        contract = local_file(shell.get('contract'), 'shell contract')
        need(contract is not None and shell.get('contract_sha256') == hashlib.sha256(contract.read_bytes()).hexdigest(), 'shell contract hash mismatch')
    for ref in current:
        label = str(ref.get('id'))
        need(ref.get('status') in ('proposed', 'confirmed'), label + ': invalid current status')
        artifact = local_file(ref.get('artifact'), label)
        actual_hash = hashlib.sha256(artifact.read_bytes()).hexdigest() if artifact else None
        need(actual_hash is not None and ref.get('sha256') == actual_hash, label + ': artifact hash mismatch')
        capture = ref.get('capture', {})
        source = capture.get('source_px')
        rect = capture.get('app_rect_px')
        insets = capture.get('excluded_insets_px')
        viewport = capture.get('viewport_css')
        content = capture.get('content_css')
        scale = capture.get('scale_css_per_source_px')
        if artifact:
            try:
                need(source == image_size(artifact), label + ': source dimensions mismatch')
            except (ValueError, OSError) as exc:
                errors.append(label + ': ' + str(exc))
        shape_ok = numbers(source, 2, True) and numbers(rect, 4) and numbers(insets, 4)
        if need(shape_ok, label + ': source/rectangle/insets invalid'):
            x, y, w, h = rect
            left, top, right, bottom = insets
            need(w > 0 and h > 0 and x + w <= source[0] and y + h <= source[1], label + ': app rectangle out of bounds')
            need(rect == [left, top, source[0] - left - right, source[1] - top - bottom], label + ': crop and excluded framing disagree')
            framing = capture.get('framing')
            need(framing in ('none', 'browser', 'os', 'device', 'mixed'), label + ': invalid framing kind')
            need((framing == 'none' and sum(insets) == 0) or (framing != 'none' and sum(insets) > 0), label + ': framing kind contradicts full-canvas app bounds')
        mapping_ok = (numbers(viewport, 2, True) and numbers(content, 2, True)
                      and type(scale) in (int, float) and math.isfinite(scale) and scale > 0)
        if need(mapping_ok, label + ': logical viewport/content/uniform scale required') and shape_ok:
            need(all(math.isclose(rect[i + 2] * scale, content[i], abs_tol=0.05) for i in range(2)), label + ': source-to-CSS mapping stretches or disagrees with content dimensions')
            mode = capture.get('mode')
            need(mode in ('viewport', 'full-page'), label + ': invalid capture mode')
            need(math.isclose(content[0], viewport[0], abs_tol=0.05), label + ': content width differs from viewport')
            need((mode == 'viewport' and math.isclose(content[1], viewport[1], abs_tol=0.05))
                 or (mode == 'full-page' and content[1] >= viewport[1]), label + ': capture mode/content height disagree')
        need('device_pixel_ratio' in capture, label + ': declare known DPR or null')
        dpr = capture.get('device_pixel_ratio')
        need(dpr is None or (type(dpr) in (int, float) and math.isfinite(dpr) and dpr > 0), label + ': invalid DPR')
        need((ref.get('shell_id'), ref.get('shell_revision')) in by_shell, label + ': unknown shell revision')
        inspection = ref.get('inspection', {})
        need(actual_hash is not None and inspection.get('sha256') == actual_hash, label + ': inspection is stale or absent')
        local_file(inspection.get('evidence'), label + ' inspection')
        for check in ('content', 'framing', 'shell'):
            need(inspection.get(check) == 'pass', label + ': unresolved ' + check + ' inspection')
        if ref.get('status') == 'confirmed':
            approval = ref.get('approval', {})
            need(actual_hash is not None and approval.get('sha256') == actual_hash, label + ': approval is stale or absent')
            local_file(approval.get('evidence'), label + ' approval')
        if phase == 'confirmed':
            need(ref.get('status') == 'confirmed', label + ': proposed reference prevents confirmed phase')
    decisions = pack.get('decisions', [])
    queue = pack.get('queue', [])
    need(isinstance(decisions, list) and isinstance(queue, list), 'decisions and queue must be lists')
    for item in decisions if isinstance(decisions, list) else []:
        need(item.get('status') in ('pending', 'confirmed', 'rejected'), 'invalid decision status')
        need(item.get('category') in ('design', 'execution'), 'decision needs design/execution category')
        if item.get('status') != 'pending':
            local_file(item.get('evidence'), 'decision evidence')
        if phase == 'confirmed' and item.get('category') != 'execution':
            need(item.get('status') != 'pending', 'pending design decision prevents confirmed phase')
    for item in queue if isinstance(queue, list) else []:
        need(item.get('status') in ('open', 'blocked', 'done'), 'invalid queue status')
        need(item.get('category') in ('design', 'execution'), 'queue item needs design/execution category')
        if item.get('status') == 'blocked':
            need(all(item.get(k) for k in ('reason', 'resolver', 'affected')), 'blocked queue item needs reason/resolver/affected work')
        if phase == 'confirmed' and item.get('category') == 'design':
            need(item.get('status') == 'done', 'unfinished design queue prevents confirmed phase')
    reviews = pack.get('reviews', {})
    for name in ('coverage', 'consistency', 'tokens', 'assemblies'):
        review = reviews.get(name, {})
        result = review.get('result')
        need(result in ('pass', 'fail', 'pending'), name + ': review result required')
        if result == 'pass':
            local_file(review.get('evidence'), name + ' review')
            need(review.get('design_digest') == design_digest(pack), name + ': review refers to an older design')
        if phase == 'review' and name in ('coverage', 'consistency'):
            need(result == 'pass', name + ': incomplete proposed pack cannot enter review')
        if phase == 'confirmed':
            need(result == 'pass', name + ': unresolved review prevents confirmed phase')
            if name in ('tokens', 'assemblies'):
                local_file(review.get('approval_evidence'), name + ' owner approval')
    return errors


def checkpoint(pack, errors):
    refs = [r for r in pack.get('references', []) if r.get('status') != 'superseded']
    confirmed = sum(r.get('status') == 'confirmed' for r in refs)
    lines = ['# Current Blueprint checkpoint', '', 'Generated from pack-state.json; regenerate after changes.', '',
             'Pack revision: ' + str(pack.get('revision')), 'Record SHA-256: ' + digest(pack),
             'Design digest: ' + design_digest(pack), 'Declared phase: ' + str(pack.get('phase')), '',
             f'Current references: {len(refs)}; confirmed: {confirmed}; proposed: {len(refs) - confirmed}.',
             'Mechanical validation: ' + ('PASS' if not errors else 'FAIL'),
             'This check does not certify visual quality, owner authorization or implemented parity.', '', '## Outstanding work', '']
    for item in pack.get('queue', []):
        if item.get('status') != 'done':
            lines.append('- ' + json.dumps(item, ensure_ascii=False))
    for item in pack.get('decisions', []):
        if item.get('status') == 'pending':
            lines.append('- Pending decision: ' + json.dumps(item, ensure_ascii=False))
    for name, review in pack.get('reviews', {}).items():
        if review.get('result') != 'pass':
            lines.append('- Review ' + name + ': ' + str(review.get('result')))
    lines += ['', '## Validation findings', ''] + ['- ' + e for e in errors]
    if not errors:
        lines.append('No mechanical findings. Complete the independent visual/journey and summary-reconciliation reviews before readiness.')
    return '\n'.join(lines) + '\n'


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('state', type=Path)
    parser.add_argument('--checkpoint', type=Path)
    parser.add_argument('--print-design-digest', action='store_true')
    args = parser.parse_args()
    try:
        pack = json.loads(args.state.read_text())
        if not isinstance(pack, dict):
            raise ValueError('pack must be a JSON object')
        if args.print_design_digest:
            print(design_digest(pack))
            return 0
        errors = validate(pack, args.state.resolve().parent)
        if args.checkpoint:
            destination = args.checkpoint.resolve()
            root = args.state.resolve().parent
            if not destination.is_relative_to(root) or destination == args.state.resolve():
                raise ValueError('checkpoint must be a different file inside the project')
            destination.write_text(checkpoint(pack, errors))
        print(json.dumps({'ok': not errors, 'revision': pack.get('revision'),
                          'record_digest': digest(pack), 'design_digest': design_digest(pack),
                          'errors': errors}, indent=2))
        return 1 if errors else 0
    except (OSError, ValueError, TypeError, KeyError, AttributeError, struct.error) as exc:
        print(json.dumps({'ok': False, 'errors': ['Invalid pack: ' + str(exc)]}))
        return 1


if __name__ == '__main__':
    sys.exit(main())
