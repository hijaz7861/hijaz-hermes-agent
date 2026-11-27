---
name: refactor-with-verification
description: Refactor code with built-in test verification — combining code refactoring with autonomous testing to ensure every transformation is behavior-preserving and fully tested before and after.
version: 1.0.0
tags: [refactoring, testing, verification, code-quality, maintainability]
dependencies: [code-refactorer, autonomous-testing]
---

# Refactor with Verification

## Objective
Combine code refactoring with autonomous testing to perform behavior-preserving transformations where every change is verified by tests that pass before and after. Adds test coverage where gaps exist before refactoring.

## Trigger
- "Refactor module X with full test verification"
- "Extract method and verify with tests"
- "Refactor safely — tests must pass before and after"
- "Improve code structure with test coverage"

Anti-triggers: "Refactor without tests" / "Change behavior during refactor" — violates the verification-first principle.

## Inputs
- Target: file, function, class, or symbol to refactor
- Transformation: extract, rename, inline, move, introduce-parameter/object
- Scope: affected files/modules
- Test requirement: coverage threshold for refactored code

## Outputs
- Refactor plan: transformation, affected files, behavior contract
- Test coverage gap report: tests needed before refactor
- Diff: minimal scoped changes
- Verification: test results before and after (100% pass)
- Risk assessment: API surface affected, breakage potential

## Procedure
1. **Analyze the target** (code-refactorer)
   - Read target code, callers, tests, dependents.
   - Identify public interface; record behavior contract.
   - Note test coverage; identify gaps.

2. **Establish test baseline** (autonomous-testing)
   - Run all tests covering target; record pass/fail.
   - Run lint, typecheck, build; record results.
   - If coverage insufficient, add characterization tests first (requires approval).

3. **Design the refactor** (code-refactorer)
   - Choose smallest transformation improving structure.
   - Define behavior contract that must remain identical.
   - Map every caller/dependent referencing changed symbols.

4. **Add characterization tests if needed** (autonomous-testing)
   - For untested behavior: add tests capturing current outputs.
   - Tests must pass before refactor (establish baseline).

5. **Apply the transformation** (code-refactorer)
   - Make minimal, scoped edits; one transformation at a time.
   - Preserve public interfaces unless explicitly authorized.
   - Update all callers/dependents consistently.

6. **Verify** (autonomous-testing + code-refactorer)
   - Re-run all tests covering target + dependents; require 100% pass.
   - Run lint, typecheck, build; require clean.
   - Confirm behavior contract unchanged.
   - Inspect diff: no unrelated changes, no secrets.

7. **Report**
   - Produce refactor report: transformation, files changed, before/after metrics, verification results.

## Safety & Approval Gates
- **Behavior-preserving only:** No external behavior change without explicit approval.
- **Test gate:** Refactor not complete until tests pass before and after.
- **One transformation at a time:** No batching unrelated refactors.
- **Rollback:** Record pre-refactor state; revert if tests fail.

## Failure Handling
- Insufficient test coverage → Add characterization tests (with approval) or mark unsafe.
- Test failure after refactor → Revert immediately, report, do not proceed.
- Typecheck/build failure → Revert, fix or abort, report.
- Caller missed → Report incomplete refactor; identify missing callers.

## Completion Criteria
- Transformation applied and verified across all affected files.
- Tests pass before and after (same coverage, same pass/fail).
- Lint, typecheck, build clean.
- Behavior contract preserved and documented.
- Report produced with verification evidence.
