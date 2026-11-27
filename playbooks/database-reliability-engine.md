# Playbook: Database Reliability Engine

*Practical examples for the `database-reliability-engine` skill*

---

## Scenario 1: Complete database reliability assessment (happy path)

**Trigger:** "Ensure database reliability for the users service — optimize queries, lint schema, and cover with tests."

**Invocation:**
```
Execute database reliability for users-service:
- Optimize slow queries in src/db/users/
- Lint schema for structural and security issues
- Ensure test coverage for database layer
- Performance target: p95 query time < 50ms
- Coverage target: 90% of database layer
```

**Execution Log:**
```
## Database Reliability Engine: users-service

### Phase 1: Query Optimization (database-query-optimizer)
Slow queries found:
| Query | File:Line | Execution Time | Rows Scanned | Issue |
|-------|-----------|---------------|--------------|-------|
| SELECT * FROM users WHERE email = ? | src/db/users/repository.ts:45 | 240ms | 50,000 | Missing index on email |
| SELECT * FROM orders WHERE user_id = ? | src/db/users/orders.ts:23 | 180ms | 12,000 | Missing index on user_id |

Optimizations applied (with approval):
- Added index: CREATE INDEX idx_users_email ON users(email)
- Added index: CREATE INDEX idx_orders_user_id ON orders(user_id)
- Replaced SELECT * with specific columns in repository.ts:45

Before/After benchmarks:
| Query | Before | After | Improvement |
|-------|--------|-------|-------------|
| user lookup by email | 240ms | 12ms | 95% faster |
| user orders | 180ms | 8ms | 96% faster |

### Phase 2: Schema Linting (database-schema-linter)
Issues found:
| Issue | Table:Column | Severity | Recommendation |
|-------|-------------|----------|----------------|
| Missing index on email | users.email | HIGH | Add index (already applied above) |
| Unencrypted column | users.ssn | CRITICAL | Encrypt at rest |
| Missing audit column | users.created_at | MEDIUM | Add created_at/updated_at |
| Unsafe type | users.balance (FLOAT) | HIGH | Use DECIMAL for money |

### Phase 3: Test Coverage Analysis (test-coverage-analyzer)
Coverage gaps:
| File:Line | Symbol | Risk | Recommendation |
|-----------|--------|------|----------------|
| src/db/users/repository.ts:45 | findUserByEmail | CRITICAL | Write query test |
| src/db/users/repository.ts:78 | createUser | HIGH | Write insert test |
| src/db/users/migrations/001.ts | addSSNColumn | MEDIUM | Write migration test |

Coverage: 65% → target 90%

### Phase 4: Integrated Reliability Assessment
Cross-referenced findings:
- CRITICAL: users.ssn unencrypted + no test for SSN handling
- HIGH: missing indexes (fixed) + query tests missing
- MEDIUM: unsafe FLOAT type for balance

Prioritized remediation:
1. Encrypt users.ssn column (CRITICAL)
2. Add tests for findUserByEmail and createUser (HIGH)
3. Change balance FLOAT→DECIMAL (HIGH)
4. Add audit columns (MEDIUM)

### Phase 5: Verification and Reporting
- Query benchmarks: re-run after index addition — all pass
- Schema lint: re-run after fixes — 1 CRITICAL remaining (SSN encryption)
- Coverage: 65% → 78% after adding 3 query tests

### Report
Database reliability: IMPROVED
Query performance: 95%+ improvement on slow queries
Schema issues: 4 found, 2 resolved, 2 remaining
Coverage: 65% → 78% (target 90%, not yet met)
Exit code: 0.
```

**Expected Output:**
Database reliability report with query optimization benchmarks, schema lint issues, coverage gaps, integrated remediation plan, and before/after verification.

---

## Scenario 2: Schema encryption required (failure case)

**Trigger:** "Database reliability for payments service — SSN column must be encrypted."

**Invocation:**
```
Execute database reliability for payments-service.
Critical: users.ssn column must be encrypted at rest.
Do not proceed with release until encryption is applied.
```

**Execution Log:**
```
## Database Reliability Engine: payments-service

### Phase 2: Schema Linting
Critical issue found:
- users.ssn column: UNENCRYPTED (CRITICAL)
- Location: src/db/migrations/003_payments.ts:12
- Regulation: PCI-DSS requires encryption of cardholder data equivalents

### Gate Check
CRITICAL schema issue: unencrypted sensitive data
Release gate: BLOCKED

### Required Remediation
1. Encrypt users.ssn column at rest (AES-256)
2. Add migration for encryption
3. Update application code to decrypt on read
4. Add tests for encryption/decryption
5. Re-lint schema to verify encryption applied

### Report
Database reliability: BLOCKED
Reason: CRITICAL schema issue (unencrypted SSN)
No release permitted until encryption is applied and verified.
Exit code: 1 (critical schema issue blocks release).
```

**Expected Output:**
Database reliability report showing CRITICAL schema issue, release block, and required remediation steps.

---

## Scenario 3: Query optimization changes results (safety case)

**Trigger:** "Optimize the billing query — but results must not change."

**Invocation:**
```
Optimize billing query in src/db/billing/.
Constraint: query results must remain identical.
Rollback if any result changes.
```

**Execution Log:**
```
## Database Reliability Engine: billing-service

### Phase 1: Query Optimization
Slow query: src/db/billing/repository.ts:67
- Execution time: 350ms
- Issue: SELECT * with unnecessary join

### Optimization Applied
- Replaced SELECT * with specific columns
- Removed unused join to users table
- Added index on billing.created_at

### Verification (FAILED)
Before results: 1,240 rows, total_amount = $45,230.10
After results: 1,240 rows, total_amount = $45,229.95
Difference: $0.15 (rounding difference from removed join)

### Safety Gate Triggered
DATA INTEGRITY VIOLATION
- Query results changed (financial calculation affected)
- Rollback triggered immediately

### Rollback
- Reverted query change and index addition
- Re-ran tests: all pass, results match baseline
- No changes remain in repository

### Report
Database reliability: ROLLED BACK
Reason: data integrity violation (result mismatch)
Optimization: NOT APPLIED
Exit code: 1 (safety gate triggered, rollback completed).
```

**Expected Output:**
Database reliability report showing optimization attempt, data integrity violation, rollback confirmation, and no remaining changes.
