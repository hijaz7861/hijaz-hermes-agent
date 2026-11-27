---
name: error-budget-tracker
description: Track error budgets and SLOs by combining autonomous testing with observability instrumentation. Measures error rates against service level objectives, tracks budget consumption, and alerts when budgets are at risk.
version: 1.0.0
tags: [slo, error-budget, observability, testing, reliability]
dependencies: [autonomous-testing, observability-instrumenter]
---

# Error Budget Tracker

## Objective
Combine autonomous testing with observability to track error budgets and service level objectives (SLOs). Measures error rates against targets, tracks budget consumption over time, and alerts when budgets are at risk of exhaustion.

## Trigger
- "Track error budget for service X"
- "Monitor SLO compliance for API Y"
- "Alert when error budget is at risk"
- "Measure reliability against SLO targets"

Anti-triggers: "Set up monitoring infrastructure" / "Fix all errors" — those are separate observability or remediation tasks, not budget tracking.

## Inputs
- SLO targets: availability, latency, error rate percentages
- Time window: rolling window (e.g., 30 days, 7 days)
- Observability data: logs, metrics, traces, health checks
- Test results: test pass/fail rates from autonomous-testing

## Outputs
- SLO compliance report: target vs. actual, budget consumed, budget remaining
- Error budget status: healthy, at-risk, exhausted
- Error rate trend: over time, by endpoint, by error type
- Alert recommendations: when to page, when to slow deployments
- Remediation suggestions: reduce deploy frequency, increase testing, fix top errors

## Procedure
1. **Define SLOs** (autonomous-testing + observability-instrumenter)
   - Identify service level indicators: availability, latency (p95/p99), error rate.
   - Set SLO targets: e.g., 99.9% availability, p95 latency < 200ms, error rate < 0.1%.
   - Define error budget: 1 - SLO target (e.g., 0.1% error budget).

2. **Collect observability data** (observability-instrumenter)
   - Query metrics: request count, error count, latency distribution.
   - Query logs: error logs, exception traces, failed health checks.
   - Query traces: failed spans, timeout spans, error status codes.

3. **Run tests for baseline** (autonomous-testing)
   - Execute test suite to establish pre-production error rate.
   - Record test pass/fail rates per endpoint.
   - Identify flaky tests that could skew error measurements.

4. **Calculate error budget**
   - Error rate = error requests / total requests.
   - Budget consumed = actual error rate / error budget.
   - Budget remaining = error budget - actual error rate.
   - Track over time: daily, weekly, monthly consumption.

5. **Determine budget status**
   - Healthy: budget remaining > 50%.
   - At-risk: budget remaining 10-50%.
   - Exhausted: budget remaining <= 0%.
   - Alert when at-risk or exhausted.

6. **Recommend actions**
   - If exhausted: slow or halt deployments, fix top errors first.
   - If at-risk: prioritize error fixes over new features.
   - If healthy: normal deployment cadence.

7. **Report**
   - Produce error budget report: SLO compliance, budget status, trends, alerts, recommendations.

## Safety & Approval Gates
- **Read-only monitoring:** No production changes without explicit approval.
- **Deployment gate:** Budget exhaustion should trigger deployment slowdown (requires approval to override).
- **No secret logging:** Error logs may contain PII or credentials; redact before reporting.

## Failure Handling
- Observability data missing → Mark SLO as "unmeasurable," recommend instrumentation.
- Test suite unavailable → Use production metrics only, mark test baseline as "unavailable."
- SLO targets not defined → Recommend setting targets, mark as "not configured."
- Budget calculation ambiguous → Document assumptions, request stakeholder clarification.

## Completion Criteria
- SLO compliance report with targets vs. actual measurements.
- Error budget status explicitly classified (healthy/at-risk/exhausted).
- Error rate trends documented over time.
- Alert recommendations with thresholds.
- No secret values in output.
