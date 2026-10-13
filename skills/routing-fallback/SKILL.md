---
name: ai-routing-fallback
description: Specify model routing, provider adapters, budgets, timeouts, retries, and safe fallback behavior.
---

# Routing Fallback

## Procedure

1. Inspect existing provider adapters and classify tasks using explicit rules first.
2. Select approved models/providers based on measured quality, latency, cost, and data-handling constraints. Do not invent current pricing or model availability.
3. Define total deadline, per-attempt limits, maximum attempts, retryable errors, backoff/jitter, and circuit-breaker behavior.
4. Preserve authorization, prompt/output contracts, residency, and privacy constraints when falling back.
5. Test timeout, rate limit, server error, invalid output, auth failure, and mid-stream interruption. Denials must not become fallback successes.
6. Keep side-effecting tool retries separate and idempotent. Never replay a write just because inference failed.
7. Deliver route table, adapter contract, outage-drill evidence, and cost/quality tradeoffs. Label simulated behavior.

## Completion

Return concrete artifacts, evidence actually collected, unresolved decisions, and the next implementation step. Follow repository AGENTS.md and the user's authorized scope.
