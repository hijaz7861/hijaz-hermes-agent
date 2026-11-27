---
name: database-query-optimizer
description: Optimize database queries by combining performance profiling with code refactoring. Identifies slow queries, N+1 patterns, missing indexes, and inefficient joins; applies verified optimizations with before/after benchmarks.
version: 1.0.0
tags: [database, sql, query, optimization, indexing, performance]
dependencies: [performance-profiler, code-refactorer]
---

# Database Query Optimizer

## Objective
Combine performance profiling with code refactoring to optimize database queries. Identifies slow queries, N+1 patterns, missing indexes, and inefficient joins; applies verified optimizations with before/after execution plan and timing benchmarks.

## Trigger
- "Optimize slow database queries in module X"
- "Find N+1 query patterns in service Y"
- "Add missing indexes for table Z"
- "Database performance: profile and optimize queries"

Anti-triggers: "Design database schema" / "Migrate database" — those are separate database design or migration tasks, not query optimization.

## Inputs
- Target: database queries, ORM models, repository files, migration files
- Database type: PostgreSQL, MySQL, MongoDB, Redis, etc.
- Workload: representative query patterns, query frequency
- Performance target: query time threshold, index usage target

## Outputs
- Query performance report: slow queries, execution time, rows scanned, index usage
- Optimization recommendations: index additions, query rewrites, N+1 fixes, join optimizations
- Before/after benchmarks: query execution time, EXPLAIN ANALYZE plans
- Verification: tests pass, no data integrity issues

## Procedure
1. **Profile database queries** (performance-profiler)
   - Enable query logging or use EXPLAIN ANALYZE for slow queries.
   - Identify queries exceeding time threshold, full table scans, missing indexes.
   - Record: query text, execution time, rows scanned, rows returned, index usage.
   - Detect N+1 patterns: multiple queries in loops instead of batch queries.

2. **Analyze query patterns** (code-refactorer)
   - Read query-building code: ORM calls, raw SQL, repository methods.
   - Identify: redundant queries, inefficient joins, missing WHERE clauses, SELECT *.
   - Map queries to callers and data flow.

3. **Design optimizations**
   - Index recommendations: columns for WHERE, JOIN, ORDER BY clauses.
   - Query rewrites: replace N+1 with batch/join, add LIMIT, avoid SELECT *.
   - ORM optimizations: eager loading, select_related, prefetch_related.
   - Schema hints: partial indexes, covering indexes, composite indexes.

4. **Apply optimizations** (code-refactorer)
   - Apply smallest safe change per optimization.
   - One optimization at a time; verify before proceeding.
   - Preserve query results (same data returned) unless behavior change authorized.

5. **Verify with benchmarks**
   - Run EXPLAIN ANALYZE before and after each optimization.
   - Compare: execution time, rows scanned, index usage, query plan.
   - Run relevant tests to confirm data integrity.
   - Roll back any optimization that changes results or degrades performance.

6. **Report**
   - Produce optimization report: slow queries, optimizations applied, before/after benchmarks, remaining risks.

## Safety & Approval Gates
- **Read-only profiling by default:** No schema or query changes without explicit approval.
- **Data integrity gate:** Optimizations must not change query results unless authorized.
- **Rollback required:** Record pre-optimization state; revert if benchmarks degrade.
- **No production mutation:** Optimize on staging or read replicas first.

## Failure Handling
- Query logging unavailable → Manual code review, mark as "estimated."
- Cannot reproduce slow query → Mark as "intermittent," recommend production monitoring.
- Optimization changes results → Revert immediately, report, do not proceed.
- Index creation locks table → Recommend concurrent index creation, schedule maintenance window.

## Completion Criteria
- Query performance report with slow queries identified (query text, timing, plan).
- Each optimization has before/after EXPLAIN ANALYZE benchmarks.
- Query results preserved (no data integrity issues).
- Tests pass after optimizations.
- No secret values (connection strings, credentials) in output.
