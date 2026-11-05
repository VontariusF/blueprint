# Visual and interaction specification

Map users, entry points, goals, decisions, actions, handoffs and success/failure before choosing effects. Honor existing design systems unless the user requests change. Profiles supply provisional defaults rather than a mandatory aesthetic.

Develop journey maps, style concepts, UI/UX mockups and important states (loading, empty, errors, partial results, access denial, success/cancellation as relevant). Use available visual tools. Make interactive examples when behavior cannot be understood from still imagery. Expand coverage as scope becomes clear. If tools are unavailable, state the missing artifacts; do not call text descriptions finished mockups.

Confirm the presented direction and meaningful interaction choices. Record exact artifact/revision and approved scope; unseen screens are not approved. Preserve labels, field order, navigation, actions, responsive rules and exceptional behavior as implementation references. Generated images illustrate design, not shipped behavior or executable code.

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
