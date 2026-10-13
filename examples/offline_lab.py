"""Offline teaching simulation. Not a real LLM, gateway, or approval service."""
from dataclasses import dataclass
import json


@dataclass(frozen=True)
class Request:
    tenant: str
    query: str
    authorized: bool = True
    permission_version: str = "acl-v1"
    corpus_version: str = "docs-v1"
    task: str = "basic"
    action: str = "read"


class Lab:
    def __init__(self):
        self.cache = {}
        self.calls = []
        self.prompt_version = "prompt-v1"
        self.model_version = "mock-v1"

    def generate(self, query, provider):
        self.calls.append(provider)
        if provider == "primary-down":
            raise TimeoutError("simulated provider timeout")
        return {"answer": "Synthetic policy: 20 days annual leave.", "citations": ["policy-1"]}

    def answer(self, request, primary_down=False):
        # Production must derive this context from a verified identity and ACLs.
        if not request.authorized:
            return {"status": "denied"}
        if request.action not in {"read", "write"}:
            return {"status": "invalid_action"}
        if request.action == "write":
            return {"status": "pending_approval", "executed": False}
        if request.task not in {"basic", "advanced"} or not request.query.strip():
            return {"status": "invalid_request"}
        route = "lightweight" if request.task == "basic" else "reasoning"
        key = (request.tenant, request.permission_version, request.corpus_version,
               self.prompt_version, self.model_version, route, request.query)
        cached = key in self.cache
        fallback = False
        if cached:
            output = self.cache[key]
            provider = "cache"
        else:
            provider = "primary-down" if primary_down else "primary"
            try:
                output = self.generate(request.query, provider)
            except TimeoutError:
                provider = "approved-backup"
                fallback = True
                output = self.generate(request.query, provider)
        # Validate cached responses too; only a synthetic schema/citation check.
        if (not isinstance(output, dict) or not isinstance(output.get("answer"), str)
                or not output["answer"] or output.get("citations") != ["policy-1"]):
            return {"status": "invalid_output"}
        if not cached:
            self.cache[key] = dict(output)
        return {"status": "ok", "route": route, "provider": provider,
                "cache_hit": cached, "fallback": fallback, **output}


def main():
    lab = Lab()
    scenarios = [
        ("fresh", Request("commercial", "Leave policy?"), False),
        ("exact hit", Request("commercial", "Leave policy?"), False),
        ("other tenant", Request("hr", "Leave policy?"), False),
        ("new corpus", Request("commercial", "Leave policy?", corpus_version="docs-v2"), False),
        ("unauthorized", Request("commercial", "Leave policy?", authorized=False), False),
        ("write proposal", Request("commercial", "Publish report", action="write"), False),
        ("provider outage", Request("commercial", "Complex design", task="advanced"), True),
    ]
    for label, request, outage in scenarios:
        print(json.dumps({"scenario": label, **lab.answer(request, outage)}))


if __name__ == "__main__":
    main()
