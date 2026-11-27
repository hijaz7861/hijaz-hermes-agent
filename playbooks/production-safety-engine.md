# Playbook: Production Safety Engine

*Practical examples for the `production-safety-engine` skill*

---

## Scenario 1: Production reliability setup (happy path)

**Trigger:** "Set up production safety for the payments service — monitor SLOs, run chaos tests, and coordinate a secure release."

**Invocation:**
```
Execute production safety for payments-service:
- SLO targets: 99.9% availability, p95 latency < 200ms, error rate < 0.1%
- Chaos experiment: inject 50ms latency to Stripe API, 5% blast radius
- Release: prepare v2.1.0 with security gate
- Budget: $10, Time: 45 minutes
```

**Execution Log:**
```
## Production Safety Engine: payments-service

### Phase 1: Reliability Monitoring (error-budget-tracker)
SLOs defined:
- Availability: 99.9% target, current 99.95% ✅
- p95 latency: 200ms target, current 145ms ✅
- Error rate: 0.1% target, current 0.03% ✅
Error budget status: HEALTHY (87% remaining)

### Phase 2: Resilience Testing (chaos-engineer)
Experiment: Inject 50ms latency to Stripe API, 5% blast radius
Baseline: p95 latency 145ms, error rate 0.03%
During injection: p95 latency 192ms, error rate 0.08% (within safety threshold)
Circuit breaker: activated after 3 consecutive failures ✅
Fallback: cached payment status returned ✅
Recovery: system returned to baseline within 30s of stopping injection
Monitoring: alert fired at 0.05% error rate (detection time: 45s)

### Phase 3: Incident Response (incident-responder)
No active incidents during this cycle.
Monitoring added: Stripe API latency histogram, circuit breaker state metric
Alert: error rate > 0.05% for 2 minutes → page on-call

### Phase 4: Secure Release Coordination (secure-release)
Release v2.1.0:
- Readiness: tests PASS (89 tests), lint/typecheck/build CLEAN, review COMPLETE
- Security audit: no committed secrets, 1 MEDIUM finding (CORS *) — resolved
- Security gate: PASSED (no unresolved CRITICAL/HIGH)
- Gates: Quality PASSED, Security PASSED, Approval: PENDING
Version bump: AWAITING USER APPROVAL (not yet applied)

### Phase 5: Feedback Loop
- Chaos result → circuit breaker threshold tuned from 3 to 5 failures
- Monitoring added → alert threshold set at 0.05% error rate
- Release findings → CORS finding added to deployment checklist

### Report
Production safety: OPERATIONAL
SLO compliance: all targets met
Error budget: 87% remaining (healthy)
Chaos resilience: graceful degradation confirmed
Security gate: passed (approval pending for version bump)
Exit code: 0.
```

**Expected Output:**
Production safety report with SLO compliance, error budget status, chaos experiment results, incident response status, secure release gate status, and feedback loop actions.

---

## Scenario 2: Error budget exhausted (failure case)

**Trigger:** "Production safety for checkout-service — error budget is exhausted."

**Invocation:**
```
Execute production safety for checkout-service.
Error budget: EXHAUSTED (0% remaining).
Trigger deployment slowdown gate.
```

**Execution Log:**
```
## Production Safety Engine: checkout-service

### Phase 1: Reliability Monitoring
SLOs:
- Availability: 99.9% target, current 98.2% ❌
- Error rate: 0.1% target, current 0.45% ❌
Error budget status: EXHAUSTED (0% remaining)

### Gate Triggered
DEPLOYMENT SLOWDOWN ACTIVATED
- No new deployments permitted until error budget recovers
- Requires explicit user approval to override
- Prioritize: fix top 3 error sources

### Top Error Sources
1. Payment timeout errors (60% of errors) — checkout/payment.ts:45
2. Database connection pool exhaustion (25%) — checkout/db.ts:12
3. Inventory service 500 errors (15%) — checkout/inventory.ts:78

### Phase 2-4: Skipped
Chaos experiments: SKIPPED (budget exhausted, no fault injection permitted)
Incident response: IN PROGRESS (addressing top error sources)
Secure release: BLOCKED (budget exhausted gate)

### Report
Production safety: BLOCKED
Error budget: EXHAUSTED
Deployment slowdown: ACTIVE
Next: Fix top 3 error sources, re-measure, then request approval to resume deployments.
Exit code: 1 (budget exhausted, deployment slowdown active).
```

**Expected Output:**
Production safety report showing exhausted error budget, deployment slowdown gate, top error sources, and blocked release pipeline.

---

## Scenario 3: Chaos experiment causes cascade (safety case)

**Trigger:** "Run chaos experiment on auth-service with strict safety limits."

**Invocation:**
```
Chaos experiment: kill 10% of auth-service instances.
Safety threshold: auto-abort if error rate > 2% or latency > 500ms.
Rollback plan: restart instances, clear circuit breakers.
```

**Execution Log:**
```
## Production Safety Engine: auth-service Chaos Experiment

### Experiment Setup
Failure: instance termination (10% of pods)
Blast radius: 10%
Safety thresholds: error rate > 2% OR latency > 500ms → auto-abort
Rollback: restart terminated instances, clear circuit breakers

### Execution
- T+0s: Baseline — error rate 0.01%, p95 latency 80ms
- T+30s: 10% instances terminated — error rate 0.8%, p95 latency 140ms
- T+60s: CASCADE DETECTED — error rate 3.4% (exceeds 2% threshold)
- T+61s: AUTO-ABORT TRIGGERED
- T+65s: Instances restarted, circuit breakers cleared
- T+90s: Recovery confirmed — error rate 0.02%, p95 latency 85ms

### Root Cause of Cascade
Auth service sessions stored in-memory, not distributed. Instance termination caused session loss → re-authentication storms → downstream service overload.

### Safety Verification
- Auto-abort triggered before user impact threshold
- Rollback completed within 35 seconds
- No production data affected
- No secret values logged

### Recommendations
1. Move sessions to distributed store (Redis) — eliminates single point of failure
2. Add circuit breaker on downstream auth calls
3. Implement session retry with exponential backoff

Exit code: 1 (cascade detected, auto-abort triggered, experiment halted).
```

**Expected Output:**
Chaos experiment report showing cascade detection, auto-abort trigger, rollback confirmation, and resilience recommendations.
