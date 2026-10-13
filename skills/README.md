# Reusable team skills

These are task procedures for AI assistants and human teammates. They are separate from runtime agents in your application. The skills do not install tools, grant permissions, or guarantee automatic discovery by every assistant.

## Use a skill today

Clone this repository and provide the relevant file to your assistant. This explicit prompt works without relying on tool-specific discovery:

> Read `skills/system-design/SKILL.md` and follow it for a read-only internal FAQ assistant. Use `templates/design-brief.md`. Record assumptions and unresolved questions. Produce a design PR proposal; do not provision infrastructure or send real data to providers.

For any assistant, ensure it can read the files and verify it reports the correct skill name. Where your tool supports a project skill directory, copy the relevant **whole skill folder**, preserving `SKILL.md`; consult your installed tool's current documentation for its exact discovery path. Keep this repository as the source of truth and record the source commit when copying. Explicit file loading is the default tutorial path.

| Skill | Use when | Output |
|---|---|---|
| [Agentic BI](agentic-bi/SKILL.md) | Turning BRDs into reviewed BI proposals | Build specification and validation matrix |
| [System design](system-design/SKILL.md) | Starting a use case | Design brief and tradeoffs |
| [Guardrails](guardrails/SKILL.md) | Adding policies or tools | Trust boundaries and abuse cases |
| [Retrieval/freshness](retrieval-freshness/SKILL.md) | Connecting changing documents | Data contract and update/delete drills |
| [Routing/fallback](routing-fallback/SKILL.md) | Selecting models or handling outages | Route policy and bounded failure plan |
| [Human approval](human-approval/SKILL.md) | Enabling write actions | Approval/execution state machine |
| [Evaluation](evaluation/SKILL.md) | Comparing or releasing changes | Versioned evaluation report |
| [Observability](observability/SKILL.md) | Operating or diagnosing a system | Redacted trace schema and runbook |

Use the smallest applicable skill. Run additional skills sequentially when the design requires them. These instructions do not request sub-agent delegation. Avoid parallel edits to the same files.
