# HIJAZ ONE AI Agent

Independent AI engineering agent built on an adapted Hermes runtime foundation.

## Product identity

- Product: HIJAZ ONE AI Agent
- Product owner: M Naeem Khan
- Runtime foundation: NousResearch Hermes Agent (adapted; original licensing and attribution preserved)

## Mission

Understand a user's task, plan the work, execute changes, run tests, diagnose failures, repair defects, and report evidence-backed outcomes.

## Product requirements

- Strict free-only model routing with paid-model fallback blocked at every runtime entry point.
- Per-user GitHub authorization and genuine actor attribution for user-initiated writes.
- Isolated credentials and task ownership for each user.
- Persistent task checkpoints and recovery across model changes and interruptions.
- Reuse of the runtime's browser, terminal, filesystem, and MCP capabilities with explicit permission boundaries.
- Safe execution; destructive operations require explicit user approval.
- Android/Termux ARM64 support, alongside supported desktop/server environments.

## Engineering status

The free-only OpenRouter adapter is currently a prototype and is not yet integrated into the native runtime provider registry. GitHub identity and attribution are specified but not yet implemented. Runtime branding and platform compatibility require staged changes and tests.

## Upstream and licensing

The Hermes runtime is an adapted technical foundation. Preserve its MIT license, required copyright notices, upstream attribution, and any applicable third-party notices. Do not claim upstream code as originally authored by HIJAZ ONE AI.
