---
name: database-environment-setter
description: Set up and configure databases for development, testing, staging, and production environments. Creates database instances, schemas, users, and access controls with environment-appropriate settings.
version: 1.0.0
tags: [database, environment, setup, schema, access-control, provisioning]
dependencies: [environment-provisioner, database-schema-linter]
---

# Database Environment Setter

## Objective
Set up and configure databases for development, testing, staging, and production environments. Creates database instances, schemas, users, and access controls with environment-appropriate settings and security.

## Trigger
- "Set up database for development environment"
- "Create test database for PR #X"
- "Configure production database with backups"
- "Set up database users and access controls"

Anti-triggers: "Modify production data directly" / "Store production credentials in code" — those violate safety and security principles.

## Inputs
- Database type: PostgreSQL, MySQL, MongoDB, Redis, etc.
- Environment: development, testing, staging, production
- Schema definitions: migrations, ORM models, DDL
- Access requirements: users, roles, permissions
- Performance settings: connections, pooling, caching
- Backup and retention: frequency, retention period

## Outputs
- Database instance: created, configured, accessible
- Schema: migrated, versioned, consistent
- Users and roles: created with least-privilege access
- Access controls: network security, authentication, authorization
- Backup configuration: automated, tested, retained
- Verification: connection test, schema validation, access test

## Procedure
1. **Analyze schema requirements** (database-schema-linter)
   - Read migration files, ORM models, DDL
   - Identify tables, columns, indexes, constraints
   - Identify sensitive data columns requiring encryption

2. **Provision database instance**
   - Create database server/cluster
   - Configure network access (security groups, VPC)
   - Set up monitoring and alerting
   - Configure backup and retention

3. **Apply schema**
   - Run migrations in order
   - Create indexes, constraints, triggers
   - Verify schema consistency
   - Document schema version

4. **Configure users and access**
   - Create application user with least-privilege
   - Create admin user for maintenance
   - Configure authentication (password, IAM, certificates)
   - Configure authorization (GRANT/REVOKE)

5. **Configure environment-specific settings**
   - Development: relaxed constraints, verbose logging
   - Testing: ephemeral data, tear-down after use
   - Staging: production-like data volume, anonymized
   - Production: high availability, encryption, strict access

6. **Verify**
   - Test database connection from application
   - Validate schema against ORM models
   - Test access controls (can/cannot perform actions)
   - Verify backup and restore procedure

7. **Report**
   - Produce database report: instance, schema, users, access controls, verification

## Safety & Approval Gates
- **Production database changes require approval**
- **No production credentials in code**
- **Encryption required for production data at rest**
- **Backup required before schema changes in production**

## Failure Handling
- Schema migration failure → Rollback, report, do not proceed
- Connection failure → Report, check network/security groups
- Access control failure → Report, review permissions
- Backup failure → Report, alert, do not proceed with changes

## Completion Criteria
- Database instance created and accessible
- Schema applied and validated
- Users and access controls configured
- Backup configured and tested
- Environment-specific settings applied
- No credential values in output
