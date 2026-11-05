# Handoff and readiness

Maintain one entry point (normally BLUEPRINT.md), honoring requested format/location and project conventions. Small projects can use one document; larger projects link focused research, architecture, design and verification material. Essential decisions must survive without the originating chat.

Cover applicable topics without empty boilerplate:
- Purpose: problem, users, current workflow, motivation and desired change.
- Complete vision: intended solution and observable behavior.
- Evidence: findings, sources, alternatives, assumptions and tradeoffs.
- Scope: current delivery, included features, explicit exclusions and later work.
- System: components, data, infrastructure, integrations, boundaries and operations.
- Resources: existing/new selections, access paths, status, allocation and limits.
- Experience: journeys, confirmed style, UI/UX mockups and important states.
- Delivery: dependencies, milestones, critical path, independent work and next action.
- Decisions: rationale, unresolved options, affected work, resolver and superseded choices.
- Completion: acceptance criteria and appropriate QA by milestone.
- Agent handoff: reading order, starting milestone, discretion, constraints and dependencies.

Connect requirements to behavior/design and verification. Examples: offline connectors preserve local editing; denied permissions cannot be bypassed through another interface; a task retains its intended owner/due date; screen behavior matches a confirmed reference. Select QA appropriate to the project: tests, screenshots, working demonstrations, visual/interaction checks and user review where useful. Planned tests are not executed tests.

Express real dependencies; distinguish complete product vision from bounded initial scope. Dates/effort estimates carry assumptions, not invented precision. Explain which activities determine reaching a milestone.

Before handoff, inspect whether an independent agent can identify what to build next, required inputs, design references, constraints and what counts as done. Check links and contradictions. Missing meaningful mockups prevent visual-design completion; pending external access blocks dependent execution rather than all specification work.

Report milestone readiness with evidence:
- Ready to build: required decisions and execution inputs are available for that milestone.
- Design complete with execution dependencies: coherent design with named setup/access prerequisites.
- Still being shaped: material design/behavior decisions remain unresolved.

Reconcile changes through affected requirements, resources, experience, delivery and acceptance criteria. Preserve unrelated confirmed work and superseded rationale. A checkpoint names open matters and next action rather than claiming universal readiness.
