---
name: performance-adjuster
description: Adjust application and infrastructure performance parameters based on profiling data and benchmark results. Optimizes algorithms, caching, concurrency, and I/O patterns for better performance.
version: 1.0.0
tags: [adjustment, performance, tuning, profiling, optimization, algorithms]
dependencies: [performance-profiler, code-refactorer, autonomous-testing]
---

# Performance Adjuster

## Objective
Adjust application and infrastructure performance parameters based on profiling data and benchmark results. Optimizes algorithms, caching, concurrency, and I/O patterns for better performance while maintaining correctness.

## Trigger
- "Adjust caching strategy for service X"
- "Tune concurrency settings for API Y"
- "Optimize I/O patterns in module Z"
- "Adjust algorithm parameters for better performance"

Anti-triggers: "Premature optimization without measurement" / "Change algorithms without benchmarks" — those violate measurement-first principles.

## Inputs
- Performance parameter: cache size, concurrency level, batch size, algorithm threshold
- Current value and profiling data
- Benchmark results: before/after performance measurements
- Performance targets: response time, throughput, resource usage
- Adjustment limits: min/max values, step size

## Outputs
- Adjustment plan: parameter, current → target, expected improvement
- Adjustment log: changes, benchmarks, before/after comparisons
- Verification: benchmarks pass, correctness maintained
- Performance impact: latency reduction, throughput increase

## Procedure
1. **Profile current performance** (performance-profiler)
   - Measure current performance: latency, throughput, resource usage
   - Identify bottlenecks: slow algorithms, cache misses, I/O waits
   - Record baseline benchmarks

2. **Analyze optimization opportunities**
   - Identify parameters affecting performance: cache TTL, concurrency, batch size
   - Correlate parameter values with performance metrics
   - Assess risk: algorithm changes higher risk than cache tuning

3. **Design adjustments**
   - Calculate target values based on profiling data
   - Define benchmark scenarios for verification
   - Document expected improvement

4. **Apply adjustments** (code-refactorer)
   - Apply one parameter change at a time
   - Run benchmarks before and after
   - Verify correctness (same outputs for same inputs)
   - One adjustment at a time

5. **Verify** (autonomous-testing)
   - Run test suite: all tests pass
   - Run benchmarks: performance improved or maintained
   - Verify correctness: no behavior changes
   - Roll back if performance degrades or tests fail

6. **Report**
   - Produce adjustment report: parameters, benchmarks, improvement, verification

## Safety & Approval Gates
- **Benchmark gate**: adjustments verified with before/after benchmarks
- **Correctness gate**: same inputs must produce same outputs
- **One adjustment at a time**: no batching unrelated changes
- **Approval required** for production changes
- **Rollback**: revert if benchmarks regress or tests fail

## Failure Handling
- Profiling data unavailable → Mark as "insufficient data," recommend profiling
- Adjustment degrades performance → Revert immediately, report
- Tests fail → Revert, do not proceed
- Cannot measure improvement → Mark as "inconclusive," recommend more benchmarks

## Completion Criteria
- Adjustment plan with current → target values
- Benchmarks show improvement or maintenance
- Correctness verified (same outputs)
- Tests pass after adjustment
- No regressions
