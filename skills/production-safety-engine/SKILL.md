---
name: production-safety-engine
description: Complete production safety system combining incident response, error budget tracking, chaos engineering, and secure release coordination. Monitors SLOs, runs resilience experiments, responds to incidents, and coordinates gated releases.
version: 1.0.0
tags: [production, safety, reliability, incident, slo, chaos, release]
dependencies: [incident-responder, error-budget-tracker, chaos-engineer, secure-release]
---

# Production Safety Engine

## Objective
Combine incident response, error budget tracking, chaos engineering, and secure release coordination into a unified production safety system. Continuously monitors service reliability, proactively tests resilience through controlled failure injection, responds to incidents with verified fixes, and coordinates security-gated releases — all feeding back into improved error budgets and resilience.

## Trigger
- "Ensure production safety for service X"
- "Set up reliability monitoring and incident response"
- "Run chaos experiments and track error budgets"
- "Coordinate secure release with safety gates"

Anti-triggers: "Deploy without safety checks" / "Ignore error budgets" — violates the production safety principle.

## Inputs
- Services: list of production services to monitor
- SLO targets: availability, latency, error rate per service
- Observability data: logs, metrics, traces, health checks
- Release pipeline: version, branch, changelog, gate criteria
- Safety thresholds: error budget limits, chaos blast radius limits

## Outputs
- Safety dashboard: SLO compliance, error budget status, incident history, chaos experiment results
- Incident response: incident timeline, root cause, fix, monitoring added
- Chaos resilience: experiment results, resilience assessment, recommendations
- Release coordination: secure release report, gate status, security audit findings
- Continuous improvement: lessons learned, updated SLOs, refined runbooks

## Procedure
### Phase 1: Reliability Monitoring (error-budget-tracker)
1. Define SLOs for each service: availability, latency, error rate targets.
2. Collect observability data: logs, metrics, traces.
3. Calculate error budget consumption and remaining budget.
4. Classify budget status: healthy / at-risk / exhausted.
5. If budget exhausted → trigger deployment slowdown gate.

### Phase 2: Resilience Testing (chaos-engineer)
1. Design chaos experiments: inject latency, errors, timeouts, service outages.
2. Establish baseline: normal operation metrics.
3. Execute experiments with safety thresholds and auto-abort conditions.
4. Observe system behavior: graceful degradation vs. cascading failure.
5. Verify monitoring: did alerts fire, did dashboards show anomalies.
6. Record lessons learned: single points of failure, missing fallbacks.

### Phase 3: Incident Response (incident-responder)
1. When incidents occur: capture details, correlate observability data.
2. Form hypotheses, test one cause at a time.
3. Apply minimal verified fix with regression test.
4. Add monitoring: logs, metrics, alerts, health checks to prevent recurrence.
5. Verify incident no longer reproducible.

### Phase 4: Secure Release Coordination (secure-release)
1. Define release scope: version, branch, commits since last release.
2. Verify readiness: tests pass, review complete, security clean.
3. Run security audit: secrets, vulnerabilities, insecure config.
4. Enforce security gate: no release with unresolved CRITICAL/HIGH findings.
5. With approval: bump version, create tag, prepare for deploy.
6. Produce release report with gate status.

### Phase 5: Feedback Loop
1. Incident findings → update SLOs, refine runbooks.
2. Chaos results → improve error handling, add circuit breakers.
3. Release findings → update deployment checklist, security checklist.
4. Error budget trends → adjust alert thresholds, prioritize reliability work.

## Safety & Approval Gates
- **Approval required** before any production change: code, config, rollback, deployment.
- **Chaos engineering safety:** safety thresholds mandatory, auto-abort conditions defined, blast radius limited.
- **Error budget gate:** exhausted budget triggers deployment slowdown (requires explicit approval to override).
- **Security gate mandatory:** unresolved CRITICAL/HIGH findings block release.
- **Rollback plan required** before any production fix or deployment.
- **No secret logging:** incident logs, error traces, security findings redacted.

## Failure Handling
- Error budget exhausted → slow deployments, prioritize error fixes, request approval to override.
- Chaos experiment causes cascade → abort immediately, report, recommend circuit breakers.
- Incident cannot be reproduced → document hypotheses, recommend increased observability.
- Security audit tool unavailable → manual review, mark findings as "unverified."
- Approval denied → stop, report findings only, no production changes.

## Completion Criteria
- Safety dashboard produced with SLO compliance, error budget status, incident history.
- At least one chaos experiment executed with resilience assessment.
- Incident response procedure verified with at least one resolved incident.
- Secure release coordinated with all gates explicitly marked passed/failed/blocked.
- Feedback loop documented: lessons learned fed back into SLOs and runbooks.
- No secret values in output.
