---
name: ai-agentic-bi
description: Turn BI requirements into a governed build specification and validated report/model proposal with explicit human approval gates.
---

# Agentic BI delivery

## Procedure

1. Read docs/enterprise-ai-team.md and docs/diagrams.md. Inspect the BRD and authorized metadata; use synthetic fixtures until real-data access is approved.
2. Capture business questions, existing governed measures, dimensions, audience, refresh needs, and acceptance criteria. Flag unresolved metric definitions; never invent them.
3. Produce a versioned build specification and obtain the required business requirement approval before dependent build work.
4. Inventory authorized tables, relationships, DAX measures, RLS/OLS configuration, and lineage. Record metadata freshness and permissions.
5. Propose report pages and model/DAX changes. Prefer existing governed measures; separate generated proposals from executed changes.
6. Validate syntax, dependency changes, numerical outputs, security under test identities, performance, and regression cases using available BI tooling. Report checks that could not run.
7. Package exact artifacts, versions/hashes, validation evidence, and rollback plan for publishing approval. Follow skills/human-approval/SKILL.md for executable write workflows.
8. Publish only within the user's authorized scope and project release rules. Record execution receipt and verify the deployed version.

## Deliverables

Requirements/build specification, metadata inventory, report/model proposal, validation matrix, approval records or clearly pending gates, and deployment/rollback plan. Do not claim a Power BI connection or deployment exists without actual evidence. Use skills/evaluation/SKILL.md for model-dependent task quality.
