---
name: code-refactorer
description: Perform safe, behavior-preserving code transformations (extract method, rename, inline, move, introduce parameter/object) with test verification. Use for improving code structure without changing external behavior.
version: 1.0.0
tags: [refactoring, code-quality, maintainability, transformation, verification]
---

# Code Refactorer

## Objective
Improve code structure, readability, and maintainability through behavior-preserving transformations. Every refactor is verified by tests that pass before and after; no behavior change without explicit authorization.

## Trigger
- "Refactor this module for clarity"
- "Extract method from function X"
- "Rename symbol Y across codebase"
- "Reduce complexity in file Z"
- "Improve maintainability of component W"

Anti-triggers: "Rewrite module X" / "Change behavior of function Y" / "Rewrite in another language" — those are not refactors; they require a separate implementation task with behavior-change approval.

## Inputs
- Target: file, function, class, or symbol to refactor
- Transformation: specific refactor type (extract, rename, inline, move, introduce-parameter, etc.)
- Scope: files/modules affected
- Constraints: public API stability, test coverage requirement, time budget

## Outputs
- Refactor plan: transformation, affected files, behavior contract (what must stay the same)
- Diff: minimal, scoped changes only
- Verification: test results before and after
- Risk assessment: API surface affected, breakage potential

## Procedure
1. **Analyze the target**
   - Read the target code, its callers, tests, and dependents.
   - Identify the public interface (exports, public methods, types).
   - Record current behavior contract: inputs, outputs, side effects, error handling.
   - Note test coverage for the target; identify gaps.

2. **Establish verification baseline**
   - Run all tests covering the target; record pass/fail.
   - Run lint, typecheck, build; record results.
   - Capture a reference diff of the current state (git diff baseline).
   - If tests are insufficient, add characterization tests first (requires approval).

3. **Design the refactor**
   - Choose the smallest transformation that improves structure.
   - Define the behavior contract that must remain identical.
   - Map every caller/dependent that references changed symbols.
   - Identify edge cases: default parameters, overloads, type constraints, dynamic access.

4. **Apply the transformation**
   - Make minimal, scoped edits; one transformation at a time.
   - Preserve public interfaces unless explicitly authorized to change them.
   - Do not combine refactor with bug fix or feature change.
   - Update all callers/dependents consistently.

5. **Verify**
   - Re-run all tests covering the target + dependents; require 100% pass (same as baseline).
   - Run lint, typecheck, build; require clean.
   - Confirm behavior contract unchanged (same outputs for same inputs).
   - Inspect final diff: no unrelated changes, no secrets, no debug output.

6. **Report**
   - Produce a refactor report: transformation applied, files changed, before/after metrics (lines, complexity, test count), verification results.

## Safety & Approval Gates
- **Behavior-preserving only:** No changes to external behavior without explicit approval.
- **Public API stability:** Do not change exported signatures without explicit approval.
- **Test gate:** Refactor is not complete until tests pass before and after.
- **One transformation at a time:** Do not batch unrelated refactors.
- **Rollback:** Record pre-refactor state; revert if tests fail or behavior changes.

## Failure Handling
- Insufficient test coverage → Add characterization tests (with approval) or mark refactor as "unsafe without tests."
- Test failure after refactor → Revert immediately, report, do not proceed.
- Typecheck/build failure → Revert, fix or abort, report.
- Caller missed → Report incomplete refactor, identify missing callers, request direction.

## Completion Criteria
- Transformation applied and verified across all affected files.
- Tests pass before and after (same coverage, same pass/fail).
- Lint, typecheck, build clean.
- Behavior contract preserved (documented).
- Report produced with verification evidence.
