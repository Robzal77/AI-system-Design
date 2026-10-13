# AI System Design • Team Playbook

Build AI systems the team can explain, test, and operate.

Inspired by [Codebasics: AI System Design Tutorial](https://www.youtube.com/watch?v=S6jy0T85DFs). This repository contains an original team adaptation, not a transcript or a reproduction of the creator's downloadable guide.

## Start here

1. Read the [video review](docs/video-review.md) for the recommendation and source limitations.
2. Follow the [team tutorial](docs/tutorial.md), including the offline lab.
3. Use the [architecture reference](docs/architecture.md) for your first real project.
4. Explore the [architecture diagrams](docs/diagrams.md) and [enterprise AI team guide](docs/enterprise-ai-team.md).
5. Pick a [reusable AI skill](skills/README.md) for the task you are doing.
6. Complete the [design brief](templates/design-brief.md) and open a PR with evidence.

## Run the practice lab

Requires Python 3.10+ and Git; no packages, accounts, or API keys.

```sh
git clone https://github.com/Robzal77/AI-system-Design.git
cd AI-system-Design
python3 examples/offline_lab.py
python3 -m unittest discover -s tests -v
```

The lab simulates policy checks, an exact cache, routing, provider failure, and approval. It does not run a real LLM, implement semantic search, or provide production authentication.

## Team responsibilities

| Role | Owns | Review evidence |
|---|---|---|
| Project lead | Use case, scope, acceptance criteria | Completed design brief |
| AI engineer | Prompt, routing, tool contracts | Golden examples and failure cases |
| Data engineer | Retrieval, source permissions, freshness | Update/delete replay and ACL checks |
| Platform engineer | Gateway, budgets, retries, tracing | Failure drill and redacted trace |
| Reviewer | Evaluation and release decision | Comparison with baseline |

One person can hold multiple roles. Give every project one accountable owner.

## Suggested rollout

- Week 1: Run this lab and design one read-only knowledge assistant.
- Week 2: Add authorized retrieval, citations, and a representative evaluation set.
- Week 3: Add measured routing and a tested fallback; evaluate whether caching helps.
- Week 4: Add one approved write operation, then stage and review the complete flow.

These are planning suggestions, not delivery guarantees. Start with one useful workflow and expand after evidence supports it.
