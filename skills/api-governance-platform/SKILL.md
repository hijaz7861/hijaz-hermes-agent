---
name: api-governance-platform
description: Complete API governance system combining contract testing, version management, security review, and quality gate review. Validates API contracts, manages versions and deprecation, performs adversarial security review, and enforces quality gates before any API change is approved.
version: 1.0.0
tags: [api, governance, contract, versioning, security, quality, review]
dependencies: [api-contract-tester, api-version-manager, security-review, quality-gate-review]
---

# API Governance Platform

## Objective
Combine API contract testing, version management, security review, and quality gate review into a unified API governance platform. Validates API implementations against contracts, manages version lifecycles and deprecation, performs adversarial security review, and enforces quality gates — ensuring no API change reaches production without contract compliance, security clearance, and quality validation.

## Trigger
- "Establish API governance for service X"
- "Validate API contract, version, and security before release"
- "Manage API deprecation with security and quality gates"
- "Comprehensive API review: contract + version + security + quality"

Anti-triggers: "Deploy API changes without governance" / "Skip security review for speed" — violates the governance principle.

## Inputs
- API contract: OpenAPI/GraphQL spec for each version
- API versions: route definitions, controllers, client usage data
- Security requirements: auth, authorization, input validation, encryption
- Quality gate criteria: test pass rate, severity threshold, coverage minimum
- Deprecation policy: sunset timeline, client notification requirements

## Outputs
- Contract compliance report: endpoints tested, passed, failed, missing, breaking changes
- Version inventory: active/deprecated/sunset versions, migration guides
- Security review findings: severity-classified findings, remediation, go/no-go
- Quality gate decision: PASS / FAIL / BLOCKED with evidence
- API governance report: consolidated findings across all four domains

## Procedure
### Phase 1: Contract Testing (api-contract-tester)
1. Map API implementation: routes, controllers, handlers, middleware.
2. Load and validate contract spec: OpenAPI/GraphQL syntax, endpoints, schemas.
3. Compare implementation vs. contract: missing endpoints, extra endpoints, schema mismatches, status code mismatches.
4. Detect breaking changes: removed endpoints, required field additions, type changes, enum removals.
5. Generate and execute contract tests: positive, negative, edge cases.
6. Verify contract compliance.

### Phase 2: Version Management (api-version-manager)
1. Map API versions: versioned routes, controllers, shared code.
2. Compare versions: added/removed/changed endpoints, schema diffs.
3. Classify changes: BREAKING / NON_BREAKING / DEPRECATION_WARNING.
4. Manage deprecation: check sunset dates, identify clients using deprecated versions.
5. Generate migration guides: breaking changes, migration steps, code examples.
6. Report client compliance: clients still using deprecated versions.

### Phase 3: Security Review (security-review)
1. Define scope: changed files, security requirements, severity threshold.
2. Delegate review roles: Reviewer (security), Test Analyst (security test cases).
3. Run security audit scan: secrets, insecure config, vulnerable dependencies.
4. Consolidate findings: classify CRITICAL/HIGH/MEDIUM/LOW.
5. Resolve or accept findings: CRITICAL/HIGH must be resolved before release.
6. Post-integration verification: re-review resolved findings.

### Phase 4: Quality Gate Review (quality-gate-review)
1. Define gate criteria: test pass rate, severity allowance, required test suites.
2. Execute tests: unit, integration, lint, typecheck, build.
3. Consolidate findings and test evidence: cross-reference review findings with test results.
4. Apply gate decision: PASS / FAIL / BLOCKED.
5. Re-verify after fixes: re-run review and tests on changed files only.

### Phase 5: Consolidated Governance Report
1. Aggregate findings from all four phases.
2. Identify cross-domain conflicts: e.g., contract-compliant but security-vulnerable.
3. Produce final go/no-go recommendation with rationale.
4. Document all decisions, evidence, and approvals.

## Safety & Approval Gates
- **Approval required** before any API change based on governance findings.
- **Quality gate is mandatory:** changes cannot bypass review or testing.
- **Security gate mandatory:** unresolved CRITICAL/HIGH findings block release.
- **No secret logging:** API keys, tokens, credentials redacted from all reports.
- **No worker merges or deploys** without explicit authorization.

## Failure Handling
- Contract spec invalid → report spec errors, stop contract testing, mark as BLOCKED.
- Security scan unavailable → manual review, mark findings as "unverified."
- Tests flaky → mark as "flaky," recommend isolation, do not gate-pass.
- Reviewer/Test Analyst disagreement → Coordinator resolves, documents rationale.
- Approval denied → stop, report findings only, no changes applied.

## Completion Criteria
- API governance report produced with all four domain results.
- Contract compliance: all endpoints classified (pass/fail/missing).
- Version inventory: active/deprecated/sunset classification with migration guides.
- Security review: findings classified, CRITICAL/HIGH resolved or accepted.
- Quality gate: explicit PASS/FAIL/BLOCKED decision with evidence.
- Final go/no-go recommendation with rationale.
- No secret values in output.
