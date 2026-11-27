---
name: performance-profiler
description: Profile code to identify performance bottlenecks, measure execution characteristics, and recommend targeted optimizations. Use for slow endpoints, high CPU/memory usage, and latency-sensitive paths.
version: 1.0.0
tags: [performance, profiling, optimization, benchmarking, bottleneck]
---

# Performance Profiler

## Objective
Identify performance bottlenecks in code through measurement (not guesswork), produce an evidence-based optimization report with prioritized recommendations, and verify improvements with before/after benchmarks.

## Trigger
- "Profile this code for performance"
- "Find performance bottlenecks in X"
- "This endpoint is slow, investigate"
- "High CPU/memory usage in component Y"
- "Optimize hot path in module Z"

Anti-triggers: "Rewrite for performance without measuring" / "Apply micro-optimizations blindly" — those violate the measurement-first principle.

## Inputs
- Target: file path, module, function, or endpoint to profile
- Baseline: current behavior metrics (if available)
- Workload: representative input/request pattern
- Constraints: time budget, acceptable risk, production vs. staging

## Outputs
- Bottleneck report: function/file:line, metric (CPU/time/memory/allocations), severity, evidence
- Optimization recommendations: ranked by impact × effort, with before/after estimates
- Benchmark results: before and after measurements for each applied change
- Risk assessment: regression risk per recommendation

## Procedure
1. **Establish measurement baseline**
   - Record runtime version, environment, and hardware characteristics.
   - Identify existing benchmark/test commands for the target.
   - Capture baseline measurements: wall time, CPU, memory, allocations, I/O.
   - Distinguish cold vs. warm start; run multiple iterations (min 3) for stability.

2. **Profile the target**
   - Use language-appropriate profiler: `perf`, `pprof`, `cProfile`, `node --prof`, `ruby-stackprof`, language tracing, or manual instrumentation.
   - Focus on hot paths: entry points, loops, database queries, external calls, serialization.
   - Record: top functions by self-time, total time, call counts, allocation hotspots.
   - Avoid profiling production traffic unless read-only and approved.

3. **Identify bottlenecks**
   - Classify each bottleneck: CPU-bound, I/O-bound, memory-bound, lock contention, N+1 queries, unnecessary allocations, synchronous blocking.
   - Record file:line, metric value, call frequency, and percentage of total time.
   - Distinguish structural issues (algorithm complexity) from implementation issues (inefficient code).

4. **Prioritize optimizations**
   - Score each: impact (time/memory saved) × likelihood × risk (regression potential).
   - Rank: high-impact low-risk first, high-impact high-risk with approval gate, low-impact last.
   - Estimate effort: trivial (<30min), moderate (hours), major (days).

5. **Apply optimizations (requires approval for code changes)**
   - With explicit approval, apply the smallest safe change per optimization.
   - Prefer algorithmic/data-structure changes over micro-optimizations.
   - Preserve public interfaces and behavior unless behavior change is explicitly authorized.

6. **Verify with before/after benchmarks**
   - Re-run the same workload and measurement suite after each change.
   - Compare: before vs. after for each metric; require statistical significance (min 3 runs).
   - Run full test suite, lint, typecheck, build to detect regressions.
   - Roll back any change that degrades correctness or introduces new bottlenecks.

7. **Report**
   - Write a Markdown report: executive summary, bottleneck table, recommendations table, benchmark before/after, risk assessment, rollback notes.

## Safety & Approval Gates
- **Read-only profiling by default:** No code changes without explicit approval.
- **No production mutation:** Do not profile production with write traffic; use staging or synthetic workloads.
- **Approval required before any code change.**
- **Rollback required:** Record pre-change state; revert if benchmarks degrade or tests fail.
- **No secret logging:** Profiling output may contain sensitive data; redact before reporting.

## Failure Handling
- Profiler unavailable → Use manual timing instrumentation, mark as "approximate."
- Workload not representative → State limitation, use best-available input, mark unverified.
- Optimization breaks tests → Revert, report failure, do not proceed.
- Cannot isolate bottleneck → Report "inconclusive," list candidates, recommend deeper instrumentation.

## Completion Criteria
- Bottleneck report produced with at least one measured hotspot (file:line + metric).
- Each recommendation has impact estimate, effort estimate, and risk level.
- Applied changes verified with before/after benchmarks (or explicitly marked pending approval).
- No secret or production data in output.
- Report distinguishes verified measurements from estimates.
