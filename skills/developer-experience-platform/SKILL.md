---
name: developer-experience-platform
description: Complete developer experience system combining test coverage analysis, refactoring with verification, architecture documentation, and code refactoring. Analyzes coverage gaps, performs verified refactoring, generates architecture docs, and improves code maintainability — all with test gates and quality verification.
version: 1.0.0
tags: [developer-experience, refactoring, documentation, testing, coverage, maintainability]
dependencies: [test-coverage-analyzer, refactor-with-verification, architecture-documentation, code-refactorer]
---

# Developer Experience Platform

## Objective
Combine test coverage analysis, refactoring with verification, architecture documentation, and code refactoring into a unified developer experience platform. Identifies test coverage gaps, performs behavior-preserving refactoring with test verification, generates accurate architecture documentation from code, and improves overall code maintainability — all with test gates and quality verification at every step.

## Trigger
- "Improve developer experience for module X"
- "Analyze coverage, refactor safely, and document architecture"
- "DX improvement: coverage + refactoring + documentation"
- "Make codebase more maintainable with verified changes"

Anti-triggers: "Rewrite codebase without tests" / "Generate docs without code analysis" — violates the verification-first DX principle.

## Inputs
- Target: module, package, or repository to improve
- Coverage threshold: minimum acceptable coverage percentage
- Refactoring goals: extract methods, reduce complexity, improve naming
- Documentation format: markdown, API reference, architecture overview
- Quality thresholds: test pass rate, typecheck clean, lint clean

## Outputs
- DX improvement report: coverage gaps, refactorings applied, documentation generated
- Coverage analysis: gaps, risk classification, test recommendations
- Refactoring results: transformations applied, before/after metrics, test verification
- Architecture documentation: module overview, API reference, data flow, coverage report
- Maintainability metrics: complexity reduction, coverage improvement, documentation coverage

## Procedure
### Phase 1: Test Coverage Analysis (test-coverage-analyzer)
1. Map codebase: modules, functions, classes, entry points, trust boundaries.
2. Analyze existing coverage: tested vs. untested symbols, branches, paths.
3. Identify gaps: untested public functions, error paths, boundary conditions, trust boundaries.
4. Classify gaps: CRITICAL (security boundaries untested), HIGH (critical paths untested), etc.
5. Prioritize recommendations: P0 (security), P1 (regression surface), P2 (edge cases).

### Phase 2: Refactoring with Verification (refactor-with-verification)
1. Analyze refactoring target: public interface, behavior contract, test coverage gaps.
2. Establish test baseline: run existing tests, add characterization tests where needed.
3. Design refactoring: smallest transformation, behavior-preserving, one at a time.
4. Apply refactoring: extract method, rename, inline, move — minimal scoped changes.
5. Verify: tests pass before and after, lint/typecheck/build clean, behavior preserved.
6. Roll back if tests fail or behavior changes.

### Phase 3: Architecture Documentation (architecture-documentation)
1. Map codebase structure: directories, languages, entry points, dependencies.
2. Extract code contracts: public symbols, signatures, parameters, return types, errors.
3. Synthesize documentation: module overview, API reference, data flow, dependencies.
4. Use real examples from tests/callers; never invent usage.
5. Reconcile with existing docs: flag contradictions, gaps, staleness.

### Phase 4: Code Refactoring (code-refactorer)
1. Apply additional refactoring transformations identified in Phase 1-3.
2. Preserve public interfaces unless explicitly authorized to change.
3. Verify each transformation independently with tests.
4. Inspect final diff: no unrelated changes, no secrets, no debug output.

### Phase 5: Integrated DX Assessment
1. Cross-reference findings: coverage gaps addressed by refactoring, documentation accuracy verified against refactored code.
2. Measure maintainability improvement: complexity reduction, coverage increase, documentation coverage.
3. Produce integrated remediation plan: remaining coverage gaps, future refactoring targets, documentation updates.

### Phase 6: Verification and Reporting
1. Re-run test suite: confirm no regressions.
2. Re-measure coverage: confirm improvement.
3. Verify documentation accuracy: signatures match refactored code.
4. Produce final DX report with before/after comparison.

## Safety & Approval Gates
- **Behavior-preserving only:** No external behavior change without explicit approval.
- **Test gate:** Every refactoring verified with tests passing before and after.
- **One transformation at a time:** No batching unrelated refactors.
- **Read-only documentation:** No doc changes without explicit approval.
- **No secret logging:** Documentation and reports exclude credentials, tokens, connection strings.

## Failure Handling
- Insufficient test coverage → add characterization tests (with approval) or mark as unsafe.
- Test failure after refactoring → revert immediately, report, do not proceed.
- Documentation contradiction → report conflict, do not auto-resolve.
- Cannot isolate refactoring target → mark as "ambiguous," recommend clarification.
- Approval denied → stop, report findings only, no changes applied.

## Completion Criteria
- DX improvement report produced with coverage, refactoring, and documentation results.
- Coverage gaps identified with risk classification and test recommendations.
- Refactorings applied and verified (tests pass before and after).
- Architecture documentation generated and verified against code.
- Maintainability metrics documented: complexity, coverage, documentation coverage.
- No secret values in output.
