---
name: ai-human-approval
description: Design approval and execution for consequential AI-proposed write actions.
---

# Human Approval

## Procedure

1. Enumerate write tools, allowed targets, actor/approver permissions, and maximum action scope.
2. Present the exact normalized action payload for review. Store an immutable payload hash, action ID, requester, approver, expiry, and status.
3. Define pending, approved, rejected, expired, executing, completed, and failed transitions. Specify concurrency control and revocation.
4. Before executing, verify payload/hash, expiry, approval authority, current authorization, and idempotency receipt.
5. Make the state transition and execution record durable. Define recovery after a crash or uncertain downstream result.
6. Verify rejection, expiry, altered payload, revoked permissions, duplicate execution, and concurrent approval using synthetic tools.
7. Return the state machine, contracts, and evidence. Model output is a proposal; it cannot authorize its own tool execution.

## Completion

Return concrete artifacts, evidence actually collected, unresolved decisions, and the next implementation step. Follow repository AGENTS.md and the user's authorized scope.
