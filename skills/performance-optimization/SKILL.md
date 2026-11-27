---
name: performance-optimization
description: Profile code to find performance bottlenecks, then refactor the hot paths to eliminate them — combining measurement-driven profiling with behavior-preserving refactoring for verified performance gains.
version: 1.0.0
tags: [performance, optimization, profiling, refactoring, benchmarking]
dependencies: [performance-profiler, code-refactorer]
---

# Performance Optimization

## Objective
Combine performance profiling with safe refactoring to identify bottlenecks and eliminate them through verified, behavior-preserving code changes. Every optimization is measured before and after; no change is accepted without benchmark evidence.

## Trigger
- "Optimize this code for performance"
- "Profile and fix the slow endpoint in X"
- "Reduce latency in module Y"
- "Find and eliminate performance bottlenecks"

Anti-triggers: "Rewrite for performance without measuring" / "Apply micro-optimizations blindly" — violates the measurement-first principle.

## Inputs
- Target: file, module, function, or endpoint to optimize
- Workload: representative input/request pattern
- Constraints: time budget, performance target, acceptable risk

## Outputs
- Baseline profile: bottlenecks with file:line, metric, severity
- Optimization plan: refactor targets, expected impact, effort, risk
- Before/after benchmarks: latency, CPU, memory for each applied change
- Verification: test results confirming behavior is preserved

## Procedure
1. **Profile the target** (performance-profiler)
   - Establish measurement baseline: wall time, CPU, memory, allocations.
   - Use language-appropriate profiler to find hot paths.
   - Record top bottlenecks with file:line and % of total time.

2. **Plan optimizations** (performance-profiler + code-refactorer)
   - Score each bottleneck: impact × likelihood × risk.
   - Prioritize: high-impact low-risk first.
   - Define behavior contract that must be preserved for each refactor.

3. **Refactor hot paths** (code-refactorer)
   - Apply smallest behavior-preserving transformation per bottleneck.
   - One transformation at a time; no combining with unrelated changes.
   - Preserve public interfaces unless explicitly authorized.

4. **Verify each change** (code-refactorer + performance-profiler)
   - Re-run the same workload and measurement suite.
   - Compare before vs. after; require statistical significance (min 3 runs).
   - Run full test suite, lint, typecheck, build.
   - Roll back any change that degrades correctness or introduces new bottlenecks.

5. **Report**
   - Produce optimization report: baseline, bottlenecks, changes applied, before/after benchmarks, risk assessment.

## Safety & Approval Gates
- **Read-only profiling by default:** No code changes without explicit approval.
- **Test gate:** Every refactor verified with tests passing before and after.
- **Rollback required:** Record pre-change state; revert if benchmarks degrade.
- **No production mutation:** Profile on staging or synthetic workloads only.

## Failure Handling
- Profiler unavailable → Manual timing instrumentation, mark as approximate.
- Optimization breaks tests → Revert immediately, report, do not proceed.
- Cannot isolate bottleneck → Report "inconclusive," list candidates.
- No measurable improvement → Report "no significant gain," do not claim optimization.

## Completion Criteria
- Baseline profile with at least one measured hotspot.
- Each optimization has before/after benchmark evidence.
- Tests pass before and after every change.
- Report distinguishes verified improvements from estimates.
