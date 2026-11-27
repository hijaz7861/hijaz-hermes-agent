---
name: security-adjuster
description: Adjust security parameters and controls based on threat intelligence, audit findings, and security scan results. Fine-tunes access controls, rate limits, encryption settings, and security policies.
version: 1.0.0
tags: [adjustment, security, access-control, rate-limiting, encryption, policies]
dependencies: [security-audit, security-review, observability-instrumenter]
---

# Security Adjuster

## Objective
Adjust security parameters and controls based on threat intelligence, audit findings, and security scan results. Fine-tunes access controls, rate limits, encryption settings, and security policies to maintain optimal security posture.

## Trigger
- "Adjust rate limiting for API X"
- "Tune access controls for service Y"
- "Adjust encryption settings for data Z"
- "Optimize security policy configuration"

Anti-triggers: "Weaken security for convenience" / "Change security settings without audit" — those violate security principles.

## Inputs
- Security parameter: rate limit, access control rule, encryption setting, policy threshold
- Current value and security requirements
- Threat intelligence: known threats, attack patterns
- Audit findings: security scan results, compliance gaps
- Adjustment limits: min/max values, compliance requirements

## Outputs
- Adjustment plan: parameter, current → target, security rationale
- Adjustment log: changes, timestamps, security impact
- Verification: security scan passes, compliance maintained
- Security impact: reduced attack surface, improved detection

## Procedure
1. **Collect security data** (security-audit)
   - Review security scan results, audit findings, threat intelligence
   - Identify security gaps and improvement opportunities
   - Record current security configurations

2. **Analyze security posture**
   - Identify parameters needing adjustment: rate limits too permissive, access too broad, encryption weak
   - Correlate security incidents with configuration weaknesses
   - Assess risk: changing access controls affects availability, changing encryption affects compatibility

3. **Design adjustments**
   - Calculate target values based on security requirements and threat intelligence
   - Ensure compliance with regulatory requirements
   - Document rollback values

4. **Apply adjustments** (requires approval)
   - Apply one security parameter change at a time
   - Run security scans after each change
   - Verify compliance requirements met
   - One change at a time

5. **Verify** (security-review)
   - Run security scan: no new vulnerabilities
   - Verify compliance requirements met
   - Confirm access controls work correctly
   - Roll back if security posture degrades

6. **Report**
   - Produce adjustment report: parameters, security impact, compliance status, verification

## Safety & Approval Gates
- **Approval required** for all security parameter changes
- **Security scan gate**: adjustments verified with passing security scan
- **Compliance gate**: regulatory requirements must be maintained
- **One change at a time**: no batching unrelated security changes
- **Rollback**: revert if security posture degrades
- **Never weaken security**: adjustments must maintain or improve security

## Failure Handling
- Security scan failure → Revert immediately, report
- Compliance violation → Revert, report, do not proceed
- Cannot determine target → Mark as "security review required," do not guess
- Access control breakage → Revert, report, investigate

## Completion Criteria
- Adjustment plan with current → target values
- Security scan passes after adjustment
- Compliance requirements maintained
- No security posture degradation
- Rollback values documented
