# Playbook: Quality Gate Review

*Practical examples for the `quality-gate-review` skill*

---

## Scenario 1: PR review with quality gate (happy path)

**Trigger:** "Review PR #445 with quality gate — tests must pass and no security findings."

**Invocation:**
```
Review PR #445 (OAuth2 provider) with quality gate.
Requirements: all tests pass, no CRITICAL/HIGH review findings, security clean.
Gate threshold: 100% test pass rate, zero CRITICAL/HIGH findings.
```

**Execution Log:**
```
## Quality Gate Review: PR #445 - OAuth2 Provider

### Gate Criteria
- Test pass rate: 100% of affected tests
- Review findings: zero CRITICAL/HIGH unresolved
- Security audit: clean

### Review Findings (multi-agent-review)
| ID | File | Line | Severity | Finding | Status |
|----|------|------|----------|---------|--------|
| SEC-001 | token-exchange.ts | 67 | CRITICAL | Subject token audience not validated | RESOLVED (PR #446) |
| SEC-002 | provider.ts | 45 | HIGH | client_secret logged in error stack | RESOLVED |

### Test Evidence (autonomous-testing)
| Phase | Command | Exit | Result |
|-------|---------|------|--------|
| Unit (oauth2) | pnpm test tests/unit/auth/oauth2/ | 0 | 23 passed |
| Integration (oauth2) | pnpm test tests/integration/auth/oauth2/ | 0 | 15 passed |
| Lint | pnpm lint | 0 | Clean |
| Typecheck | pnpm typecheck | 0 | Clean |

### Security Audit (security-audit)
- Committed secrets: none detected
- Dependencies: all clean
- Insecure config: none found

### Gate Decision
- CRITICAL/HIGH findings: 0 unresolved ✅
- Test pass rate: 100% ✅
- Security: clean ✅
- Result: PASS

### Report
Quality gate: PASS. All criteria met. Change approved for merge.
Exit code: 0.
```

**Expected Output:**
Quality gate report with review findings, test evidence matrix, security audit results, and explicit PASS/FAIL/BLOCKED decision.

---

## Scenario 2: Tests failing — gate fails (failure case)

**Trigger:** "Review PR #500 with quality gate."

**Invocation:**
```
Review PR #500 (billing changes) with quality gate.
Tests must pass and no CRITICAL/HIGH findings.
```

**Execution Log:**
```
## Quality Gate Review: PR #500 - Billing Changes

### Review Findings
| ID | File | Line | Severity | Finding |
|----|------|------|----------|---------|
| SEC-001 | billing/webhook.ts:34 | HIGH | Webhook signature not verified |

### Test Evidence
| Phase | Command | Exit | Result |
|-------|---------|------|--------|
| Unit (billing) | pnpm test tests/unit/billing/ | 1 | 3 failed |
| Integration (billing) | pnpm test tests/integration/billing/ | 1 | 2 failed |

### Test Failures
- tests/unit/billing/proration.test.ts: "proration edge case" — AssertionError
- tests/unit/billing/refund.test.ts: "refund authorization" — TimeoutError

### Gate Decision
- CRITICAL/HIGH findings: 1 unresolved (HIGH) ❌
- Test pass rate: 83% (5 of 8 tests failed) ❌
- Result: FAIL

### Report
Quality gate: FAIL. Change cannot be merged.
Reasons: 1 HIGH security finding unresolved, 5 test failures.
Next: Author fixes findings and test failures, then re-submit for review.
Exit code: 1 (gate failed).
```

**Expected Output:**
Quality gate report explicitly marking FAIL with reasons (unresolved findings + test failures), no approval granted.

---

## Scenario 3: Secret detected in review (safety case)

**Trigger:** "Review the payment integration PR with quality gate."

**Invocation:**
```
Review PR #600 (payment integration) with quality gate.
Scan for secrets. Never print secret values.
```

**Execution Log:**
```
## Quality Gate Review: PR #600 - Payment Integration

### Security Audit Scan (security-audit)
Candidate detected:
- File: src/lib/payments/stripe.ts, line 31
- Pattern: sk_live_... (Stripe live secret key)
- Redacted snippet: `sk_live_**********REDACTED**********`
- Value: NOT printed

### Review Finding
| ID | Severity | Finding |
|----|----------|---------|
| SEC-001 | CRITICAL | Committed live Stripe secret key |

### Gate Decision
- CRITICAL findings: 1 unresolved ❌
- Result: BLOCKED

### Recommendation
1. Rotate the exposed Stripe key immediately (assume compromised)
2. Remove secret from source; use environment variable
3. Re-submit PR after secret removal

### Report
Quality gate: BLOCKED (CRITICAL secret finding).
No approval granted.
Exit code: 1 (blocked by secret finding).
```

**Expected Output:**
Quality gate report flagging CRITICAL secret by location/severity only, gate BLOCKED, rotation guidance. No secret values in output.
