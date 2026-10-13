---
name: ai-evaluation
description: Build and run a reproducible evaluation for AI quality, boundary behavior, latency, and cost.
---

# Evaluation

## Procedure

1. Define the workflow and freeze acceptance criteria before comparing candidates.
2. Build a versioned synthetic or authorized dataset covering ordinary, ambiguous, unsupported, conflicting, injection, isolation, freshness, and outage cases.
3. Define rubrics for correctness, evidence support, citation validity, abstention, and policy compliance. Include human calibration when using model judges.
4. Record dataset, prompt, model, corpus, route, and code versions. Keep held-out cases separate from development examples.
5. Compare baseline and candidate under matching conditions. Report sample counts, failures, variability, p95 latency, and cost per successful task; label missing measurements.
6. Fail releases on authorization leakage or unapproved actions. Set other thresholds with project owners instead of inventing universal targets.
7. Produce a reproducible report with commands, representative failures, decision, and limitations. Never present simulated provider text as real LLM-quality evidence.

## Completion

Return concrete artifacts, evidence actually collected, unresolved decisions, and the next implementation step. Follow repository AGENTS.md and the user's authorized scope.
