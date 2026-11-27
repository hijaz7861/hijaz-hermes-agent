---
name: compliance-auditor
description: Audit code and configuration for regulatory compliance by combining security auditing with documentation synthesis. Checks for GDPR, SOC2, HIPAA, PCI-DSS requirements: data handling, consent, encryption, access controls, audit logging, and retention policies.
version: 1.0.0
tags: [compliance, audit, governance, gdpr, soc2, hipaa, pci, documentation]
dependencies: [security-audit, documentation-synthesizer]
---

# Compliance Auditor

## Objective
Combine security auditing with documentation synthesis to evaluate code and configuration against regulatory compliance frameworks (GDPR, SOC2, HIPAA, PCI-DSS). Identifies compliance gaps, produces remediation recommendations, and generates compliance documentation.

## Trigger
- "Audit for GDPR compliance"
- "Check SOC2 requirements for service X"
- "Audit HIPAA data handling in module Y"
- "PCI-DSS compliance check for payment code"

Anti-triggers: "Certify compliance" / "Guarantee regulatory approval" — those require external auditors, not internal skill analysis.

## Inputs
- Compliance framework: GDPR, SOC2, HIPAA, PCI-DSS, or custom
- Target: code files, configuration, data flow diagrams, infrastructure
- Data classification: what data types are processed (PII, PHI, payment data, etc.)
- Existing compliance documentation: policies, procedures, prior audits

## Outputs
- Compliance gap report: requirement, current state, gap, severity, remediation
- Data handling inventory: data types, storage locations, retention, access controls
- Compliance documentation: policy gaps, procedure documentation, evidence checklist
- Remediation plan: prioritized fixes, effort estimate, owner assignment
- Verification: before/after compliance check for applied fixes

## Procedure
1. **Inventory data handling** (security-audit)
   - Map data types: PII, PHI, payment card data, authentication credentials.
   - Trace data flow: collection → storage → processing → sharing → deletion.
   - Identify storage locations: databases, logs, backups, third-party services.
   - Record access controls: who can access what data, authentication, authorization.

2. **Extract compliance requirements** (documentation-synthesizer)
   - For the selected framework, list applicable requirements:
     - GDPR: consent, right to erasure, data minimization, breach notification, DPO
     - SOC2: access controls, change management, monitoring, incident response
     - HIPAA: PHI encryption, access controls, audit logs, BAAs
     - PCI-DSS: card data encryption, vulnerability management, access logging
   - Map each requirement to code/config areas responsible.

3. **Audit against requirements** (security-audit)
   - Check for: data encryption at rest/in transit, access logging, consent management, data retention policies, breach detection.
   - Flag: missing audit logs, unencrypted sensitive data, excessive data collection, missing deletion mechanisms.
   - Classify gaps: CRITICAL (regulatory violation), HIGH (control gap), MEDIUM (best practice), LOW (enhancement).

4. **Prioritize remediation**
   - CRITICAL: must fix before production/deployment.
   - HIGH: fix before next audit or release.
   - MEDIUM: fix in next sprint.
   - LOW: track for future improvement.

5. **Generate compliance documentation**
   - Produce compliance gap report with remediation recommendations.
   - Document data handling inventory and retention policies.
   - Create evidence checklist for external auditors.

6. **Verify**
   - Re-check remediated areas against requirements.
   - Confirm documentation matches current code/config.
   - Validate that no new gaps introduced.

7. **Report**
   - Produce compliance report: framework, scope, gaps, remediation plan, verification results.

## Safety & Approval Gates
- **Read-only analysis:** No code/config changes without explicit approval.
- **No secret logging:** PII, PHI, payment data, credentials redacted from reports.
- **Does not certify compliance:** Reports gaps only; external auditor required for certification.
- **Approval required** before any remediation code change.

## Failure Handling
- Framework requirements unclear → Mark as "interpretation needed," recommend legal/compliance review.
- Data flow cannot be traced → Mark as "opaque," recommend instrumentation.
- Conflicting requirements → Document conflict, request stakeholder resolution.
- No prior compliance docs → Start from scratch, mark as "initial assessment."

## Completion Criteria
- Compliance gap report produced with requirements mapped to code/config.
- Each gap classified by severity with remediation recommendation.
- Data handling inventory documented.
- Compliance documentation generated for external audit readiness.
- No PII/PHI/payment data values in output.
