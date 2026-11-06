# Resources, credentials and access

Read during resource planning, whenever research selects a capability, and before milestone readiness. Every project blueprint includes a Resources and access section in its entry Markdown, with a detailed register inline or linked as RESOURCES.md. Use the resource register template in ../assets/resource-register.template.md when useful. The portable inventory schema in ../assets/resource-inventory.example.json contains no live access.

## Discover and select

Read the user's designated inventory and authorized configured connections first. Research the actual capabilities required by the proposed solution. Separate existing reusable resources, confirmed project allocations, proposed selections and newly needed access. Confirm meaningful new selections after research, explaining their purpose and alternatives; do not demand every possible key during initial intake.

For each selected resource, assign an ID and record:
- Capability and why the build needs it; provider/tool/service and exact target account, organization, project or repository when known.
- Consumer: build agent, server, client, CI or operator; development, test/staging and production environments separately.
- Least permissions needed, read/write or administrative operations, target scope and any expiry. Browser-safe public identifiers are separate from privileged credentials.
- Resource owner and person able to grant/configure access; approved project allocation, spend/usage limits and approval evidence.
- Required credential/configuration names, authentication method, secure source reference, destination store/connection and intended binding. A destination is not proof the credential exists there.
- Selection, authorization, availability and verification statuses; evidence/date, dependent milestones and next action.

A single resource can have different permissions, approval and availability in different environments. A resource in the shared inventory is not automatically allocated to this project. Project access decisions remain local unless the user designates reuse.

## Request missing access

When a selected capability lacks the access needed for an upcoming milestone, create a named access request linked to its resource ID. Ask the user in plain language for the missing decision or setup—not for the secret value. Include the purpose, target, consumer/environment, minimum permissions, intended secure destination, setup/grant owner, spend/usage limit, dependent milestone, verification action and what can proceed meanwhile. Identify an alternative if access is declined or delayed.

Example request: “The server needs a credential limited to sending project invitations from the selected email service. May the project use that capability in staging, and who can configure EMAIL_API_KEY in the staging service's secret store? No paid allocation has been approved. Email delivery testing waits for configuration; the portal design and local review workflow can continue.” Adapt this to the actual selection; do not invent an email-provider dependency for a project that does not need one.

Use existing authorization when it covers the exact operation, target and scope; ask only about gaps. Record the user's answer and its scope. A question, proposed setup, existing subscription or silence is not approval. Approving a design or capability does not by itself approve creating credentials, expanding permissions, purchasing service or changing production access. Apply the host's action-specific permission rules when execution is requested.

## Obtain or locate access

Offer the applicable path: reuse an authorized configured connector; have the authorized owner grant scoped membership/service identity; use a supported secure credential setup flow; or have the user place a key directly into the agreed local/deployment secret store. Explain provider-specific setup only after checking the selected provider's current official instructions. State manual steps precisely when no available tool can perform them. Provision or configure only within actual execution authorization; a blueprint request alone does not authorize those mutations.

Keep secret values out of chat requests, blueprint Markdown, diagrams, generated images, fixtures, logs, source control and downloadable packages. Record variable names and secure location references instead. Avoid reading or printing secret contents merely to prove existence. Public/client configuration belongs in a separate classification; privileged credentials remain server/CI/operator-only. An .env.example may list names and descriptions without real values; it does not establish configured access.

Private project resource registers may include user-authorized concrete access references needed by the builder. The shared skill, public examples and reusable presets contain only generic schemas/templates; they never inherit personal paths, credentials or private account inventory.

## Track independent statuses

Keep these dimensions separate:
- Selection: proposed / confirmed / rejected.
- Authorization: not required / pending / approved / denied. Record exact actions and scope; “not required” applies only to an operation that actually requires no grant, such as local fixture design.
- Availability: not configured / configured, unverified / verified / unavailable / expired / revoked.
- Verification: not run / passed / failed, with the capability checked, environment, actor, date and nonsecret evidence. Testing can be blocked independently of configuration.

“Approved” never means “configured”; “configured” never means the permission or capability works. Verify only through an authorized check proportionate to the capability, preferably a harmless read/status check. Sending email, spending money or other writes require authorization for that test action. Use fixtures for unconnected development and label them. Recheck affected readiness when access expires, is revoked, changes scope or fails verification.

## Compile the build handoff

The final entry Markdown must identify required resource IDs, approved/current capabilities, pending requests and which milestones they affect. The register must tell a fresh builder where authorized access is configured or where it is intended to exist, which variable/connection binding to use, who supplies it, and the setup/verification still required. Mark unknown locations explicitly and name the resolver; do not fabricate paths, accounts, credentials or successful connectivity.

Readiness is milestone-specific. Design can be complete with access dependencies if the capabilities and contracts are coherent. A milestone needing live access is execution-ready only when the required grant/allocation, configuration and relevant verification evidence are present. Missing production keys cannot block independent research, tab mockups, local fixtures or design contracts. If an unknown provider capability affects the design itself, identify that specific dependency and continue unaffected work.
