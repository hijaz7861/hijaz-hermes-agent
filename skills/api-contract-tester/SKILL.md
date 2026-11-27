---
name: api-contract-tester
description: Validate API implementations against OpenAPI/GraphQL contracts by combining codebase intelligence with autonomous testing. Detects breaking changes, missing endpoints, and schema mismatches before deployment.
version: 1.0.0
tags: [testing, api, contract, validation, openapi, graphql]
dependencies: [codebase-intelligence, autonomous-testing]
---

# API Contract Tester

## Objective
Combine codebase mapping with risk-based testing to validate API implementations against their contracts (OpenAPI/GraphQL). Detects breaking changes, missing endpoints, schema mismatches, and response validation failures before they reach production.

## Trigger
- "Validate API contracts for endpoint X"
- "Check for breaking API changes in module Y"
- "Test API schema compliance for service Z"
- "Detect API drift between code and spec"

Anti-triggers: "Generate API documentation" / "Design new API endpoints" — those are documentation-synthesizer or separate design tasks, not contract validation.

## Inputs
- Contract spec: OpenAPI (Swagger) JSON/YAML or GraphQL schema
- Target API: base URL, endpoints, authentication config
- Codebase: source files implementing the API
- Breaking change threshold: what constitutes a breaking change

## Outputs
- Contract compliance report: endpoints tested, passed, failed, missing
- Breaking change detection: removed endpoints, required fields added, type changes, enum removals
- Schema mismatch report: response bodies not matching spec, missing required fields
- Test results: pass/fail matrix with evidence for each endpoint
- Recommendations: fix contract, fix implementation, or update spec

## Procedure
1. **Map API implementation** (codebase-intelligence)
   - Identify API route definitions, controllers, handlers, and middleware.
   - Map request/response flow: route → validation → business logic → response serialization.
   - Identify authentication/authorization points and content type handling.
   - Record existing test coverage for API endpoints.

2. **Load and validate contract** (autonomous-testing)
   - Parse OpenAPI/GraphQL spec; validate spec syntax.
   - Extract expected endpoints, methods, request schemas, response schemas, status codes.
   - Identify required vs. optional fields, enum values, patterns, formats.

3. **Compare implementation vs. contract**
   - Missing endpoints: contract has endpoint, implementation doesn't.
   - Extra endpoints: implementation has endpoint, contract doesn't.
   - Method mismatches: contract says GET, implementation uses POST.
   - Schema mismatches: response fields missing, type changes, enum removals.
   - Status code mismatches: expected 200, implementation returns 201 or 400.

4. **Detect breaking changes**
   - Removed endpoints or parameters → BREAKING.
   - Added required fields → BREAKING for clients.
   - Type changes (string → integer) → BREAKING.
   - Enum value removals → BREAKING.
   - New optional fields → NON_BREAKING.
   - New endpoints → NON_BREAKING.

5. **Generate and execute contract tests**
   - For each contract endpoint: positive test (valid request), negative test (invalid request), edge case (missing required field, invalid enum).
   - Execute against target API (staging, not production).
   - Capture: status code, response body, response time, schema validation.

6. **Verify and report**
   - Re-run tests after any implementation fix.
   - Confirm breaking changes resolved or documented.
   - Produce compliance report with recommendations.

## Safety & Approval Gates
- **Read-only analysis by default:** No code changes without explicit approval.
- **No production API calls:** Test against staging or local instances only.
- **Approval required** before modifying API implementation or contract spec.
- **No secret logging:** API keys, tokens, and credentials redacted from test output.

## Failure Handling
- Contract spec invalid → Report spec errors, stop testing.
- Target API unreachable → Report connection failure, mark as "unverified."
- Schema validation library unavailable → Manual schema comparison, mark as "estimated."
- Breaking change detected without fix → Report as BLOCKED, recommend remediation.

## Completion Criteria
- Contract compliance report produced with all endpoints classified (pass/fail/missing).
- Breaking changes explicitly listed with severity.
- Test results with evidence for each executed endpoint.
- Recommendations provided for each failure.
- No secret values in output.
