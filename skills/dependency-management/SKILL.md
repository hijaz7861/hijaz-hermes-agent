---
name: dependency-management
description: Audit, update, and patch repository dependencies. Checks for outdated, vulnerable, or unmaintained packages and proposes minimal, tested updates. Use for dependency hygiene and vulnerability remediation.
version: 1.0.0
tags: [remediation, dependencies, vulnerabilities, updates, licensing]
---

# Dependency Management

## Objective
Keep dependencies current, secure, and maintainable with the smallest safe changes. Identify outdated/vulnerable packages, propose updates with fixed versions, and verify updates do not break the build or tests.

## Trigger
- "Update dependencies" / "Bump dependencies"
- "Patch vulnerable dependencies"
- "Check for outdated packages"
- "Review dependency licenses"

Anti-triggers: "Upgrade all major versions automatically" / "Update without testing" — those require explicit approval and run only after a full test pass.

## Procedure
1. **Inventory dependencies**
   - Read dependency manifests and lockfiles (package.json/package-lock.json, requirements.txt, go.mod/go.sum, Cargo.toml/Cargo.lock, pom.xml, etc.).
   - Record direct and transitive dependencies with current versions.
   - Identify the package manager and its audit/outdated commands.

2. **Detect issues**
   - Run the package manager's audit command where available (e.g., `npm audit`, `cargo audit`, `pip-audit`, `mvn dependency:check`).
   - Identify: vulnerable versions, outdated versions, unmaintained packages (no recent releases), and license-conflict candidates.
   - Record package, current version, available fix, severity, and advisory reference.

3. **Prioritize updates**
   - P0: Vulnerabilities with a fix available (security).
   - P1: Outdated direct dependencies with breaking-change risk low.
   - P2: Unmaintained packages or license concerns.
   - Prefer patch/minor updates over major version bumps unless a major bump is required for a fix.

4. **Propose minimal updates**
   - For each proposed update, record: package, from version → to version, reason (vulnerability / outdated / unmaintained), and breaking-change risk.
   - Group related updates; avoid unrelated version churn.

5. **Apply and verify (requires approval)**
   - With explicit user approval, apply the smallest set of updates.
   - Run install, build, lint/type-check, and the test suite.
   - Compare before/after: confirm tests pass, no regressions, and the vulnerability is resolved.

6. **Report**
   - Produce a dependency report: audited packages, findings, applied updates, failed updates, and remaining risks.
   - State which updates were applied vs. proposed-but-pending-approval.

## Safety & Approval Gates
- **Approval required** before modifying manifests, lockfiles, or installing packages.
- **No automatic major version bumps** without explicit approval.
- **Test gate:** An update is not "done" until the test suite passes after the update.
- **Rollback plan:** Record the pre-update lockfile state so changes can be reverted if tests fail.

## Failure Handling
- Audit tool unavailable → Record as hypothesis, list packages manually, continue.
- Update breaks tests → Revert the change, report failure, do not proceed with dependent updates.
- Network/package registry unavailable → Report "could not fetch latest versions", continue with local data.
- Lockfile conflict → Report, request manual resolution, stop.

## Completion Criteria
- Dependency audit report produced with findings and severity.
- Vulnerable packages with available fixes are identified and either applied (with approval) or explicitly flagged as pending.
- Build and tests pass after any applied update (or the failure is reported and reverted).
- No secret or credential values logged.
