# Playbook: Code Duplicate Remover

*Practical examples for the `code-duplicate-remover` skill*

---

## Scenario 1: Extract duplicate function (happy path)

**Trigger:** "Find and remove duplicate code in src/utils/"

**Invocation:**
```
Remove duplicate code from src/utils/. Extract shared functionality into reusable modules.
Similarity threshold: 85%. Tests must pass before and after each extraction.
```

**Execution Log:**
```
## Code Deduplication: src/utils/

### Duplicate Scan
Scanned 12 files, 45 functions. Found 4 duplicate groups:

| Group | Files | Lines | Similarity | Type |
|-------|-------|-------|------------|------|
| formatDate | utils/date.ts:45, utils/time.ts:32 | 18 | 100% | Exact |
| validateEmail | utils/validation.ts:12, utils/auth.ts:67 | 24 | 92% | Near-duplicate |
| retryLogic | utils/retry.ts:8, utils/api.ts:15 | 31 | 88% | Near-duplicate |
| parseCSV | utils/csv.ts:5, utils/import.ts:22 | 22 | 95% | Exact |

### Extraction Plan
1. formatDate → src/utils/shared/date.ts (exact duplicate)
2. validateEmail → src/utils/shared/validation.ts (parameterized)
3. retryLogic → src/utils/shared/retry.ts (parameterized)
4. parseCSV → src/utils/shared/csv.ts (exact duplicate)

### Applied Changes (with approval)
Extracted 4 shared modules, updated 8 call sites.

### Verification
- Tests: 89 passed before, 89 passed after
- Typecheck: CLEAN
- Lines of code: 1,240 → 1,168 (-72 lines, -5.8%)
- Duplicate count: 4 → 0

Exit code: 0.
```

**Expected Output:**
Deduplication report with duplicate groups, extraction plan, before/after metrics, and verification results.

---

## Scenario 2: Near-duplicate with variations (failure case)

**Trigger:** "Deduplicate the validation logic across the auth module."

**Invocation:**
```
Remove duplicate validation code from src/auth/. Handle variations in validation rules.
```

**Execution Log:**
```
## Code Deduplication: src/auth/

### Duplicate Scan
Found 3 validation functions with variations:

| Function | Files | Lines | Similarity | Variation |
|----------|-------|-------|------------|-----------|
| validatePassword | auth/password.ts:23, auth/reset.ts:45 | 42 | 78% | Different error messages, different rules |
| validateEmail | auth/email.ts:12, auth/register.ts:34 | 19 | 85% | Same logic, different field names |

### Challenge
validatePassword has 78% similarity - below 85% threshold. Variations include:
- Different password rules (min length 8 vs 10)
- Different error messages
- Different return types

### Options
1. Lower threshold to 75% and parameterize rules
2. Extract common logic only, keep variations separate
3. Manual review required

### Decision
Option 2 selected: Extract common validation core, keep variations in callers.

### Applied Changes
- Extracted validateCore() to src/auth/shared/validation.ts
- Updated both call sites to use validateCore() with their specific rules
- validatePassword keeps its own rules and error messages

### Verification
- Tests: 24 passed before, 24 passed after
- Typecheck: CLEAN
- Lines saved: 12 lines

Exit code: 0.
```

**Expected Output:**
Deduplication report showing near-duplicate handling, extraction of common core, and verification.

---

## Scenario 3: Extraction breaks tests (safety case)

**Trigger:** "Remove duplicate code from src/billing/processor.ts"

**Invocation:**
```
Refactor src/billing/processor.ts to remove duplicate calculateTotal logic.
Tests must pass before and after. Rollback if any test fails.
```

**Execution Log:**
```
## Code Deduplication: src/billing/processor.ts

### Duplicate Scan
Found duplicate calculateTotal logic in:
- src/billing/processor.ts:67 (original)
- src/billing/processor.ts:145 (duplicate copy)

### Extraction Applied
Extracted calculateTotal() to src/billing/shared/totals.ts
Updated both call sites.

### Verification (FAILED)
- Tests before: 34 passed
- Tests after: 31 passed, 3 failed
- Failure: calculateTotal() test - rounding behavior changed

### Root Cause
The duplicate copy had slightly different rounding logic that was intentional
for a specific edge case. Extraction used the original version's rounding.

### Rollback Triggered
- Reverted to pre-extraction state
- Re-ran tests: 34 passed, 0 failed
- No changes remain

### Report
Deduplication: ROLLED BACK
Reason: test failure (behavior change detected)
No changes applied to repository
Exit code: 1 (safety gate triggered, rollback completed).
```

**Expected Output:**
Deduplication report showing rollback due to test failure, with no remaining changes.
