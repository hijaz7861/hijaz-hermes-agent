# HIJAZ ONE AI Agent — Upstream Runtime Integration Map

## Why this document exists

The GitHub repository `hijaz7861/hijaz-hermes-agent` currently contains a
skills-and-playbooks package and an experimental Python router adapter. It is
not a complete copy of the Hermes runtime.

The runtime foundation remains `NousResearch/hermes-agent`. The upstream
repository was inspected at commit:

`45e9584556a97f50a3cb6394a6e7f6afa97bb66a`

HIJAZ ONE AI Agent is the independent product identity; Hermes remains the
adapted technical runtime foundation with its original licensing and attribution.
Do not build parallel browser, MCP, provider-registry, or agent-loop
implementations until the existing runtime interfaces have been tested.

## Verified upstream capabilities

### 1. Model/provider architecture

Upstream Hermes already has:

- A provider profile registry under `providers/`.
- Provider plugins under `plugins/model-providers/`.
- Runtime provider resolution in `hermes_cli/runtime_provider.py` and related modules.
- OpenAI-compatible chat-completions support for OpenRouter.
- Provider routing configuration under `provider_routing`.
- Existing agent-loop error handling and provider/model fallback paths.

Relevant upstream references:

- `providers/README.md`
- `website/docs/user-guide/features/provider-routing.md`
- `website/docs/developer-guide/agent-loop.md`
- `hermes_cli/runtime_provider_custom.py`

**Integration rule:** extend Hermes' native provider/model-selection path. Do not
introduce a second independent HTTP client into the live agent loop unless the
native extension points prove insufficient.

### 2. Browser / computer environment

Upstream Hermes already provides browser automation through `browser_exec`,
with Chromium controlled through Chrome DevTools Protocol (CDP). Documented modes include:

- Local headless Chromium launched for a Hermes browser session.
- Headed/visible browser mode where the host supports a display.
- Supported cloud browser providers.
- Connecting to an existing Chrome instance through CDP.

Browser sessions can preserve tabs and cookies across calls within their
session. A fresh throwaway profile is the default; authenticated profile use
is a separate explicit configuration.

Relevant upstream reference:

- `website/docs/user-guide/features/browser.md`

**Integration rule:** reuse Hermes' existing browser tool and session model.
Do not install another browser automation stack before testing this path on
the target device/host.

### 3. MCP

Upstream includes an MCP server entry point:

```bash
python -m agent.transports.hermes_tools_mcp_server
```

The documented server exposes a curated set of Hermes tools over stdio MCP.
Its current exposed list intentionally excludes some host-sensitive or
agent-context-bound tools, including terminal/file operations and
`browser_exec` in that specific Codex-facing transport.

Relevant upstream reference:

- `agent/transports/hermes_tools_mcp_server.py`

**Integration rule:** inventory the existing MCP transports and their tool
allowlists before adding another MCP server. MCP is a tool protocol; it does
not provide an LLM or grant access to a ChatGPT model.

### 4. ChatGPT browser conversation

A browser session may be used to open ChatGPT after the account owner signs in.
This is a UI-automation experiment, not a native Hermes provider and not a
guaranteed machine-to-machine API.

Requirements and constraints:

- The user signs in interactively; never collect or store the user's ChatGPT password.
- Do not scrape session cookies or extract authentication tokens.
- Browser UI changes, login challenges, account limits, and session expiry can interrupt the flow.
- Keep a structured task packet and response parser so the workflow can resume safely.
- Require user approval before sending sensitive repository contents or performing external actions.
- Do not claim that a new browser tab automatically shares the history of the user's current ChatGPT conversation.
- This route is separate from OpenRouter and does not make OpenRouter inference free or unlimited.

## Free-only model policy

The experimental adapter in `runtime/openrouter_free.py` is intentionally strict:

1. Read the live OpenRouter model catalogue.
2. Accept only entries with zero published input and output token prices.
3. Verify preferred IDs against that catalogue.
4. Use bounded failover only among verified free candidates.
5. Fail closed if no verified free candidate remains.
6. Never silently fall back to a paid model.

OpenRouter still requires an API key for API access, including zero-priced model
calls. Free model access is subject to current provider availability and quotas.

Hermes' `provider_routing.sort: price` can influence underlying provider
selection, but price-sorted provider routing alone is not proof that a model
is free. Keep the explicit zero-price gate.

## Integration sequence

| Phase | Work | Acceptance evidence |
|---|---|---|
| 0 | Verify local Hermes checkout, remotes, branch, commit, dirty files and runtime version | Captured diagnostics; no destructive changes |
| 1 | Run the free-only router unit tests and add mocked HTTP integration tests | All tests pass without paid calls |
| 2 | Map Hermes provider profile and fallback extension points | Exact files/functions and compatibility tests |
| 3 | Integrate free-only model eligibility into native provider/model selection | Runtime selects only verified zero-price models |
| 4 | Verify task persistence and resume behavior across model switches | Interrupted task resumes with tool results/checkpoints intact |
| 5 | Reuse native browser sessions for authorized web work | Browser navigation, screenshots and session tests pass |
| 6 | Inventory and expose the required MCP tools safely | MCP client can list/call only approved tools |
| 7 | Prototype ChatGPT UI handoff with manual sign-in | Explicitly user-authorized exchange; no credential extraction |
| 8 | End-to-end acceptance test on the actual target environment | Task completed, tests run, artifacts and audit report returned |

## Non-goals and safety boundaries

- No paid API model may be used as an automatic fallback under the free-only policy.
- No claim of unlimited free tokens or guaranteed uninterrupted provider availability.
- No automatic merging, production deployment, credential changes, or destructive filesystem actions.
- No duplicate browser, MCP, or model-provider implementation until upstream capability gaps are demonstrated.
- No installation on the user's phone until the existing environment and available storage are checked.

## Immediate next action

The local checkout must be identified before connecting this skills package to it
or changing its Git remotes. The local Termux audit is separate from this GitHub
repository and must not be treated as a clean or synchronized checkout.
