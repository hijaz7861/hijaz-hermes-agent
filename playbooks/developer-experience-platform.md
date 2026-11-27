# Playbook: Developer Experience Platform

*Practical examples for the `developer-experience-platform` skill*

---

## Scenario 1: Complete DX improvement (happy path)

**Trigger:** "Improve developer experience for the billing module — coverage, refactoring, documentation."

**Invocation:**
```
Execute DX improvement for billing-module:
- Coverage target: 90%
- Refactor: extract calculateTax(), validatePayment() from processPayment()
- Document: API reference, module overview, data flow
- Quality: 100% tests pass, typecheck clean
```

**Execution Log:**
```
## Developer Experience Platform: billing-module

### Phase 1: Test Coverage Analysis (test-coverage-analyzer)
Coverage gaps:
| File:Line | Symbol | Risk | Recommendation |
|-----------|--------|------|----------------|
| src/billing/calculator.ts:23 | calculateTax() | HIGH | Unit test for tax calculation |
| src/billing/processor.ts:67 | validatePayment() | HIGH | Unit test for payment validation |
| src/billing/processor.ts:89 | processPayment() | MEDIUM | Integration test |

Coverage: 62% → target 90%

### Phase 2: Refactoring with Verification (refactor-with-verification)
Refactoring plan:
| Transformation | New Method | Behavior Preserved |
|----------------|------------|-------------------|
| extract-method | calculateTax() | Yes |
| extract-method | validatePayment() | Yes |

Test baseline: 34 tests passed before refactoring
Characterization tests added: 4 (capture current behavior)
Refactor applied: processPayment() reduced from 95 to 32 lines
Verification: 38 tests passed after refactoring (34 original + 4 characterization)
Typecheck: CLEAN, Lint: CLEAN

### Phase 3: Architecture Documentation (architecture-documentation)
Generated documentation:
- Module overview: billing-module purpose, key abstractions, data flow
- API reference: 8 public symbols with signatures, params, returns, errors
- Data flow: payment request → validation → tax calculation → processing → response
- Dependencies: stripe, tax-service, database
Coverage: 0% → 100% of public symbols documented

### Phase 4: Code Refactoring (code-refactorer)
Additional refactoring:
- Rename: amt → amount (clarity)
- Inline: unused helper function formatCurrency()
- Verification: tests pass, no behavior change

### Phase 5-6: Integrated DX Assessment and Reporting
Maintainability improvement:
- Complexity: 14 → 9 (processPayment)
- Coverage: 62% → 81% (+19%)
- Documentation coverage: 0% → 100%
- All tests pass (38 tests), typecheck clean, lint clean

### Report
DX improvement: SUCCESS
Coverage: 62% → 81% (target 90%, progress made)
Refactoring: 2 methods extracted, 1 inline, 1 rename
Documentation: 8 symbols documented, data flow mapped
Quality: all gates passed
Exit code: 0.
```

**Expected Output:**
DX improvement report with coverage analysis, refactoring results, architecture documentation, and maintainability metrics.

---

## Scenario 2: Coverage target not met (failure case)

**Trigger:** "Improve DX for reporting module — coverage target 95%."

**Invocation:**
```
Execute DX improvement for reporting-module.
Coverage target: 95% (strict).
```

**Execution Log:**
```
## Developer Experience Platform: reporting-module

### Phase 1: Test Coverage Analysis
Current coverage: 48%
Target: 95%
Gap: 47 percentage points

Major gaps:
| File:Line | Symbol | Risk |
|-----------|--------|------|
| src/reporting/generator.ts | generateReport() | HIGH |
| src/reporting/exporter.ts | exportToPDF() | HIGH |
| src/reporting/scheduler.ts | scheduleReport() | CRITICAL |

### Phase 2: Refactoring with Verification
Refactoring attempted: extract methods from generateReport()
Verification: tests pass before and after

### Phase 3-6: Assessment
Coverage after refactoring: 54% (+6%)
Target: 95% — NOT MET
Gap remaining: 41 percentage points

### Report
DX improvement: PARTIAL
Refactoring: successful (behavior preserved, tests pass)
Documentation: generated (100% of public symbols)
Coverage: 48% → 54% (target 95% not met)
Next: add 20+ tests for reporting layer to reach target
Exit code: 0 (improvement made, target not yet reached).
```

**Expected Output:**
DX improvement report showing partial progress, coverage gap remaining, and next steps.

---

## Scenario 3: Refactoring breaks behavior (safety case)

**Trigger:** "Improve DX for auth module — refactor with strict behavior preservation."

**Invocation:**
```
Execute DX improvement for auth-module.
Constraint: behavior must be preserved exactly.
Rollback if any test fails or behavior changes.
```

**Execution Log:**
```
## Developer Experience Platform: auth-module

### Phase 2: Refactoring with Verification
Refactor: extract validateCredentials() from authenticate()
Test baseline: 28 tests passed

### Verification (FAILED)
After refactoring: 26 tests passed, 2 failed
Failure: authenticate() test — "returns correct user object"
Root cause: refactored validateCredentials() changed return type (null → undefined)
Behavior change detected

### Safety Gate Triggered
BEHAVIOR PRESERVATION VIOLATED
- Rollback triggered immediately
- Reverted to pre-refactoring state

### Rollback Confirmation
- Re-ran tests: 28 passed, 0 failed (baseline restored)
- Typecheck: CLEAN
- No changes remain in repository

### Report
DX improvement: ROLLED BACK
Reason: behavior change detected (return type mismatch)
Refactoring: NOT APPLIED
Exit code: 1 (safety gate triggered, rollback completed).
```

**Expected Output:**
DX improvement report showing refactoring attempt, behavior change detection, rollback confirmation, and no remaining changes.
