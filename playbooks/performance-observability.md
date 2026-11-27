# Playbook: Performance Observability

*Practical examples for the `performance-observability` skill*

---

## Scenario 1: Instrument and profile a service (happy path)

**Trigger:** "Add observability to the payments service and measure the overhead."

**Invocation:**
```
Instrument src/services/payments.ts with structured logging and metrics.
Profile before and after. Overhead budget: <5% latency increase.
```

**Execution Log:**
```
## Performance Observability: src/services/payments.ts

### Baseline Profile (performance-profiler)
- processPayment(): 150ms avg (5 iterations)
- Memory per request: 45MB
- No existing instrumentation

### Instrumentation Applied (observability-instrumenter)
| Location | Type | Message | Level |
|----------|------|---------|-------|
| processPayment entry | log | "payment.process.start" | info |
| processPayment success | log | "payment.process.complete" | info |
| processPayment error | log | "payment.process.error" | error |
| Stripe API call | metric | "stripe.request.duration" | histogram |
| Health check | endpoint | GET /health/payments | — |

### Data Classification
- paymentId: public (logged OK)
- amount: internal (logged OK)
- card number: restricted (REDACTED)
- Stripe API key: restricted (REDACTED)

### Post-Instrumentation Profile
- processPayment(): 153ms avg (5 iterations) — +2% overhead
- Memory per request: 46MB — +2% overhead
- Overhead within budget (<5%)

### Verification
- Typecheck: CLEAN
- Tests: all pass (24 payment tests)
- No secret fields in log output (verified by grep)

Exit code: 0.
```

**Expected Output:**
Observability report with baseline profile, instrumentation diff, post-instrumentation profile, overhead %, data classification, and verification.

---

## Scenario 2: Overhead exceeds budget (failure case)

**Trigger:** "Instrument the hot loop. Overhead must stay under 1%."

**Invocation:**
```
Add logging to the hot loop in src/lib/hot-loop.ts. Overhead budget: <1%.
```

**Execution Log:**
```
## Performance Observability: src/lib/hot-loop.ts

### Baseline Profile
- hotLoop(): 5ms per iteration (10,000 iterations)

### Instrumentation Applied
- Added debug-level log per iteration: "iteration.complete" with 5 fields

### Post-Instrumentation Profile
- hotLoop(): 5.8ms per iteration — +16% overhead
- Exceeds budget (<1%)

### Decision
OVERHEAD EXCEEDS BUDGET. Do not deploy.
Recommendations:
1. Reduce log level to error-only in production
2. Sample logging (1% of iterations)
3. Move logging outside the hot loop

Exit code: 1 (overhead exceeds budget, instrumentation not deployed).
```

**Expected Output:**
Report showing baseline vs. post-instrumentation profile, overhead % exceeding budget, and recommendations for reduction.

---

## Scenario 3: Secret data in logging path (safety case)

**Trigger:** "Add logging to the auth token module. Never log secret keys or tokens."

**Invocation:**
```
Add structured logging to src/auth/tokens.ts for token issuance events.
DO NOT log JWT secret or token values.
```

**Execution Log:**
```
## Performance Observability: src/auth/tokens.ts

### Data Classification
- JWT signing secret: RESTRICTED — never log
- Token values: CONFIDENTIAL — never log in plaintext
- User ID: INTERNAL — OK to log
- Token ID (JTI): PUBLIC — OK to log

### Instrumentation (safe fields only)
| Location | Message | Logged Fields | Redacted |
|----------|---------|---------------|----------|
| issueToken | "token.issue.start" | userId, tokenId, algorithm | secret |
| issueToken | "token.issue.complete" | userId, tokenId, expiryMs | token value |

### Safety Verification
- Grep for secret patterns in log output: NONE found
- Token values never logged (only tokenId)
- JWT secret never logged

Exit code: 0.
```

**Expected Output:**
Instrumentation with explicit data classification, redacted secret fields, verification that no secrets are logged.
