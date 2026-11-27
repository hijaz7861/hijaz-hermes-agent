---
name: environment-config-manager
description: Manage environment-specific configuration and secrets across development, staging, and production. Ensures consistent configuration, secure secret storage, and configuration drift detection.
version: 1.0.0
tags: [configuration, environment, secrets, config-management, drift]
dependencies: [configuration-validator, observability-instrumenter]
---

# Environment Config Manager

## Objective
Manage environment-specific configuration and secrets across development, staging, and production. Ensures consistent configuration, secure secret storage, and configuration drift detection between environments.

## Trigger
- "Manage configuration for environment X"
- "Sync configuration between staging and production"
- "Detect configuration drift in environment Y"
- "Rotate secrets in production environment"

Anti-triggers: "Store secrets in plaintext" / "Modify production config without approval" — those violate security principles.

## Inputs
- Configuration files: .env, config.yaml, config.json, settings.py
- Environment variables: required vs. optional, defaults
- Secret storage: AWS Secrets Manager, HashiCorp Vault, environment variables
- Environment targets: development, staging, production
- Configuration schema: required fields, types, validation rules

## Outputs
- Configuration files per environment
- Secret references (not values): paths to secret storage
- Configuration schema: required fields, types, validation
- Drift report: differences between environments
- Secret rotation log: when secrets were last rotated

## Procedure
1. **Inventory configuration** (configuration-validator)
   - Identify all configuration files and environment variables
   - Map configuration readers and validation logic
   - Identify secret-handling code and storage locations

2. **Classify configuration by sensitivity**
   - Public: non-sensitive configuration (feature flags, timeouts)
   - Internal: configuration for internal services (database hosts, ports)
   - Confidential: API keys, service credentials
   - Restricted: production secrets, encryption keys, payment data

3. **Create environment-specific configuration**
   - Development: local services, debug logging, test credentials
   - Staging: production-like services, info logging, staging credentials
   - Production: production services, error logging, production credentials

4. **Configure secret storage**
   - Store secrets in secret manager (not in code)
   - Reference secrets by path/ID in configuration
   - Set up secret rotation policies
   - Audit secret access

5. **Detect configuration drift**
   - Compare configuration across environments
   - Identify intentional vs. unintentional differences
   - Flag unintentional drift for remediation

6. **Verify**
   - Validate configuration against schema
   - Confirm secrets are not in code
   - Verify environment-specific values are correct
   - Test configuration loading in each environment

7. **Report**
   - Produce configuration report: environments, secrets, drift, validation results

## Safety & Approval Gates
- **No secrets in code or configuration files**
- **Production config changes require approval**
- **Secret rotation requires authorization**
- **Drift detection must run before production deployments**

## Failure Handling
- Secret not found → Report, request secret creation, do not proceed
- Configuration validation failure → Report, fix, revalidate
- Drift detected → Report, recommend remediation, block deployment if critical
- Secret rotation failure → Report, alert, do not proceed with deployment

## Completion Criteria
- Configuration files created for all environments
- Secrets stored in secret manager (not in code)
- Configuration schema validated
- Drift report produced
- No secret values in output
