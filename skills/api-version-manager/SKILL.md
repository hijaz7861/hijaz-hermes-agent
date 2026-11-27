---
name: api-version-manager
description: Manage API versioning and deprecation by combining codebase intelligence with documentation synthesis. Tracks API versions, detects breaking changes, manages deprecation timelines, and generates migration guides.
version: 1.0.0
tags: [api, versioning, deprecation, documentation, migration]
dependencies: [codebase-intelligence, documentation-synthesizer]
---

# API Version Manager

## Objective
Combine codebase mapping with documentation synthesis to manage API version lifecycles. Tracks which versions are active/deprecated, detects breaking changes between versions, manages deprecation timelines, and generates client migration guides.

## Trigger
- "Manage API versioning for service X"
- "Deprecate API v1 and migrate clients to v2"
- "Detect breaking changes between API versions"
- "Generate migration guide for API upgrade"

Anti-triggers: "Design new API endpoints" / "Deploy API changes" — those are separate design/deployment tasks, not version management.

## Inputs
- API versions: version identifiers, route definitions, controllers
- Deprecation policy: sunset timeline, client notification requirements
- Client usage: which clients use which versions (from logs or config)
- Breaking change definition: what constitutes a breaking change

## Outputs
- Version inventory: active, deprecated, sunset versions with routes
- Breaking change detection: changed endpoints, removed parameters, type changes
- Deprecation timeline: sunset dates, client notification deadlines
- Migration guide: breaking changes, migration steps, code examples
- Compliance report: clients still using deprecated versions

## Procedure
1. **Map API versions** (codebase-intelligence)
   - Identify versioned routes: /v1/, /v2/, version headers, version parameters.
   - Map controllers, handlers, and models per version.
   - Trace shared code between versions (common libs, shared models).
   - Identify clients and their version usage from config or logs.

2. **Compare versions** (codebase-intelligence + documentation-synthesizer)
   - Diff endpoints between versions: added, removed, changed.
   - Compare request/response schemas per version.
   - Identify breaking changes: removed endpoints, required field additions, type changes.
   - Classify changes: BREAKING / NON_BREAKING / DEPRECATION_WARNING.

3. **Manage deprecation**
   - Check sunset dates against current date.
   - Identify clients still using deprecated versions.
   - Calculate notification deadlines based on deprecation policy.
   - Flag versions past sunset date.

4. **Generate migration guide**
   - List breaking changes between old and new versions.
   - Provide code examples for before/after migration.
   - Document new endpoints, changed parameters, new authentication.
   - Include testing recommendations for migrated clients.

5. **Report**
   - Produce version report: inventory, breaking changes, deprecation status, migration guide, client compliance.

## Safety & Approval Gates
- **Read-only analysis:** No version changes without explicit approval.
- **No client notification without approval:** Deprecation notices require authorization.
- **No production deployment:** Version management is analysis and planning only.

## Failure Handling
- Version routes unclear → Mark as "ambiguous," recommend explicit versioning.
- Client usage data unavailable → Mark as "unknown," recommend analytics integration.
- No deprecation policy → Recommend creating one, mark versions as "active."
- Conflicting version definitions → Document conflict, request stakeholder resolution.

## Completion Criteria
- Version inventory produced with active/deprecated/sunset classification.
- Breaking changes explicitly listed between versions.
- Deprecation timeline with sunset dates and notification deadlines.
- Migration guide generated with code examples.
- Client compliance report identifying users of deprecated versions.
- No secret values in output.
