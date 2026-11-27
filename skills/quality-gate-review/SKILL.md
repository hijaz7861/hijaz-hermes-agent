---
name: quality-gate-review
description: Perform gated code review by combining multi-agent review roles with autonomous testing validation. Ensures changes pass both independent review AND test execution before approval.
version: 1.0.0
tags: [review, quality, gates, testing, governance]
dependencies: [multi-agent-review, autonomous-testing]
---

# Quality Gate Review

## Objective
Combine multi-agent review with autonomous testing to enforce a quality gate: no change is approved unless it passes both independent security/correctness review AND test execution. Combines adversarial review with empirical test evidence.

## Trigger
- "Review PR #X with quality gate — tests must pass"
- "Gate this change: review + test before merge"
- "Quality review for module Y — security and tests"
- "Review and validate change Z before release"

Anti-triggers: "Review without tests" / "Tests without review" — those are multi-agent-review or autonomous-testing alone, not the combined gate.

## Inputs
- Change: diff, PR number, or file scope
- Acceptance criteria: functional, security, performance requirements
- Test requirements: which test suites must pass
- Gate threshold: pass/fail criteria (e.g., 100% of affected tests, no CRITICAL findings)

## Outputs
- Review findings: ID, file:line, severity, evidence, remediation (from Reviewer role)
- Test evidence: pass/fail matrix, coverage impact, failure details (from Test Analyst + autonomous-testing)
- Consolidated gate decision: PASS / FAIL / BLOCKED with rationale
- Post-fix re-verification: confirm fixes resolved findings and tests pass

## Procedure
1. **Define scope and gate criteria** (multi-agent-review Coordinator)
   - Define acceptance criteria and file ownership before delegation.
   - Set gate threshold: what constitutes "pass" (test pass rate, severity allowance).
   - Identify which test suites must execute.

2. **Delegate review roles** (multi-agent-review)
   - Reviewer: inspects diff against correctness, security, maintainability checklist.
   - Test Analyst: designs risk-based test cases, identifies edge cases.
   - Each worker returns findings with file paths, line references, severity, evidence.

3. **Execute tests** (autonomous-testing)
   - Run all tests covering the changed files and their dependents.
   - Run lint, typecheck, build; require clean.
   - Record pass/fail matrix, coverage impact, failure details.
   - Include negative and boundary cases for changed logic.

4. **Consolidate findings and evidence**
   - Cross-reference review findings with test results.
   - Flag: finding with no test coverage, test failure with no review finding.
   - Classify: CRITICAL/HIGH/MEDIUM/LOW findings; PASS/FAIL test status.

5. **Apply gate decision**
   - PASS: All CRITICAL/HIGH findings resolved, all tests pass.
   - FAIL: CRITICAL/HIGH findings unresolved OR tests failing.
   - BLOCKED: Cannot complete review or testing (missing info, tool failure).

6. **Re-verify after fixes**
   - Author applies fixes for findings and test failures.
   - Re-run review (affected files only) and tests.
   - Confirm gate criteria now met.

7. **Report**
   - Produce quality gate report: review findings, test evidence, gate decision, re-verification results.

## Safety & Approval Gates
- **Approval required** before any code change based on review findings.
- **Gate is mandatory:** Changes cannot bypass review or testing.
- **No secret logging:** Finding location and redacted context only; never secret values.
- **No worker merges or deploys** without explicit authorization.

## Failure Handling
- Reviewer and Test Analyst disagree → Coordinator resolves, documents rationale.
- Tests flaky → Mark as "flaky," recommend isolation, do not gate-pass on flaky results.
- Test suite unavailable → Mark as "blocked," require test infrastructure.
- Approval denied → Stop, report findings only, no changes applied.

## Completion Criteria
- Gate decision explicitly recorded: PASS / FAIL / BLOCKED.
- All CRITICAL/HIGH findings resolved or explicitly accepted with documented risk.
- Test evidence recorded for all changed files and dependents.
- Post-fix re-verification confirms gate criteria met.
- No secret values in output.
