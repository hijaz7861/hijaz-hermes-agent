# Playbook: Security Debugger

*Practical examples for the `security-debugger` skill*

---

## Scenario 1: SQL injection debug and fix (happy path)

**Trigger:** "Debug the SQL injection vulnerability in the user lookup endpoint."

**Invocation:**
```
Debug SQL injection in src/api/users.ts: getUserById endpoint.
Reproduce the injection, find root cause, apply fix, verify with regression test.
```

**Execution Log:**
```
## Security Debug: SQL Injection in getUserById

### Capture the security failure (autonomous-debugging)
- Vulnerability: SQL injection in getUserById endpoint
- Exploit input: userId = "1 OR 1=1"
- Expected: return one user
- Actual: returns all users (bypasses WHERE clause)
- Reproduction: deterministic — exploit works every time

### Security audit scan (security-audit)
- Scanned src/api/users.ts and related files
- No committed secrets detected
- No additional injection points found in this module
- Related file: src/api/users.ts:23 — string concatenation in query

### Root Cause
File: src/api/users.ts:23
Code: `const query = "SELECT * FROM users WHERE id = " + userId`
Vulnerability type: SQL injection (unsanitized string concatenation)
Evidence: userId directly interpolated into SQL query without parameterization

### Fix Applied
- src/api/users.ts:23 — Replaced string concatenation with parameterized query
  `const query = "SELECT * FROM users WHERE id = $1"`
  `const result = await db.query(query, [userId])`

### Regression Test Added
- tests/security/users/injection.test.ts: "getUserById blocks SQL injection"
  - Before fix: exploit returns all users (test FAILS)
  - After fix: exploit returns empty or one user (test PASSES)

### Verification (security-audit + autonomous-debugging)
- Reproduction: exploit no longer succeeds (returns 0 or 1 user)
- Security scan of src/api/users.ts: no new findings
- Full test suite: PASS (89 tests)
- Typecheck: CLEAN
- No secret values logged

Exit code: 0.
```

**Expected Output:**
Security debug report with reproduction evidence, root cause (file:line, vulnerability type), fix, regression test, before/after verification.

---

## Scenario 2: Cannot reproduce exploit (failure case)

**Trigger:** "Debug intermittent auth bypass in the session middleware."

**Invocation:**
```
Debug intermittent auth bypass in src/auth/middleware.ts.
Occurs occasionally under load — not always reproducible.
```

**Execution Log:**
```
## Security Debug: Intermittent Auth Bypass

### Capture the security failure
- Vulnerability: occasional auth bypass under high load
- Reproduction: NOT deterministic (1 in 50 requests under load)
- Cannot reliably reproduce on demand

### Hypotheses (labeled as unconfirmed)
1. Race condition in session validation — UNCONFIRMED
2. Token validation timeout under load — UNCONFIRMED
3. Middleware execution order issue — UNCONFIRMED

### Security audit scan (security-audit)
- Scanned src/auth/middleware.ts
- No committed secrets detected
- No static injection points found
- No weak crypto identified

### Status
- Cannot reproduce deterministically
- Continuing with labeled hypotheses only
- Recommendation: Add structured logging to capture next occurrence under load
- Recommendation: Run load test with session validation tracing

Exit code: 0 (investigation ongoing, hypotheses documented, no fix applied).
```

**Expected Output:**
Report stating non-reproducible issue, labeled hypotheses, security scan results, and recommendations for capturing next occurrence.

---

## Scenario 3: Secret detected during debugging (safety case)

**Trigger:** "Debug the auth token module. It handles JWT secrets."

**Invocation:**
```
Debug token verification issue in src/auth/tokens.ts.
DO NOT log or expose JWT secret keys or token values.
```

**Execution Log:**
```
## Security Debug: Token Verification in src/auth/tokens.ts

### Data Classification
- JWT signing secret: RESTRICTED — never log or expose
- Token values: CONFIDENTIAL — never log in plaintext
- User ID: INTERNAL — OK to log
- Token ID (JTI): PUBLIC — OK to log

### Security audit scan (security-audit)
- Scanned src/auth/tokens.ts
- No committed secrets detected in current code
- Token verification logic: uses jwt.verify() with secret from env var

### Root Cause
File: src/auth/tokens.ts:45
Issue: jwt.verify() called without options — algorithm not constrained
Vulnerability type: algorithm confusion (none algorithm acceptance)

### Fix Applied
- src/auth/tokens.ts:45 — Added algorithm constraint: { algorithms: ['HS256'] }

### Regression Test Added
- tests/security/tokens/algorithm.test.ts: "rejects none algorithm"
  - Before fix: token with "alg: none" accepted (test FAILS)
  - After fix: token with "alg: none" rejected (test PASSES)

### Safety Verification
- No secret values in fix, tests, or output
- JWT secret never logged
- Token values never logged (only JTI)

Exit code: 0.
```

**Expected Output:**
Security debug report with data classification, root cause, fix, regression test, and explicit confirmation that no secrets were logged or exposed.
