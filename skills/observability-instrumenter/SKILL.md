---
name: observability-instrumenter
description: Add structured logging, metrics, distributed tracing, and health checks to code. Use when observability is missing or insufficient for debugging production issues.
version: 1.0.0
tags: [observability, logging, metrics, tracing, monitoring, instrumentation]
---

# Observability Instrumenter

## Objective
Improve system observability by adding structured logs, metrics, traces, and health checks. Every instrumentation change is verified to compile and not alter production behavior. No secret data is logged.

## Trigger
- "Add logging to module X"
- "Instrument service Y for metrics"
- "Add distributed tracing to request flow Z"
- "Create health check endpoint"
- "Improve debuggability of component W"

Anti-triggers: "Send all logs to external analytics" / "Log user PII" / "Enable profiling in production without approval" — those require explicit approval and data-classification review.

## Inputs
- Target: file, module, service, or request flow to instrument
- Telemetry type: logging, metrics, tracing, health checks (one or more)
- Destination: stdout, file, metrics backend, tracing collector (or "unspecified")
- Constraints: performance overhead budget, data classification, log level defaults

## Outputs
- Instrumentation diff: added logging/metrics/tracing/health-check code
- Configuration: log levels, metric names, trace span names, health endpoints
- Verification: build/typecheck/test results, overhead estimate
- Data-classification review: what may/may not be logged

## Procedure
1. **Assess observability gaps**
   - Read the target code; identify entry/exit points, external calls, error paths, state changes.
   - Check existing logging/metrics/tracing coverage; find gaps (silent failures, unlogged errors, untraced calls).
   - Identify data sensitivity at each point (public, internal, confidential, restricted).

2. **Design instrumentation**
   - Logging: structured (JSON), levels (error/warn/info/debug), contextual fields (request ID, user ID, operation), no secrets.
   - Metrics: counters (requests, errors), histograms (latency, size), gauges (connections, queue depth).
   - Tracing: span boundaries at entry/exit and external calls, trace ID propagation, span attributes.
   - Health checks: dependency readiness (DB, cache, external API), liveness probe.

3. **Apply instrumentation**
   - Add code with minimal diff; one concern at a time.
   - Use the project's existing logging/metrics/tracing libraries if present.
   - Respect log level defaults; avoid debug-level in production by default.
   - Never log secrets, tokens, PII, or credentials (redact or omit).

4. **Configure telemetry**
   - Set log levels, metric prefixes, trace service names, health check intervals.
   - Document where telemetry is sent (stdout vs. backend).
   - Provide configuration for enabling/disabling per environment.

5. **Verify**
   - Run build, lint, typecheck; require clean.
   - Run relevant tests; require pass.
   - Estimate overhead: logging cost per request, metric cardinality, trace sampling rate.
   - Confirm no secret fields in log output (grep for common secret patterns).

6. **Report**
   - Produce instrumentation report: what was added, where, configuration, overhead estimate, data-classification notes.

## Safety & Approval Gates
- **No secret logging:** Redact or omit credentials, tokens, PII, connection strings.
- **Overhead budget:** Instrumentation must not materially degrade performance (document estimate).
- **Approval required before enabling external telemetry endpoints.**
- **Read-only analysis by default; code changes need approval.**

## Failure Handling
- Library unavailable → Use standard library logging, mark as "limited telemetry."
- Cannot determine data sensitivity → Mark as "review required," do not log field.
- Build/test failure → Revert, report, do not proceed.
- Cardinality risk (high-cardinality metric) → Flag, recommend aggregation, do not deploy.

## Completion Criteria
- Instrumentation code added and verified (build + tests pass).
- No secret fields in log/metric/trace output.
- Overhead estimate documented.
- Configuration for log levels/endpoints provided.
- Report produced with data-classification notes.
