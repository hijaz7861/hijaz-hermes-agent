# HIJAZ ONE AI Agent — Free-only OpenRouter adapter

## Status

This is the first executable model-routing prototype for HIJAZ ONE AI Agent.
It is deliberately isolated: it does **not** yet replace or modify the adapted
upstream Hermes runtime's native model/provider layer.

## Guarantees

- Requires an `OPENROUTER_API_KEY`; it does not pretend MCP or a browser session grants API access.
- Reads the live OpenRouter `/models` catalogue.
- Allows only model entries whose published `pricing.prompt` and
  `pricing.completion` values both parse to exactly zero.
- Rejects preferred model IDs that are not in that verified free catalogue.
- Tries a bounded sequence of eligible models after retryable network, rate-limit,
  and server errors.
- Does not retry authentication/authorization failures.
- Never falls back to a paid model.
- Keeps the caller's messages unchanged across attempts.

## Run tests

From the repository root:

```bash
python -m unittest discover -s tests -v
```

## Configure

Set `OPENROUTER_API_KEY` in the process environment. Do not commit keys or put
them in shell history. The key is required even when selecting zero-priced models;
free model access is still subject to the account's current provider limits.

## Known limitations before runtime integration

1. This adapter is a synchronous Python prototype, not yet wired into the upstream
   Hermes provider registry, subagent spawning, or task checkpoint system.
2. It uses published catalogue pricing as the free-only gate. Provider limits,
   availability, context size, tool support, and free-tier policies can change.
3. A successful model switch preserves the submitted messages, but a caller must
   persist workflow state, tool results, and checkpoints outside this adapter.
4. Browser-based ChatGPT interaction and MCP tool connectivity are separate
   integrations; this adapter does not provide either.
5. If the free catalogue is empty or all eligible models fail, it stops safely
   and reports failure rather than silently using a paid model.

## Next integration gates

- Verify the upstream Hermes provider adapter interface and supported Python version.
- Add a compatibility layer with explicit capability checks for tool calling.
- Persist task state outside model-specific conversation state.
- Add integration tests against a mocked OpenRouter-compatible HTTP server.
- Verify actual free-model availability before enabling unattended workloads.
