---
name: secret-duplicate-remover
description: Detect and remove duplicate secret declarations across configuration files, environment files, and secret stores. Consolidates to single secret sources to reduce exposure surface and rotation complexity.
version: 1.0.0
tags: [duplicate, removal, secrets, security, deduplication, secret-management]
dependencies: [secret-scanner-historical, security-audit, environment-config-manager]
---

# Secret Duplicate Remover

## Objective
Detect and remove duplicate secret declarations across configuration files, environment files, and secret stores. Consolidates to single secret sources to reduce exposure surface and rotation complexity.

## Trigger
- "Remove duplicate secrets across config files"
- "Consolidate duplicate API keys and tokens"
- "Deduplicate secret declarations in environment files"
- "Find and remove repeated secret declarations"

Anti-triggers: "Rotate all secrets automatically" / "Remove secrets without verification" — those require separate authorization and careful planning.

## Inputs
- Configuration files: .env, config.yaml, config.json, settings.py
- Secret stores: AWS Secrets Manager, HashiCorp Vault, environment variables
- CI/CD files: GitHub Actions, GitLab CI, Jenkinsfiles
- Secret patterns: API keys, tokens, passwords, connection strings

## Outputs
- Duplicate report: secret locations, types, environments (values redacted)
- Consolidation plan: which secret source to keep, which to remove
- Updated configuration files referencing consolidated secrets
- Verification: applications load secrets correctly after consolidation

## Procedure
1. **Scan for secrets** (secret-scanner-historical)
   - Scan configuration files, CI/CD files, environment files
   - Identify secret patterns: API keys, tokens, passwords, connection strings
   - Record locations (file:line), never values

2. **Detect duplicates**
   - Same secret value declared in multiple locations
   - Same secret referenced by different names
   - Duplicate secrets in config files and secret stores
   - Same secret in multiple environments unnecessarily

3. **Classify duplicates**
   - True duplicates: same secret, same purpose → consolidate
   - Environment-specific: different secrets per environment → keep separate
   - Active rotation: secrets in rotation period → preserve both temporarily

4. **Plan consolidation**
   - For true duplicates: determine single source of truth (secret store preferred)
   - For environment-specific: keep separate, standardize naming
   - Map all files referencing the affected secrets

5. **Apply consolidation** (requires approval)
   - Remove duplicate declarations from config files
   - Reference single secret store entry
   - Update CI/CD files
   - One secret at a time

6. **Verify**
   - Confirm applications load secrets correctly
   - Verify no missing secrets after consolidation
   - Test secret retrieval from secret store
   - Roll back any consolidation that breaks secret retrieval

7. **Report**
   - Produce deduplication report: secrets found (locations only, values redacted), consolidated, files updated, verification results

## Safety & Approval Gates
- **No secret values in output**: Only locations and types reported
- **Approval required** before modifying configuration or secret references
- **Secret retrieval gate**: consolidation verified with applications working
- **One secret at a time**: no batching unrelated changes
- **Rollback**: restore duplicate declarations if retrieval breaks

## Failure Handling
- Secret scan error → Skip, mark as unanalyzable, continue
- Consolidation breaks secret retrieval → Revert immediately, report
- Cannot determine if secret is intentional duplicate → Mark as "manual review," do not remove
- No duplicates found → Report "no duplicate secrets detected"

## Completion Criteria
- Duplicate report with locations and types (no values)
- Each consolidation verified with applications working
- No true duplicate secret declarations remain
- Environment-specific secrets preserved
- No secret values printed anywhere
