---
name: database-reliability-engine
description: Complete database reliability system combining query optimization, schema linting, and test coverage analysis. Optimizes slow queries, lints schemas for structural and security issues, and ensures test coverage for the database layer.
version: 1.0.0
tags: [database, reliability, optimization, schema, testing, coverage]
dependencies: [database-query-optimizer, database-schema-linter, test-coverage-analyzer]
---

# Database Reliability Engine

## Objective
Combine database query optimization, schema linting, and test coverage analysis into a unified database reliability system. Optimizes slow queries and N+1 patterns, lints schemas for structural and security issues, and ensures adequate test coverage for the database layer — providing comprehensive database reliability assurance.

## Trigger
- "Ensure database reliability for service X"
- "Optimize queries, lint schema, and cover DB layer with tests"
- "Database health check: performance, schema, coverage"
- "Complete database reliability assessment"

Anti-triggers: "Migrate database schema" / "Design new tables" — those are separate migration/design tasks, not reliability assurance.

## Inputs
- Database: type (PostgreSQL, MySQL, MongoDB, etc.), connection info (redacted)
- Schema files: migrations, ORM models, schema definitions
- Query files: repository methods, ORM calls, raw SQL
- Test files: database-layer tests, integration tests
- Workload: representative query patterns, query frequency
- Performance target: query time threshold, coverage minimum

## Outputs
- Database reliability report: query performance, schema issues, coverage gaps
- Query optimizations: before/after benchmarks, index recommendations
- Schema lint: missing indexes, constraints, unsafe types, security issues
- Coverage analysis: untested queries, untested schema changes, risk classification
- Prioritized remediation plan: effort, risk, approval requirements

## Procedure
### Phase 1: Query Optimization (database-query-optimizer)
1. Profile database queries: EXPLAIN ANALYZE, query logging, slow query identification.
2. Detect N+1 patterns: multiple queries in loops instead of batch queries.
3. Analyze query patterns: redundant queries, inefficient joins, missing WHERE clauses.
4. Design optimizations: index recommendations, query rewrites, ORM optimizations.
5. Apply optimizations (with approval): smallest safe change per optimization.
6. Verify: before/after EXPLAIN ANALYZE benchmarks, tests pass, data integrity preserved.

### Phase 2: Schema Linting (database-schema-linter)
1. Map schema definitions: migrations, ORM models, tables, columns, indexes, constraints.
2. Lint for structural issues: missing indexes, missing constraints, unsafe types, naming violations.
3. Audit for security: unencrypted sensitive columns, missing audit columns, excessive privileges.
4. Classify issues: CRITICAL (unencrypted sensitive data, missing foreign keys), HIGH (missing indexes, unsafe types), MEDIUM (missing NOT NULL, naming violations).
5. Report schema issues with location, severity, and recommendations.

### Phase 3: Test Coverage Analysis (test-coverage-analyzer)
1. Map database layer: models, repositories, queries, migrations.
2. Analyze existing coverage: which queries, tables, and schema changes have tests.
3. Identify gaps: untested queries, untested migrations, untested schema changes.
4. Classify gaps: CRITICAL (write queries without tests), HIGH (complex queries without tests), MEDIUM (simple queries without tests).
5. Recommend tests: unit tests for queries, integration tests for migrations, contract tests for schema.

### Phase 4: Integrated Reliability Assessment
1. Cross-reference findings: slow queries with missing tests, schema issues with missing coverage.
2. Prioritize remediation: queries that are both slow AND untested = CRITICAL priority.
3. Produce integrated remediation plan: query optimizations, schema fixes, test additions.
4. Estimate effort and risk for each remediation item.

### Phase 5: Verification and Reporting
1. Re-run query benchmarks after optimizations.
2. Re-lint schema after fixes.
3. Re-measure coverage after test additions.
4. Produce final database reliability report with before/after comparison.

## Safety & Approval Gates
- **Read-only analysis by default:** No schema or query changes without explicit approval.
- **Data integrity gate:** Query optimizations must not change results unless authorized.
- **Rollback required:** Record pre-change state; revert if benchmarks degrade or tests fail.
- **No production mutation:** Optimize on staging or read replicas first.
- **No secret logging:** Connection strings, credentials redacted from reports.

## Failure Handling
- Query logging unavailable → manual code review, mark as "estimated."
- Cannot reproduce slow query → mark as "intermittent," recommend production monitoring.
- Optimization changes results → revert immediately, report, do not proceed.
- Schema files encrypted → mark as "encrypted, cannot lint."
- Test suite unavailable → mark coverage as "unmeasurable," recommend test framework setup.

## Completion Criteria
- Database reliability report produced with query, schema, and coverage findings.
- Query optimizations verified with before/after benchmarks.
- Schema issues classified by severity with recommendations.
- Coverage gaps identified with risk classification and test recommendations.
- Integrated remediation plan with prioritized items.
- No secret values in output.
