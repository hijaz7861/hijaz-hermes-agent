# Playbook: Refactor with Verification

*Practical examples for the `refactor-with-verification` skill*

---

## Scenario 1: Extract method with full test verification (happy path)

**Trigger:** "Refactor processOrder in src/billing/orders.ts. Extract validateOrder, calculateTotal, persistOrder. Tests must pass before and after."

**Invocation:**
```
Refactor src/billing/orders.ts: processOrder function.
Apply extract-method transformation. Tests must pass before and after.
Coverage: 100% of refactored code.
```

**Execution Log:**
```
## Refactor with Verification: src/billing/orders.ts

### Target Analysis (code-refactorer)
- Function: processOrder (120 lines, complexity 14)
- Public: Yes, exported
- Callers: 3 (routes.ts, jobs.ts, orders.test.ts)
- Test coverage: 87% (12 tests)

### Test Baseline (autonomous-testing)
- Tests: 12 passed, 0 failed
- Typecheck: CLEAN
- Lint: CLEAN

### Refactor Plan
| Transformation | New Method | Behavior Preserved? |
|----------------|------------|---------------------|
| extract-method | validateOrder() | Yes |
| extract-method | calculateTotal() | Yes |
| extract-method | persistOrder() | Yes |

### Applied Changes
- processOrder: 120 → 18 lines
- 3 new methods added
- All 3 callers updated (no signature change)

### Verification
- Tests: 12 passed before, 12 passed after
- Typecheck: CLEAN
- Lint: CLEAN
- Behavior contract: unchanged

Exit code: 0.
```

**Expected Output:**
Refactor report with target analysis, test baseline, refactor plan, applied changes, verification results.

---

## Scenario 2: Characterization tests first (gap filling)

**Trigger:** "Refactor formatTimestamp in src/utils/format.ts. No tests exist."

**Invocation:**
```
Refactor src/utils/format.ts: extract formatDate() from formatTimestamp().
No existing tests — add characterization tests first.
```

**Execution Log:**
```
## Refactor with Verification: src/utils/format.ts

### Target Analysis
- Function: formatTimestamp (45 lines)
- Test coverage: 0% (no tests)
- Behavior contract: unknown

### Characterization Tests Added (autonomous-testing)
- tests/utils/format.test.ts: 5 tests
  - Valid ISO date → formatted string
  - Invalid date → throws error
  - Null input → returns null
  - Empty string → returns empty string
  - Timezone handling → correct offset

### Test Baseline (before refactor)
- Characterization tests: 5 passed
- Establishes behavior contract

### Refactor Applied (code-refactorer)
- formatDate() extracted (12 lines)
- formatTimestamp() now calls formatDate()

### Verification
- Characterization tests: 5 passed before, 5 passed after
- Behavior contract: established and preserved
- Typecheck: CLEAN

Exit code: 0.
```

**Expected Output:**
Report showing characterization tests added, behavior contract established, refactor applied and verified.

---

## Scenario 3: Test failure after refactor (safety case)

**Trigger:** "Refactor the billing calculator. Tests must pass."

**Invocation:**
```
Refactor src/billing/calculator.ts: extract calculateTax() method.
Tests must pass before and after. Rollback if tests fail.
```

**Execution Log:**
```
## Refactor with Verification: src/billing/calculator.ts

### Test Baseline
- Tests: 24 passed, 0 failed

### Refactor Applied
- calculateTax() extracted from calculateTotal()

### Verification (FAILED)
- Tests: 22 passed, 2 failed
- Failure: calculateTax() test — wrong rounding for negative amounts
- Root cause: refactor changed rounding behavior

### Rollback (code-refactorer safety gate)
- Reverted to pre-refactor state (git commit abc123)
- Re-ran tests: 24 passed, 0 failed
- Baseline restored

### Report
- Refactor: ATTEMPTED, ROLLED BACK
- Reason: test failure (behavior change detected)
- No changes applied to repository

Exit code: 1 (refactor rolled back due to test failure).
```

**Expected Output:**
Report showing test baseline, refactor applied, test failure, rollback performed, baseline restored, no changes remain.
