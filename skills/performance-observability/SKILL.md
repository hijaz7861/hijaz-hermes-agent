---
name: performance-observability
description: Instrument code with structured logging, metrics, and tracing, then profile to measure the performance impact — combining observability setup with measurement-driven profiling for observable, optimized systems.
version: 1.0.0
tags: [observability, performance, profiling, instrumentation, monitoring]
dependencies: [observability-instrumenter, performance-profiler]
---

# Performance Observability

## Objective
Combine observability instrumentation with performance profiling to add monitoring capability and measure its performance impact. Every instrumentation change is profiled before and after to confirm overhead stays within budget.

## Trigger
- "Instrument and profile service X"
- "Add observability and measure overhead"
- "Instrument code for monitoring, verify performance impact"
- "Add logging/metrics/tracing and confirm no regression"

Anti-triggers: "Enable profiling in production without overhead budget" / "Log everything without measurement" — requires explicit overhead approval.

## Inputs
- Target: file, module, service, or request flow to instrument
- Telemetry type: logging, metrics, tracing, health checks
- Overhead budget: acceptable performance impact percentage
- Destination: stdout, file, metrics backend, tracing collector

## Outputs
- Instrumentation diff: added logging/metrics/tracing/health-check code
- Baseline profile: performance before instrumentation
- Post-instrumentation profile: performance after instrumentation
- Overhead report: delta in latency, CPU, memory per request
- Data-classification review: what may/may not be logged

## Procedure
1. **Establish baseline** (performance-profiler)
   - Profile the target before any instrumentation.
   - Record: wall time, CPU, memory, allocations per request.
   - Run min 3 iterations for stability.

2. **Assess observability gaps** (observability-instrumenter)
   - Read target code; identify entry/exit points, external calls, error paths.
   - Check existing coverage; find gaps (silent failures, unlogged errors).
   - Identify data sensitivity at each point.

3. **Apply instrumentation** (observability-instrumenter)
   - Add structured logging, metrics, traces, health checks.
   - Use project's existing libraries if present.
   - Never log secrets, tokens, PII, credentials.

4. **Profile after instrumentation** (performance-profiler)
   - Re-profile the instrumented target under the same workload.
   - Compare before vs. after: latency, CPU, memory delta.
   - Confirm overhead is within the declared budget.

5. **Verify**
   - Run build, lint, typecheck; require clean.
   - Run relevant tests; require pass.
   - Confirm no secret fields in log/metric/trace output.

6. **Report**
   - Produce observability report: what was added, overhead %, configuration, data-classification notes.

## Safety & Approval Gates
- **No secret logging:** Redact or omit credentials, tokens, PII.
- **Overhead budget:** Instrumentation must not materially degrade performance.
- **Approval required** before enabling external telemetry endpoints.
- **Read-only analysis by default; code changes need approval.**

## Failure Handling
- Library unavailable → Use standard library, mark as "limited telemetry."
- Overhead exceeds budget → Report, do not deploy; recommend sampling/reduction.
- Cannot determine data sensitivity → Mark "review required," do not log field.
- Build/test failure → Revert, report, do not proceed.

## Completion Criteria
- Instrumentation code added and verified (build + tests pass).
- No secret fields in output.
- Overhead measured and documented (before/after profiles).
- Configuration for log levels/endpoints provided.
- Report produced with data-classification notes.
