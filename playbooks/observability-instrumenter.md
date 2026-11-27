# Playbook: Observability Instrumenter

*Practical examples for the `observability-instrumenter` skill*

---

## Scenario 1: Add structured logging to a service (happy path)

**Trigger:** "Add structured logging to src/services/payments.ts — it currently has no logs."

**Invocation:**
```
Add structured logging to src/services/payments.ts.
Log: request start, request completion, errors, external API calls.
Use JSON format. No secret data. Log level: info for normal, error for failures.
```

**Execution Log:**
```
## Observability Instrumentation: src/services/payments.ts

### Gap Analysis
Entry/exit points: processPayment(), refundPayment(), verifyWebhook()
External calls: Stripe API (3 endpoints)
Error paths: 4 catch blocks, no logging
Silent failures: 2 (catch blocks swallow errors without logging)

### Instrumentation Added
| Location | Type | Message | Fields | Level |
|----------|------|---------|--------|-------|
| processPayment entry | log | "payment.process.start" | paymentId, amount, currency | info |
| processPayment success | log | "payment.process.complete" | paymentId, durationMs, stripeChargeId | info |
| processPayment error | log | "payment.process.error" | paymentId, errorCode, errorMessage | error |
| Stripe API call | log | "stripe.api.request" | endpoint, method, durationMs | debug |
| Stripe API error | log | "stripe.api.error" | endpoint, statusCode, errorType | error |
| refundPayment entry/exit | log | "refund.process.start/complete" | refundId, amount | info |
| verifyWebhook | log | "webhook.verify" | eventId, eventType, verified | info |

### Configuration
- Log format: JSON
- Default level: info
- Debug level: disabled in production by default
- Sensitive fields redacted: card numbers, API keys

### Data Classification Review
- paymentId: public (log OK)
- amount: internal (log OK)
- card number: restricted (REDACTED — not logged)
- Stripe API key: restricted (REDACTED — not logged)
- Customer email: confidential (REDACTED — not logged)

### Verification
- Typecheck: CLEAN
- Tests: all pass (24 payment tests)
- No secret fields in log output (verified by grep)
- Estimated overhead: <2% per request

Exit code: 0.
```

**Expected Output:**
Instrumentation diff showing added logging, configuration, data-classification review, and verification results.

---

## Scenario 2: Add metrics and health checks (happy path)

**Trigger:** "Add Prometheus metrics and a health check endpoint to the billing service."

**Invocation:**
```
Add metrics (request count, latency, error count) and health check endpoint to src/services/billing.ts.
Prometheus format. Health check verifies DB connectivity.
```

**Execution Log:**
```
## Observability Instrumentation: src/services/billing.ts

### Metrics Added
| Metric | Type | Name | Labels | Purpose |
|--------|------|------|--------|---------|
| billing_requests_total | counter | billing_requests_total | endpoint, method, status | Request volume |
| billing_request_duration_seconds | histogram | billing_request_duration_seconds | endpoint | Latency distribution |
| billing_errors_total | counter | billing_errors_total | endpoint, error_type | Error tracking |
| db_connections_active | gauge | db_connections_active | — | Pool utilization |

### Health Check Added
Endpoint: GET /health/billing
Checks: database connectivity (query: SELECT 1)
Response: {"status": "healthy", "checks": {"database": "up"}}

### Configuration
- Metrics endpoint: /metrics (Prometheus format)
- Metrics path: /metrics
- Health check interval: 30 seconds
- Timeout: 5 seconds per check

### Verification
- Typecheck: CLEAN
- Tests: all pass (18 billing tests)
- Health check returns 200 when DB available
- Metrics endpoint returns valid Prometheus format
- Estimated overhead: <1% per request

Exit code: 0.
```

**Expected Output:**
Added metrics definitions, health check endpoint, configuration, and verification results.

---

## Scenario 3: Secret data detected in logging path (safety case)

**Trigger:** "Add logging to src/auth/tokens.ts — it handles JWT secret keys."

**Invocation:**
```
Add logging to src/auth/tokens.ts for token issuance and verification events.
DO NOT log secret keys or token values.
```

**Execution Log:**
```
## Observability Instrumentation: src/auth/tokens.ts

### Data Classification
- JWT signing secret: RESTRICTED — must never be logged
- Token values: CONFIDENTIAL — must never be logged in plaintext
- User ID: INTERNAL — OK to log
- Token ID (JTI): PUBLIC — OK to log
- Token algorithm: PUBLIC — OK to log
- Expiry timestamp: INTERNAL — OK to log

### Instrumentation Added (safe fields only)
| Location | Message | Logged Fields | Redacted Fields |
|----------|---------|---------------|-----------------|
| issueToken entry | "token.issue.start" | userId, tokenId, algorithm | secret (redacted) |
| issueToken success | "token.issue.complete" | userId, tokenId, expiryMs | token value (redacted) |
| verifyToken entry | "token.verify.start" | tokenId, algorithm | token value (redacted) |
| verifyToken success | "token.verify.complete" | tokenId, userId, valid | — |
| verifyToken failure | "token.verify.failed" | tokenId, errorType | secret, token value |

### Safety Verification
- Grep for secret patterns in log output: NONE found
- Token values never logged (only tokenId)
- JWT secret never logged

### Verification
- Typecheck: CLEAN
- Tests: all pass (15 token tests)
- No secret data in any log statement

Exit code: 0.
```

**Expected Output:**
Instrumentation with explicit data classification, redacted secret fields, verification that no secrets are logged.
