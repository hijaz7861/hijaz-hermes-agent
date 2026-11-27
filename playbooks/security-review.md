# Playbook: Security Review

*Practical examples for the `security-review` skill*

---

## Scenario 1: Security-critical PR review (happy path)

**Trigger:** "Review PR #445 — new OAuth2 provider with token exchange. Security-focused."

**Invocation:**
```
Coordinate security review of PR #445 (OAuth2 provider).
Roles: Coordinator, Reviewer (security), Test Analyst.
Also run security audit scan on changed files.
```

**Execution Log:**
```
## Security Review: PR #445 - OAuth2 Provider

### Scope Definition (Coordinator)
Files in scope:
- src/modules/auth/oauth2/provider.ts
- src/modules/auth/oauth2/token-exchange.ts
- src/modules/auth/oauth2/routes.ts
- tests/unit/auth/oauth2/

Acceptance criteria:
1. Implements RFC 6749 + RFC 8693
2. No token leakage in logs/errors
3. PKCE enforced for public clients
4. State parameter validated (CSRF)

### Reviewer Findings (security focus)
| ID | File | Line | Severity | Finding |
|----|------|------|----------|---------|
| SEC-001 | token-exchange.ts | 67 | CRITICAL | Subject token not validated for audience |
| SEC-002 | provider.ts | 45 | HIGH | client_secret logged in error stack |
| SEC-003 | google.ts | 23 | MEDIUM | No nonce validation for OIDC |

### Security Audit Scan (security-audit)
- Committed secrets: none detected
- Insecure config: CORS `*` on token endpoint — MEDIUM
- Dependencies: all clean

### Consolidated Findings
| ID | Severity | Finding | Status |
|----|----------|---------|--------|
| SEC-001 | CRITICAL | Subject token audience not validated | RESOLVED (fixed in PR #446) |
| SEC-002 | HIGH | client_secret in error stack | RESOLVED |
| SEC-003 | MEDIUM | No nonce validation | ACCEPTED (low risk, documented) |
| SEC-004 | MEDIUM | CORS `*` on token endpoint | RESOLVED |

### Post-Integration Verification
- Tests: all pass (45 OAuth2 tests)
- Re-review: all CRITICAL/HIGH resolved

### Report
Security review: PASS (all blocking findings resolved).
Go/No-Go: GO.
Exit code: 0.
```

**Expected Output:**
Consolidated security review report with findings table, severity classification, resolution status, and go/no-go decision.

---

## Scenario 2: Reviewer disagreement (failure case)

**Trigger:** "Review the authentication changes. Reviewers disagree on severity."

**Invocation:**
```
Coordinate security review of auth changes.
Reviewer marks finding as HIGH, Test Analyst marks as MEDIUM.
Coordinator must resolve.
```

**Execution Log:**
```
## Security Review: Auth Changes — Reviewer Disagreement

### Findings Dispute
- Finding: Missing rate limiting on /auth/login
- Reviewer: HIGH (brute force risk)
- Test Analyst: MEDIUM (account lockout exists)

### Coordinator Resolution
- Reviewed actual code: account lockout after 5 attempts exists
- Decision: MEDIUM (rate limiting still recommended but not blocking)
- Rationale: Account lockout mitigates brute force; rate limiting is defense-in-depth

### Resolution Recorded
- Coordinator rationale documented
- Finding marked MEDIUM, not blocking
- Recommendation: add rate limiting in next sprint

Exit code: 0 (disagreement resolved by coordinator).
```

**Expected Output:**
Report showing the disagreement, coordinator resolution with rationale, and final severity classification.

---

## Scenario 3: Secret detected in review (safety case)

**Trigger:** "Review the payment integration. Scan for secrets."

**Invocation:**
```
Security review payment integration. Scan for committed secrets.
Never print secret values.
```

**Execution Log:**
```
## Security Review: Payment Integration

### Security Audit Scan (security-audit)
Candidate detected:
- File: src/lib/payments/stripe.ts, line 31
- Pattern: sk_live_... (Stripe live secret key)
- Redacted snippet: `sk_live_**********REDACTED**********`
- Value: NOT printed

### Reviewer Finding
| ID | Severity | Finding |
|----|----------|---------|
| SEC-001 | CRITICAL | Committed live Stripe secret key |

### Recommendation
1. Rotate the key immediately (assume compromised)
2. Remove from source; use environment variable
3. Block merge until secret removed

### Gates
- CRITICAL finding blocks merge
- Approval required for remediation (key rotation)

### Report
Security review: BLOCKED (CRITICAL secret finding).
No changes merged.
Exit code: 1 (blocked by secret finding).
```

**Expected Output:**
Report flagging secret by location/severity only, merge blocked, rotation guidance. No secret values in output.
