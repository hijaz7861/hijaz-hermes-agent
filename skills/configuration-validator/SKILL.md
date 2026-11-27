---
name: configuration-validator
description: Validate application configuration by combining codebase intelligence with security auditing. Checks for hardcoded secrets, insecure defaults, missing validation, environment-specific issues, and configuration drift between environments.
version: 1.0.0
tags: [configuration, validation, security, secrets, defaults, environment]
dependencies: [codebase-intelligence, security-audit]
---

# Configuration Validator

## Objective
Combine codebase mapping with security auditing to validate application configuration. Identifies hardcoded secrets, insecure defaults, missing validation, environment-specific issues, and configuration drift. Produces a validated configuration baseline with remediation recommendations.

## Trigger
- "Validate application configuration"
- "Find hardcoded secrets in config files"
- "Check for insecure defaults in module X"
- "Detect configuration drift between environments"

Anti-triggers: "Generate configuration files" / "Deploy configuration changes" — those are separate deployment or config management tasks, not validation.

## Inputs
- Configuration files: .env, config.yml, config.json, settings.py, etc.
- Environment variables: required vs. optional, defaults
- Code: configuration readers, default values, validation logic
- Environments: development, staging, production (for drift detection)

## Outputs
- Configuration validation report: hardcoded secrets, insecure defaults, missing validation
- Environment comparison: config drift between dev/staging/prod
- Secret inventory: locations of secrets (redacted), recommendations for secret management
- Validation gaps: config read without validation, missing required fields
- Remediation plan: move secrets to env/secret manager, add validation, align environments

## Procedure
1. **Map configuration usage** (codebase-intelligence)
   - Identify all configuration files and environment variables used.
   - Trace config readers: where configs are loaded, defaults applied, validation performed.
   - Map environment-specific configurations and their differences.
   - Identify secret-handling code: where secrets are read, logged, or transmitted.

2. **Scan for security issues** (security-audit)
   - Search for hardcoded secrets: API keys, passwords, tokens, connection strings.
   - Check .env files, config files, CI/CD files, commit history (bounded scan).
   - Flag candidates by location only (never print secret values).
   - Check for insecure defaults: debug mode enabled, verbose errors, CORS `*`, weak crypto.

3. **Validate configuration completeness**
   - Check required environment variables are documented and have defaults or are mandatory.
   - Validate config values have type/range checking where applied.
   - Identify config read without validation (e.g., using raw env var directly).
   - Flag missing required fields in config schemas.

4. **Detect configuration drift**
   - Compare configs across environments (dev, staging, production).
   - Identify: different database URLs, different feature flags, different security settings.
   - Classify drift: intentional (expected differences) vs. unintentional (oversights).

5. **Prioritize remediation**
   - CRITICAL: hardcoded production secrets, missing auth config, debug mode in prod.
   - HIGH: insecure defaults, missing validation, unintentional drift.
   - MEDIUM: undocumented config, inconsistent naming.
   - LOW: cosmetic issues.

6. **Generate remediation plan**
   - Move secrets to environment variables or secret manager.
   - Add configuration validation at startup.
   - Align environment configs; document intentional differences.
   - Add .env.example with required variables (no real values).

7. **Report**
   - Produce configuration validation report: findings, drift, remediation plan.

## Safety & Approval Gates
- **Read-only analysis:** No config changes without explicit approval.
- **No secret output:** Secret locations redacted; values never printed.
- **Approval required** before moving secrets or changing production config.
- **No production mutation:** Validate on local copies first.

## Failure Handling
- Config files encrypted → Mark as "encrypted, cannot validate," recommend decryption for review.
- Secret scanning tool unavailable → Manual grep patterns, mark as "estimated."
- Cannot access production config → Compare dev/staging only, mark production as "unverified."
- Conflicting configs → Document conflict, request stakeholder resolution.

## Completion Criteria
- Configuration validation report produced with findings classified by severity.
- Hardcoded secret locations identified (redacted, not printed).
- Configuration drift between environments documented.
- Remediation plan with prioritized fixes.
- No secret values in output.
