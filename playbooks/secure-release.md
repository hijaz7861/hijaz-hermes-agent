# Playbook: Secure Release

*Practical examples for the `secure-release` skill*

---

## Scenario 1: Clean security audit, release approved (happy path)

**Trigger:** "Prepare secure release v1.3.0. Security audit must pass."

**Invocation:**
```
Prepare secure release v1.3.0 on branch release/v1.3.0.
Verify readiness, run security audit, assemble changelog.
Bump version only with approval. Security gate: no unresolved CRITICAL/HIGH.
```

**Execution Log:**
```
## Secure Release: v1.3.0

### Release Scope (release-coordinator)
- Target version: 1.3.0 (minor)
- Branch: release/v1.3.0
- Commit range: v1.2.0..HEAD (22 commits)

### Readiness Checks
1. Test suite — PASS (89 tests, 0 failures)
2. Lint + typecheck + build — PASS
3. Code review — COMPLETE (all 22 commits reviewed)
4. Dependency updates — none pending

### Security Audit (security-audit)
Findings:
- No committed secrets detected
- `lodash` 4.17.20 — CVE-2021-23337 — CRITICAL — fixed in 4.17.21
- All other dependencies: clean

### Security Gate
- CRITICAL finding: lodash prototype pollution
- Fix available: 4.17.20 → 4.17.21 (patch)
- Fix applied and verified: tests pass, `npm audit` clean
- Gate status: PASSED (vulnerability resolved)

### Changelog (assembled)
## v1.3.0 — 2026-11-27
### Features
- OAuth2 provider support (#345)
### Fixes
- Payment webhook retry (#318)
### Dependencies
- lodash 4.17.20 → 4.17.21 (security patch)

### Gates
- Quality: PASSED
- Security: PASSED
- Approval: PENDING (user sign-off required before version bump)

### Report
Release v1.3.0: READY FOR APPROVAL.
Security gate passed (vulnerability remediated).
Version bump not yet performed (awaiting approval).
No deploy/publish attempted.
Exit code: 0.
```

**Expected Output:**
Release report with scope, readiness checks, security audit findings, gate status, changelog, and pending-approval state.

---

## Scenario 2: Security findings block release (blocked case)

**Trigger:** "Cut release v2.0.0. Everything is ready."

**Invocation:**
```
Prepare secure release v2.0.0. Verify readiness and security before bumping.
```

**Execution Log:**
```
## Secure Release: v2.0.0

### Readiness Checks
1. Test suite — PASS
2. Lint + build — PASS
3. Code review — COMPLETE

### Security Audit (security-audit)
Findings:
1. `src/auth/middleware.ts:45` — hardcoded API key — CRITICAL
2. `src/config/cors.ts:8` — CORS origin `*` — HIGH

### Security Gate
- CRITICAL: hardcoded API key — UNRESOLVED → GATE BLOCKED
- HIGH: permissive CORS — UNRESOLVED → GATE BLOCKED
- Release status: BLOCKED

### Report
Release v2.0.0: BLOCKED.
Reasons: CRITICAL (hardcoded secret) and HIGH (permissive CORS) findings unresolved.
Version not bumped. No tag created.
Next: Remediate security findings, re-run audit, then request approval.
Exit code: 1 (release blocked by security gate).
```

**Expected Output:**
Release report explicitly marking BLOCKED with security reasons, no version bump or tag.

---

## Scenario 3: Approval denied despite clean security (safety case)

**Trigger:** "Release v1.4.0. All checks pass. Request approval before version bump."

**Invocation:**
```
Prepare secure release v1.4.0. All checks pass. Request approval before version bump/tag.
```

**Execution Log:**
```
## Secure Release: v1.4.0

### Readiness Checks — ALL PASSED
- Tests: PASS
- Lint/type/build: PASS
- Review: COMPLETE
- Security: CLEAN (no unresolved findings)

### Changelog — Assembled
(Features: 3, Fixes: 4, Docs: 1)

### Gates
- Quality: PASSED
- Security: PASSED
- Approval: DENIED — "Hold release pending QA sign-off"

### Report
Release v1.4.0: READY BUT ON HOLD.
All technical gates passed including security. Version bump and tag NOT performed (approval denied).
No deploy/publish attempted.
Next: Re-request approval after QA sign-off.
Exit code: 0.
```

**Expected Output:**
Release report showing all gates passed but release held due to denied approval. No version change, tag, or publish.
