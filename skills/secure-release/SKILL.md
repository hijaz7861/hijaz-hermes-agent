---
name: secure-release
description: Coordinate a release with a mandatory security audit gate — combining release readiness verification with security auditing to ensure no release proceeds with unresolved critical security findings.
version: 1.0.0
tags: [release, security, gates, governance, orchestration]
dependencies: [release-coordinator, security-audit]
---

# Secure Release

## Objective
Combine release coordination with security auditing to enforce a security gate before any release. A release cannot proceed if unresolved CRITICAL/HIGH security findings exist unless explicitly accepted with documented risk.

## Trigger
- "Prepare secure release vX.Y.Z"
- "Release with security audit gate"
- "Cut release only if security is clean"
- "Security-gated release coordination"

Anti-triggers: "Release despite security findings" / "Skip security audit for speed" — violates the security gate principle.

## Inputs
- Target version, branch, release date target
- Commits/PRs included since last release
- Security policy: which findings block release (CRITICAL/HIGH by default)

## Outputs
- Release readiness report: tests, review, build status
- Security audit findings: severity, location, remediation priority
- Gate status: passed/failed/blocked for each gate (quality, security, approval)
- Release report: version, changelog, gate status, next steps

## Procedure
1. **Define release scope** (release-coordinator)
   - Record target version, branch, commit range since last release.
   - List changed files, features, fixes, breaking changes.

2. **Verify release readiness** (release-coordinator)
   - Confirm test suite passes, lint/type-check/build passes.
   - Confirm code review complete for all changes.
   - Confirm dependency updates are tested.

3. **Run security audit** (security-audit)
   - Scan for committed secrets, vulnerable dependencies, insecure config.
   - Map data flow across trust boundaries.
   - Classify findings: CRITICAL/HIGH/MEDIUM/LOW/INFO.

4. **Enforce security gate**
   - CRITICAL/HIGH findings unresolved → release BLOCKED.
   - Findings accepted with documented risk → release may proceed.
   - No secrets in report output.

5. **Assemble changelog and bump version (requires approval)**
   - With explicit approval, bump version and create git tag.
   - No deploy/publish by this skill; only prepares and reports.

6. **Report**
   - Produce release report: version, changelog, gate status, artifacts, next steps.

## Safety & Approval Gates
- **Approval required** before version bump, git tag, or any publish/deploy.
- **Security gate is mandatory:** unresolved CRITICAL/HIGH findings block release.
- **No deploy/publish** by this skill; it only prepares and reports.
- **No secret logging** in changelog or reports.

## Failure Handling
- Tests failing → Release BLOCKED, report failing tests.
- Security gate unmet → Release BLOCKED, list findings, require acceptance/remediation.
- Approval denied → Stop, report findings only, no tag or version change.
- Security audit tool unavailable → Mark as unverified, require manual security review.

## Completion Criteria
- Release report with version, changelog, gate status.
- Every gate explicitly marked passed/failed/blocked.
- Security findings classified and either resolved or accepted with documented risk.
- No version bump or tag without explicit user approval.
