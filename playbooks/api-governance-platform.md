# Playbook: API Governance Platform

*Practical examples for the `api-governance-platform` skill*

---

## Scenario 1: Complete API governance review (happy path)

**Trigger:** "Govern the orders API v2 — validate contract, manage version, security review, and quality gate."

**Invocation:**
```
Execute API governance for orders API v2:
- Contract: OpenAPI spec at docs/openapi/orders-v2.yaml
- Version: v2 (deprecating v1)
- Security: auth, authorization, input validation
- Quality gate: 100% test pass, zero CRITICAL/HIGH findings
- Deprecation: v1 sunset in 90 days
```

**Execution Log:**
```
## API Governance Platform: orders API v2

### Phase 1: Contract Testing (api-contract-tester)
Contract: OpenAPI 3.0, 12 endpoints
Implementation: src/api/orders/ (6 controllers, 14 routes)
Results:
- Endpoints tested: 12/12 ✅
- Missing endpoints: 0
- Schema mismatches: 0
- Breaking changes: 0 (v2 is backward compatible with v1)
Contract compliance: PASS

### Phase 2: Version Management (api-version-manager)
Versions:
- v1: ACTIVE (sunset: 2027-02-27, 90 days from now)
- v2: ACTIVE (new, fully implemented)
- v0: SUNSET (sunset date passed, 2 clients still using)
Breaking changes v1→v2: NONE (additive only)
Migration guide: generated — clients can move to v2 without changes
Client compliance: 2 clients on v0 (sunset), 15 on v1, 3 on v2

### Phase 3: Security Review (security-review)
Scope: src/api/orders/ (changed files)
Findings:
| ID | Severity | Finding | Status |
|----|----------|---------|--------|
| SEC-001 | MEDIUM | Order ID sequential — predictable | ACCEPTED (low risk) |
| SEC-002 | LOW | Missing rate limit on GET /orders | RESOLVED |
Security audit: no committed secrets, dependencies clean
Security review: PASS (no unresolved CRITICAL/HIGH)

### Phase 4: Quality Gate Review (quality-gate-review)
Gate criteria: 100% test pass, zero CRITICAL/HIGH
Test results:
- Unit: 47 passed, 0 failed ✅
- Integration: 23 passed, 0 failed ✅
- Lint/typecheck/build: CLEAN ✅
Gate decision: PASS

### Phase 5: Consolidated Report
- Contract: PASS (12/12 endpoints compliant)
- Version: v2 ACTIVE, v1 sunset planned, v0 SUNSET (2 clients need migration)
- Security: PASS (no blocking findings)
- Quality: PASS (100% test pass)
Final decision: GO — orders API v2 approved for release
Exit code: 0.
```

**Expected Output:**
API governance report with contract compliance, version inventory, security findings, quality gate decision, and final go/no-go recommendation.

---

## Scenario 2: Breaking contract change detected (failure case)

**Trigger:** "Govern the payments API v3 — there are breaking changes."

**Invocation:**
```
Execute API governance for payments API v3.
Contract: OpenAPI spec at docs/openapi/payments-v3.yaml
```

**Execution Log:**
```
## API Governance Platform: payments API v3

### Phase 1: Contract Testing
Breaking changes detected:
| Change | Type | Severity |
|--------|------|----------|
| Removed endpoint: POST /payments/refund | BREAKING | CRITICAL |
| Changed parameter: amount (integer → string) | BREAKING | HIGH |
| Added required field: currency | BREAKING | MEDIUM |

Contract compliance: FAIL (3 breaking changes)

### Phase 2: Version Management
Versions:
- v2: ACTIVE
- v3: PROPOSED (has breaking changes)
Migration guide: generated — clients must update refund workflow
Client impact: 8 clients use /payments/refund endpoint

### Phase 3-5: Blocked
Security review: SKIPPED (contract failure blocks gate)
Quality gate: BLOCKED (contract non-compliance)
Final decision: NO-GO — breaking changes must be resolved

### Report
API governance: BLOCKED
Breaking changes: 3 (1 CRITICAL, 1 HIGH, 1 MEDIUM)
Required actions:
1. Restore POST /payments/refund endpoint or provide migration path
2. Keep amount as integer or add versioned endpoint
3. Make currency optional or provide default
Exit code: 1 (contract non-compliance, gate blocked).
```

**Expected Output:**
API governance report showing breaking changes, contract compliance failure, NO-GO decision, and required remediation actions.

---

## Scenario 3: Secret detected during security review (safety case)

**Trigger:** "Govern the auth API — scan for secrets in the code."

**Invocation:**
```
Execute API governance for auth API.
Security review: scan for committed secrets.
NEVER print secret values.
```

**Execution Log:**
```
## API Governance Platform: auth API

### Phase 1-2: Contract and Version
Contract compliance: PASS
Version management: v1 ACTIVE, no breaking changes

### Phase 3: Security Review
Security audit scan:
Candidate detected:
- File: src/api/auth/tokens.ts, line 31
- Pattern: sk_live_... (Stripe live secret key)
- Redacted snippet: `sk_live_**********REDACTED**********`
- Value: NOT printed anywhere

Security finding:
| ID | Severity | Finding |
|----|----------|---------|
| SEC-001 | CRITICAL | Committed live Stripe secret key |

Security review: BLOCKED (CRITICAL unresolved)

### Phase 4-5: Blocked
Quality gate: BLOCKED (security gate unmet)
Final decision: NO-GO — CRITICAL security finding

### Recommendation
1. Rotate the Stripe key immediately (assume compromised)
2. Remove secret from source; use environment variable
3. Add pre-commit hook to prevent future commits
4. Re-submit for governance after remediation

Exit code: 1 (CRITICAL secret finding, governance blocked).
```

**Expected Output:**
API governance report flagging CRITICAL secret by location/severity only, governance BLOCKED, rotation guidance. No secret values in output.
