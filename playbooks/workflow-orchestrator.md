# Playbook: Workflow Orchestrator

*Practical examples for the `workflow-orchestrator` skill*

---

## Scenario 1: End-to-End Bug Resolution

**Trigger:** "Fix the payment reconciliation bug end-to-end — explore, diagnose, fix, review, test."

**Invocation:**
```
Execute full bug resolution workflow for issue #1847:
- Payment reconciliation runs daily at 2AM
- Fails silently — no alert, no logs, data drift
- Discovered 3 days later during audit
- Goal: Root cause fix + monitoring + regression tests
```

**Execution Log:**
```
## Workflow Execution: Payment Reconciliation Bug (#1847)

### Goal Analysis & Planning (Orchestrator)
**Objective:** Fix silent reconciliation failure + prevent recurrence
**Decomposed into DAG:**
```
1. codebase-intelligence (target: billing/reconciliation)
   → map: job scheduler, reconciliation logic, alerting, data flow
2. autonomous-debugging (input: map + "silent failure, no logs")
   → reproduce, root cause, minimal fix, regression test
3. [GATE: User approves fix]
4. multi-agent-review (scope: billing/reconciliation + alerting)
   → security: financial data, correctness: money math
5. autonomous-testing (scope: reconciliation + alerting + scheduler)
   → unit, integration, scheduled job test
6. Reporter: consolidated report
```

### Phase 1: Codebase Intelligence
**Agent:** Subagent (isolated session)
**Duration:** 4.2 min
**Output:**
- Reconciliation job: `src/jobs/reconciliation.ts` (daily 2AM, cron)
- Calls: `billing/service.ts:reconcileAccounts()` → Stripe API → DB update
- Alerting: None (try/catch swallows errors, no metrics)
- Scheduler: `node-cron`, no persistence, no retry
- Tests: 3 unit tests (happy path only), no integration tests

### Phase 2: Autonomous Debugging
**Agent:** Subagent (isolated session)
**Duration:** 12.7 min
**Reproduction:**
- Simulated Stripe API 500 error → job catches, logs nothing, marks "success"
- Simulated network timeout → same
- Simulated partial data → processes subset, no discrepancy flag

**Root Cause (3 issues):**
1. `reconcileAccounts()`: `catch (e) { logger.debug(e); return { success: true }; }` — swallows errors
2. No idempotency key → retries create duplicate adjustments
3. Scheduler: no lock → concurrent runs if job > 24h

**Fix Applied:**
```typescript
// reconciliation.ts
export async function runReconciliation() {
  const lock = await acquireLock('reconciliation', 30*60*1000); // 30min TTL
  if (!lock) throw new Error('Reconciliation already running');
  
  try {
    const result = await reconcileAccounts({
      idempotencyKey: `recon-${Date.now()}`,
      onError: (err, ctx) => {
        metrics.increment('reconciliation.errors', { type: err.code });
        alerting.critical('Reconciliation failed', { error: err.message, context: ctx });
        throw err; // Don't swallow!
      }
    });
    metrics.gauge('reconciliation.discrepancies', result.discrepancies.length);
    return result;
  } finally {
    await releaseLock(lock);
  }
}
```

**Regression Test:**
```typescript
test('reconciliation fails loudly on Stripe error', async () => {
  stripeMock.onError('internal_server_error');
  await expect(runReconciliation()).rejects.toThrow('Stripe error');
  expect(alerting.critical).toHaveBeenCalledWith('Reconciliation failed', expect.any(Object));
  expect(metrics.increment).toHaveBeenCalledWith('reconciliation.errors', { type: 'internal_server_error' });
});
```

### Phase 3: Gate — User Approval
**Presenter:** Orchestrator
**Evidence:** Root cause, fix diff, regression test
**Decision:** ✅ APPROVED (user confirms fix addresses all 3 issues)

### Phase 4: Multi-Agent Review
**Coordinator:** Orchestrator (inline)
**Reviewer (Security):** 
- CRITICAL: Idempotency key uses timestamp — collision possible
  - Fix: Use UUID v7 (time-ordered, unique)
- HIGH: Alerting includes Stripe error details — potential PII leak
  - Fix: Sanitize error before alerting

**Test Analyst:**
- Added: Concurrency test (2 simultaneous runs)
- Added: Idempotency key collision test
- Added: Alert sanitization test

**Implementer Fixes:**
```diff
- const idempotencyKey = `recon-${Date.now()}`;
+ const idempotencyKey = `recon-${uuidv7()}`;
...
- alerting.critical('Reconciliation failed', { error: err.message, context: ctx });
+ alerting.critical('Reconciliation failed', { error: sanitizeForAlert(err), context: ctx });
```

**Re-Review:** ✅ All findings resolved

### Phase 5: Autonomous Testing
**Scope:** billing/reconciliation + alerting + scheduler
**Results:**
| Suite | Tests | Pass | Fail | Duration |
|-------|-------|------|------|----------|
| Unit (reconciliation) | 15 | 15 | 0 | 2.1s |
| Unit (alerting) | 8 | 8 | 0 | 0.8s |
| Integration (reconciliation) | 12 | 12 | 0 | 18.3s |
| Integration (scheduler) | 5 | 5 | 0 | 45.2s |
| E2E (daily job simulation) | 3 | 3 | 0 | 2.1m |

**Coverage:** reconciliation.ts 94% (was 31%)

### Phase 6: Final Report
**Consolidated Report Generated:**
- **Executive Summary:** Silent reconciliation failure fixed. 3 root causes addressed. Monitoring added. Regression tests in place.
- **Skill Evidence:** 6 skill executions, 0 failed, 4 gates passed
- **Diff:** 4 files changed, 127 lines added, 23 removed
- **Tests:** 43 new/updated tests, all passing
- **Risks:** None critical. Medium: Scheduler lock TTL tuning may need adjustment.
- **Audit Trail:** Complete with timestamps, approvals, findings

**Artifacts:**
- `workflow-report-1847.json` (machine-readable)
- `workflow-report-1847.md` (human)
- `reconciliation-fix.patch`
- `test-results-1847.xml`
```

---

## Scenario 2: Feature Implementation Pipeline

**Trigger:** "Implement OAuth2 device flow from spec to tested code."

**Invocation:**
```
Execute feature implementation workflow for OAuth2 Device Flow (RFC 8628):
- Spec: https://datatracker.ietf.org/doc/html/rfc8628
- Scope: New endpoints, device code storage, polling, user consent UI API
- Constraints: Security review required, no breaking changes, <2 weeks
```

**Execution Log:**
```
## Workflow Execution: OAuth2 Device Flow Implementation

### DAG (Planned by Orchestrator)
```
1. codebase-intelligence (auth module, existing OAuth2 patterns)
2. model-router (select model for code generation)
3. [PARALLEL]
   3a. Implementer: Write device flow endpoints + storage + tests
   3b. Test Analyst: Design security test cases + integration plan
4. multi-agent-review (security-focused)
5. autonomous-testing (full auth suite + new device flow)
6. Reporter
```

### Phase 1-2: Intelligence + Model Selection
- Map: Existing auth at `src/modules/auth/`, routes, tokens, clients
- Model: `claude-3.5-sonnet` (security-sensitive code gen)
- Context: 2,400 lines (auth module + RFC 8628 spec)

### Phase 3: Parallel Implementation
**Implementer Subagent (45 min):**
- Created: `device-flow.ts`, `device-codes.ts`, `routes.ts` (3 new endpoints)
- Tests: 18 unit + 7 integration
- Patterns: Followed existing auth code style, Prisma models, error hierarchy

**Test Analyst Subagent (20 min):**
- Security tests: 12 cases (rate limit, code entropy, polling bounds, consent bypass)
- Integration: Device authorization → user consent → token polling → token issuance
- Negative: Expired codes, revoked codes, malicious client_id

### Phase 4: Multi-Agent Review
**Findings:**
| ID | Severity | Finding | Resolution |
|----|----------|---------|------------|
| SEC-001 | CRITICAL | Device code entropy: `Math.random()` not crypto-secure | `crypto.randomBytes(32)` |
| SEC-002 | HIGH | No rate limit on `/device/authorize` | Added: 10/min per IP |
| SEC-003 | MEDIUM | User code (8 chars) brute-forcible | Increased to 12 chars + rate limit |
| SEC-004 | LOW | Consent page not in this repo | Documented: frontend team owns |

**All resolved in re-review.**

### Phase 5: Testing
- Full auth suite: 67 tests pass
- New device flow: 25 tests pass
- Security tests: 12 pass
- E2E: Device flow happy path + 3 error paths

### Phase 6: Report
- **Delivered:** Complete RFC 8628 implementation
- **Security:** 4 findings resolved, penetration test ready
- **Tests:** 37 new tests, coverage 89%
- **Time:** 2.3 hours total (vs estimated 2 weeks manual)
```

---

## Scenario 3: Release Validation Pipeline

**Trigger:** "Validate v3.0.0 release candidate — full pipeline."

**Invocation:**
```
Execute release validation for v3.0.0-rc.2:
- Breaking changes: Auth v2, new billing engine
- Migration: 12 DB migrations
- Required: Full test, perf baseline, security, migration dry-run, rollback test
```

**Execution Log:**
```
## Workflow Execution: v3.0.0-rc.2 Release Validation

### DAG
```
1. autonomous-testing (full suite + perf baseline)
2. multi-agent-review (changelog, migrations, breaking changes)
3. [PARALLEL]
   3a. Security scan (deps + SAST)
   3b. Dependency audit (license + vulnerability)
   3c. Migration dry-run (staging clone)
4. [GATE: Release approval]
5. rollback-test (deploy → smoke → rollback → smoke)
6. Reporter + release notes generation
```

### Phase 1: Testing
- Unit: 523 passed
- Integration: 187 passed
- E2E: 52 passed (3 browsers)
- Perf: 12/15 endpoints improved, 3 within 5% (acceptable)

### Phase 2: Review
- Migration review: 12 migrations, all reversible, <30s each
- Breaking changes: Documented in CHANGELOG, migration guide linked
- Config changes: 3 new required env vars documented

### Phase 3: Parallel Security
- SAST: 0 new findings, 2 pre-existing low tracked
- Deps: 0 critical/high, 3 moderate (dev deps only)
- License: All compatible (MIT, Apache-2.0, BSD-3)

### Phase 4: Migration Dry-Run
- Staging clone restored from prod snapshot (sanitized)
- All 12 migrations applied: 18.4s total
- Data integrity verified: Row counts, FK constraints, indexes

### Phase 5: Gate — Release Approval
**Presented:** All evidence above
**Decision:** ✅ APPROVED by Platform + Security + Product

### Phase 6: Rollback Test
- Deploy rc.2 to staging: 47s
- Smoke tests: 15/15 pass
- Rollback to v2.9.1: 22s
- Smoke tests on v2.9.1: 15/15 pass
- Data integrity: Verified

### Final Report
- **Verdict:** ✅ RELEASE READY
- **Artifacts:** Release notes drafted, migration guide, rollback procedure
- **Risk:** Low — all gates passed, rollback verified
```

---

## Scenario 4: Autonomous Refactoring with Safety

**Trigger:** "Replace all `any` types in codebase — safely, with verification."

**Invocation:**
```
Execute safe refactoring workflow:
- Target: 247 `any` types across 89 files (TypeScript)
- Strategy: Incremental, per-module, with test verification each step
- Safety: No behavior change, only type strengthening
- Gate: Each module requires review before next
```

**Execution Log:**
```
## Workflow Execution: `any` Elimination (247 occurrences)

### DAG (Dynamic — Orchestrator builds per-module)
```
FOR EACH MODULE (topological order by dependency):
  1. codebase-intelligence (module scope)
  2. autonomous-debugging (analyze each `any` — infer real type)
  3. [GATE: Module review]
  4. Implement fix (type annotations, generics, narrowing)
  5. autonomous-testing (module tests + typecheck)
  6. [GATE: Typecheck clean + tests pass]
NEXT MODULE
```

### Execution (First 3 Modules)

#### Module: `shared/utils` (12 `any`)
- Intelligence: Utility functions, no external deps
- Debugging: 8 `any` → inferred from usage, 4 → generics needed
- Fix: 3 PRs (batched by pattern)
- Testing: All pass, `tsc --noEmit` clean
- Gate: ✅ Approved

#### Module: `auth/tokens` (23 `any`)
- Intelligence: JWT, crypto, Prisma — high security
- Debugging: JWT payloads, crypto callbacks, Prisma delegates
- Fix: Proper `JWTPayload` interface, `KeyLike` from `jose`, Prisma generics
- Testing: All pass + 3 new type tests
- Gate: ✅ Approved (Security reviewer)

#### Module: `billing/calculations` (41 `any`)
- Intelligence: Financial math, Decimal.js, Stripe types
- Debugging: Stripe webhook types, Decimal operations, currency codes
- Fix: `Stripe.WebhookEvent`, `Decimal` arithmetic, `Currency` enum
- Testing: All pass + property-based tests for math
- Gate: ✅ Approved

### Progress Tracking (Orchestrator State)
```json
{
  "workflowId": "wf_any-elimination",
  "totalModules": 12,
  "completed": 3,
  "inProgress": "users/profile",
  "totalAnys": 247,
  "resolved": 76,
  "remaining": 171,
  "estimatedCompletion": "2026-11-25T14:00:00Z"
}
```

### Safety Features Demonstrated
- **Per-module gates:** No module advances without review
- **Typecheck verification:** `tsc --noEmit` clean required at each step
- **Test preservation:** All existing tests must pass
- **Rollback ready:** Each module in separate commit, revertible
- **Progress visibility:** Real-time state, estimates, blockers
```

---

## Configuration for Advanced Workflows

```yaml
# workflow-orchestrator advanced config
workflow_orchestrator:
  # Parallel execution
  max_parallel_skills: 3
  max_parallel_subagents: 2
  
  # Checkpointing
  checkpoint_every_n_nodes: 1
  checkpoint_dir: ".workflow/checkpoints"
  retain_checkpoints: 10
  
  # Budgets
  default_time_budget_ms: 3600000      # 1 hour
  default_cost_budget_usd: 10.00
  max_cost_per_skill_usd: 2.00
  
  # Model routing for subagents
  subagent_model_policy:
    codebase-intelligence: "gemini-1.5-flash"      # Cheap, large context
    autonomous-debugging: "claude-3.5-sonnet"      # Best reasoning
    autonomous-testing: "gpt-4o-mini"              # Fast, structured output
    multi-agent-review: "claude-3.5-sonnet"        # Security reasoning
    skill-creator: "gpt-4o"                        # Balanced
  
  # Gates
  require_approval_for:
    - write
    - deploy
    - secret
    - external_write
    - budget_exceeded
  
  auto_approve:
    - read_only_analysis
    - test_execution
    - report_generation
  
  # Evidence
  evidence_format: "json+markdown"
  evidence_retention_days: 90
  audit_log_enabled: true
  
  # Notifications
  notify_on:
    - gate_required
    - budget_warning (80%)
    - skill_failed
    - workflow_completed
```

---

## Tips for Effective Use

1. **Define clear acceptance criteria** — Orchestrator plans to those
2. **Use gates for high-risk transitions** — Fix approval, release approval
3. **Parallelize independent work** — Implementer + Test Analyst simultaneously
4. **Trust but verify** — Orchestrator re-validates all skill outputs
5. **Budget awareness** — Set limits, get warnings at 80%
6. **Checkpoint frequently** — Enables rollback, resumption, audit