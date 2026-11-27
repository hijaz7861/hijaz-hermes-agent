---
name: security-dependency-audit
description: Audit repository dependencies specifically for security vulnerabilities — combining dependency inventory with security scanning to find vulnerable, outdated, or unmaintained packages and recommend secure remediation.
version: 1.0.0
tags: [security, dependencies, vulnerabilities, audit, remediation]
dependencies: [security-audit, dependency-management]
---

# Security Dependency Audit

## Objective
Combine dependency inventory with security auditing to identify vulnerable and outdated packages, prioritize them by security severity, and recommend minimal secure updates. Every finding is verified against both dependency data and security advisories.

## Trigger
- "Audit dependencies for security vulnerabilities"
- "Find vulnerable packages in this repo"
- "Check if any dependencies have known CVEs"
- "Secure our dependency tree before release"

Anti-triggers: "Update all packages to latest" / "Patch without security review" — those are general dependency management, not security-focused.

## Inputs
- Dependency manifests and lockfiles (package.json, requirements.txt, go.mod, Cargo.toml, etc.)
- Security advisory feeds or vulnerability databases (where available)
- Severity threshold for reporting

## Outputs
- Vulnerable dependency report: package, current version, fixed version, CVE/advisory ID, severity
- Prioritized remediation plan: fix version, effort, risk, approval requirement
- Verification: before/after audit results for applied fixes

## Procedure
1. **Inventory dependencies** (dependency-management)
   - Read all dependency manifests and lockfiles.
   - List direct and transitive dependencies with current versions.
   - Identify the package manager and its audit capabilities.

2. **Scan for vulnerabilities** (security-audit)
   - Run package manager audit commands (npm audit, cargo audit, pip-audit, etc.).
   - Cross-reference with vulnerability databases for CVE/advisory IDs.
   - Record package, version, vulnerability ID, severity, and affected versions.

3. **Prioritize by security risk**
   - Rank findings: CRITICAL (active exploit, fix available) → HIGH → MEDIUM → LOW.
   - Flag packages with fixes available vs. those requiring version changes or alternatives.
   - Identify unmaintained packages (no recent releases) as risk even without CVEs.

4. **Recommend secure remediation**
   - For each vulnerability: proposed fix version, breaking-change risk, testing requirement.
   - Group related updates; avoid unrelated version churn.
   - Mark each fix as requiring approval (security changes always need approval).

5. **Apply and verify (requires approval)**
   - With explicit approval, apply the smallest set of security fixes.
   - Run install, build, lint/type-check, and test suite.
   - Re-run the security audit to confirm vulnerabilities are resolved.

6. **Report**
   - Produce a security dependency report: audited packages, vulnerabilities found, fixes applied, pending approvals, remaining risk.

## Safety & Approval Gates
- **Approval required** before modifying manifests, lockfiles, or installing packages.
- **Security changes always require approval** — no automatic patching.
- **Test gate:** A fix is not complete until tests pass after the update.
- **No secret logging:** Vulnerability IDs and package names only, no credentials.

## Failure Handling
- Audit tool unavailable → Manual manifest review, mark findings as "unverified."
- Fix breaks tests → Revert, report failure, do not proceed with dependent fixes.
- No fix available → Flag as "unpatched vulnerability," recommend mitigation or alternative package.
- Network unavailable → Report "could not verify against advisory feed," continue with local data.

## Completion Criteria
- Dependency audit report produced with vulnerability findings and severity.
- Each vulnerability has a CVE/advisory ID, fix version (if available), and severity.
- Applied fixes verified with before/after audit and passing tests.
- No secret or credential values in output.
