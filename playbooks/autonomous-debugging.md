# Playbook: Autonomous Debugging

*Practical examples for the `autonomous-debugging` skill*

---

## Scenario 1: Flaky Test Diagnosis

**Trigger:** "Test `tests/integration/billing/webhook.test.ts` fails 1/10 times."

**Invocation:**
```
Debug the flaky test in tests/integration/billing/webhook.test.ts:
- Reproduce the failure locally
- Identify the root cause (race condition, timing, state leak, external dependency)
- Provide minimal fix with regression test
- Verify fix eliminates flakiness
```

**Execution Log:**
```
## Debugging Session: Flaky Webhook Test

### 1. Capture Failure
```
$ pnpm test tests/integration/billing/webhook.test.ts --reporter=verbose
✓ handles valid stripe webhook (124ms)
✓ rejects invalid signature (89ms)
✗ handles concurrent webhooks (2341ms)
  → AssertionError: Expected 2 processed, got 1
  → at webhook.test.ts:67
```
- Failure rate: ~10% (confirmed by 50 runs in CI)
- Always the same test, same assertion
- Only fails under concurrency

### 2. Baseline & Reproduction
- Isolated test: passes 100/100 runs
- With `--parallel`: fails ~10%
- Suspected: shared state in test DB or Redis

### 3. Hypothesis Ranking
| Rank | Hypothesis | Evidence Needed |
|------|------------|-----------------|
| 1 | Redis idempotency key collision | Check key generation |
| 2 | Test DB transaction isolation | Verify rollback |
| 3 | Stripe mock timing | Add delays |
| 4 | Event loop tick ordering | Check async handling |

### 4. Targeted Experiments
**Experiment A: Redis key inspection**
```typescript
// Added debug logging to webhook handler
const idempotencyKey = `stripe:${event.id}:${event.api_version}`;
console.log('[DEBUG] idempotency key:', idempotencyKey);
```
→ **Result:** Keys unique per event. Not the issue.

**Experiment B: Transaction isolation**
```typescript
// Check if test uses real transactions
// webhook.test.ts:12 — uses `testDb` fixture with transaction rollback
```
→ **Result:** Each test gets clean DB. Not the issue.

**Experiment C: Concurrency simulation**
```typescript
// Run handler twice in same tick
await Promise.all([
  handleWebhook(event1),
  handleWebhook(event2), // same stripe event.id!
]);
```
→ **Result:** **REPRODUCED!** Second call returns early due to idempotency check but test expects both to "process"

### 5. Root Cause
**File:** `src/modules/billing/webhook-handler.ts:45`
```typescript
// Idempotency check — returns early if already processed
const existing = await redis.get(idempotencyKey);
if (existing) {
  return { status: 'duplicate', processed: false }; // ← Test expects processed: true
}
```

**Test Expectation (webhook.test.ts:67):**
```typescript
const results = await Promise.all([
  handler.handle(event),
  handler.handle(event), // Same event = duplicate
]);
expect(results.filter(r => r.processed)).toHaveLength(2); // WRONG
```

**Actual Behavior:** First call processes, second returns `{ processed: false }`. This is **correct** idempotency behavior.

### 6. Fix
**Option A: Fix test (recommended)** — Test should expect 1 processed, 1 duplicate
**Option B: Fix handler** — Return `processed: true` for duplicates (breaks idempotency semantics)

**Chosen: Option A** — Test was wrong, not the code.

**Patch:**
```diff
--- tests/integration/billing/webhook.test.ts
+++ tests/integration/billing/webhook.test.ts
@@ -64,7 +64,7 @@
   const results = await Promise.all([
     handler.handle(event),
     handler.handle(event),
   ]);
-  expect(results.filter(r => r.processed)).toHaveLength(2);
+  expect(results.filter(r => r.processed)).toHaveLength(1);
+  expect(results.filter(r => r.status === 'duplicate')).toHaveLength(1);
```

### 7. Verification
```
$ pnpm test tests/integration/billing/webhook.test.ts --reporter=verbose --repeat=100
✓ 100/100 runs passed
Duration: 45.2s

$ pnpm test --reporter=dot
✓ 234 passed
✗ 0 failed
```

### 8. Report
- **Root cause:** Test assertion error — expected duplicate webhook to be "processed" twice
- **Fix:** Corrected test to match idempotency contract (1 processed, 1 duplicate)
- **Files changed:** `tests/integration/billing/webhook.test.ts` (3 lines)
- **Tests run:** 100 stress runs + full suite — all pass
- **Risk:** None — test-only change, behavior unchanged
```

---

## Scenario 2: Production Crash Analysis

**Trigger:** "Server crashes with `RangeError: Maximum call stack size exceeded` in `auth/tokens.ts`"

**Invocation:**
```
Analyze this production crash:
- Error: RangeError: Maximum call stack size exceeded
- Stack: auth/tokens.ts:89 → auth/tokens.ts:67 → auth/tokens.ts:89 (recursive)
- Frequency: 3x in last hour, all on POST /api/auth/refresh
- Environment: Node 20.11, Redis 7.2, 2 replicas
```

**Execution Log:**
```
## Debugging Session: Stack Overflow in Token Refresh

### 1. Capture Failure
```
RangeError: Maximum call stack size exceeded
    at generateAccessToken (src/modules/auth/tokens.ts:89:12)
    at refreshAccessToken (src/modules/auth/tokens.ts:67:5)
    at generateAccessToken (src/modules/auth/tokens.ts:89:12)
    at refreshAccessToken (src/modules/auth/tokens.ts:67:5)
    ... (repeats ~10,000 times)
```

### 2. Code Inspection
**tokens.ts:67 (refreshAccessToken):**
```typescript
export async function refreshAccessToken(refreshToken: string) {
  const payload = await verifyRefreshToken(refreshToken);
  // BUG: Calls generateAccessToken which can call refreshAccessToken
  return generateAccessToken(payload.userId, payload.scopes);
}
```

**tokens.ts:89 (generateAccessToken):**
```typescript
export async function generateAccessToken(userId: string, scopes: string[]) {
  const user = await db.user.findUnique({ where: { id: userId } });
  if (!user.active) {
    // Attempt to "refresh" the user status — RECURSIVE CALL
    await refreshAccessToken(user.refreshToken); // ← INFINITE LOOP
  }
  return jwt.sign({ sub: userId, scopes }, secret, { expiresIn: '15m' });
}
```

### 3. Root Cause
**Circular dependency:** `generateAccessToken` → checks user.active → if false, calls `refreshAccessToken` → calls `generateAccessToken` → ∞

**Trigger condition:** User account deactivated (`active: false`) but has valid refresh token.

### 4. Fix
**Principle:** Token generation must never trigger token refresh.

**Patch:**
```diff
--- src/modules/auth/tokens.ts
+++ src/modules/auth/tokens.ts
@@ -86,10 +86,10 @@ export async function generateAccessToken(userId: string, scopes: string[]) {
   const user = await db.user.findUnique({ where: { id: userId } });
-  if (!user.active) {
-    // Attempt to "refresh" the user status
-    await refreshAccessToken(user.refreshToken);
-  }
+  if (!user.active) {
+    // User deactivated — reject token generation, don't recurse
+    throw new AppError('USER_DEACTIVATED', 'Account is deactivated', 401);
+  }
   return jwt.sign({ sub: userId, scopes }, secret, { expiresIn: '15m' });
 }
```

### 5. Regression Test
```typescript
// tests/unit/auth/tokens.test.ts
test('generateAccessToken throws for deactivated user (no recursion)', async () => {
  const user = await createTestUser({ active: false });
  await expect(generateAccessToken(user.id, ['read']))
    .rejects.toThrow('USER_DEACTIVATED');
});

test('refreshAccessToken fails gracefully for deactivated user', async () => {
  const user = await createTestUser({ active: false });
  const refreshToken = await issueRefreshToken(user.id);
  await expect(refreshAccessToken(refreshToken))
    .rejects.toThrow('USER_DEACTIVATED');
});
```

### 6. Verification
```
$ pnpm test tests/unit/auth/tokens.test.ts
✓ 12 passed (including 2 new regression tests)

$ pnpm test
✓ 234 passed

# Load test: 1000 concurrent refresh requests for deactivated users
$ artillery run load-test/deactivated-refresh.yml
✓ 0 errors, 0 stack overflows
✓ All return 401 USER_DEACTIVATED
```

### 7. Report
- **Root cause:** Infinite recursion between `generateAccessToken` and `refreshAccessToken` when user.deactivated=true
- **Trigger:** Valid refresh token for deactivated account
- **Fix:** Throw `USER_DEACTIVATED` instead of recursing; added 2 regression tests
- **Files changed:** `src/modules/auth/tokens.ts` (5 lines), `tests/unit/auth/tokens.test.ts` (2 tests)
- **Verification:** Unit tests + full suite + load test — all pass
- **Remaining risk:** None — behavioral change only for already-broken case
```

---

## Scenario 3: Silent Data Corruption

**Trigger:** "Billing amounts don't match Stripe — off by exactly $0.01 sometimes."

**Invocation:**
```
Investigate billing discrepancy: amounts in our DB differ from Stripe by $0.01 intermittently.
- Check calculation logic, rounding, currency handling
- Trace from Stripe webhook → DB persistence
- Identify exact code path causing penny drift
```

**Execution Log:**
```
## Debugging Session: Penny Drift in Billing

### 1. Evidence Collection
- 47/10,000 transactions off by $0.01 in last 30 days
- Always $0.01 (never $0.02, never negative)
- Correlates with: subscriptions with trial periods + tax

### 2. Trace Data Flow
```
Stripe webhook (invoice.paid)
  → billing/webhook-handler.ts:handleInvoicePaid()
  → billing/service.ts:recordPayment()
  → billing/calculations.ts:calculateTotals()
  → DB: billing_transactions.amount (integer cents)
```

### 3. Hypothesis: Rounding in calculateTotals()
**calculations.ts:34:**
```typescript
function calculateTotals(subtotal: number, taxRate: number, discount: number) {
  const tax = Math.round(subtotal * taxRate); // ← ROUNDS TAX
  const total = subtotal + tax - discount;
  return { subtotal, tax, discount, total };
}
```

**Stripe calculates:** `tax = round(subtotal * taxRate, 2)` (banker's rounding)
**We calculate:** `tax = Math.round(subtotal * taxRate)` (away from zero)

### 4. Reproduction
```typescript
// Subtotal: $29.99, Tax: 8.875%, Discount: $0
// Stripe: 29.99 * 0.08875 = 2.6616125 → round to 2.66
// Ours:   29.99 * 0.08875 = 2.6616125 → Math.round = 3
// Diff: $0.01 ✓
```

### 5. Fix
**Match Stripe's rounding:** Banker's rounding (round half to even)
```typescript
function roundToCents(amount: number): number {
  // Banker's rounding: round half to even
  const rounded = Math.round(amount * 100) / 100;
  // Handle floating point: 2.665 → 2.66 (not 2.67)
  return Math.round(rounded * 100) / 100;
}

// Or use decimal.js for precision
import { Decimal } from 'decimal.js';
function roundToCents(amount: number): number {
  return new Decimal(amount).toDecimalPlaces(2, Decimal.ROUND_HALF_EVEN).toNumber();
}
```

### 6. Migration
- Backfill 47 affected transactions
- Add integration test with Stripe fixture data
- Monitor for 1 week

### 7. Verification
```
$ pnpm test tests/integration/billing/calculations.test.ts
✓ 15 passed (includes Stripe parity tests)

$ pnpm test
✓ 234 passed

# Backfill script
$ pnpm tsx scripts/backfill-tax-rounding.ts
✓ 47 transactions corrected
✓ 0 errors
```

### 8. Report
- **Root cause:** `Math.round()` vs Stripe's banker's rounding for tax calculation
- **Fix:** Replace with `Decimal.ROUND_HALF_EVEN` to match Stripe
- **Files changed:** `src/modules/billing/calculations.ts` (8 lines), test file (12 lines)
- **Backfill:** 47 historical transactions corrected
- **Verification:** Parity tests + full suite + production backfill — all pass
```

---

## Tips for Effective Use

1. **Provide exact error** — Stack trace, frequency, environment
2. **Share reproduction** — Minimal test case, curl command, steps
3. **Accept "can't reproduce"** — Skill will state hypotheses clearly labeled
4. **Expect regression tests** — Fix includes test that fails before, passes after
5. **Review the diff** — Skill reports only justified changes