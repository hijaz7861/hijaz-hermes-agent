---
name: debug-performance
description: Debug performance-related defects — combining autonomous debugging with performance profiling to reproduce slow behavior, find root cause, and apply verified performance fixes with regression benchmarks.
version: 1.0.0
tags: [debugging, performance, profiling, root-cause, regression]
dependencies: [autonomous-debugging, performance-profiler]
---

# Debug Performance

## Objective
Combine autonomous debugging with performance profiling to diagnose performance defects (slow endpoints, high CPU, memory leaks, latency spikes). Reproduce the performance issue, find the root cause, apply a minimal fix, and verify with before/after benchmarks.

## Trigger
- "Debug why endpoint X is slow"
- "Find the performance regression in module Y"
- "Debug high CPU/memory usage in component Z"
- "Performance issue: reproduce, diagnose, fix, benchmark"

Anti-triggers: "Optimize everything" / "Profile without a reported issue" — those are performance-optimization, not defect debugging.

## Inputs
- Performance issue: error, slow endpoint, high resource usage, latency spike
- Reproduction steps or workload
- Environment details
- Acceptable performance target

## Outputs
- Reproduction evidence: exact commands, workload, observed performance
- Root cause: file:line, explanation, evidence
- Fix: minimal patch, before/after benchmarks
- Regression test: performance test that fails before, passes after
- Verification: test suite, lint, typecheck, build results

## Procedure
1. **Capture the performance failure** (autonomous-debugging)
   - Obtain exact error, expected vs. actual performance, environment.
   - Identify deterministic reproduction path. If impossible, state hypotheses.

2. **Establish performance baseline** (performance-profiler)
   - Profile the failing path under load.
   - Record: wall time, CPU, memory, allocations per request/iteration.
   - Distinguish pre-existing slowness from newly introduced regression.

3. **Form hypotheses** (autonomous-debugging)
   - Rank likely causes: N+1 queries, inefficient algorithms, locking, allocations, external calls.
   - Trace failing input through code and dependencies.

4. **Profile to confirm** (performance-profiler)
   - Use profiler to confirm each hypothesis with measurements.
   - Record top bottlenecks with file:line and % of total time.

5. **Test one cause at a time** (autonomous-debugging)
   - Prefer focused experiment: add instrumentation, isolate the hot path.
   - Avoid unrelated refactors.

6. **Implement the fix** (autonomous-debugging + code-refactorer principles)
   - Add regression test that fails before fix, passes after.
   - Smallest safe patch; preserve public interfaces.

7. **Verify** (performance-profiler + autonomous-debugging)
   - Re-run reproduction: performance now meets target.
   - Before/after benchmarks with statistical significance.
   - Run full test suite, lint, typecheck, build.

8. **Report**
   - State root cause, fix, benchmarks, remaining risks.

## Safety & Approval Gates
- **Approval required** before any code change.
- **Rollback:** Record pre-fix state; revert if benchmarks degrade or tests fail.
- **No production mutation:** Profile on staging or synthetic workloads.
- **No secret logging:** Profiling output may contain sensitive data; redact.

## Failure Handling
- Cannot reproduce → State why, continue with labeled hypotheses only.
- Profiler unavailable → Manual timing, mark as approximate.
- Fix breaks tests → Revert, report, do not proceed.
- No measurable improvement → Report "fix did not resolve," continue investigation.

## Completion Criteria
- Original performance failure no longer reproducible.
- Regression test protects the behavior (fails before, passes after).
- Before/after benchmarks show improvement.
- Diff contains only justified changes.
