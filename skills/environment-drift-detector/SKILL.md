---
name: environment-drift-detector
description: Detect configuration and infrastructure drift between environments. Compares expected vs. actual state across development, staging, and production, and reports unintentional differences requiring remediation.
version: 1.0.0
tags: [drift, detection, configuration, infrastructure, comparison, remediation]
dependencies: [configuration-validator, environment-provisioner, observability-instrumenter]
---

# Environment Drift Detector

## Objective
Detect configuration and infrastructure drift between environments. Compares expected vs. actual state across development, staging, and production, and reports unintentional differences requiring remediation to maintain environment consistency and reliability.

## Trigger
- "Detect drift between staging and production"
- "Compare environment configurations for differences"
- "Audit environment drift across all environments"
- "Report unintentional configuration changes"

Anti-triggers: "Apply drift fixes automatically without review" / "Ignore intentional configuration differences" — those require human judgment.

## Inputs
- Environments: development, staging, production (and others)
- Expected state: IaC definitions, version control, configuration baselines
- Actual state: live environment state from APIs, configurations, infrastructure
- Drift thresholds: acceptable difference levels per resource type
- Exclusions: intentionally different resources (e.g., dev uses smaller instances)

## Outputs
- Drift report: resource, environment, expected value, actual value, drift type
- Drift classification: intentional vs. unintentional
- Severity classification: critical, high, medium, low
- Remediation recommendations: align, document, or exclude
- Trend report: drift over time, frequency, resources most affected

## Procedure
1. **Collect expected state** (environment-provisioner)
   - Read IaC definitions, version control, configuration baselines
   - Identify expected resource configurations per environment
   - Document intentional differences between environments

2. **Collect actual state**
   - Query live environment state via APIs, CLI tools, configuration files
   - Capture current resource configurations, tags, settings
   - Record runtime state: running versions, active connections

3. **Compare expected vs. actual**
   - Compare resource configurations field by field
   - Identify differences: added, removed, modified resources
   - Classify drift: configuration, version, tag, label, annotation

4. **Classify drift**
   - Intentional: approved changes, environment-specific differences
   - Unintentional: manual changes, forgotten updates, configuration errors
   - Unknown: requires investigation

5. **Assess severity**
   - Critical: security groups, IAM policies, encryption settings
   - High: instance types, database configurations, network settings
   - Medium: tags, labels, non-critical configuration
   - Low: descriptions, comments, cosmetic differences

6. **Generate remediation recommendations**
   - Align: update actual state to match expected
   - Document: update expected state to match actual (if intentional)
   - Exclude: add to exclusions list (if permanently different)
   - Investigate: require manual review (if unknown)

7. **Report**
   - Produce drift report: findings, classification, severity, recommendations

## Safety & Approval Gates
- **Read-only detection**: Does not modify environments without approval
- **Drift remediation requires approval**: Changes to align environments need authorization
- **Intentional differences documented**: Not flagged as issues repeatedly
- **No secrets in reports**: Configuration values redacted where sensitive

## Failure Handling
- API access failure → Report, mark environment as uncheckable
- Configuration parse error → Report, mark as unparseable, continue with others
- State inconsistency → Report, recommend manual investigation
- No baseline available → Report, recommend establishing baseline first

## Completion Criteria
- Drift report produced with all environments compared
- Each drift classified (intentional/unintentional/unknown)
- Severity assigned to each finding
- Remediation recommendations provided
- No secret values in output
