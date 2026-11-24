---
name: autonomous-debugging
description: Reproduce and resolve software defects using controlled experiments, root-cause analysis and regression verification. Use for bug reports, failing tests, crashes, incorrect behavior and runtime errors.
---

# Autonomous Debugging

## Objective
Fix the demonstrated root cause with the smallest safe patch. A plausible edit is not a verified fix.

## Procedure
1. **Capture the failure**
   - Obtain the exact error, stack trace, expected behavior, actual behavior and environment.
   - Identify a deterministic reproduction path. If reproduction is impossible, state why and continue only with clearly labeled hypotheses.
2. **Establish baseline**
   - Inspect repository instructions and working-tree changes.
   - Run the narrowest failing test or reproduction before editing.
   - Save the exact command and failure signature.
3. **Form hypotheses**
   - Rank likely causes and identify evidence that would confirm or reject each.
   - Trace the failing input through relevant code and dependencies.
   - Check recent changes and configuration differences when available.
4. **Test one cause at a time**
   - Prefer a focused test, debugger, log, or minimal experiment.
   - Avoid unrelated refactors and speculative multi-file changes.
5. **Implement the fix**
   - Add or update a regression test that fails before the fix where practical.
   - Validate inputs and error handling at trust boundaries.
   - Preserve public interfaces unless a breaking change is explicitly authorized.
6. **Verify**
   - Run the regression test, relevant unit/integration tests, lint/type checks and build as applicable.
   - Inspect the final diff for unrelated changes, secrets, debug output and unsafe behavior.
   - Re-run the original reproduction.
7. **Report**
   - State root cause, changed files, tests run, exact outcomes and remaining risks.
   - Separate verified fixes from hypotheses or checks that could not be run.

## Escalation and approval
Stop and request approval before deleting user data, changing production systems, rotating credentials, altering billing, weakening security controls, or performing irreversible migrations. Never conceal a failed check or disable a test merely to obtain a green result.

## Completion criteria
The original failure is no longer reproducible in the tested environment, a regression check protects the behavior, and the diff contains only justified changes.
