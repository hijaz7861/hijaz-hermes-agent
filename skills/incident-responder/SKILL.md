---
name: incident-responder
description: Respond to production incidents by combining autonomous debugging with observability instrumentation. Reproduces incidents, correlates logs/metrics/traces, finds root cause, applies verified fixes, and adds monitoring to prevent recurrence.
version: 1.0.0
tags: [incident, response, debugging, observability, production, root-cause]
dependencies: [autonomous-debugging, observability-instrumenter]
---

# Incident Responder

## Objective
Combine autonomous debugging with observability to respond to production incidents. Reproduces the incident, correlates structured logs, metrics, and distributed traces to find root cause, applies a verified fix, and adds monitoring to prevent recurrence.

## Trigger
- "Respond to production incident #X"
- "Debug the outage in service Y"
- "Investigate the error spike in component Z"
- "Production incident: reproduce, diagnose, fix, monitor"

Anti-triggers: "Deploy hotfix without diagnosis" / "Monitor without incident" — those are separate deployment or monitoring tasks, not incident response.

## Inputs
- Incident: error message, stack trace, time window, affected service, user impact
- Observability data: logs, metrics, traces, health check results
- Environment: production/staging, version deployed, recent changes
- Rollback plan: how to revert if fix fails

## Outputs
- Incident timeline: detection, reproduction, diagnosis, fix, verification
- Root cause: file:line, explanation, correlation evidence (logs/metrics/traces)
- Fix: minimal patch, before/after incident metrics
- Monitoring: new logs, metrics, alerts, health checks added to prevent recurrence
- Verification: incident no longer reproducible, tests pass, monitoring alerts configured

## Procedure
1. **Capture the incident** (autonomous-debugging)
   - Record incident details: time window, error rate, affected endpoints, user impact.
   - Identify recent changes (deploys, config changes, dependency updates).
   - Establish deterministic reproduction if possible; otherwise state hypotheses.

2. **Correlate observability data** (observability-instrumenter)
   - Query structured logs for error patterns during the incident window.
   - Analyze metrics: error rate, latency, CPU, memory, queue depth spikes.
   - Trace distributed traces: identify slow/failing spans, external call failures.
   - Cross-reference: error in logs ↔ spike in metrics ↔ failed trace span.

3. **Form hypotheses** (autonomous-debugging)
   - Rank likely causes: dependency failure, config change, resource exhaustion, code regression, data corruption.
   - Trace failing requests through validation, business logic, persistence.

4. **Test one cause at a time** (autonomous-debugging)
   - Prefer focused experiment: replay incident request, isolate the failing component.
   - Avoid unrelated refactors during incident response.

5. **Implement the fix** (autonomous-debugging)
   - Smallest safe patch to resolve the incident.
   - Add regression test that reproduces the incident and verifies the fix.
   - Preserve public interfaces unless behavior change is authorized.

6. **Add monitoring** (observability-instrumenter)
   - Add structured logs for the failure path (error codes, context fields).
   - Add metrics: error counter, latency histogram for the affected path.
   - Add health check: dependency readiness for external services involved.
   - Add alert: error rate threshold, latency threshold.

7. **Verify**
   - Re-run reproduction: incident no longer occurs.
   - Confirm monitoring alerts would have caught the incident earlier.
   - Run full test suite, lint, typecheck, build.
   - Confirm rollback plan is ready if fix introduces new issues.

8. **Report**
   - Produce incident report: timeline, root cause, fix, monitoring added, lessons learned.

## Safety & Approval Gates
- **Approval required** before any production change (code, config, rollback).
- **Rollback plan required** before applying fix to production.
- **No secret logging:** Incident logs may contain PII or credentials; redact before reporting.
- **No production mutation without approval:** Debug on staging or synthetic inputs first.

## Failure Handling
- Cannot reproduce → State hypotheses, recommend increased observability, continue investigation.
- Fix introduces new issues → Rollback immediately, report, do not proceed.
- Observability data incomplete → Mark findings as "estimated," recommend instrumentation.
- Approval denied → Stop, report findings only, no production changes.

## Completion Criteria
- Incident no longer reproducible in tested environment.
- Root cause identified with correlating evidence (logs + metrics + traces).
- Fix verified with before/after incident metrics.
- Monitoring added to prevent recurrence (logs, metrics, alerts, health checks).
- Incident report produced with timeline and lessons learned.
- No secret values in output.
