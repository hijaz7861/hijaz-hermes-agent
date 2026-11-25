# Playbook: Skill Creator

*Practical examples for the `skill-creator` skill*

---

## Scenario 1: Create Skill from Recurring Workflow

**Trigger:** "We keep doing 'API contract testing' manually. Make it a skill."

**Invocation:**
```
Create a skill for API contract testing:
- Trigger: "Validate API contracts" / "Check breaking changes"
- Input: OpenAPI spec, base URL, auth config
- Output: Contract test results, breaking change report
- Steps: Fetch spec → Generate tests → Run against staging → Report
- Safety: Read-only against production, write only to test reports
```

**Execution Log:**
```
## Skill Creation: API Contract Testing

### 1. Trigger Analysis
- **User intent:** "Ensure API doesn't break consumers"
- **Situations:** Pre-deploy, PR with API changes, scheduled nightly
- **Specificity:** Only for REST/GraphQL APIs with OpenAPI spec
- **Anti-triggers:** "Test the database" / "Check UI" — not this skill

### 2. Outcome Definition
| Aspect | Specification |
|--------|---------------|
| **Objective** | Validate API implementation matches contract, detect breaking changes |
| **Required inputs** | OpenAPI spec (URL or file), base URL, auth (optional), consumer contracts (optional) |
| **Expected outputs** | Test results (PASS/FAIL), breaking change diff, coverage report |
| **Boundaries** | READ: spec, staging API. WRITE: test reports only. NO: production calls, deployments |

### 3. Runtime Inspection
- **Hermes skill discovery:** `.agents/skills/` + user skills dir
- **Frontmatter:** `name`, `description` (required), `version`, `tags` (optional)
- **Tools available:** file read/write, shell, HTTP fetch, subagent spawn
- **Not available:** Direct DB access, browser automation, secret management

### 4. Skill Draft (api-contract-testing/SKILL.md)
```markdown
---
name: api-contract-testing
description: Validate API implementations against OpenAPI contracts and detect breaking changes. Use pre-deploy, on API changes, or scheduled.
version: 1.0.0
tags: [testing, api, contract, validation]
---

# API Contract Testing

## Objective
Verify API implementation conforms to its OpenAPI contract and detect breaking changes against consumer expectations.

## Trigger
- "Validate API contracts"
- "Check for breaking API changes"
- "Run contract tests against staging"

## Procedure
1. **Fetch Contract**
   - Input: OpenAPI spec URL/file, base URL, auth config
   - Validate spec (Spectral lint)
   - Resolve $refs, normalize

2. **Generate Tests**
   - Use `openapi-spec-validator` + custom generators
   - Cover: status codes, response schemas, required fields, enum values
   - Generate: positive tests, negative tests (invalid input), edge cases

3. **Execute Against Target**
   - Configure auth (Bearer, API key, none)
   - Run tests in parallel with rate limiting
   - Capture: latency, status, response body, schema validation

4. **Compare with Consumer Contracts** (optional)
   - Input: Pact files or recorded consumer requests
   - Verify provider satisfies all consumer expectations

5. **Detect Breaking Changes**
   - Compare current spec vs baseline (git tag, stored spec)
   - Classify: BREAKING / NON_BREAKING / UNKNOWN
   - Breaking: removed endpoints, required fields added, type changes, enum removals

6. **Report**
   - Summary: pass/fail counts, breaking changes list
   - Artifacts: full test results (JSON), diff (Markdown), coverage
   - Exit code: 0 = no breaking changes, 1 = breaking changes found

## Safety Gates
- **Approval required:** Never call production APIs
- **Read-only:** Only GET/HEAD by default; POST/PUT/DELETE require explicit flag
- **Rate limit:** Max 10 RPS default, configurable
- **Timeout:** 30s per request, 10 min total

## Failure Handling
- Spec fetch failed → Report error, exit 2
- Target unreachable → Report error, exit 3
- Schema validation error → Record as test failure, continue
- Consumer contract missing → Warn, skip consumer validation

## Completion Criteria
- All generated tests executed
- Breaking changes explicitly listed
- Report artifacts produced
- Exit code reflects breaking change status
```

### 5. Validation
```bash
# Frontmatter check
$ yq '.name, .description' api-contract-testing/SKILL.md
api-contract-testing
Validate API implementations against OpenAPI contracts...

# Reference check
$ grep -oP '(?<=`)[^`]+(?=`)' api-contract-testing/SKILL.md | sort -u
openapi-spec-validator
Spectral
Pact
# All tools verified available in runtime

# Walkthrough: Normal case
# Input: spec.yaml, https://staging.api.com, Bearer token
# → Fetch → Generate 47 tests → Execute → 45 pass, 2 fail (bug in impl) → Report

# Walkthrough: Failure case
# Input: invalid spec URL
# → Fetch fails → Clear error message → Exit code 2

# Walkthrough: Safety case
# Input: production URL without --allow-production
# → Gate triggers → "Production calls require approval" → Exit code 4
```

### 6. Maintenance Note
- **Owner:** Platform team
- **Review:** Quarterly or when OpenAPI tooling updates
- **Versioning:** Semantic (breaking change detection logic = major)

---

## Scenario 2: Improve Existing Skill

**Trigger:** "The debugging skill doesn't handle TypeScript type errors well."

**Invocation:**
```
Improve autonomous-debugging skill:
- Add TypeScript type error handling procedure
- Include tsc --noEmit as baseline check
- Add type error reproduction steps
- Update completion criteria
```

**Execution Log:**
```
## Skill Improvement: autonomous-debugging (TypeScript Support)

### Current Gap Analysis
- Skill mentions "lint/type checks" but no TypeScript-specific procedure
- Type errors are compile-time, not runtime — different debugging approach
- No guidance on `--noEmit`, `tsc --watch`, or type-only debugging

### Proposed Changes
```diff
--- skills/autonomous-debugging/SKILL.md
+++ skills/autonomous-debugging/SKILL.md
@@ -15,6 +15,12 @@ ## Procedure
 2. **Establish baseline**
    - Inspect repository instructions and working-tree changes.
    - Run the narrowest failing test or reproduction before editing.
    - Save the exact command and failure signature.
+   - **For TypeScript projects:** Run `tsc --noEmit` to capture type errors.
+     Record exact file:line:col, error code (TSXXXX), and message.
+     Distinguish: pre-existing vs new type errors.
 
 3. **Form hypotheses**
    - Rank likely causes and identify evidence that would confirm or reject each.
@@ -22,6 +28,12 @@ ## Procedure
    - Trace the failing input through relevant code and dependencies.
    - Check recent changes and configuration differences when available.
+   - **For type errors:** Check tsconfig.json changes, dependency type updates,
+     generic constraint changes, and inference regressions.
+     Use `tsc --traceResolution` for module resolution issues.
 
 4. **Test one cause at a time**
    - Prefer a focused test, debugger, log, or minimal experiment.
@@ -29,6 +41,12 @@ ## Procedure
    - Validate inputs and error handling at trust boundaries.
    - Preserve public interfaces unless a breaking change is explicitly authorized.
+   - **For type fixes:** Prefer type narrowing over `any`, fix inference at source,
+     avoid `@ts-ignore` unless justified with comment and ticket reference.
 
 6. **Verify**
    - Run the regression test, relevant unit/integration tests, lint/type checks and build as applicable.
+   - **Always run `tsc --noEmit`** after type-related fixes.
+   - Verify no new type errors introduced in unrelated files.
 
 7. **Report**
    - State root cause, changed files, tests run, exact outcomes and remaining risks.
```

### Validation
```bash
# Check YAML frontmatter still valid
$ yq '.name' skills/autonomous-debugging/SKILL.md
autonomous-debugging

# Verify new commands exist
$ grep -n 'tsc --noEmit' skills/autonomous-debugging/SKILL.md
18:    - **For TypeScript projects:** Run `tsc --noEmit` to capture type errors.
44:   - **Always run `tsc --noEmit`** after type-related fixes.

# Walkthrough: Type error case
# Error: TS2322: Type 'string' not assignable to 'number'
# → Baseline: tsc --noEmit shows 3 pre-existing, 1 new
# → Hypothesis: Recent change to function signature
# → Fix: Update call site or signature
# → Verify: tsc --noEmit shows 3 pre-existing, 0 new
```

---

## Scenario 3: Skill Composition Pattern

**Trigger:** "Create a skill that combines codebase-intelligence + autonomous-testing for 'test planning'."

**Invocation:**
```
Create composite skill: test-planning
- Uses codebase-intelligence to map affected areas
- Uses autonomous-testing to design risk-based test plan
- Output: Test plan document with priorities, estimates, gaps
```

**Execution Log:**
```
## Skill Creation: test-planning (Composite)

### Design Decision: Composite vs Orchestration
- **Composite skill:** Single SKILL.md that invokes other skills' procedures inline
- **Orchestration:** workflow-orchestrator skill manages separate skill executions
- **Choice:** Composite — simpler, single artifact, no multi-agent needed

### Skill Draft (test-planning/SKILL.md)
```markdown
---
name: test-planning
description: Generate a risk-based test plan for a change by mapping affected code and prioritizing test scenarios. Combines codebase intelligence and testing methodology.
version: 1.0.0
tags: [testing, planning, risk-analysis]
---

# Test Planning

## Objective
Produce a prioritized, risk-based test plan for a proposed change before implementation or review.

## Trigger
- "Create a test plan for this change"
- "What tests do I need for this feature?"
- "Risk assessment for PR #XXX"

## Procedure
1. **Map Impact** (codebase-intelligence)
   - Input: Change description, diff, or PR number
   - Trace: Affected modules, data flow, external dependencies
   - Identify: Entry points, trust boundaries, stateful components

2. **Assess Risk** (autonomous-testing prioritization)
   - Critical paths: Auth, payments, data mutation, security boundaries
   - Regression surface: Changed logic, modified contracts, config changes
   - Complexity: Cyclomatic, cognitive, dependency depth

3. **Design Test Scenarios**
   - For each risk area: Happy path, error cases, boundary, negative
   - Map to test types: Unit, integration, contract, E2E, performance
   - Identify gaps: Missing tests, untested paths, flaky tests

4. **Prioritize & Estimate**
   - P0: Must pass before merge (critical path + regression)
   - P1: Should pass before release (integration + boundary)
   - P2: Nice to have (performance, chaos, edge cases)
   - Estimate: Time to write, time to run, maintenance burden

5. **Produce Plan**
   - Markdown document with: Risk matrix, test scenarios, priorities, estimates
   - Machine-readable JSON for CI integration
   - Gap report: What's not covered and why

## Output Format
```markdown
# Test Plan: PR #234 (Add MFA)

## Risk Matrix
| Area | Risk | Rationale | Test Types |
|------|------|-----------|------------|
| auth/mfa.ts | CRITICAL | New security feature, TOTP crypto | Unit, Integration, E2E |
| auth/routes.ts | HIGH | New endpoints, rate limiting | Integration, Contract |
| users/schema.prisma | MEDIUM | New columns, migration | Migration test |

## Test Scenarios (Prioritized)
### P0 - Merge Gate
- [ ] Unit: TOTP verification (10 cases)
- [ ] Unit: Backup code generation/validation
- [ ] Integration: /auth/mfa/enable flow
- [ ] Integration: /auth/mfa/verify with valid/invalid codes
- [ ] Regression: Login still works without MFA

### P1 - Release Gate
- [ ] Integration: Rate limiting on /verify
- [ ] Integration: Backup code exhaustion
- [ ] Contract: OpenAPI spec matches implementation
- [ ] E2E: Full login + MFA enable + login with MFA

### P2 - Post-Release
- [ ] Performance: TOTP verification <50ms p99
- [ ] Chaos: Clock skew handling
- [ ] Accessibility: QR code alt text

## Gaps
- No test for SMS fallback (not implemented)
- No load test for concurrent MFA enrollments
- Recovery codes UI not in this repo (separate frontend)
```

## Safety
- Read-only: Only analyzes code, generates plan
- No test execution (that's autonomous-testing)
- No code modification
```

### Validation
- Frontmatter valid ✅
- References codebase-intelligence + autonomous-testing procedures ✅
- No new tools required ✅
- Clear boundaries (planning only, no execution) ✅
```

---

## Tips for Effective Use

1. **Start with trigger** — Specific user intent prevents over-generalization
2. **Define boundaries** — What the skill does NOT do is as important
3. **Verify every tool/command** — Don't assume availability
4. **Walk through 3 cases** — Normal, failure, safety
5. **Keep reusable knowledge in skill** — Task-specific values stay out
6. **Composite skills > copy-paste** — Reference other skills by name