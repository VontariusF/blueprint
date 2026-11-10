# Visual and interaction specification

Map users, entry points, goals, decisions, actions, handoffs and success/failure before choosing effects. Honor existing design systems unless the user requests change. Profiles supply provisional defaults rather than a mandatory aesthetic.

## Coverage before rendering

Create a view inventory from both navigation and user journeys. Assign a stable ID to each tab/subtab, selected content panel, materially distinct role view, create/edit form, dialog, journey step and consequential outcome. Include persona, entry point, required data, permissions, actions, outcome, recovery and applicable responsive variants. One parent page cannot conceal its Files/People/Settings tabs. A confirmation dialog does not cover its resulting success or closed view.

Walk each in-scope journey from entry through input, action, handoff and result. Examine every visible navigation destination and control that opens a distinct view. Cross-check this walk against the inventory so omissions cannot disappear merely because the inventory is internally valid. Include loading, empty/no matches, validation, denied/expired access, offline, stale data, conflict, partial/unknown outcomes, cancellation and success where applicable. Inventory only meaningful combinations; avoid a mechanical Cartesian product of unrelated states and viewports.

Mark exclusions with rationale and obtain user disposition for exclusions affecting core journeys, consequential states or required responsive variants. Scale depth to actual scope, never to an arbitrary page or image quota. Maintain an explicit unblocked generation queue and a separate list of branches waiting for consequential decisions.

## Establish direction before full mockup expansion

Discuss the visual brief before generating concepts. Reuse known answers and ask about remaining consequential choices: existing branding/design systems, audience, reference examples, desired mood, information density, typography/color preferences, platform and treatments to avoid. Profiles and reusable styles are starting proposals unless already confirmed for this project. A detailed user brief can settle these questions without another intake round.

When the direction remains unresolved, use actual image generation to produce a small comparison set, usually three materially different concepts. Depict the same representative product screen with the same requirements, realistic content, state and viewport so the user can compare design rather than different features. Choose a screen that exposes the product's core components. Explore meaningful differences in layout, typography, palette, density and component treatment within the agreed brief; minor recolors alone do not establish distinct concepts. Inspect the images before presenting them, with stable candidate IDs/revisions and a short explanation of each direction.

Present the actual variations and invite the user to select one, combine specified elements, request refinements, reject them all or suggest a different direction. Iterate on that feedback rather than treating the first set as the only choices. Refine a selected or combined direction into an actual primary-screen anchor and concrete visual tokens. Material changes to the chosen image require review of the revised anchor; an unchanged, already accepted candidate needs no repeated approval. Reuse an existing confirmed project direction/reference without forcing new alternatives, and record its evidence.

Full mockup expansion waits for confirmation of the actual anchor and its visual direction. While that decision is pending, continue independent research, resource/access planning, view inventory, journeys and functional contracts. A concept-review checkpoint names the actual candidates, pending choice, affected visual work and independent work completed; the incomplete full mockup set is not presented as a finished design.

Record the brief, candidate artifacts/revisions, feedback, selected anchor, confirmed tokens and decision evidence in the blueprint or design index. Direction approval establishes the visual foundation only; later screens and states retain their own review status. If the direction changes later, identify affected references and regenerate/review those rather than silently mixing styles or transferring old approvals.

## Generate the visual specification

After the direction gate above is resolved, use the available image-generation tool to create high-fidelity product mockups, following its instructions. This is an actual generation step, not a suggestion in the final document. Use the confirmed anchor and tokens as references for consistent screen-specific generations, preserving the selected direction across the full set. Produce fresh, large, readable screen, state and responsive images wherever a compressed overview cannot specify the interface. Detail key tables, forms, dialogs and inspectors separately when needed. Realistic synthetic content must exercise the requirements. Avoid invented capabilities or claims; reconcile any generated extras explicitly.

Apply [canonical pack controls](canonical-pack.md) before generating the remaining views. Establish shared shell/component references from the anchor and compare each related state against them. Record verified framing, app bounds, logical viewport and mapping for every current image. These controls keep empty/error/outcome variants in the same application and make the eventual screenshot comparison reproducible.

Every distinct tab, journey view, form, role layout and consequential decision/outcome requires an actual readable mockup. Show each tab's selected contents, not merely its label. Generate required responsive compositions when their structure changes. Cover each applicable shared-state inventory row with a named visual reference: either a dedicated mockup or an explicitly inherited canonical component/state with exact differences. Inheritance is for genuinely shared component/state composition, not an unpictured tab, role layout or journey step. Each inherited row names its actual base artifact and revision, viewport, unchanged geometry, exact copy/control differences and confirmation scope. The base must exist and be inspected; pending confirmation keeps the proposed inheritance unapproved, not missing. A shared loading component may serve several screens; a different booking, approval or access decision needs its own reference. A journey poster, collage of tiny screens, generic dashboard, text diagram or rough SVG cannot stand in for the finished mockup set. Nonvisual products use complete command, conversation or process examples instead.

Once direction is confirmed, continue generation in coherent batches until the unblocked queue is exhausted, reviewing and correcting each batch. Batch completion triggers the next available work, not a final checkpoint. Pending review of later screens does not reopen the direction gate or stop independent generation. Ask about meaningful decisions while continuing independent artifacts. Approval requests should show actual revisions; group related references to reduce unnecessary interruptions.

Inspect each generated image at usable resolution for content accuracy, state coverage, readability and design consistency. Regenerate weak images. Derive the design system: exact typography, colors, spacing, geometry, icons, component variants, density, interaction timing and reduced-motion/transparency alternatives. Resolve image ambiguity through inspectable layout references and written values, rather than asking the builder to improvise. When proposed values alter the pictured layout, show the resolved interpretation for review and update affected references; declaring prose authoritative does not resolve a visible contradiction. Generated text errors and invented controls are corrections to make before freezing the pack.

If image generation is unavailable, explain the gap, continue research/specification and label visual readiness incomplete. Never claim generation occurred, silently substitute a low-fidelity drawing, or call the visual design finished.

## Confirm and freeze

Present actual images and journey/state coverage for confirmation. Record artifact paths, viewport, revision, confirmation evidence and approved scope. Unseen screens and inherited references outside confirmed scope remain unconfirmed. Keep proposed, confirmed, superseded and implementation-verified statuses distinct.

Build a canonical pack with one index, screen/state manifest, exact tokens, per-screen contracts, image references and inspectable interaction/layout references where useful. Each screen contract states layout, field order, exact copy, validation, permissions, actions, feedback, persistence, exceptional behavior and responsive rules. Separate review instrumentation and synthetic data from production behavior. Identify the authority order among functional requirements, canonical layout and generated imagery; resolve contradictions before readiness.

## Enforce 1:1 parity

The confirmed canonical pack is the implementation target. Preserve composition, typography, component geometry, assets, labels, density, responsive behavior and interaction outcomes. The builder may choose internal implementation details inside that contract. Visual or behavioral deviations require a recorded reason and explicit user disposition, with updated references when accepted.

Specify visual QA at the same viewport and state as each canonical reference. Compare screenshots directly and inspect copy, layout, type, colors, spacing, icons, assets and state transitions. Maintain a parity manifest for every applicable screen/state/viewport: reference revision, implementation screenshot, comparison result, unresolved deviation and user disposition. Missing rows or evidence keep parity incomplete. Track mismatches by screen/state ID through correction and recheck. Use overlays or image diffs when helpful; software rendering variation is not permission for a redesigned interface. Functional tests complement visual evidence. Passing a build or producing attractive screenshots alone does not establish parity.

Before handing off, walk actual navigation and journey transitions again. Every distinct view must map to a current image; shared-state rows must resolve to existing component references with exact inheritance. Check required responsive layouts, role permissions, forms, dialogs and outcomes. Fix missing references, contradictory generated copy and unresolved geometry while tools and decisions permit. Keep this coverage audit separate from link/JSON integrity and future implementation parity checks.

Readiness requires complete applicable coverage, user-confirmed references, resolved design contradictions and executable acceptance criteria. Implemented parity additionally requires comparison evidence from the running product. Planned QA is never executed QA.

## Reference library

Read ../assets/ui-library/sources.json to choose source families. Search entries with:

    python3 <skill-directory>/scripts/search_catalog.py 'approval'
    python3 <skill-directory>/scripts/search_catalog.py 'fade' --source amicro --limit 6

When execution is unavailable, search components.json directly. Do not load the full catalog into every conversation. Read the linked CREDITS.md for creator attribution; carry creator/source credit into the project's design references.

Beautiful UI supplies functional interface references; Amicro/Kinetics interactions; Vault expressive treatments; Gooey/Orbs specialized effects; Dither compatible chart/visual patterns; Cuelume optional sound. Select a coherent subset for the journey, with bespoke design when appropriate. Catalog membership means available for consideration, not installed, approved or tested. These are captured references; verify selected source details when material.

Third-party skill packs remain source material until intentionally selected/reviewed. No third-party implementation is bundled. Resolve selected public source/docs on demand, retaining revision and notices if code is copied. Credit inspiration. Attribution and permission are separate; unresolved code permission can remain an implementation dependency while design proceeds. Do not copy protected code merely because a credit is attached.

## Selection record

Record source/creator, intended screen/journey/state, rationale, platform compatibility, relevant configuration/tokens/dependencies, exact mockup and confirmation status. Include motion trigger/timing and static/reduced-motion equivalent when relevant, keyboard/focus/touch behavior and performance requirements. Sound is optional, with mute preference and visual equivalents. Tie activity states to real events rather than inventing progress. Snippets can be partial examples, not drop-in components.

Use candidate, selected, visually confirmed and implementation-verified statuses according to evidence. Carry only selected components into required build instructions, not every explored effect.
