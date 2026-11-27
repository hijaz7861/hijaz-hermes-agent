---
name: database-schema-linter
description: Lint database schemas by combining codebase intelligence with security auditing. Checks for missing indexes, unsafe column types, missing constraints, naming convention violations, and security issues in schema definitions.
version: 1.0.0
tags: [database, schema, linting, validation, security, indexes]
dependencies: [codebase-intelligence, security-audit]
---

# Database Schema Linter

## Objective
Combine codebase mapping with security auditing to lint database schemas. Identifies missing indexes, unsafe column types, missing constraints (foreign keys, not null, unique), naming convention violations, and security issues (unencrypted sensitive columns, excessive privileges).

## Trigger
- "Lint the database schema for service X"
- "Check for missing indexes in table Y"
- "Audit database schema for security issues"
- "Validate schema naming conventions"

Anti-triggers: "Migrate database schema" / "Design new tables" — those are separate migration or design tasks, not schema linting.

## Inputs
- Schema files: SQL migrations, ORM models, schema.rb, prisma schema, etc.
- Database type: PostgreSQL, MySQL, SQLite, MongoDB, etc.
- Naming conventions: table names, column names, index names
- Security requirements: encryption, access controls, sensitive column types

## Outputs
- Schema lint report: issues found, severity, location, recommendation
- Missing indexes: columns that should be indexed (WHERE, JOIN, ORDER BY)
- Missing constraints: absent foreign keys, not null, unique, check constraints
- Unsafe types: text instead of varchar, float instead of decimal for money
- Security issues: unencrypted sensitive columns, missing audit columns
- Naming violations: convention non-compliance

## Procedure
1. **Map schema definitions** (codebase-intelligence)
   - Identify all schema definition files: migrations, ORM models, schema files.
   - Map tables, columns, indexes, constraints, relationships.
   - Identify sensitive columns: email, SSN, payment data, credentials, PII.
   - Record existing indexes and constraints.

2. **Lint for structural issues** (codebase-intelligence)
   - Check for missing indexes on foreign keys, frequently filtered columns.
   - Check for missing NOT NULL constraints on required fields.
   - Check for missing UNIQUE constraints on business keys.
   - Check for unsafe types: using FLOAT for monetary values, TEXT for bounded strings.
   - Check for missing default values where appropriate.

3. **Audit for security** (security-audit)
   - Check sensitive columns for encryption at rest.
   - Check for audit columns: created_at, updated_at, created_by, deleted_at.
   - Check for excessive column privileges or overly permissive grants.
   - Check for missing row-level security where applicable.
   - Flag connection strings with embedded credentials (location only, no values).

4. **Check naming conventions**
   - Table names: snake_case, singular/plural consistency.
   - Column names: snake_case, no reserved words.
   - Index names: consistent prefix/suffix pattern.
   - Constraint names: descriptive, consistent format.

5. **Prioritize issues**
   - CRITICAL: unencrypted sensitive data, missing foreign keys on relationships.
   - HIGH: missing indexes on high-traffic columns, unsafe types for money.
   - MEDIUM: missing NOT NULL, naming violations.
   - LOW: cosmetic convention issues.

6. **Report**
   - Produce schema lint report: issues table, severity, location, recommendations.

## Safety & Approval Gates
- **Read-only analysis:** No schema changes without explicit approval.
- **No secret logging:** Connection strings, credentials redacted from reports.
- **Approval required** before applying schema changes or adding indexes.

## Failure Handling
- Schema files encrypted → Mark as "encrypted, cannot lint."
- ORM models dynamic → Mark as "dynamic schema," recommend manual review.
- Multiple database types → Lint each separately, report per-database.
- No schema files found → Report "no schema definitions located."

## Completion Criteria
- Schema lint report with issues classified by severity.
- Missing indexes, constraints, unsafe types, security issues identified.
- Naming violations documented.
- Recommendations provided for each issue.
- No secret values in output.
