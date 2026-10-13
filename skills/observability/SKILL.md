---
name: ai-observability
description: Add or review AI traces, monitoring, incident diagnosis, and operational runbooks.
---

# Observability

## Procedure

1. Trace gateway → retrieval → model → validation → approval/tool using a shared request ID.
2. Record route/provider, version identifiers, durations, token usage/cost where available, cache outcome, freshness lag, and error classes.
3. Redact credentials, personal data, and sensitive prompt/document content. Define access controls and retention for telemetry.
4. Propose alerts for error rate, p95 latency, budget burn, ingestion lag, and approval backlog based on project targets.
5. Run a synthetic outage and stale-data incident. Verify traces identify the failing component without exposing raw sensitive content.
6. Create a runbook with owner, impact triage, permitted mitigation, rollback, recovery check, and escalation path.
7. Deliver trace schema, dashboard/alert specification, and drill evidence. Do not claim monitoring is deployed when only specifications exist.

## Completion

Return concrete artifacts, evidence actually collected, unresolved decisions, and the next implementation step. Follow repository AGENTS.md and the user's authorized scope.
