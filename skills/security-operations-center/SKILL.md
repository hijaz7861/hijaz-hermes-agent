---
name: security-operations-center
description: Complete security operations system combining historical secret scanning, security debugging, compliance auditing, security review, and dependency audit. Provides end-to-end security: find leaked secrets, debug vulnerabilities, audit compliance, review changes, and audit dependencies.
version: 1.0.0
tags: [security, operations, compliance, secrets, vulnerabilities, audit, dependencies]
dependencies: [secret-scanner-historical, security-debugger, compliance-auditor, security-review, security-dependency-audit]
---

# Security Operations Center

## Objective
Combine historical secret scanning, security debugging, compliance auditing, security review, and dependency audit into a unified security operations center. Provides end-to-end security coverage: detect leaked secrets in history, debug active vulnerabilities, audit regulatory compliance, review code changes for security, and audit dependencies for vulnerabilities — all with coordinated remediation and reporting.

## Trigger
- "Establish security operations for repository X"
- "Complete security audit: secrets, vulnerabilities, compliance, dependencies"
- "Security operations: scan, debug, audit, review, remediate"
- "Full security assessment before production release"

Anti-triggers: "Fix all security issues automatically" / "Guarantee security" — those require expert security engineers, not automated skill execution.

## Inputs
- Repository: source code, git history, configuration files
- Compliance frameworks: GDPR, SOC2, HIPAA, PCI-DSS (as applicable)
- Dependency manifests: package.json, requirements.txt, go.mod, etc.
- Change scope: PRs, commits, or files to review
- Security policy: severity thresholds, blocking criteria, remediation timelines

## Outputs
- Security operations report: consolidated findings across all five domains
- Secret findings: historical and current secret exposures (redacted)
- Vulnerability debugging: active security defects, root causes, fixes
- Compliance gaps: regulatory requirement gaps, remediation priorities
- Security review findings: change-level security findings, go/no-go
- Dependency vulnerabilities: vulnerable packages, CVEs, fix versions
- Prioritized remediation plan: effort, risk, approval requirements

## Procedure
### Phase 1: Historical Secret Scanning (secret-scanner-historical)
1. Establish scan scope: repository, commit depth, file types, exclusions.
2. Scan commit history for secret patterns: API keys, tokens, private keys, connection strings.
3. Check current files for active secret exposure.
4. Assess exposure risk: public/private repo, secret type, age.
5. Recommend: rotate exposed secrets, remove from history, add pre-commit hooks.

### Phase 2: Security Debugging (security-debugger)
1. Capture security failures: vulnerability reports, exploit patterns, insecure behavior.
2. Scan affected modules for related issues: secrets, weak crypto, insecure config.
3. Form hypotheses: injection points, auth bypass, data exposure.
4. Test one cause at a time: focused experiments with exploit inputs.
5. Apply minimal security fix with regression test (exploit blocked after fix).
6. Verify: exploit no longer succeeds, security scan clean, tests pass.

### Phase 3: Compliance Auditing (compliance-auditor)
1. Inventory data handling: PII, PHI, payment data, credentials.
2. Extract compliance requirements for selected frameworks.
3. Audit against requirements: encryption, access logging, consent, retention.
4. Classify gaps: CRITICAL (regulatory violation), HIGH (control gap), etc.
5. Generate compliance documentation and remediation plan.

### Phase 4: Security Review (security-review)
1. Define review scope: changed files, security requirements, severity threshold.
2. Delegate roles: Reviewer (security), Test Analyst (security test cases).
3. Run security audit scan on changed files.
4. Consolidate findings: classify, verify against actual code.
5. Resolve or accept findings: CRITICAL/HIGH must be resolved before release.
6. Post-integration verification: re-review resolved findings.

### Phase 5: Dependency Audit (security-dependency-audit)
1. Inventory dependencies: direct and transitive, current versions.
2. Scan for vulnerabilities: package manager audit, vulnerability databases.
3. Prioritize by security risk: CRITICAL/HIGH/MEDIUM/LOW.
4. Recommend secure remediation: fix versions, breaking-change risk, approval.
5. Apply fixes (with approval): smallest set, verify with tests and re-audit.

### Phase 6: Consolidated Security Operations Report
1. Aggregate findings from all five phases.
2. Cross-reference: e.g., dependency vulnerability found in code with hardcoded secret.
3. Prioritize remediation: CRITICAL findings first, then HIGH, etc.
4. Produce final security posture assessment with go/no-go recommendation.

## Safety & Approval Gates
- **Read-only analysis by default:** No code/config/secret changes without explicit approval.
- **No secret output:** Secret values NEVER printed; only location and redacted context.
- **Approval required** before rotating secrets, rewriting history, or changing code.
- **Assume compromised:** Any secret found in history should be treated as compromised.
- **No worker merges or deploys** without explicit authorization.

## Failure Handling
- Git history unavailable → scan current files only, mark history as "unavailable."
- Vulnerability database unavailable → manual review, mark as "unverified."
- Compliance requirements unclear → mark as "interpretation needed," recommend legal review.
- Secret scanner finds nothing → report "no secrets detected" (does not guarantee absence).
- Approval denied → stop, report findings only, no changes applied.

## Completion Criteria
- Security operations report produced with all five domain results.
- Secret findings classified: current vs. historical exposure.
- Vulnerability debugging: root causes identified, fixes verified.
- Compliance gaps: classified by severity with remediation plan.
- Security review: findings classified, CRITICAL/HIGH resolved or accepted.
- Dependency vulnerabilities: identified with CVEs, fix versions, applied/pending status.
- Prioritized remediation plan with effort and risk estimates.
- No secret values in output.
