# Team tutorial: from concepts to a working design

**Goal:** Every teammate can trace an AI request, identify trust boundaries, run failure cases, and propose a small feature with reviewable evidence.

## 1. Orient yourself — 15 minutes

Read the video review, architecture reference, and `docs/diagrams.md`. For CoE or BI work, continue with `docs/enterprise-ai-team.md` and `skills/agentic-bi/SKILL.md`. Watch the linked chapters for context. Pick a first project: an internal FAQ assistant that reads authorized documents and cites its sources. Write its scope in the design brief. Example requirement: “Answer questions about the published travel policy; abstain when the evidence is missing.”

Choose an owner for product scope, data permissions, implementation, and review. Decide which documents may be sent to which model providers. Use synthetic documents for initial exercises.

## 2. Run the offline lab — 20 minutes

From the repository root:

```sh
python3 examples/offline_lab.py
python3 -m unittest discover -s tests -v
```

Expected scenarios: a fresh answer, an exact cache hit, a tenant-isolated miss, a corpus-version miss, an unauthorized rejection, a pending write approval, and fallback after a simulated timeout. All are printed as JSON. The tests check these boundaries independently of the demonstration output.

Open `examples/offline_lab.py`. Follow `answer()` from authorization through cache, routing, generation, and validation. Find the cache key. Explain why a query alone would be unsafe as a key. Change the corpus version and observe a miss. Compare the `basic` and `advanced` route values.

This is an executable teaching model: identity is passed by the caller, policy is simple Python, and providers return fixed text. The semantic-cache, CDC, retrieval, and real approval components are design exercises below, not implemented features.

## 3. Design the real read-only baseline — 45 minutes

Copy `templates/design-brief.md` into `designs/<project>.md`. Fill in users, authorized sources, exclusions, and acceptance criteria. Use `skills/system-design/SKILL.md` with your coding assistant, or follow it manually.

Specify the API request and response. Derive user and tenant identity from a verified server session, never from client-supplied JSON. Return answer, citations, source versions, and request ID. Define what happens when evidence is insufficient.

Implement one provider adapter and authorized retrieval first. Validate output shape and citation IDs. Keep write tools disabled. Store provider credentials in the platform secret store; never put them in this public repository.

## 4. Add evidence and controlled complexity — 45 minutes

Create a synthetic evaluation set with ordinary questions, unsupported questions, conflicting sources, prompt injection, and cross-tenant requests. Use `skills/evaluation/SKILL.md`. Record dataset version, prompt/model versions, grounded-answer rate, abstention behavior, p95 latency, and cost per successful answer. Define release thresholds before looking at results.

Then use the routing/fallback skill to add one route and one failure drill. Use the retrieval/freshness skill to test a source update, delete, and permission revocation. Use the guardrails skill to test hostile retrieved text and malformed tool requests.

For caching, start with exact reuse of non-sensitive read-only answers. Invalidate on source, prompt, model, and permission changes. Consider semantic caching only if repeat traffic warrants it; test similar-looking questions with different dates, entities, and negations before enabling it.

## 5. Practice approval — 30 minutes

Propose one write operation such as creating a draft support ticket. Use `skills/human-approval/SKILL.md`. Draw pending → approved → executing → completed transitions, including rejected, expired, and failed outcomes. Bind approval to the exact payload. Demonstrate that editing the payload, replaying execution, or losing permission prevents another write.

Do not make the model the approval authority. Start with draft-only behavior until the executor and approval state machine are verified.

## 6. Open a reviewable PR — 20 minutes

Include the design brief, implementation or clearly labeled proposal, evaluation evidence, failure drills, and rollout/rollback plan. Use the repository PR template. A reviewer should be able to run the commands and see the same result.

## Team workshop

| Exercise | Deliverable | Pass condition |
|---|---|---|
| Request trace | Annotated architecture | Identifies auth, retrieval ACLs, output checks, and writes |
| Freshness drill | Before/after query and event evidence | Old/deleted/revoked data stops appearing |
| Provider outage | Redacted trace | Deadline and permitted fallback respected |
| Injection drill | Malicious synthetic document | Text cannot grant tool permissions |
| Approval replay | Execution receipt | At most one side effect for the idempotency key |
| Evaluation review | Baseline/candidate comparison | Predeclared quality and operational gates met |

Suggested learning path: everyone does the request trace; AI engineers add routing/evaluation; data engineers add freshness; platform engineers add failure/observability; reviewers independently repeat boundary checks.
