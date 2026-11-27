---
name: release-coordinator
description: Coordinate a software release: verify readiness, manage version bumps, assemble changelogs, enforce gates, and report release status. Use for production or staging releases.
version: 1.0.0
tags: [orchestration, release, versioning, changelog, gates]
---

# Release Coordinator

## Objective
Run a disciplined, gated release process. Verify the release candidate is ready (tests pass, review complete, security clean), bump the version, assemble the changelog, enforce approval gates, and produce a release report. Does not deploy without explicit approval.

## Trigger
- "Prepare release vX.Y.Z" / "Cut a release"
- "Release readiness check"
- "Assemble changelog for vX.Y.Z"
- "Gate production deployment"

Anti-triggers: "Deploy to production" / "Publish package" — those are separate, user-authorized actions performed after this skill's gates pass.

## Procedure
1. **Define release scope**
   - Record target version (semver), target branch, and release date target.
   - Identify commits/PRs included since the last release (git log range).
   - List changed files, features, fixes, and breaking changes.

2. **Verify readiness**
   - Confirm test suite passes on the release branch/candidate.
   - Confirm lint/type-check/build passes.
   - Confirm code review is complete for all included changes.
   - Confirm security audit findings are resolved or accepted with documented risk.
   - Confirm dependency updates (if any) are tested.

3. **Assemble changelog**
   - Group entries: Features, Fixes, Breaking Changes, Security, Dependencies, Documentation.
   - For each entry: description, linked PR/issue, author.
   - Exclude internal chores and unrelated commits.

4. **Bump version (requires approval)**
   - With explicit approval, update version in manifest files (package.json, Cargo.toml, __version__.py, etc.) and create a git tag.
   - Record old version → new version and files changed.

5. **Enforce gates**
   - `approval` gate: user must sign off before tagging or publishing.
   - `quality` gate: all tests green, review complete.
   - `security` gate: no unresolved CRITICAL/HIGH findings unless accepted.

6. **Report**
   - Produce a release report: version, date, changelog, gate status (passed/failed/blocked), artifacts, and next steps.
   - State explicitly whether the release is approved to proceed to deploy/publish.

## Safety & Approval Gates
- **Approval required** before version bump, git tag, or any publish/deploy action.
- **No deploy/publish** by this skill; it only prepares and reports.
- **Block on failure:** If any readiness check fails, the release is BLOCKED and the report states why.
- **No secret logging:** Changelog and reports exclude credentials, tokens, and internal hostnames.

## Failure Handling
- Tests failing → Release BLOCKED, report failing tests, do not bump version.
- Review incomplete → Release BLOCKED, list unreviewed changes, do not proceed.
- Security gate unmet → Release BLOCKED, list findings, require acceptance or remediation.
- Approval denied → Stop, report findings only, no tag or version change.

## Completion Criteria
- Release report produced with version, changelog, and gate status.
- Every gate explicitly marked passed/failed/blocked.
- No version bump or tag occurs without explicit user approval.
- Release state (ready / blocked / approved-to-deploy) is unambiguous.
