# Using this playbook for an enterprise AI team

The user-provided notes frame two applications: a shared AI Centre of Excellence (CoE) and a governed Agentic BI platform. Treat both as proposed applications of the system-design topics, rather than verified deployments from the video.

## Shared platform, accountable project teams

The CoE owns reusable standards and components: provider catalogue, identity patterns, tool contracts, evaluation templates, tracing, cost allocation, and release criteria. Business project teams own requirements, source correctness, user outcomes, and support. A shared platform must preserve function and tenant permissions.

Start an application inventory with owner, business function, workflow, environment, data classification, approved provider/model, monthly budget, release status, and support contact. Record credentials in a secret manager, not the inventory. Review approval and source-access requirements before implementation.

## Three delivery phases

| Phase | Deliver first | Exit evidence |
|---|---|---|
| Foundation | Identity, authorized sources, provider catalogue, validators, basic audit, read-only baseline | Cross-function access denial; citations; owner and support plan |
| Reliability | Durable workflow where needed, approval service, evaluations, deadlines, fallback, redacted traces | Outage, replay, approval, and recovery drills |
| Optimization | Measured caching, task routing, event-driven freshness, cost/value reporting | No freshness regression; measured quality, latency, and spend comparison |

Data must meet correctness and freshness requirements in phase one; the optional optimization is moving suitable sources from a simpler refresh method to CDC, not postponing freshness controls.

## Human team skills and milestones

| Capability | Practice task | Completion evidence |
|---|---|---|
| HLD and LLD | Explain diagrams and API contracts | Peer can trace an authorized and denied request |
| Security | Implement service ACL checks | Cross-tenant, forged-identity, and tool-denial cases pass |
| Retrieval and BI data | Compare document evidence with governed measures | Update/delete/revocation drill; validated KPI query |
| Workflow engineering | Design approval and recovery | Payload changes and retries cannot duplicate a write |
| AI evaluation | Compare prompt/model candidates | Versioned dataset and reproducible baseline comparison |
| Operations | Diagnose a synthetic failure | Redacted trace and recovery runbook |
| Value measurement | Define one business outcome | Accepted completed tasks, measured effort saved, and attribution limits |

## Agentic BI first project

Use the [BI workflow diagram](diagrams.md#6-agentic-bi-workflow) and the BI skill. Start with **BRD to reviewed build specification**, then a sandbox report artifact. Defer production publishing until permissions, validation, rollback, and approvals are established.

1. Intake owner captures business questions, measures, dimensions, refresh requirements, intended audience, and exclusions.
2. Analysis task identifies ambiguities and produces a requirements document. A business reviewer approves its version.
3. Metadata task reads only authorized model schemas, measure definitions, relationships, lineage, and access configuration.
4. Builder proposes report pages and DAX/model changes using existing governed measures where possible.
5. QA checks numerical outputs against known fixtures, RLS/OLS under actual test identities, dependencies, performance, and regressions.
6. Release owner reviews the exact artifact and validation evidence. Deployment targets a sandbox or staged environment before production.
7. Operations records deployment version, audit receipt, failures, accepted output rate, and measured task outcomes.

Separate model choices from workflow ownership. A router chooses an LLM for analysis or generation; an orchestrator manages stage transitions and durable state. Multiple agents are optional. Deterministic validators and existing BI deployment tooling are often more reliable than another reasoning agent.

## Suggested acceptance gates

Set numeric quality, latency, budget, and freshness targets in the project brief. Do not adopt generic thresholds without business context. Require no unauthorized access or unapproved production actions in the evaluated boundary cases; require accountable reviewers and reproducible evidence before release. Passing test cases is evidence, not proof of absence of every possible flaw.

For business value, compare accepted completed tasks and measured human effort with a documented baseline. Deduct review and correction effort. Avoid counting generated drafts as completed work or token reductions as verified ROI.
