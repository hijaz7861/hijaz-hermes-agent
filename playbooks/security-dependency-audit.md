# Playbook: Security Dependency Audit

*Practical examples for the `security-dependency-audit` skill*

---

## Scenario 1: Pre-release dependency security audit (happy path)

**Trigger:** "Audit dependencies for security vulnerabilities before the v2.0.0 release."

**Invocation:**
```
Audit all dependencies for security vulnerabilities. Focus on CRITICAL and HIGH findings.
Package manager: npm. Report vulnerable packages with CVE IDs and fix versions.
```

**Execution Log:**
```
## Security Dependency Audit: v2.0.0 release

### Dependency Inventory (dependency-management)
Manifest: package.json + package-lock.json
Direct dependencies: 34
Transitive dependencies: 218
Package manager: npm

### Vulnerability Scan (security-audit)
Tool: `npm audit` (available)
Findings:
1. `lodash` 4.17.20 — CVE-2021-23337 — Prototype Pollution — CRITICAL — fixed in 4.17.21
2. `minimist` 1.2.5 — CVE-2021-3918 — Prototype Pollution — HIGH — fixed in 1.2.6
3. `ansi-regex` 5.0.1 — CVE-2022-1884 — ReDoS — MEDIUM — fixed in 6.0.1 (major bump)

### Prioritization
| Priority | Package | Current | Fixed | CVE | Severity | Breaking Risk | Approval Required |
|----------|---------|---------|-------|-----|----------|---------------|-------------------|
| P0 | lodash | 4.17.20 | 4.17.21 | CVE-2021-23337 | CRITICAL | No (patch) | Yes |
| P1 | minimist | 1.2.5 | 1.2.6 | CVE-2021-3918 | HIGH | No (patch) | Yes |
| P2 | ansi-regex | 5.0.1 | 6.0.1 | CVE-2022-1884 | MEDIUM | Yes (major) | Yes |

### Applied (with user approval)
- `lodash` 4.17.20 → 4.17.21 — applied, tests pass, `npm audit` clean for this vuln
- `minimist` 1.2.5 → 1.2.6 — applied, tests pass

### Pending (approval required)
- `ansi-regex` 5.0.1 → 6.0.1 — major bump, not applied

### Report
Audited: 252 packages. Vulnerabilities: 3 (1 CRITICAL, 1 HIGH, 1 MEDIUM).
Fixed: 2. Pending: 1 (major version bump, approval required).
Remaining risk: 0 unpatched CRITICAL/HIGH vulnerabilities.
Exit code: 0.
```

**Expected Output:**
Security dependency report with vulnerability findings, CVE IDs, severity, fix versions, applied/pending status, and approval requirements.

---

## Scenario 2: No fix available (failure case)

**Trigger:** "Audit dependencies. Some packages have vulnerabilities with no fix."

**Invocation:**
```
Audit dependencies. Report vulnerabilities even if no fix is available.
```

**Execution Log:**
```
## Security Dependency Audit: legacy-service

### Vulnerability Scan
Tool: `npm audit` (available)
Findings:
1. `old-package` 1.0.0 — CVE-2020-9999 — Remote Code Execution — CRITICAL — NO FIX AVAILABLE
2. `deprecated-lib` 2.3.1 — CVE-2019-1234 — Information Disclosure — HIGH — NO FIX AVAILABLE

### Remediation Options (no fix available)
| Package | Vulnerability | Option | Risk |
|---------|--------------|--------|------|
| old-package | CVE-2020-9999 | Replace with alternative package | High (code changes) |
| old-package | CVE-2020-9999 | Network-level mitigation (WAF rule) | Medium |
| deprecated-lib | CVE-2019-1234 | Pin version, monitor for patches | Medium |

### Status
- Unpatched CRITICAL: 1 (old-package)
- Unpatched HIGH: 1 (deprecated-lib)
- Release gate: BLOCKED (unresolved CRITICAL vulnerability)
Exit code: 1 (release blocked due to unpatched critical vulnerability).
```

**Expected Output:**
Report listing unpatched vulnerabilities, remediation options (replacement, mitigation), and explicit release block status.

---

## Scenario 3: Secret detected during audit (safety case)

**Trigger:** "Audit dependencies. Also scan for committed secrets."

**Invocation:**
```
Security audit dependencies and scan for secrets. Never print secret values.
```

**Execution Log:**
```
## Security Dependency Audit: feature/payment-integration

### Secrets Scan (security-audit)
Candidate detected:
- File: src/lib/payments/stripe.ts, line 31
- Pattern: sk_live_... (Stripe live secret key)
- Redacted snippet: `sk_live_**********REDACTED**********`
- Value: NOT printed. Location recorded only.

### Dependency Vulnerabilities
- `stripe` 8.120.0 — current, no known vulnerabilities — INFO

### Recommendation
1. Rotate the exposed Stripe key immediately (assume compromised).
2. Remove secret from source; use environment variable or secret manager.
3. Patch: none needed for stripe dependency.

### Status
- Secret finding: CRITICAL — committed live secret key
- Approval required before any remediation (key rotation, file change)
- No secret values printed anywhere in output
Exit code: 0 (finding reported; remediation blocked on approval).
```

**Expected Output:**
Report flagging secret by location and severity only, with rotation guidance. No secret values appear in output.
