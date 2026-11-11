# Canonical pack controls

Use these controls for visual blueprints after direction selection. Keep actual image generation and complete view/journey coverage from visual-design.md. Scale the records to the project; these controls do not prescribe an aesthetic or an image quota.

## Preserve shared layouts

Before expansion, identify the shared application shells and components exposed by the confirmed anchor: header, navigation, content origin/width, typography, controls and responsive behavior. Give each shell a stable ID and revision, an actual reference and a short geometry/token contract. Different roles and breakpoints may intentionally use different shells.

Bind each screen/state to its shell revision. Generate with the actual anchor and relevant shared references. Compare related variants side by side at the same logical width: normal versus empty/loading/error, current versus terminal, and form versus dialog. State changes update the content or component concerned while retaining the surrounding shell. Record the comparison against the exact image hash. A changed header, sidebar, content origin or control treatment is an unresolved mismatch until corrected or explicitly accepted as a named deviation. Material shell changes produce a new revision, identify affected references and receive review; earlier approvals remain attached to their original artifacts.

Inspect content and layout together. A corrected label that introduces a different shell or removes required fields is still a failed revision. Keep the last valid reference current until the replacement passes inspection; preserve failed attempts as superseded history. A shared-state assembly names actual source components, exact geometry/copy/control deltas and its target shell. It cannot supply an unpictured distinct role layout or journey outcome.

## Make screenshot comparison reproducible

Prefer generation of app UI without decorative browser/device framing. Inspect every image individually, including replacements. Record:

- Actual source pixel dimensions and SHA-256.
- App rectangle `[x,y,width,height]` in source pixels, excluded framing insets `[left,top,right,bottom]`, and framing kind. Visible browser bars, native status bars, device borders and surrounding presentation canvas are framing; product headers remain app UI.
- Logical browser viewport `[width,height]` in CSS pixels, logical app-content dimensions, and capture mode `viewport` or `full-page`.
- One uniform source-to-CSS scale. Both dimensions must map to the logical app-content size. For a viewport capture the content size equals the viewport; a full-page capture records the browser viewport separately from the longer document.
- Device pixel ratio when known from a real capture. Use null for a synthetic image with unknown DPR; an inferred image scale is not a measured device DPR.
- Framing inspection evidence tied to this exact image hash, including why a full-canvas rectangle is correct when no framing is present.

Use per-image bounds, not one assumed crop for every phone/tablet image. A visible native status bar cannot coexist with a claim of no framing/full-canvas app bounds. Verify the crop visually without altering the source. Record the mapping so the builder can capture the same app region/content/viewport without stretching or including OS chrome.

Derive tokens from the inspected design. If exact font/geometry values require interpretation, show an inspectable resolved layout at the target viewport and obtain disposition of the visible difference. Update affected canonical references or a precisely scoped, reviewed layout assembly. A prose authority order cannot make contradictory images and values agree. Pixel bounds alone do not prove typography, color, spacing or behavior parity.

## Keep one durable pack record

Maintain `pack-state.json` in the project as the current source for reference selection, hashes, shells, reviews, decisions, dependencies and work queue. Start from [the record template](../assets/pack-state.template.json), replacing its illustrative paths/values with actual artifacts. Use project-relative artifact/evidence paths. Update it after every inspected batch and owner decision, before launching the next expensive batch. A record may be incomplete while work continues; the checkpoint must accurately expose those gaps. This makes interruption recovery possible without a last-minute audit rewrite.

The record has `revision`, `phase` (`shaping`, `review`, `confirmed`), `required_views`, `shells`, `references`, `decisions`, `queue` and `reviews`. Each reference has `id`, `view_id`, `artifact`, `sha256`, `status` (`proposed`, `confirmed`, `superseded`), `shell_id`, `shell_revision`, `capture`, `inspection` and, when confirmed, `approval`. Record role/state/viewport distinctions in the IDs and screen contracts. Each shell record has `id`, `revision`, `reference_id`, `contract` and `contract_sha256`. Shell comparison evidence belongs in the reference inspection.

`capture` fields are `source_px`, `app_rect_px`, `excluded_insets_px`, `framing` (`none`, `browser`, `os`, `device`, `mixed`), `viewport_css`, `content_css`, `scale_css_per_source_px`, `device_pixel_ratio` and `mode`. `inspection` records the artifact `sha256`, evidence path, `content`, `framing` and `shell` results (`pass`, `fail`, `pending`). An accepted shell deviation additionally names its decision ID. `approval` records the artifact `sha256` and actual owner evidence path. Replacing an image invalidates its inspection/approval until reviewed again.

`reviews` contains `coverage`, `consistency`, `tokens` and `assemblies`, each with result (`pass`, `fail`, `pending`) and an evidence path. A passing review includes the current `design_digest`; obtain it with the checker's `--print-design-digest` option only after reviewing that exact design. Changed images, capture mappings or shell contracts invalidate older passing reviews. Coverage evidence includes the independent navigation/journey walk, not just manifest totals. Consistency evidence records shell comparisons and reconciled contracts. Tokens and assemblies additionally need `approval_evidence` for the confirmed phase; their approval scope is separate from image approval. `decisions` record ID, category (`design`, `execution`), status (`pending`, `confirmed`, `rejected`) and evidence. Queue items record ID, category and status (`open`, `blocked`, `done`); blocked items identify reason, resolver and affected work. Later setup/access dependencies can remain blocked while the design is confirmed; unfinished design work keeps it unready. Resource register authorization/configuration/verification remains separate.

Run the bundled checker with the pack record:

    python3 <skill-directory>/scripts/check_pack.py <project>/pack-state.json --checkpoint <project>/CHECKPOINT.md

It checks artifact hashes/dimensions, coordinate mappings, reference/shell bindings, review evidence and confirmation invariants, and writes a checkpoint from that same record even when validation fails. It reads PNG dimensions directly; other raster formats require Pillow in the host environment. A failing result is work to resolve or explicitly checkpoint. The checker does not inspect pixels, authenticate owner evidence, infer omitted journeys or certify aesthetics. Actual visual/semantic review remains required.

## Refresh together, then reconcile before handoff

Use `sync_handoff.py` for visual-pack progress, not the optional checkpoint-only checker command. Immediately after recording each inspected batch, owner decision, changed contract or blocker, run:

    python3 <skill-directory>/scripts/sync_handoff.py <project>/pack-state.json

Run this before the next expensive batch, before asking for review, and before yielding or resuming after interruption. It generates CHECKPOINT.md and AUDIT.md, refreshes managed status blocks in the entry/handoff/index/approval summaries, and snapshots the current document hashes. Validation failures still produce a truthful partial checkpoint. It preserves substantive document bodies and review evidence, archiving an existing authored AUDIT.md under audit-history/ on first adoption; refresh is not an audit approval. Keep enough execution budget for this inexpensive refresh. After an interruption, refresh before further generation.

### Declare the handoff surface

The record's `handoff` object has an `entry`, `summaries` and `documents`. `summaries` lists every current Markdown document carrying progress/readiness claims, including the entry, handoff, gallery's Markdown index and approval ledger when present. `documents` includes those summaries plus all specification/research/resource/decision/contract/traceability and supporting review documents a fresh builder relies on. Use actual project-relative paths, remove unused template examples, and add new relied-on documents as they are created. HTML galleries belong in `documents`; link the current Markdown index/status rather than duplicating hand-written progress counts inside HTML. CHECKPOINT.md, AUDIT.md and handoff-snapshot.json are generated and excluded from these lists.

Managed status blocks carry current progress. Keep the surrounding narrative about stable requirements and rationale; replace obsolete next steps and approval/readiness statements rather than retaining competing current claims. The script preserves narrative so a substantive reconciliation is still necessary.

### Bind substantive reconciliation to the actual specification

Before any final handoff, independently walk the requested scope and journeys against the actual artifacts using handoff.md. Reconcile every declared document: entry status, selected anchor, current image set, approval scope, resources/access, contracts, QA claims, reading order, next milestone and remaining work. Write the actual findings, reviewed documents and readiness rationale to a separate AUDIT-REVIEW.md (or equivalent). This is an agent's fresh review pass; it does not require another agent or imply owner confirmation. Return unblocked gaps to the queue and resolve them first. A blocked partial handoff still needs an accurate current review.

After reviewing the exact current contents, obtain the review target:

    python3 <skill-directory>/scripts/sync_handoff.py <project>/pack-state.json --print-context-digest

Set `handoff_review` to `result: pass`, that `context_digest`, the project-relative review `evidence` path and its actual `evidence_sha256`. Pass means the handoff accurately represents current work, including any blockers; it does not promote design phase or approve images. The evidence file is separate from `handoff.documents` and generated outputs, avoiding a circular digest. Then refresh and run the read-only final gate:

    python3 <skill-directory>/scripts/sync_handoff.py <project>/pack-state.json
    python3 <skill-directory>/scripts/sync_handoff.py <project>/pack-state.json --check

Add `--require-confirmed` to the final check when claiming the canonical design is confirmed. A successful partial-handoff check only establishes current reconciliation, not design completion. Changed record fields or document bodies invalidate the review; changed generated summaries, evidence or snapshots fail freshness checks. Re-review affected material, update evidence and digest, then refresh. Never copy the new digest into an old review without reviewing the changes.

The final gate checks hashes and freshness, not whether prose is true or the declared document list is exhaustive. Inspect meaning and links during reconciliation. Report the gate result together with phase and unresolved dependencies. Mechanical PASS in shaping is still partial.

A completed proposed pack can enter review with pending screen/token/assembly approvals, explicitly labeled. A confirmed design requires all current references and required interpretation reviews confirmed, resolved visual/behavior contradictions, and no open independent design work. Service access may still block later execution. Implementation parity additionally requires actual implementation screenshots and behavioral evidence; `phase: confirmed` never asserts implementation.

Preflight an approved rendering route before committing to resolved token/layout assemblies. If unavailable, record the capability, resolver and affected reviews in resources and queue while continuing independent design. Preserve exact proposed work and outstanding review scope; unseen composites remain unconfirmed.
