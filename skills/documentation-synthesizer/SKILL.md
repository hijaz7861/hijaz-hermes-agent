---
name: documentation-synthesizer
description: Generate and update documentation from code: API reference, README sections, inline docstrings, architecture overviews, and integration guides. Use when docs are stale, missing, or need synchronization with code.
version: 1.0.0
tags: [documentation, api-docs, readme, docstrings, architecture]
---

# Documentation Synthesizer

## Objective
Produce accurate, up-to-date documentation directly from source code. Synthesize API references, module overviews, usage examples, and integration guides. Never invent behavior; document only what the code actually does.

## Trigger
- "Generate API docs for module X"
- "Update README with new feature Y"
- "Write docstrings for file Z"
- "Create architecture overview for this repo"
- "Docs are stale, sync them with code"

Anti-triggers: "Write marketing copy" / "Create tutorial content" / "Document behavior that doesn't exist" — those require human-authored content, not code synthesis.

## Inputs
- Target: file, module, package, or repository to document
- Format: markdown, openapi, inline docstrings, README, architecture overview
- Audience: developers, operators, or consumers (affects detail level)
- Existing docs: current README, docstrings, API specs to reconcile

## Outputs
- Generated documentation: API reference, module docs, README sections, docstrings
- Coverage report: documented vs. undocumented public symbols
- Staleness report: docs that contradict current code
- Change list: files created/modified

## Procedure
1. **Inventory the target**
   - List all public symbols: exported functions, classes, methods, types, constants.
   - Identify modules, packages, entry points, and configuration keys.
   - Read existing docs (README, docstrings, API specs) if present.
   - Note language/runtime and doc conventions (JSDoc, docstrings, Godoc, etc.).

2. **Extract code contracts**
   - For each public symbol: signature, parameters, return type, exceptions, side effects.
   - Read implementation to confirm behavior (not just signatures).
   - Identify required vs. optional parameters, defaults, constraints.
   - Capture usage patterns from tests and callers (real examples).

3. **Synthesize documentation**
   - API reference: one entry per public symbol with signature, description, params, returns, errors, example.
   - Module overview: purpose, key abstractions, data flow, dependencies.
   - README sections: installation, quickstart, configuration, usage examples.
   - Inline docstrings: where the language convention supports them.
   - Use real examples from tests/callers; never invent usage.

4. **Reconcile with existing docs**
   - Compare generated content with existing docs.
   - Flag contradictions (doc says X, code does Y).
   - Flag gaps (public symbol with no doc).
   - Flag staleness (doc references removed/renamed symbol).

5. **Review and verify**
   - Check generated examples against code (do they run?).
   - Verify signatures match current code.
   - Confirm no invented behavior or parameters.
   - Run doc validation if available (e.g., doctest, openapi validator).

6. **Report**
   - Produce documentation report: coverage %, staleness findings, files changed, symbols documented/undocumented.

## Safety & Approval Gates
- **Code-as-source-of-truth:** Document only what code does; never invent behavior.
- **No secret exposure:** Do not document credential values, keys, or connection strings (document that they exist, not their values).
- **Approval required before writing docs to repo.**
- **Read-only analysis by default.**

## Failure Handling
- Undocumented dynamic behavior (metaprogramming, reflection) → Mark as "dynamic, document manually."
- No tests/callers for examples → State "no usage example found," do not invent one.
- Conflicting docs → Report conflict, do not auto-resolve; request human decision.
- Build/doc-tool unavailable → Generate markdown manually from code reading, mark as "unvalidated."

## Completion Criteria
- Coverage report produced: % of public symbols documented.
- Staleness report: contradictions between docs and code listed.
- Generated docs verified against code (signatures, examples).
- No secret values in output.
- Report distinguishes verified vs. manually-reviewed content.
