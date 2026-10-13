---
name: ai-retrieval-freshness
description: Design or verify authorized retrieval, source updates, deletes, permission changes, and cache freshness.
---

# Retrieval Freshness

## Procedure

1. Inventory source IDs, owners, versions, ACLs, update frequency, and allowable freshness lag.
2. Define chunk/citation IDs and apply tenant/document authorization before ranking or model context assembly.
3. Specify idempotent ingestion, version ordering, checkpoints, durable acknowledgements, retries, and dead-letter handling.
4. Replay update, delete, duplicate, out-of-order, and permission-revocation events with synthetic sources.
5. Invalidate affected cache/index entries and verify obsolete content cannot reappear. Include corpus and permission versions in cache boundaries.
6. Measure source-to-index lag and retrieval relevance. Separate exact caching from semantic reuse; require false-hit evaluation before enabling semantic cache.
7. Deliver data contract, freshness runbook, and observed drill results. Do not claim CDC or semantic search exists when only a design is present.

## Completion

Return concrete artifacts, evidence actually collected, unresolved decisions, and the next implementation step. Follow repository AGENTS.md and the user's authorized scope.
