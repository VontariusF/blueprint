---
name: blueprint
description: Develop and maintain build-ready design specifications using the Contextual Resolution Method for problem deconstruction and contextual research, followed by resource planning, user journeys, mockups, and acceptance criteria. Use to turn ideas or existing projects into blueprints, refine design specs, or reconcile them during implementation. Ordinary implementation tasks do not require this workflow.
---

# vontariusf/blueprint

Develop an executable design specification with the user around three questions:
- Why do I want to solve this?
- What do I need to solve this?
- What does it look like once this is solved?

Lead with the **Contextual Resolution Method (CRM)**: understand and deconstruct the problem with the user, investigate its relationships and surroundings, and reframe it before committing to a solution. Create project artifacts as decisions develop, rather than hurrying from a vague idea to a confident specification. Preserve the complete vision while defining a bounded next delivery. Blueprint plans and maintains specifications; implementing the product requires the user's implementation request.

## Start from existing context

Resolve create, refine, or reconcile. Read relevant conversation, project instructions, existing specifications and repository evidence. Reuse settled answers. Read [context and profiles](references/context.md) at the start. Load only the selected default/hackathon/startup preset and designated reusable context. Labels such as blueprint/hackathon select a profile conversationally; they do not promise a native slash command. Use default when none is selected.

## Lead with the Contextual Resolution Method

Read [the CRM workflow](references/contextual-resolution.md) before opening a new inquiry or revisiting a material problem/scope decision. Guide the user through Define → Break down → Look around → Rethink. In plain language, establish why the problem matters, map its parts and relationships, separate symptoms from possible causes, then derive and run research from the consequential unknowns. Compare the initial and refined understanding and establish the intended outcome and delivery boundaries together. Reuse settled inquiry when refining an existing blueprint.

This is Blueprint's leading phase. Its problem map and research agenda must guide tool, infrastructure and solution investigation. Preliminary research can inform the discussion; keep the proposed product provisional until the need is sufficiently understood. Ask a small coherent set of questions, continue independent work while waiting, and seek owner decisions where required. Elapsed time is not an answer.

Persist this foundation in the entry document or linked PROBLEM.md, with evidence, open questions and links to research/decisions/resources. The CRM workflow defines its outputs and transition criterion. Continue from that foundation into solution design and compilation below; revisit the inquiry when later evidence changes the problem or approach.

Read [research and decisions](references/research.md) when investigating or comparing responses. Read [context and profiles](references/context.md) for reuse and ambiguity rules.

## Define resources and access

Read [resources and access](references/resources.md). Include a Resources and access section in every blueprint Markdown, with a detailed register inline or linked. Research needed capabilities, reuse designated inventory, and request missing keys, grants or setup through an appropriate secure route when authorized. Record permission scope, owner, configuration names, where access exists or is intended to exist, allocation limits, approval evidence and dependent milestones. Store references rather than secret values. Keep approval, configuration and verification distinct; pending access blocks its dependent execution, not independent design.

## Define the experience

For visual interfaces, journeys and interaction design, read [visual design](references/visual-design.md). Inventory navigation, role views and journeys before rendering concepts so the representative screen has defined requirements. Discuss visual direction before generating mockups, reusing settled preferences. When direction is unresolved, generate distinct image-based variations of the same representative screen, let the user select, combine, refine or redirect them, and confirm an actual anchor reference before expanding the full mockup set. A direction choice establishes the visual foundation; it does not approve subsequent screens. Reuse an already confirmed direction without repeating selection.

Inventory each navigation tab/subtab, distinct role view, creation/edit form, dialog and user-journey step/outcome before producing high-fidelity image-generated mockups. Give every distinct view its own ID and actual reference; a screenshot containing a tab label does not cover that tab's contents. Once the direction gate is resolved, develop the complete canonical design pack with screen contracts and responsive references, generating every unblocked view and applicable responsive/state reference. Read [canonical pack controls](references/canonical-pack.md) before expansion: preserve shared layouts, verify each image's app bounds and logical viewport, and maintain a durable pack record through review and interruption. Present exact revisions for confirmation; pending screen review keeps artifacts proposed, not uncreated. The accepted pack is the build target: require 1:1 visual and behavioral parity, with screenshot evidence and explicit deviation handling. An overview image or text wireframe cannot satisfy these gates. Nonvisual systems use appropriate conversation, command, service or process examples.

## Plan and compile

Take a project-manager approach: jointly refine dependencies, milestones, the critical path and independent work. Define observable completion and proper QA. Give the build agent discretion inside confirmed purpose, visual requirements, resource access, budgets and real constraints; avoid invented restrictions.

Read [handoff and readiness](references/handoff.md) before compiling or claiming readiness. Maintain one entry point with supporting artifacts proportional to complexity. Honor requested destinations and repository conventions; otherwise use a clearly named blueprints/<project>/ directory in the workspace. Never overwrite an unrelated blueprint. Project outputs belong outside the installed skill.

For changes discovered during design or authorized implementation, reopen the affected CRM problem/context questions and trace consequences through decisions, resources, journeys, milestones and acceptance criteria. Reconcile those portions, preserve unrelated confirmed work and retain consequential rationale.

## Complete the work

Maintain a work queue through research, decisions, resources, contracts and visual coverage. Continue available work until the requested blueprint is complete or each remaining branch has a concrete blocker. A progress update or a missing-work list is not a stopping condition. Pending production access, an arbitrary image count, or the end of a generation batch does not justify stopping independent design. Unresolved visual direction blocks full mockup expansion; continue independent research, resources, journeys and functional contracts while waiting for that choice. After direction confirmation, generate unblocked proposed references while awaiting their screen review; approval of unseen artifacts is never inferred.

Before final handoff, walk every navigation destination and journey transition against actual artifacts and resolve uncovered tabs, forms, outcomes and applicable responsive/state variants. Run the completion audit in [handoff and readiness](references/handoff.md). Use the refresh-and-check procedure in [canonical pack controls](references/canonical-pack.md) after every inspected batch or owner decision, before the next expensive batch and before yielding. It generates the checkpoint, current audit and shared status blocks from one record. Final handoff also requires a fresh independent reconciliation bound to the current specification; generated summaries alone cannot establish readiness. If remaining work genuinely requires a user decision, unavailable tool, authorization or explicit pause, checkpoint with the exact blocker, affected work, resolver and independent work exhausted. Resume available work when resolved.

Report what is defined, what needs a decision/access, and the next available action. Assess readiness per milestone: ready to build; design complete with execution dependencies; or still being shaped. Pending access does not stop independent specification work. Proposed designs are not tested implementations; unconfirmed mockups are not approved.

Return actual blueprint/artifact links, profile and overrides, and outstanding dependencies. Promote project choices into reusable context only when the user designates that update.
