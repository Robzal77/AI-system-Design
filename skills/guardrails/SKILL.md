---
name: ai-guardrails
description: Review or implement AI request, output, retrieval, and tool safety boundaries.
---

# Guardrails

## Procedure

1. Identify trusted identity, tenant, source data, model outputs, and executable tools. Treat retrieved text and model output as untrusted.
2. Define deterministic authorization and schemas outside the prompt. Bound input size, tool scope, step count, and spend.
3. Specify output checks for schema, citations, sensitive data, and unsupported answers. Ensure cached results pass relevant checks.
4. Add synthetic cases for cross-tenant access, forged identity, hostile documents, unsupported citations, malformed tool arguments, and unauthorized writes.
5. Distinguish heuristic content filters from enforcement. Regex or model-based detection is not a complete prompt-injection defense.
6. Report each boundary, expected deny/abstain behavior, verification evidence, and residual limitations. Never relax authorization to improve answer rate.

## Completion

Return concrete artifacts, evidence actually collected, unresolved decisions, and the next implementation step. Follow repository AGENTS.md and the user's authorized scope.
