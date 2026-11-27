---
name: test-coverage-analyzer
description: Analyze test coverage gaps by combining codebase intelligence mapping with autonomous testing prioritization. Identifies untested code paths, recommends targeted tests, and verifies coverage improvement.
version: 1.0.0
tags: [testing, coverage, analysis, gap-analysis, quality]
dependencies: [codebase-intelligence, autonomous-testing]
---

# Test Coverage Analyzer

## Objective
Combine codebase mapping with risk-based testing to identify untested code paths, recommend targeted tests, and verify coverage improvement. Every gap is mapped to a specific file:line with a test recommendation.

## Trigger
- "Analyze test coverage gaps in module X"
- "Find untested code paths in the repo"
- "Recommend tests for uncovered areas"
- "Improve coverage for component Y"

Anti-triggers: "Write all tests automatically" / "Achieve 100% coverage without analysis" — those require a separate test generation task, not gap analysis.

## Inputs
- Target: file, module, package, or repository to analyze
- Coverage threshold: minimum acceptable coverage percentage
- Existing coverage data: coverage reports if available

## Outputs
- Coverage gap report: file:line, uncovered code, risk level, test recommendation
- Prioritized test recommendations: P0 (critical paths), P1 (regression surface), P2 (edge cases)
- Verification: before/after coverage comparison for applied recommendations

## Procedure
1. **Map the codebase** (codebase-intelligence)
   - Identify all modules, functions, classes, entry points, and trust boundaries.
   - Trace data flow: external input → validation → business logic → persistence → output.
   - Identify risk areas: auth, payments, data mutation, security boundaries, external integrations.

2. **Analyze existing coverage** (autonomous-testing)
   - Read existing coverage reports if available (coverage directory, lcov, cobertura, etc.).
   - Identify tested vs. untested files, functions, and branches.
   - Record baseline coverage percentage per module.

3. **Identify gaps** (codebase-intelligence + autonomous-testing)
   - Map each public symbol to its test coverage status.
   - Flag: untested public functions, untested error paths, untested boundary conditions, untested trust boundaries.
   - Classify each gap: CRITICAL (security boundary untested), HIGH (critical path untested), MEDIUM (logic untested), LOW (trivial untested).

4. **Prioritize recommendations**
   - P0: Security boundaries, auth, payment, data mutation — no tests.
   - P1: Changed logic, modified contracts, config changes — regression surface.
   - P2: Edge cases, boundary values, negative tests, error handling.

5. **Generate test recommendations**
   - For each gap: test type (unit/integration/contract/E2E), test scenario, expected assertions, file:line target.
   - Use real examples from existing tests as templates where available.

6. **Verify**
   - Apply recommendations (with approval) and re-measure coverage.
   - Confirm coverage improvement meets the declared threshold.
   - Run full test suite to ensure no regressions.

7. **Report**
   - Produce coverage gap report: baseline, gaps table, recommendations, before/after verification.

## Safety & Approval Gates
- **Analysis is read-only:** No code changes without explicit approval.
- **Test gate:** Coverage improvement claims require before/after measurement.
- **No production mutation:** Analyze on staging or local copies.

## Failure Handling
- No coverage data available → Perform static analysis only, mark as "estimated."
- Coverage tool unavailable → Map untested symbols manually, mark as "unverified."
- Cannot access test files → Report gaps based on code structure, mark test recommendations as "pending test file creation."

## Completion Criteria
- Coverage gap report produced with at least one identified gap (file:line, risk, recommendation).
- Each recommendation has test type, scenario, and target location.
- Baseline and target coverage percentages documented.
- No secret values in output.
