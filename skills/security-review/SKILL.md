---
name: security-review
description: Security-focused multi-agent review — combining multi-agent review roles with security audit to perform independent, adversarial security review of code changes with findings classified by severity.
version: 1.0.0
tags: [security, review, multi-agent, audit, governance]
dependencies: [multi-agent-review, security-audit]
---

# Security Review

## Objective
Combine multi-agent review with security auditing to perform independent, adversarial security review of substantial code changes. Multiple review roles (Coordinator, Reviewer, Test Analyst) examine the diff against security requirements; findings are classified by severity and must be resolved before release.

## Trigger
- "Security review this PR"
- "Review auth module for security issues"
- "Adversarial security review of payment code"
- "Independent security review before merge"

Anti-triggers: "General code review without security focus" / "Approve without security review" — those are multi-agent-review, not security-review.

## Inputs
- Change: diff, PR number, or file scope
- Security requirements: auth, authorization, input validation, secrets, crypto
- Severity threshold for blocking: CRITICAL/HIGH by default

## Outputs
- Review findings: ID, file:line, severity, evidence, remediation
- Role reports: Reviewer security findings, Test Analyst test cases
- Consolidated report: findings summary, severity distribution, go/no-go
- Verification: post-fix re-review confirmation

## Procedure
1. **Define scope** (multi-agent-review Coordinator)
   - Define acceptance criteria and file ownership before delegation.
   - Identify security-relevant areas: auth, payments, data handling, external integrations.

2. **Delegate review roles** (multi-agent-review)
   - Reviewer: inspects diff against security checklist (injection, auth, secrets, crypto).
   - Test Analyst: designs security test cases for edge cases.
   - Each worker returns findings with file paths, line references, severity, evidence.

3. **Security audit scan** (security-audit)
   - Scan changed files for committed secrets, insecure config, weak crypto.
   - Check dependencies in changed manifests for vulnerabilities.
   - Flag any candidate secret by location only (never print values).

4. **Consolidate findings** (multi-agent-review Coordinator)
   - Classify: CRITICAL/HIGH/MEDIUM/LOW.
   - Verify every material finding against actual code.
   - Cross-reference security audit findings with reviewer findings.

5. **Resolve or accept findings**
   - CRITICAL/HIGH: must be resolved before release.
   - MEDIUM/LOW: resolve or document accepted risk.
   - Approval required before any security-related code change.

6. **Post-integration verification**
   - Run complete relevant test suite after integrating changes.
   - Re-review resolved findings.

7. **Report**
   - Produce consolidated security review report: findings, severity, remediation, go/no-go.

## Safety & Approval Gates
- **Approval required** before any code change based on review findings.
- **No secret logging:** Finding location and redacted context only; never secret values.
- **CRITICAL/HIGH findings block release** until resolved or explicitly accepted.
- **No worker merges, deploys, or alters production** without explicit authorization.

## Failure Handling
- Reviewer and Test Analyst disagree → Coordinator resolves, documents rationale.
- Security audit tool unavailable → Manual review, mark findings as "unverified."
- Finding cannot be reproduced → Mark as "hypothesis," recommend further investigation.
- Approval denied → Stop, report findings only, no changes applied.

## Completion Criteria
- All blocking findings resolved or explicitly escalated.
- Independent review evidence recorded for each finding.
- Post-integration tests run and passing.
- Consolidated report with go/no-go decision.
