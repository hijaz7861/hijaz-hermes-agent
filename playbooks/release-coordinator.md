# Playbook: Release Coordinator

*Practical examples for the `release-coordinator` skill*

---

## Scenario 1: Prepare a patch release (happy path)

**Trigger:** "Prepare release v1.2.1. All fixes are merged and reviewed."

**Invocation:**
```
Prepare release v1.2.1 on branch release/v1.2.1.
Verify: tests pass, review complete, security clean.
Assemble changelog. Bump version only with approval.
```

**Execution Log:**
```
## Release Coordination: v1.2.1

### Scope
- Target version: 1.2.1 (patch)
- Branch: release/v1.2.1
- Commit range: v1.2.0..HEAD (14 commits)
- Changed files: src/lib/auth.ts, src/lib/payments.ts, tests/auth.test.ts

### Readiness Checks
1. Test suite — PASS (47 tests, 0 failures)
2. Lint + type-check + build — PASS
3. Code review — COMPLETE (all 14 commits reviewed and merged)
4. Security audit — CLEAN (no unresolved CRITICAL/HIGH findings)
5. Dependency updates — none pending

### Changelog (assembled)
## v1.2.1 — 2026-11-27

### Fixes
- Fix token expiration check in auth middleware (#312) — @dev-alice
- Retry failed payment webhook with idempotency key (#318) — @dev-bob

### Dependencies
- Bump lodash 4.17.20 → 4.17.21 (security patch)

### Gates
- Approval: PENDING (user sign-off required before tag)
- Quality: PASSED
- Security: PASSED

### Version Bump (approval requested)
Current: 1.2.0 → Proposed: 1.2.1
Files: package.json, src/version.ts
Action: AWAITING USER APPROVAL — no tag created yet.

### Report
Release v1.2.1: READY FOR APPROVAL.
All gates passed except user approval (pending).
Not deployed/published.
Exit code: 0.
```

**Expected Output:**
A release report with scope, readiness check results, changelog, gate status, and an explicit pending-approval state for the version bump. No tag or publish occurs.

---

## Scenario 2: Tests failing (blocked case)

**Trigger:** "Cut release v2.0.0. Everything is ready."

**Invocation:**
```
Prepare release v2.0.0. Verify readiness before bumping version.
```

**Execution Log:**
```
## Release Coordination: v2.0.0

### Readiness Checks
1. Test suite — FAILURE: 3 tests fail
   - `tests/billing/flow.test.ts::webhook idempotency` — TimeoutError
   - `tests/billing/flow.test.ts::reconciliation` — AssertionError
2. Lint + build — PASS
3. Code review — COMPLETE
4. Security audit — CLEAN

### Gates
- Quality: FAILED (tests not green)
- Security: PASSED
- Approval: NOT REQUESTED (blocked on quality gate)

### Report
Release v2.0.0: BLOCKED.
Reason: 3 test failures in billing flow. Version not bumped. No tag created.
Next: Fix failing tests, re-run readiness check, then request approval.
Exit code: 1 (release blocked).
```

**Expected Output:**
A release report explicitly marking the release BLOCKED with reasons, no version bump or tag, and clear next steps.

---

## Scenario 3: Approval denied (safety case)

**Trigger:** "Release v1.3.0. Bump version and tag when ready."

**Invocation:**
```
Prepare release v1.3.0. All checks pass. Request approval before version bump/tag.
```

**Execution Log:**
```
## Release Coordination: v1.3.0

### Readiness Checks — ALL PASSED
- Tests: PASS
- Lint/type/build: PASS
- Review: COMPLETE
- Security: CLEAN

### Changelog — Assembled
(Features: 2, Fixes: 5, Docs: 1)

### Gates
- Quality: PASSED
- Security: PASSED
- Approval: DENIED by user — "Hold release pending QA sign-off"

### Report
Release v1.3.0: READY BUT ON HOLD.
All technical gates passed. Version bump and tag NOT performed (approval denied).
No deploy/publish attempted.
Next: Re-request approval after QA sign-off.
Exit code: 0.
```

**Expected Output:**
A release report showing all technical gates passed but the release held due to denied approval. No version change, tag, or publish occurs.
