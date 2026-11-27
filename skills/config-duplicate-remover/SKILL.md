---
name: config-duplicate-remover
description: Detect and remove duplicate configuration entries, environment variables, and settings across environment files. Consolidates to single sources of truth to prevent configuration drift and inconsistencies.
version: 1.0.0
tags: [duplicate, removal, configuration, deduplication, environment, config-management]
dependencies: [configuration-validator, environment-config-manager]
---

# Config Duplicate Remover

## Objective
Detect and remove duplicate configuration entries, environment variables, and settings across environment files. Consolidates to single sources of truth to prevent configuration drift and inconsistencies between environments.

## Trigger
- "Remove duplicate config entries across environments"
- "Consolidate duplicate environment variables"
- "Deduplicate configuration settings in config files"
- "Find and remove repeated config values"

Anti-triggers: "Change configuration values without analysis" / "Remove config without checking usage" — those violate stability principles.

## Inputs
- Configuration files: .env, config.yaml, config.json, settings.py, .ini
- Environment files: .env.development, .env.staging, .env.production
- Configuration readers: code that reads config values
- Usage map: which config values are used where

## Outputs
- Duplicate report: duplicate entries, locations, environments
- Consolidation plan: which value to keep, where to centralize
- Updated configuration files
- Verification: applications load config correctly after consolidation

## Procedure
1. **Inventory configuration** (configuration-validator)
   - Read all configuration files across environments
   - List all configuration keys and values
   - Identify which keys are used in code

2. **Detect duplicates**
   - Same key with same value in multiple files
   - Same key with different values across environments (legitimate or duplicate?)
   - Duplicate settings expressed in different formats
   - Environment variables that duplicate config file values

3. **Classify duplicates**
   - True duplicates: same key, same value, same purpose → consolidate
   - Legitimate differences: same key, different values per environment → keep separate
   - Format duplicates: same setting in different formats → standardize

4. **Plan consolidation**
   - For true duplicates: determine single source of truth
   - For legitimate differences: document as environment-specific
   - Map all files referencing the affected keys

5. **Apply consolidation** (requires approval)
   - Remove duplicate entries, keep single source
   - Centralize shared configuration
   - Update references
   - One key at a time

6. **Verify**
   - Confirm applications load configuration correctly
   - Verify no missing keys after consolidation
   - Test in each environment
   - Roll back any consolidation that breaks configuration loading

7. **Report**
   - Produce deduplication report: duplicates found, consolidated, files updated, verification results

## Safety & Approval Gates
- **Approval required** before modifying configuration files
- **Configuration loading gate**: consolidation verified in each environment
- **One key at a time**: no batching unrelated changes
- **Rollback**: revert if configuration loading breaks

## Failure Handling
- Config file parse error → Skip, mark as unanalyzable, continue
- Consolidation breaks config loading → Revert immediately, report
- Cannot determine if duplicate is legitimate → Mark as "manual review," do not force
- No duplicates found → Report "no duplicate configuration detected"

## Completion Criteria
- Duplicate report with keys and locations
- Each consolidation verified in each environment
- No true duplicate entries remain
- Environment-specific differences preserved and documented
