# Playbook: Code Refactorer

*Practical examples for the `code-refactorer` skill*

---

## Scenario 1: Extract method refactor (happy path)

**Trigger:** "Refactor the processOrder function in src/billing/orders.ts. It's 120 lines and does too much."

**Invocation:**
```
Refactor src/billing/orders.ts: processOrder function.
Apply extract-method transformation. Split into validateOrder, calculateTotal, persistOrder.
Preserve all public behavior. Tests must pass before and after.
```

**Execution Log:**
```
## Code Refactor: src/billing/orders.ts

### Target Analysis
- Function: processOrder (120 lines, cyclomatic complexity 14)
- Public: Yes, exported from module
- Callers: src/billing/routes.ts:23, src/billing/jobs.ts:17, tests/billing/orders.test.ts
- Test coverage: 87% (12 tests)
- Behavior contract: Takes order input, validates, calculates, persists, returns order ID

### Baseline Verification
- Tests: 12 passed, 0 failed
- Typecheck: CLEAN
- Lint: CLEAN

### Refactor Plan
| Transformation | Affected Symbol | New Location | Behavior Preserved? |
|----------------|-----------------|--------------|---------------------|
| extract-method | validateOrder logic | validateOrder() | Yes |
| extract-method | calculateTotal logic | calculateTotal() | Yes |
| extract-method | persistOrder logic | persistOrder() | Yes |
| Inline callers | processOrder() | calls 3 new methods | Yes |

### Applied Changes (minimal diff)
- src/billing/orders.ts: processOrder reduced from 120 to 18 lines
- 3 new methods added: validateOrder(), calculateTotal(), persistOrder()
- All 3 callers updated (no signature change to processOrder)

### Verification
- Tests: 12 passed (same as baseline), 0 failed
- Typecheck: CLEAN
- Lint: CLEAN
- Behavior contract: unchanged (same inputs → same outputs)
- Diff inspection: only refactor changes, no unrelated modifications

Exit code: 0.
```

**Expected Output:**
A refactor report showing the transformation, before/after metrics (lines, complexity), verification results, and confirmation that behavior is preserved.

---

## Scenario 2: Rename across codebase (happy path)

**Trigger:** "Rename `legacyUserId` to `customerId` across the auth module."

**Invocation:**
```
Rename symbol legacyUserId → customerId in src/auth/.
Update all references. Public API change — requires approval.
```

**Execution Log:**
```
## Code Refactor: Symbol Rename

### Impact Analysis
- Symbol: legacyUserId
- References: 23 files (src/auth/, src/users/, tests/auth/)
- Public API: Yes (exported type and function parameter)
- Approval required: YES (public interface change)

### Approval Gate
Decision: APPROVED — proceed with rename.

### Applied Changes
- src/auth/types.ts: legacyUserId → customerId (type definition)
- src/auth/middleware.ts: 5 references updated
- src/auth/routes.ts: 3 references updated
- src/users/profile.ts: 4 references updated
- tests/auth/: 10 references updated

### Verification
- Tests: all auth + user tests pass (47 tests)
- Typecheck: CLEAN
- Lint: CLEAN
- No remaining references to legacyUserId

Exit code: 0.
```

**Expected Output:**
A report listing all files changed, the before/after symbol names, verification results, and approval status.

---

## Scenario 3: Insufficient test coverage (safety case)

**Trigger:** "Refactor src/utils/format.ts — extract the date formatting logic."

**Invocation:**
```
Refactor src/utils/format.ts: extract formatDate() from formatTimestamp().
No existing tests for this module.
```

**Execution Log:**
```
## Code Refactor: src/utils/format.ts

### Target Analysis
- Function: formatTimestamp (45 lines)
- Test coverage: 0% (no tests exist for this module)
- Behavior contract: unknown (no tests to verify)

### Safety Gate
Insufficient test coverage — cannot verify behavior preservation.
Characterization tests required before refactor.

### Options Presented to User
1. Add characterization tests first (records current behavior), then refactor
2. Proceed without tests (UNSAFE — not recommended)
3. Abort refactor

### User Decision
Option 1 selected — add characterization tests.

### Characterization Tests Added (with approval)
- tests/utils/format.test.ts: 5 tests covering formatTimestamp
  - Valid ISO date → formatted string
  - Invalid date → throws error
  - Null input → returns null
  - Empty string → returns empty string
  - Timezone handling → correct offset

### Refactor Applied (after tests established)
- formatDate() extracted (12 lines)
- formatTimestamp() now calls formatDate()

### Verification
- Characterization tests: 5 passed before refactor, 5 passed after
- Behavior contract: established and preserved
- Typecheck: CLEAN

Exit code: 0.
```

**Expected Output:**
A report showing the safety gate triggered, characterization tests added, refactor applied and verified with tests passing before and after.
