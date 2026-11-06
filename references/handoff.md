# Handoff and readiness

Maintain one entry point (normally BLUEPRINT.md), honoring requested format/location and project conventions. Small projects can use one document; larger projects link focused research, architecture, design and verification material. Essential decisions must survive without the originating chat.

Cover applicable topics without empty boilerplate:
- Purpose: problem, users, current workflow, motivation and desired change.
- Complete vision: intended solution and observable behavior.
- Evidence: findings, sources, alternatives, assumptions and tradeoffs.
- Scope: current delivery, included features, explicit exclusions and later work.
- System: components, data, infrastructure, integrations, boundaries and operations.
- Resources and access: mandatory entry-Markdown section; inline register or linked RESOURCES.md with resource IDs, required keys/grants, consumers/environments, permission scopes, configuration locations, owners, allocations, authorization/setup/verification evidence, access requests and milestone dependencies. Follow resources.md; never include secret values.
- Experience: journeys, confirmed style, UI/UX mockups and important states.
- Delivery: dependencies, milestones, critical path, independent work and next action.
- Decisions: rationale, unresolved options, affected work, resolver and superseded choices.
- Completion: acceptance criteria and appropriate QA by milestone.
- Agent handoff: reading order, starting milestone, discretion, constraints and dependencies.

## Executable depth

Use stable requirement IDs and a traceability matrix: requirement → journey → screen/state → system/API/data behavior → acceptance check. For each feature specify triggers, actors, preconditions, inputs, rules, transitions, outputs, permissions, failure/recovery, persistence and concurrency/idempotency where relevant. Name exact interfaces, data fields, invariants, access paths, cost limits, operational ownership and evidence behind selections. Before readiness, verify that each acceptance criterion is supported by specified fields, interfaces and state transitions; resolve missing contracts rather than leaving them for the builder to invent. Provide concrete examples rather than headings with aspirational prose.

For substantial interfaces, link the complete canonical visual pack required by visual-design.md. Audit coverage against the scope and contract; an attractive happy path is insufficient. Missing actual mockups, unconfirmed decisions, unknown resource access and unexecuted tests retain their real statuses. A public worked example labels synthetic assumptions and proposal status instead of implying user approval or product validation.

Include build dos/don'ts grounded in the project, an ordered critical path with dependency reasons, parallel work, milestone-specific access prerequisites, test fixtures, expected results, rollback/backup behavior, and a fresh-agent reading order. Avoid arbitrary length quotas: completeness is the ability to execute without inventing consequential decisions.

Connect requirements to behavior/design and verification. Examples: offline connectors preserve local editing; denied permissions cannot be bypassed through another interface; a task retains its intended owner/due date; screen behavior matches a confirmed reference. Select QA appropriate to the project: tests, screenshots, working demonstrations, visual/interaction checks and user review where useful. Planned tests are not executed tests.

Express real dependencies; distinguish complete product vision from bounded initial scope. Dates/effort estimates carry assumptions, not invented precision. Explain which activities determine reaching a milestone.

## Completion audit

Use the requested scope and actual navigation/journeys as independent evidence, not just the agent's own manifest. Verify:
- Every in-scope tab/subtab, distinct role view, form, dialog, journey step and outcome has a view ID, contract and actual current mockup; applicable responsive references exist.
- Shared-state references resolve to actual inspected artifacts with precise inheritance; exclusions have appropriate user disposition. Counts of files, IDs or superseded images are not completeness evidence.
- Requirements, images, field/action rules, permissions, data/interfaces and acceptance criteria agree. Exact layout dimensions/tokens are resolved for the canonical revision.
- Resources and access appear in the entry Markdown/register with named bindings/destinations, owners, scope, approvals, configuration/verification status, requests and milestone dependencies. Unknown access cannot masquerade as configured.
- The next build milestone is executable without inventing consequential requirements; later access dependencies are identified without blocking independent design.

Keep integrity, coverage, semantic consistency, confirmation and readiness results separate. All unblocked gaps return to the work queue. If only review is outstanding, present the completed proposed pack for confirmation rather than leaving unseen views uncreated. A genuine checkpoint names each blocking decision/capability/authorization, resolver, affected artifacts and independent work exhausted; incompleteness itself is not the blocker.

Before handoff, inspect whether an independent agent can identify what to build next, required inputs, design references, constraints and what counts as done. Check links and contradictions. Missing meaningful mockups prevent visual-design completion; pending external access blocks dependent execution rather than all specification work.

Report milestone readiness with evidence:
- Ready to build: required decisions and execution inputs are available for that milestone, including the necessary access authorization, allocation, configuration and relevant verification evidence.
- Design complete with execution dependencies: coherent design with named setup/access prerequisites, owners and intended configuration locations; existing access is distinguished from proposed setup.
- Still being shaped: material design/behavior decisions remain unresolved.

Reconcile changes through affected requirements, resources, experience, delivery and acceptance criteria. Preserve unrelated confirmed work and superseded rationale. A checkpoint names open matters and next action rather than claiming universal readiness.
