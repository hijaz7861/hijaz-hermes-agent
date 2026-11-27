"""Strict free-only OpenRouter adapter for HIJAZ ONE AI Agent.

This is an isolated adapter prototype. It does not yet replace Hermes'
native provider/runtime integration.
"""
from __future__ import annotations

import json
import os
import time
import urllib.error
import urllib.request
from dataclasses import dataclass
from typing import Any, Callable, Iterable


class RouterError(RuntimeError):
    pass


class ProviderError(RouterError):
    def __init__(self, status: int | None, message: str):
        super().__init__(message)
        self.status = status

    @property
    def retryable(self) -> bool:
        return self.status is None or self.status in {408, 409, 425, 429, 500, 502, 503, 504}


@dataclass(frozen=True)
class FreeModel:
    model_id: str
    context_length: int | None = None


class OpenRouterFreeRouter:
    """Discover zero-priced models and fail over only between verified free models."""

    def __init__(
        self,
        api_key: str | None = None,
        *,
        base_url: str = "https://openrouter.ai/api/v1",
        timeout: float = 45.0,
        max_attempts: int = 4,
        sleep: Callable[[float], None] = time.sleep,
        opener: Callable[..., Any] = urllib.request.urlopen,
    ) -> None:
        self.api_key = api_key or os.getenv("OPENROUTER_API_KEY")
        if not self.api_key:
            raise RouterError("OPENROUTER_API_KEY is required; no unauthenticated API access is assumed.")
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout
        self.max_attempts = max(1, max_attempts)
        self.sleep = sleep
        self.opener = opener

    @staticmethod
    def _is_zero_price(value: Any) -> bool:
        try:
            return float(value) == 0.0
        except (TypeError, ValueError):
            return False

    def _request_json(self, path: str, payload: dict[str, Any] | None = None) -> dict[str, Any]:
        body = None if payload is None else json.dumps(payload).encode("utf-8")
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Accept": "application/json",
        }
        if body is not None:
            headers["Content-Type"] = "application/json"
        request = urllib.request.Request(
            f"{self.base_url}{path}", data=body, headers=headers,
            method="GET" if body is None else "POST",
        )
        try:
            with self.opener(request, timeout=self.timeout) as response:
                return json.loads(response.read().decode("utf-8"))
        except urllib.error.HTTPError as exc:
            detail = exc.read().decode("utf-8", errors="replace")
            raise ProviderError(exc.code, detail or f"HTTP {exc.code}") from exc
        except (urllib.error.URLError, TimeoutError, OSError) as exc:
            raise ProviderError(None, str(exc)) from exc
        except (json.JSONDecodeError, UnicodeDecodeError) as exc:
            raise RouterError(f"Provider returned invalid JSON: {exc}") from exc

    def discover_free_models(self) -> list[FreeModel]:
        """Return only models whose published input AND output token prices are zero."""
        response = self._request_json("/models")
        entries = response.get("data")
        if not isinstance(entries, list):
            raise RouterError("OpenRouter model catalogue response has no data array.")
        free: list[FreeModel] = []
        for entry in entries:
            if not isinstance(entry, dict) or not isinstance(entry.get("id"), str):
                continue
            pricing = entry.get("pricing")
            if not isinstance(pricing, dict):
                continue
            if not (
                self._is_zero_price(pricing.get("prompt"))
                and self._is_zero_price(pricing.get("completion"))
            ):
                continue
            context = entry.get("context_length")
            free.append(FreeModel(entry["id"], context if isinstance(context, int) else None))
        return free

    def complete(
        self,
        messages: list[dict[str, Any]],
        *,
        preferred_models: Iterable[str] | None = None,
        temperature: float = 0.2,
        max_tokens: int | None = None,
        tools: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        """Call verified free models in order; fail over on transient/provider errors."""
        if not isinstance(messages, list) or not messages:
            raise RouterError("messages must be a non-empty list.")
        catalogue = self.discover_free_models()
        by_id = {model.model_id: model for model in catalogue}
        if preferred_models is None:
            candidates = catalogue
        else:
            # User preferences can reorder the verified free catalogue, never add unverified IDs.
            candidates = [by_id[mid] for mid in preferred_models if mid in by_id]
        if not candidates:
            raise RouterError("No verified zero-priced models are currently available.")

        failures: list[str] = []
        for attempt, model in enumerate(candidates[: self.max_attempts]):
            payload: dict[str, Any] = {
                "model": model.model_id,
                "messages": messages,
                "temperature": temperature,
            }
            if max_tokens is not None:
                payload["max_tokens"] = max_tokens
            if tools is not None:
                payload["tools"] = tools
            try:
                return self._request_json("/chat/completions", payload)
            except ProviderError as exc:
                failures.append(f"{model.model_id}: HTTP {exc.status or 'network'}: {exc}")
                if not exc.retryable:
                    raise
                if attempt + 1 < min(len(candidates), self.max_attempts):
                    self.sleep(min(2 ** attempt, 8))
        raise RouterError("All verified free models failed: " + " | ".join(failures))
