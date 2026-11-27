import unittest

from runtime.openrouter_free import (
    FreeModel,
    OpenRouterFreeRouter,
    ProviderError,
    RouterError,
)


class FakeRouter(OpenRouterFreeRouter):
    def __init__(self, catalogue, responses):
        super().__init__(api_key="test-key", max_attempts=4, sleep=lambda _: None)
        self.catalogue = catalogue
        self.responses = list(responses)
        self.called_models = []

    def discover_free_models(self):
        return self.catalogue

    def _request_json(self, path, payload=None):
        if path == "/models":
            raise AssertionError("FakeRouter overrides catalogue discovery")
        model_id = payload["model"]
        self.called_models.append(model_id)
        result = self.responses.pop(0)
        if isinstance(result, Exception):
            raise result
        return result


class FreeRouterTests(unittest.TestCase):
    def test_only_verified_free_models_can_be_selected(self):
        router = FakeRouter(
            [FreeModel("provider/free-a"), FreeModel("provider/free-b")],
            [{"ok": True}],
        )
        result = router.complete(
            [{"role": "user", "content": "hello"}],
            preferred_models=["provider/paid-model", "provider/free-b"],
        )
        self.assertEqual(result, {"ok": True})
        self.assertEqual(router.called_models, ["provider/free-b"])

    def test_rate_limit_fails_over_to_next_free_model(self):
        router = FakeRouter(
            [FreeModel("provider/free-a"), FreeModel("provider/free-b")],
            [ProviderError(429, "rate limited"), {"choices": [{"message": {"content": "done"}}]}],
        )
        result = router.complete([{"role": "user", "content": "task"}])
        self.assertIn("choices", result)
        self.assertEqual(router.called_models, ["provider/free-a", "provider/free-b"])

    def test_no_verified_free_models_fails_closed(self):
        router = FakeRouter([], [])
        with self.assertRaisesRegex(RouterError, "No verified zero-priced"):
            router.complete([{"role": "user", "content": "task"}])

    def test_non_retryable_auth_error_does_not_rotate(self):
        router = FakeRouter(
            [FreeModel("provider/free-a"), FreeModel("provider/free-b")],
            [ProviderError(401, "unauthorized")],
        )
        with self.assertRaises(ProviderError):
            router.complete([{"role": "user", "content": "task"}])
        self.assertEqual(router.called_models, ["provider/free-a"])


if __name__ == "__main__":
    unittest.main()
