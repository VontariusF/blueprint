---
name: blueprint
description: Develop and maintain build-ready design specifications through research, collaborative problem definition, resource planning, user journeys, mockups, and acceptance criteria. Use to turn ideas or existing projects into blueprints, refine design specs, or reconcile them during implementation. Ordinary implementation tasks do not require this workflow.
---

# vontariusf/blueprint

Develop an executable design specification with the user around three questions:
- Why do I want to solve this?
- What do I need to solve this?
- What does it look like once this is solved?

The method is research-first and collaborative. Create project artifacts as decisions develop, rather than hurrying from a vague idea to a confident specification. Preserve the complete vision while defining a bounded next delivery. Blueprint plans and maintains specifications; implementing the product requires the user's implementation request.

## Start from existing context

Resolve create, refine, or reconcile. Read relevant conversation, project instructions, existing specifications and repository evidence. Reuse settled answers. Read [context and profiles](references/context.md) at the start. Load only the selected default/hackathon/startup preset and designated reusable context. Labels such as blueprint/hackathon select a profile conversationally; they do not promise a native slash command. Use default when none is selected.

Reflect the problem and desired change in plain language. Identify consequential unknowns and begin useful investigation. Ask a small coherent set of consequential questions rather than requiring a long intake form. Research factual unknowns through available sources; the user owns intentions and consequential tradeoffs. Continue independent work while waiting. Required unanswered decisions keep dependent work pending; elapsed time is not an answer.

## Research and shape

Read [research and decisions](references/research.md) when investigating or comparing solutions. Start with what the user knows and explore missing angles. Inspect existing systems before choosing reuse, extension, replacement or greenfield. Gather evidence proportionate to the decision. Distinguish sourced findings, user-confirmed choices, inspected behavior and assumptions. Report unavailable research honestly.

Research and discussion may develop in the initial chat. Persist essential findings and choices into the project blueprint so a fresh build agent can reconstruct requirements without that chat. Revise decisions when new evidence warrants it.

Develop purpose, complete vision, intended users, features, scope exclusions, friction, boundaries, infrastructure and resources together. Follow reuse and ambiguity rules in [context](references/context.md).

## Define resources and access

Read [resources and access](references/resources.md). Include a Resources and access section in every blueprint Markdown, with a detailed register inline or linked. Research needed capabilities, reuse designated inventory, and request missing keys, grants or setup through an appropriate secure route when authorized. Record permission scope, owner, configuration names, where access exists or is intended to exist, allocation limits, approval evidence and dependent milestones. Store references rather than secret values. Keep approval, configuration and verification distinct; pending access blocks its dependent execution, not independent design.

## Define the experience

For visual interfaces, journeys and interaction design, read [visual design](references/visual-design.md). Inventory navigation, role views and journeys before rendering concepts so the representative screen has defined requirements. Discuss visual direction before generating mockups, reusing settled preferences. When direction is unresolved, generate distinct image-based variations of the same representative screen, let the user select, combine, refine or redirect them, and confirm an actual anchor reference before expanding the full mockup set. A direction choice establishes the visual foundation; it does not approve subsequent screens. Reuse an already confirmed direction without repeating selection.

Inventory each navigation tab/subtab, distinct role view, creation/edit form, dialog and user-journey step/outcome before producing high-fidelity image-generated mockups. Give every distinct view its own ID and actual reference; a screenshot containing a tab label does not cover that tab's contents. Once the direction gate is resolved, develop the complete canonical design pack with screen contracts and responsive references, generating every unblocked view and applicable responsive/state reference. Read [canonical pack controls](references/canonical-pack.md) before expansion: preserve shared layouts, verify each image's app bounds and logical viewport, and maintain a durable pack record through review and interruption. Present exact revisions for confirmation; pending screen review keeps artifacts proposed, not uncreated. The accepted pack is the build target: require 1:1 visual and behavioral parity, with screenshot evidence and explicit deviation handling. An overview image or text wireframe cannot satisfy these gates. Nonvisual systems use appropriate conversation, command, service or process examples.

## Plan and compile

Take a project-manager approach: jointly refine dependencies, milestones, the critical path and independent work. Define observable completion and proper QA. Give the build agent discretion inside confirmed purpose, visual requirements, resource access, budgets and real constraints; avoid invented restrictions.

Read [handoff and readiness](references/handoff.md) before compiling or claiming readiness. Maintain one entry point with supporting artifacts proportional to complexity. Honor requested destinations and repository conventions; otherwise use a clearly named blueprints/<project>/ directory in the workspace. Never overwrite an unrelated blueprint. Project outputs belong outside the installed skill.

For changes discovered during implementation, trace affected decisions, resources, journeys, milestones and acceptance criteria. Reconcile those portions, preserve unrelated confirmed work and retain consequential rationale.

## Complete the work

Maintain a work queue through research, decisions, resources, contracts and visual coverage. Continue available work until the requested blueprint is complete or each remaining branch has a concrete blocker. A progress update or a missing-work list is not a stopping condition. Pending production access, an arbitrary image count, or the end of a generation batch does not justify stopping independent design. Unresolved visual direction blocks full mockup expansion; continue independent research, resources, journeys and functional contracts while waiting for that choice. After direction confirmation, generate unblocked proposed references while awaiting their screen review; approval of unseen artifacts is never inferred.

Before final handoff, walk every navigation destination and journey transition against actual artifacts and resolve uncovered tabs, forms, outcomes and applicable responsive/state variants. Run the completion audit in [handoff and readiness](references/handoff.md). Reconcile entry point, index, approvals and audit against the current pack record; a stale checkpoint cannot describe current readiness. If remaining work genuinely requires a user decision, unavailable tool, authorization or explicit pause, checkpoint with the exact blocker, affected work, resolver and independent work exhausted. Resume available work when resolved.

Report what is defined, what needs a decision/access, and the next available action. Assess readiness per milestone: ready to build; design complete with execution dependencies; or still being shaped. Pending access does not stop independent specification work. Proposed designs are not tested implementations; unconfirmed mockups are not approved.

Return actual blueprint/artifact links, profile and overrides, and outstanding dependencies. Promote project choices into reusable context only when the user designates that update.
