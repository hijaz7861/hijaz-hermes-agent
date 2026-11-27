# Playbook: Security Operations Center

*Practical examples for the `security-operations-center` skill*

---

## Scenario 1: Full security assessment (happy path)

**Trigger:** "Establish security operations for the auth repository — scan secrets, debug vulnerabilities, audit compliance, review changes, and audit dependencies."

**Invocation:**
```
Execute security operations for auth-repo:
- Scan git history for secrets (last 500 commits)
- Debug: auth token verification vulnerability
- Compliance: GDPR audit for user data handling
- Review: PR #500 (OAuth2 provider)
- Dependencies: audit package.json vulnerabilities
```

**Execution Log:**
```
## Security Operations Center: auth-repo

### Phase 1: Historical Secret Scanning (secret-scanner-historical)
Scan depth: 500 commits
Findings:
| Commit | File | Pattern | Severity | Exposure |
|--------|------|---------|----------|----------|
| a1b2c3d | config/secrets.yml | AWS access key | HIGH | Historical only |
| e4f5g6h | src/auth/tokens.ts | Stripe test key | MEDIUM | Current file |
Current exposure: 1 secret still in current file
Historical exposure: 1 secret in git history only
Recommendation: rotate Stripe test key, remove AWS key from history

### Phase 2: Security Debugging (security-debugger)
Vulnerability: JWT algorithm confusion (none algorithm accepted)
Root cause: src/auth/tokens.ts:45 — jwt.verify() without algorithm constraint
Fix: Added { algorithms: ['HS256'] } option
Regression test: "rejects none algorithm" — fails before, passes after
Verification: exploit blocked, security scan clean, tests pass

### Phase 3: Compliance Auditing (compliance-auditor)
Framework: GDPR
Data types: PII (email, name, IP address), authentication credentials
Gaps:
| Requirement | Current State | Gap | Severity |
|-------------|--------------|-----|----------|
| Right to erasure | No deletion mechanism | Missing user data deletion | HIGH |
| Consent management | Consent not recorded | No consent tracking | HIGH |
| Breach notification | No alerting for breaches | Missing breach detection | MEDIUM |

### Phase 4: Security Review (security-review)
PR #500: OAuth2 provider
Findings:
| ID | Severity | Finding | Status |
|----|----------|---------|--------|
| SEC-001 | HIGH | client_secret in error stack | RESOLVED |
| SEC-002 | MEDIUM | No nonce validation | ACCEPTED |
Security review: PASS (no unresolved CRITICAL/HIGH)

### Phase 5: Dependency Audit (security-dependency-audit)
Vulnerabilities:
| Package | Version | CVE | Severity | Fix |
|---------|---------|-----|----------|-----|
| lodash | 4.17.20 | CVE-2021-23337 | CRITICAL | 4.17.21 |
| minimist | 1.2.5 | CVE-2021-3918 | HIGH | 1.2.6 |
Fixes applied (with approval): lodash → 4.17.21, minimist → 1.2.6
Tests: all pass after fixes

### Phase 6: Consolidated Report
Security posture: NEEDS ATTENTION
- Secrets: 1 current, 1 historical (rotation recommended)
- Vulnerabilities debugged: 1 (JWT algorithm confusion) — FIXED
- Compliance gaps: 2 HIGH, 1 MEDIUM (GDPR)
- Security review: PASS
- Dependencies: 2 fixed (CRITICAL/HIGH resolved)
Prioritized remediation:
1. Rotate Stripe test key (CRITICAL)
2. Implement GDPR user data deletion (HIGH)
3. Implement GDPR consent tracking (HIGH)
4. Add breach detection alerting (MEDIUM)
Exit code: 0.
```

**Expected Output:**
Security operations report with findings from all five phases, prioritized remediation plan, and overall security posture assessment.

---

## Scenario 2: Active vulnerability cannot be fixed (failure case)

**Trigger:** "Security operations — debug the authentication bypass vulnerability."

**Invocation:**
```
Debug auth bypass in src/auth/middleware.ts.
Exploit still works after attempted fix.
```

**Execution Log:**
```
## Security Operations Center: auth-repo — Debug Phase

### Phase 2: Security Debugging
Vulnerability: auth bypass in session middleware
Exploit: modified session cookie grants admin access
Reproduction: deterministic — works every time

### Hypotheses tested
1. Session signature not verified — TESTED, not the cause
2. Session expiration not checked — TESTED, not the cause  
3. Admin flag not validated — CONFIRMED as root cause

### Fix Applied
- src/auth/middleware.ts:89 — Added admin flag validation
- Regression test: "rejects unauthorized admin access" — added

### Verification (FAILED)
Exploit test after fix: STILL SUCCEEDS
Root cause analysis: second validation path in src/auth/middleware.ts:145 also missing admin check

### Status
Vulnerability: NOT RESOLVED
Fix attempt: 1 applied, exploit still works
Additional investigation needed: second code path

### Report
Security debugging: INCOMPLETE
Vulnerability: auth bypass — still exploitable
Next: investigate second validation path, apply second fix, re-verify
Exit code: 1 (vulnerability not resolved, investigation ongoing).
```

**Expected Output:**
Security debugging report showing root cause, fix attempt, failed verification, and next investigation steps.

---

## Scenario 3: Secret found in current production file (safety case)

**Trigger:** "Security operations — scan for secrets. Production key found."

**Invocation:**
```
Scan git history and current files for secrets.
Production API key found in src/config/production.yml.
DO NOT print the key value.
```

**Execution Log:**
```
## Security Operations Center: auth-repo — Secret Scan

### Phase 1: Historical Secret Scanning
Findings:
| Commit | File | Pattern | Severity | Exposure |
|--------|------|---------|----------|----------|
| current | src/config/production.yml | Stripe live secret key | CRITICAL | CURRENT FILE |
| 9f8e7d6 | .env.example | Stripe test key | MEDIUM | Historical only |

### Safety Verification
- Secret value: NOT printed anywhere in output
- File location recorded: src/config/production.yml:15
- Pattern type: Stripe live secret key
- Exposure: CURRENT (active production risk)

### Immediate Actions Required
1. ROTATE the Stripe live key immediately (assume compromised)
2. Remove key from source code; use environment variable
3. Audit git history for prior exposures
4. Add .gitignore for *.yml files containing secrets
5. Add pre-commit hook to block secret patterns

### Phase 6: Consolidated Report
Security posture: CRITICAL RISK
- Active production secret exposed: 1 (Stripe live key)
- Release gate: BLOCKED (active secret in production code)
- No changes deployed until secret is removed and rotated
Exit code: 1 (critical active secret, release blocked).
```

**Expected Output:**
Security operations report flagging active production secret by location/severity only, release blocked, rotation guidance. No secret values in output.
