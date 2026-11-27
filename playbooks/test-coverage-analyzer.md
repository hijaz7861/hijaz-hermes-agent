# Playbook: Test Coverage Analyzer

*Practical examples for the `test-coverage-analyzer` skill*

---

## Scenario 1: Coverage gap analysis for auth module (happy path)

**Trigger:** "Analyze test coverage gaps in src/auth/ — find untested code paths."

**Invocation:**
```
Analyze test coverage gaps in src/auth/. Target threshold: 90% coverage.
Report uncovered file:line locations with risk levels and test recommendations.
```

**Execution Log:**
```
## Test Coverage Analysis: src/auth/

### Codebase Map (codebase-intelligence)
Modules: AuthService, SessionManager, TokenValidator, Middleware
Public symbols: 14 (authenticate, logout, refreshToken, validateSession, etc.)
Entry points: src/auth/routes.ts (/auth/* endpoints)
Trust boundaries: external input → validation → business logic → DB
Risk areas: token handling, password comparison, session fixation

### Existing Coverage Analysis (autonomous-testing)
Baseline coverage: 68% (14 public symbols, 9 tested, 5 untested)
Coverage report found: tests/unit/auth/ (12 tests), tests/integration/auth/ (8 tests)

### Coverage Gaps Identified
| File:Line | Symbol | Risk | Untested Aspect | Test Recommendation |
|-----------|--------|------|-----------------|---------------------|
| src/auth/middleware.ts:45 | authenticate() | CRITICAL | Invalid credentials rejection | Unit: invalid creds → 401 |
| src/auth/middleware.ts:67 | validateSession() | CRITICAL | Expired session rejection | Unit: expired token → 401 |
| src/auth/TokenValidator.ts:23 | validateToken() | HIGH | Malformed token handling | Unit: malformed JWT → error |
| src/auth/SessionManager.ts:89 | createSession() | MEDIUM | Session creation with metadata | Integration: create + verify |
| src/auth/password.ts:12 | hashPassword() | MEDIUM | Weak password rejection | Unit: weak password → error |

### Prioritized Recommendations
P0 (Critical - Security): authenticate(), validateSession() — add unit tests for rejection cases
P1 (High - Logic): validateToken() — add unit test for malformed tokens
P2 (Medium - Coverage): createSession(), hashPassword() — add integration/unit tests

### Verification (after applying P0 + P1, with approval)
- Coverage: 68% → 85% (+17%)
- All existing tests pass (20 tests)
- No new bottlenecks or failures

Exit code: 0.
```

**Expected Output:**
Coverage gap report with baseline, gaps table (file:line, risk, recommendation), prioritized test plan, and before/after coverage verification.

---

## Scenario 2: No coverage data available (failure case)

**Trigger:** "Analyze coverage gaps. No coverage reports exist in this repo."

**Invocation:**
```
Analyze test coverage gaps in src/utils/. No coverage data available.
Use static analysis to estimate gaps.
```

**Execution Log:**
```
## Test Coverage Analysis: src/utils/

### Coverage Data Check
- Coverage reports: none found (no lcov, cobertura, or json reports)
- Coverage tool: not configured in package.json

### Fallback: Static Analysis Only
- Mapped 12 public symbols across 4 files
- Identified 0 existing test files for src/utils/
- All 12 symbols marked as "untested — no test files found"

### Estimated Gaps (static analysis, unverified)
| File:Line | Symbol | Estimated Risk | Basis |
|-----------|--------|----------------|-------|
| src/utils/format.ts:15 | formatDate() | MEDIUM | No test file exists |
| src/utils/validation.ts:8 | validateEmail() | HIGH | Input validation, no tests |
| src/utils/crypto.ts:22 | hashData() | CRITICAL | Crypto function, no tests |

### Limitations
- Coverage percentages: cannot be computed (no coverage data)
- Risk levels: estimated from code structure only
- Test recommendations: pending test file creation

### Status
- Verified gaps: 0 (no coverage data)
- Estimated gaps: 3 (static analysis)
- Note: Install coverage tooling (e.g., nyc, coverage.py) for verified measurements.

Exit code: 0 (analysis incomplete due to missing coverage data, clearly reported).
```

**Expected Output:**
Report stating coverage analysis is incomplete due to missing data, providing static-analysis-based gap estimates with clear limitations.

---

## Scenario 3: High-risk untested security boundary (safety case)

**Trigger:** "Analyze coverage in src/payments/ — focus on security boundaries."

**Invocation:**
```
Analyze test coverage gaps in src/payments/. Focus on security boundaries and data mutation.
Flag any untested security-critical paths as CRITICAL.
```

**Execution Log:**
```
## Test Coverage Analysis: src/payments/ (Security Focus)

### Codebase Map
Modules: PaymentProcessor, WebhookHandler, RefundService
Public symbols: 18
Trust boundaries: external webhook → validation → payment mutation → DB
Risk areas: webhook signature verification, refund authorization, payment idempotency

### Coverage Analysis
Baseline: 45% (18 symbols, 8 tested, 10 untested)

### Security-Critical Gaps
| File:Line | Symbol | Risk | Security Concern |
|-----------|--------|------|------------------|
| src/payments/WebhookHandler.ts:34 | verifyWebhookSignature() | CRITICAL | Webhook not signature-verified — spoofing risk |
| src/payments/PaymentProcessor.ts:67 | processRefund() | CRITICAL | Refund without authorization check |
| src/payments/PaymentProcessor.ts:89 | processPayment() | HIGH | Idempotency key not validated — duplicate charges |

### Status
- CRITICAL untested security boundaries: 2
- HIGH untested critical paths: 1
- Release gate: BLOCKED (security-critical code untested)

### Recommendation
Add tests BEFORE any release:
1. Unit test: verifyWebhookSignature rejects invalid signatures
2. Unit test: processRefund requires authorization
3. Integration test: processPayment idempotency with duplicate key

Exit code: 1 (security-critical coverage gaps found, release blocked).
```

**Expected Output:**
Coverage report flagging security-critical untested paths as CRITICAL, with explicit release block status and test recommendations.
