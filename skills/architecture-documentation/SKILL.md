---
name: architecture-documentation
description: Map a repository's architecture with codebase intelligence, then synthesize comprehensive documentation — combining structural analysis with doc generation to produce accurate, up-to-date architecture overviews and API references.
version: 1.0.0
tags: [documentation, architecture, codebase-intelligence, mapping, api-docs]
dependencies: [codebase-intelligence, documentation-synthesizer]
---

# Architecture Documentation

## Objective
Combine codebase intelligence mapping with documentation synthesis to produce accurate architecture overviews, module documentation, and API references directly from source code. Documents only what the code actually does; never invents behavior.

## Trigger
- "Document this repository's architecture"
- "Generate architecture overview for module X"
- "Create API docs from code"
- "Sync documentation with current code structure"

Anti-triggers: "Write marketing copy" / "Create tutorial content" / "Document behavior that doesn't exist" — requires human-authored content.

## Inputs
- Target: repository, module, or package to document
- Format: markdown, architecture overview, API reference, inline docstrings
- Audience: developers, operators, or consumers

## Outputs
- Architecture map: modules, dependencies, data flow, entry points, risk areas
- Generated documentation: module overviews, API reference, usage examples
- Coverage report: documented vs. undocumented public symbols
- Staleness report: contradictions between existing docs and code

## Procedure
1. **Map the codebase** (codebase-intelligence)
   - Establish context: repo root, branch, working-tree status.
   - Map structure: directories, languages, entry points, dependencies.
   - Trace target: features, data flow, trust boundaries, external services.
   - Establish baseline: test, lint, build commands.

2. **Extract code contracts** (documentation-synthesizer)
   - Inventory public symbols: functions, classes, methods, types, constants.
   - Read implementations to confirm behavior (not just signatures).
   - Capture usage patterns from tests and callers as real examples.

3. **Synthesize documentation** (documentation-synthesizer)
   - Architecture overview: purpose, key abstractions, data flow, dependencies.
   - API reference: one entry per public symbol with signature, params, returns, errors, example.
   - Module overviews: purpose, responsibilities, key files.
   - Use real examples from tests/callers; never invent usage.

4. **Reconcile with existing docs** (documentation-synthesizer)
   - Compare generated content with existing docs.
   - Flag contradictions (doc says X, code does Y).
   - Flag gaps (public symbol with no doc) and staleness.

5. **Report**
   - Produce documentation report: coverage %, staleness findings, files changed, symbols documented.

## Safety & Approval Gates
- **Code-as-source-of-truth:** Document only what code does; never invent behavior.
- **No secret exposure:** Document that credentials exist, not their values.
- **Approval required** before writing docs to repo.
- **Read-only analysis by default.**

## Failure Handling
- Dynamic behavior (metaprogramming, reflection) → Mark as "document manually."
- No tests/callers for examples → State "no usage example found," do not invent.
- Conflicting docs → Report conflict, request human decision; do not auto-resolve.
- Doc tool unavailable → Generate markdown manually from code reading, mark as "unvalidated."

## Completion Criteria
- Architecture map produced with modules, dependencies, data flow.
- Coverage report: % of public symbols documented.
- Staleness report: contradictions between docs and code listed.
- Generated docs verified against code (signatures, examples).
- No secret values in output.
