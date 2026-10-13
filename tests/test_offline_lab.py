import unittest
from examples.offline_lab import Lab, Request


class BoundaryTests(unittest.TestCase):
    def setUp(self):
        self.lab = Lab()
        self.query = "Leave policy?"

    def test_exact_hit_avoids_another_provider_call(self):
        self.lab.answer(Request("a", self.query))
        before = len(self.lab.calls)
        self.assertTrue(self.lab.answer(Request("a", self.query))["cache_hit"])
        self.assertEqual(len(self.lab.calls), before)

    def test_tenant_and_versions_prevent_reuse(self):
        self.lab.answer(Request("a", self.query))
        for request in (Request("b", self.query),
                        Request("a", self.query, permission_version="acl-v2"),
                        Request("a", self.query, corpus_version="docs-v2"),
                        Request("a", self.query, task="advanced")):
            with self.subTest(request=request):
                self.assertFalse(self.lab.answer(request)["cache_hit"])

    def test_denial_precedes_cache_and_provider(self):
        self.lab.answer(Request("a", self.query))
        before = len(self.lab.calls)
        self.assertEqual(self.lab.answer(Request("a", self.query, authorized=False)),
                         {"status": "denied"})
        self.assertEqual(len(self.lab.calls), before)

    def test_write_never_calls_model_or_executes(self):
        result = self.lab.answer(Request("a", "Publish", action="write"))
        self.assertEqual(result["status"], "pending_approval")
        self.assertFalse(result["executed"])
        self.assertEqual(self.lab.calls, [])

    def test_outage_uses_one_approved_fallback(self):
        result = self.lab.answer(Request("a", self.query), primary_down=True)
        self.assertTrue(result["fallback"])
        self.assertEqual(self.lab.calls, ["primary-down", "approved-backup"])

    def test_policy_denial_does_not_trigger_fallback(self):
        result = self.lab.answer(Request("a", self.query, authorized=False), primary_down=True)
        self.assertEqual(result["status"], "denied")
        self.assertEqual(self.lab.calls, [])

    def test_corrupt_cached_output_is_rejected(self):
        self.lab.answer(Request("a", self.query))
        key = next(iter(self.lab.cache))
        self.lab.cache[key] = {"answer": "Unsupported", "citations": ["invented"]}
        self.assertEqual(self.lab.answer(Request("a", self.query))["status"], "invalid_output")

    def test_unknown_action_is_rejected(self):
        self.assertEqual(self.lab.answer(Request("a", self.query, action="delete"))["status"],
                         "invalid_action")
        self.assertEqual(self.lab.calls, [])


if __name__ == "__main__":
    unittest.main()
