---
name: ai-system-design
description: Design an AI system for a concrete use case, define contracts, and compare implementation tradeoffs.
---

# System Design

## Procedure

1. Read README.md, docs/architecture.md, and the provided use case. Inspect existing interfaces before proposing new infrastructure.
2. Identify users, read/write actions, identity source, authorized data, expected load, quality requirements, and budget. Record unknowns; ask only for choices that block the design.
3. Fill templates/design-brief.md with explicit assumptions and measurable acceptance criteria.
4. Trace one request through gateway, policy, retrieval, model, validation, and any approval/execution. Describe failures at each boundary.
5. Propose a minimal read-only baseline and explain when cache, queues, routing, or orchestration become necessary.
6. Compare at least one simpler alternative. Label estimates and provider-specific claims that require verification.
7. Return a design brief, diagram, staged backlog with owners, and validation plan. Do not provision services merely to produce a design.

## Completion

Return concrete artifacts, evidence actually collected, unresolved decisions, and the next implementation step. Follow repository AGENTS.md and the user's authorized scope.
