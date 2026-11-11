#!/usr/bin/env python3
"""Refresh or verify pack-derived handoff summaries; never manufacture semantic approval."""
import argparse
import hashlib
import json
import os
from pathlib import Path
import sys

from check_pack import checkpoint, digest, validate

START = '<!-- blueprint:status:start -->'
END = '<!-- blueprint:status:end -->'
RESERVED = {'pack-state.json', 'CHECKPOINT.md', 'AUDIT.md', 'handoff-snapshot.json'}


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def local(root, name):
    if not isinstance(name, str) or not name:
        raise ValueError('handoff paths must be nonempty project-relative strings')
    path = (root / name).resolve()
    if Path(name).is_absolute() or not path.is_relative_to(root):
        raise ValueError('handoff path escapes project: ' + name)
    return path


def body(text):
    if START not in text and END not in text:
        return text
    if text.count(START) != 1 or text.count(END) != 1:
        raise ValueError('status markers must occur exactly once')
    before, rest = text.split(START)
    _, after = rest.split(END)
    return before + after


def context(pack, root):
    config = pack.get('handoff', {})
    documents = config.get('documents', [])
    summaries = config.get('summaries', [])
    entry = config.get('entry')
    if not documents or len(set(documents)) != len(documents):
        raise ValueError('handoff.documents must list unique specification/evidence documents')
    if not summaries or len(set(summaries)) != len(summaries) or entry not in summaries:
        raise ValueError('handoff.summaries must include the entry and every current status-bearing summary')
    if not set(summaries).issubset(documents):
        raise ValueError('handoff summaries must also be documents')
    contents = {}
    for name in documents:
        path = local(root, name)
        if path.name in RESERVED or not path.is_file():
            raise ValueError('missing or reserved handoff document: ' + name)
        contents[name] = hashlib.sha256(body(path.read_text()).lstrip('\n').encode()).hexdigest() if name in summaries else sha(path)
    # Review result itself is excluded so recording the review cannot invalidate its target.
    state = {k: v for k, v in pack.items() if k != 'handoff_review'}
    return digest({'pack': state, 'documents': contents})


def review_errors(pack, root, target):
    review = pack.get('handoff_review', {})
    errors = []
    if review.get('result') != 'pass':
        errors.append('independent handoff reconciliation pending or failed')
    if review.get('context_digest') != target:
        errors.append('handoff review is stale for current specification/record')
    try:
        evidence = local(root, review.get('evidence'))
        if not evidence.is_file() or review.get('evidence_sha256') != sha(evidence):
            errors.append('handoff review evidence missing or changed')
        if review.get('evidence') in pack.get('handoff', {}).get('documents', []) or review.get('evidence') in RESERVED:
            errors.append('handoff review evidence must be separate from generated summaries and reviewed documents')
    except ValueError as exc:
        errors.append(str(exc))
    return errors


def status(pack, errors, reconciled):
    if errors:
        return 'Partial — mechanical findings remain'
    if not reconciled:
        return 'Partial — current handoff reconciliation required'
    if pack.get('phase') != 'confirmed':
        return 'Partial — design review or design work remains'
    return 'Design confirmed — check milestone-specific execution dependencies; implementation parity is separate'


def outputs(pack, errors, reconciled):
    state = status(pack, errors, reconciled)
    block = '\n'.join([START, '## Current delivery status', '',
        'Pack revision: ' + str(pack.get('revision')), 'Record SHA-256: ' + digest(pack),
        'Status: ' + state, '',
        'Current work, decisions and review results: [checkpoint](CHECKPOINT.md).',
        'Current audit and reconciliation evidence: [audit](AUDIT.md).',
        'This generated status is authoritative for progress. Historical narrative is not a readiness claim.', END])
    review = pack.get('handoff_review', {})
    audit = ['<!-- blueprint:generated-audit -->', '# Current Blueprint audit', '', 'Generated from the current pack; substantive review remains separate.', '',
        'Pack revision: ' + str(pack.get('revision')), 'Record SHA-256: ' + digest(pack),
        'Status: ' + state, '', '## Independent reconciliation', '',
        'Result: ' + ('PASS for current context' if reconciled else 'PENDING / STALE / FAILED')]
    if review.get('evidence'):
        audit.append('Review evidence: [' + str(review['evidence']) + '](' + str(review['evidence']) + ')')
    audit += ['', 'The reviewer must reconcile scope, journeys, resources, contracts, visuals, approvals, reading order and next milestone against actual artifacts. Refreshing this file does not perform that review.', '',
              '## Current record findings', '', checkpoint(pack, errors)]
    return block, '\n'.join(audit) + '\n'


def run(state, check=False, require_confirmed=False, print_context=False):
    root = state.resolve().parent
    pack = json.loads(state.read_text())
    if not isinstance(pack, dict) or state.name != 'pack-state.json':
        raise ValueError('use the project pack-state.json object')
    target = context(pack, root)
    if print_context:
        return {'context_digest': target}, 0
    mechanical = validate(pack, root)
    reconciliation = review_errors(pack, root, target)
    block, audit = outputs(pack, mechanical, not reconciliation)
    expected = {'CHECKPOINT.md': checkpoint(pack, mechanical), 'AUDIT.md': audit}
    for name in pack['handoff']['summaries']:
        path = local(root, name)
        if path.suffix.lower() != '.md':
            raise ValueError('status-bearing summaries must be Markdown; list HTML galleries under documents and link a Markdown status index')
        text = path.read_text()
        # Place first, so an interrupted run leaves the latest machine status prominent.
        scoped = block.replace('(CHECKPOINT.md)', '(' + os.path.relpath(root / 'CHECKPOINT.md', path.parent) + ')').replace('(AUDIT.md)', '(' + os.path.relpath(root / 'AUDIT.md', path.parent) + ')')
        expected[name] = scoped + '\n' + body(text).lstrip('\n')
    errors = list(mechanical)
    if check:
        for name, content in expected.items():
            if not local(root, name).is_file() or local(root, name).read_text() != content:
                errors.append('stale generated summary: ' + name)
    else:
        # Preserve an existing authored audit when adopting generated summaries.
        old_audit = root / 'AUDIT.md'
        if old_audit.is_file() and '<!-- blueprint:generated-audit -->' not in old_audit.read_text():
            history = local(root, 'audit-history/' + sha(old_audit) + '.md')
            history.parent.mkdir(parents=True, exist_ok=True)
            if not history.exists():
                history.write_bytes(old_audit.read_bytes())
        # Compute all outputs before mutation. Never rewrite substantive review or specification bodies.
        for name, content in expected.items():
            path = local(root, name)
            temp = path.with_name(path.name + '.blueprint-tmp')
            temp.write_text(content)
            temp.replace(path)
    tracked = set(pack['handoff']['documents']) | set(expected) | {'pack-state.json'}
    evidence = pack.get('handoff_review', {}).get('evidence')
    if evidence:
        evidence_path = local(root, evidence)
        if evidence_path.is_file():
            tracked.add(evidence)
    snapshot = {'record_digest': digest(pack), 'context_digest': target,
                'files': {name: sha(local(root, name)) for name in sorted(tracked)}}
    snap_path = root / 'handoff-snapshot.json'
    if check:
        if not snap_path.is_file() or json.loads(snap_path.read_text()) != snapshot:
            errors.append('handoff snapshot missing or stale')
        errors += reconciliation
        if require_confirmed and pack.get('phase') != 'confirmed':
            errors.append('confirmed design required; partial handoff cannot satisfy readiness')
    else:
        snap_path.write_text(json.dumps(snapshot, indent=2) + '\n')
    return {'ok': not errors, 'mode': 'check' if check else 'refresh',
            'status': status(pack, mechanical, not reconciliation),
            'revision': pack.get('revision'), 'context_digest': target,
            'errors': errors, 'reconciliation_findings': reconciliation}, int(bool(errors))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('state', type=Path)
    parser.add_argument('--check', action='store_true', help='read-only freshness and independent reconciliation gate')
    parser.add_argument('--require-confirmed', action='store_true', help='also require confirmed design readiness')
    parser.add_argument('--print-context-digest', action='store_true')
    args = parser.parse_args()
    try:
        if args.require_confirmed and not args.check:
            raise ValueError('--require-confirmed requires --check')
        result, code = run(args.state, args.check, args.require_confirmed, args.print_context_digest)
    except (OSError, ValueError, TypeError, KeyError, AttributeError) as exc:
        result, code = {'ok': False, 'errors': [str(exc)]}, 1
    print(json.dumps(result, indent=2))
    return code


if __name__ == '__main__':
    sys.exit(main())
