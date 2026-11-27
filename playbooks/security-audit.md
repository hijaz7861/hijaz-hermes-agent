# Playbook: Security Audit

*Practical examples for the `security-audit` skill*

---

## Scenario 1: Pre-release security audit (happy path)

**Trigger:** "Run a security audit before the v1.2.0 release."

**Invocation:**
```
Security audit this repository. Focus on:
- Committed secrets in source and config
- Vulnerable dependencies in package.json/lockfile
- Insecure configuration (TLS, CORS, cookies)
Report findings with file:line and severity.
```

**Execution Log:**
```
## Security Audit: acme-web (v1.2.0-rc)

### Scope
- Repository root: /workspace/app
- Branch: release/v1.2.0
- Working tree: clean
- Areas in scope: auth/, payments/, config/, src/lib/crypto.ts

### Secrets Scan
Scanned: source, config, CI/CD files, last 50 commits.
Result: No committed secrets detected.
Evidence: grep patterns for AWS keys, GitHub tokens, private keys, connection strings — no matches.

### Dependency Audit
Tool: npm audit (available)
Findings:
1. `lodash` 4.17.20 → FIXED in 4.17.21 — PROTOTYPE POLLUTION — HIGH — file: package.json:14
2. `express` 4.18.2 → current, no known vuln — INFO
Evidence: `npm audit` output captured.

### Configuration Review
1. CORS origin set to `*` in src/config/cors.ts:8 — MEDIUM — permits any origin
2. Session cookie missing `Secure` and `HttpOnly` flags — src/config/session.ts:22 — MEDIUM
3. TLS enforcement enabled — src/config/tls.ts:3 — PASS

### Consolidated Findings
| ID | Severity | Finding | Location | Evidence | Approval Required |
|----|----------|---------|----------|----------|-------------------|
| SEC-01 | HIGH | lodash prototype pollution | package.json:14 | npm audit advisory | Yes (patch) |
| SEC-02 | MEDIUM | Permissive CORS | src/config/cors.ts:8 | grep match `*` | Yes (config change) |
| SEC-03 | MEDIUM | Cookie missing Secure/HttpOnly | src/config/session.ts:22 | grep match | Yes (config change) |

### Status
Verified findings: 3. Hypotheses: 0. Unchecked: 0.
No secrets printed in plaintext.
Exit code: 0 (findings reported, none blocking without approval).
```

**Expected Output:**
A Markdown report with executive summary, findings table, remediation priority order, and explicit separation of verified vs. hypothesized findings.

---

## Scenario 2: Secret detected in code (safety case)

**Trigger:** "Check this branch for leaked credentials."

**Invocation:**
```
Audit feature/payment-integration for secrets. Do not print secret values.
```

**Execution Log:**
```
## Security Audit: feature/payment-integration

### Secrets Scan
Candidate detected:
- File: src/lib/payments/stripe.ts, line 31
- Pattern: sk_live_... (Stripe live secret key)
- Redacted snippet: `sk_live_**********REDACTED**********`
- Action: Value NOT printed. Location recorded only.

### Recommendation
1. Rotate the exposed key immediately (assume compromised).
2. Remove the secret from source; use environment variable or secret manager.
3. Audit git history for prior exposures (bounded scan recommended).

### Status
Finding: SEC-04 CRITICAL — committed live secret key.
Verification: Verified (pattern match, value not disclosed).
Approval required before any remediation (rotation, file change).
Exit code: 0 (finding reported; remediation blocked on approval).
```

**Expected Output:**
A report flagging the secret by location and severity only, with rotation and removal guidance. No secret value appears anywhere in output.

---

## Scenario 3: Audit tool unavailable (failure case)

**Trigger:** "Audit dependencies. `npm audit` is not available in this environment."

**Invocation:**
```
Dependency audit for requirements.txt. pip-audit may not be installed.
```

**Execution Log:**
```
## Dependency Audit: acme-api

### Tool Check
- `pip-audit`: not installed → unavailable
- Fallback: manual manifest review of requirements.txt

### Findings (hypothesized, unverified)
- `django` 3.2.10 → latest 4.2.x — outdated — severity unverified
- `requests` 2.25.1 → current — no known issue per local data

### Status
- Verified: 0 (tool unavailable)
- Hypothesized: 2 (manual review only)
- Unchecked: all transitive dependencies
- Note: Install `pip-audit` or grant network access to verify.

Exit code: 0 (audit incomplete due to tooling limitation, clearly reported).
```

**Expected Output:**
A report distinguishing verified findings from hypotheses, clearly stating the tooling limitation and what remains unchecked.
