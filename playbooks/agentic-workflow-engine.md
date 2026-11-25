# Playbook: Agentic Workflow Engine

*Practical examples for the `agentic-workflow-engine` skill*

---

## Scenario 1: Autonomous Bug Fix with Self-Correction

**Trigger:** "Fix the memory leak in WebSocket handler completely — reproduce, fix, test, document."

**Invocation:**
```
Execute autonomous workflow:
Goal: "Fix WebSocket memory leak (issue #882) end-to-end with monitoring"
Constraints:
- Budget: $5.00
- Time: 30 minutes
- Quality: All tests pass, typecheck clean, load test stable
- Human gate: Security review for resource exhaustion fix
```

**Execution Log:**
```
## Workflow Execution: WebSocket Memory Leak Fix

### ITERATION 1 — Planning & Reconnaissance
**Planner Output (GoalSpec):**
```
Objective: Fix WebSocket memory leak #882
Success Criteria:
  - Leak reproduced and root cause identified
  - Minimal fix applied
  - Regression test added (fails before, passes after)
  - Load test: 10k messages, memory growth < 10MB
  - Monitoring/alerting added for connection leaks
  - Documentation updated
Constraints:
  - Budget: $5.00, Time: 30min
  - Human gate: Security review (resource exhaustion)
  - Quality: 100% tests pass, typecheck clean
Subtasks:
  1. map_ws_handler (codebase-intelligence)
  2. debug_leak (autonomous-debugging)
  3. apply_fix (code edit)
  4. security_review (multi-agent-review) ← HUMAN GATE
  5. regression_test (autonomous-testing)
  6. load_test (autonomous-testing)
  7. add_monitoring (code edit)
  8. update_docs (code edit)
```

### ITERATION 2 — Execute Map & Debug
**Execution:**
```
Node: map_ws_handler (codebase-intelligence)
  Status: SUCCESS (2.1 min, $0.08)
  Output: WS handler at src/ws/handler.ts, 2KB/msg leak in event listeners
  Insight: "Missing cleanup in onClose, no connection tracking"

Node: debug_leak (autonomous-debugging)
  Status: SUCCESS (8.3 min, $0.42)
  Output: Root cause confirmed — event listeners not removed on disconnect
  Fix: Add cleanup() call in onClose handler
  Regression test: Created (fails before fix)
  Insight: "Simple fix, but need to verify no other leak paths"
```

### ITERATION 3 — Apply Fix & Security Review
**Execution:**
```
Node: apply_fix
  Status: SUCCESS (1.2 min, $0.05)
  Diff: 5 lines added (cleanup call + connection tracking)
  
Node: security_review (multi-agent-review) ← HUMAN GATE
  Reviewer finding: CRITICAL — Connection tracking uses Map without size limit
  "Under attack, Map grows unbounded → new DoS vector"
  Fix required: Add max connections + LRU eviction
  
CORRECTION TRIGGERED (Self-Correction Engine):
  Failure type: VALIDATION_FAILED (security finding)
  Correction: Modify fix to include connection limits
  Confidence: 0.92
  Action: REVISE node apply_fix with enhanced fix
```

### ITERATION 4 — Revised Fix & Re-Review
**Execution:**
```
Node: apply_fix (revised)
  Status: SUCCESS (2.1 min, $0.08)
  Diff: 18 lines (cleanup + MaxConnectionsMap with LRU + metrics)
  
Node: security_review (re-review)
  Status: SUCCESS
  Findings: All resolved. MaxConnectionsMap prevents DoS.
  Verdict: APPROVED
```

### ITERATION 5 — Testing & Validation
**Execution:**
```
Node: regression_test (autonomous-testing)
  Status: SUCCESS (3.2 min, $0.12)
  Results: 15 tests pass (12 existing + 3 new regression)
  
Node: load_test (autonomous-testing)
  Status: SUCCESS (8.7 min, $0.35)
  Results: 10k messages, 500 concurrent connections
  Memory: Peak 42MB, growth < 5MB (stable)
  No leaks detected
```

### ITERATION 6 — Monitoring & Documentation
**Execution:**
```
Node: add_monitoring
  Status: SUCCESS (1.5 min, $0.06)
  Added: Prometheus metrics (ws_connections_active, ws_memory_bytes, ws_leaks_detected)
  Added: Alert rule (ws_connections_active > 1000 for 5m)
  
Node: update_docs
  Status: SUCCESS (0.8 min, $0.03)
  Updated: docs/architecture/websocket.md
  Added: Memory management section, troubleshooting guide
```

### FINAL EVALUATION (Critic)
```
Critic Model Evaluation:
- All success criteria MET with evidence
- Security finding caught and fixed (self-correction worked)
- Load test validates fix under realistic load
- Monitoring enables future detection
- Documentation complete
- Quality gates: 100% tests pass, typecheck clean, lint clean

Recommendation: COMPLETE
```

### SUMMARY
```
Status: SUCCESS
Iterations: 6
Total Cost: $1.19 (budget: $5.00)
Total Time: 24.3 minutes (budget: 30 min)
Corrections Applied: 1 (security finding → enhanced fix)
Human Gates: 1 (security review — passed)
Lessons Learned:
  - "WebSocket handlers need explicit cleanup + connection limits"
  - "Security review catches DoS vectors functional tests miss"
  - "Self-correction on security findings prevents production issues"
Artifacts:
  - Fix: src/ws/handler.ts (+18 lines)
  - Tests: tests/ws/handler.test.ts (+3 regression tests)
  - Monitoring: src/metrics/ws-metrics.ts (new)
  - Docs: docs/architecture/websocket.md (updated)
  - Report: workflow-report-882.json/md
```
```

---

## Scenario 2: Iterative Test Coverage Improvement

**Trigger:** "Get auth module to 90% test coverage — keep going until target hit."

**Invocation:**
```
Execute autonomous workflow:
Goal: "Achieve 90% test coverage for auth module"
Constraints:
- Budget: $3.00
- Max iterations: 8
- Each iteration: Find gaps → Generate tests → Verify coverage
- Quality: All new tests pass, no flaky tests
```

**Execution Log:**
```
## Workflow Execution: Auth Module Coverage Improvement

### INITIAL STATE
Coverage: 67% (auth module)
Target: 90%
Budget: $3.00

### ITERATION 1
**Phase: Analyze Gaps**
- Uncovered: token refresh (12%), MFA (18%), OAuth (22%), error paths (31%)
- Priority: Error paths (highest impact), then OAuth, MFA, token refresh

**Phase: Generate Tests (parallel)**
- Generated: 23 new tests (error paths: 8, OAuth: 7, MFA: 5, token: 3)
- Cost: $0.45

**Phase: Verify**
- All 23 tests pass
- New coverage: 78% (+11%)
- Budget used: $0.45

### ITERATION 2
**Phase: Analyze Gaps**
- Remaining: token edge cases (8%), MFA backup codes (12%), OAuth state (15%)
- Priority: OAuth state (security), MFA backup codes, token edge cases

**Phase: Generate Tests**
- Generated: 15 new tests
- Cost: $0.32

**Phase: Verify**
- 14/15 pass, 1 FLAKY (OAuth state timing)
- Flaky test isolated, marked for fix
- New coverage: 85% (+7%)
- Budget used: $0.77

### ITERATION 3
**Phase: Fix Flaky + Remaining Gaps**
- Fixed: OAuth state test (added proper async waiting)
- Generated: 8 tests for token edge cases + MFA backup codes
- Cost: $0.28

**Phase: Verify**
- All 22 new tests pass (including fixed flaky)
- New coverage: 91% (+6%)
- TARGET ACHIEVED (91% > 90%)

### CRITIC EVALUATION
```
Coverage: 91% ✅
Test quality: 38 new tests, 0 flaky, all meaningful
Edge cases covered: Token expiry, MFA exhaustion, OAuth CSRF, error paths
Budget: $1.05 << $3.00
Time: 12 min
Recommendation: COMPLETE
```

### LESSONS LEARNED
- "Error paths are highest ROI for coverage (31% gap → 8 tests)"
- "OAuth state tests need explicit clock control to avoid flakiness"
- "Parallel test generation 3x faster than sequential"
```

---

## Scenario 3: Feature Implementation with Quality Gates

**Trigger:** "Implement rate limiting for all API endpoints — token bucket, Redis backend, configurable per-route."

**Invocation:**
```
Execute autonomous workflow:
Goal: "Implement production-ready rate limiting for all API endpoints"
Constraints:
- Budget: $8.00
- Time: 45 minutes
- Gates: Security review, Load test, Integration test
- Patterns: Follow existing auth middleware patterns
```

**Execution Log:**
```
## Workflow Execution: API Rate Limiting Implementation

### PLAN (Decomposed)
1. analyze_existing_patterns (codebase-intelligence)
2. design_rate_limiter (planning)
3. implement_core (TokenBucket + RedisTokenBucket)
4. implement_middleware (Fastify integration)
5. configure_routes (per-route limits)
6. unit_tests (core + middleware)
7. integration_tests (Redis, multi-instance)
8. security_review (multi-agent-review) ← GATE
9. load_test (autonomous-testing) ← GATE
10. documentation

### EXECUTION HIGHLIGHTS

**Node: implement_core**
- Generated: TokenBucket (memory) + RedisTokenBucket (distributed)
- Used: Lua script for atomic Redis operations
- Pattern: Followed existing `auth/middleware.ts` structure
- Cost: $0.68

**Node: security_review** ← HUMAN GATE
- Finding: HIGH — Redis key explosion under attack (no key TTL cleanup)
- Finding: MEDIUM — No protection against header injection in key
- Correction applied: Added key TTL + sanitization
- Re-review: PASSED

**Node: load_test** ← GATE
- 10k RPS, 1000 concurrent users
- Latency p99: 12ms (target < 50ms) ✅
- Memory stable ✅
- Redis connection pool healthy ✅
- PASSED

**Node: integration_tests**
- Multi-instance: 3 nodes, shared Redis
- Rate limit correctly distributed ✅
- Graceful degradation on Redis failure ✅
- PASSED

### RESULT
```
Status: SUCCESS
Cost: $3.42
Time: 38 min
Files: 5 new, 3 modified
Tests: 47 new (unit: 28, integration: 12, load: 3, security: 4)
Gates passed: 2/2 (security, load)
```
```

---

## Scenario 4: Safe Refactoring with Rollback

**Trigger:** "Replace all `any` types in billing module — safely, with verification each step."

**Invocation:**
```
Execute autonomous workflow:
Goal: "Eliminate 'any' types in billing module (41 occurrences)"
Constraints:
- Budget: $4.00
- Strategy: Per-file, with typecheck + tests each step
- Rollback: Each file in separate commit
- Gate: Human review for financial calculation changes
```

**Execution Log:**
```
## Workflow Execution: Billing Module `any` Elimination

### STRATEGY: Topological Order (dependencies first)
Files: calculations.ts → proration.ts → webhooks.ts → service.ts → routes.ts

### ITERATIONS (Per File)

**File: calculations.ts (12 `any`)**
- Analysis: Decimal.js ops, Stripe webhook types, currency codes
- Fix: Proper `Decimal` arithmetic, `Stripe.WebhookEvent`, `Currency` enum
- Verification: tsc --noEmit ✅, tests ✅, property tests ✅
- Commit: "types: eliminate any in calculations.ts"

**File: proration.ts (8 `any`)**
- Analysis: Date math, plan change calculations
- Fix: Proper `PlanChange` interface, `ProrationResult` type
- Gate: Human review (financial calculations)
- Review: APPROVED (type improvements only, no logic change)
- Verification: All pass
- Commit: "types: eliminate any in proration.ts"

**File: webhooks.ts (15 `any`)**
- Analysis: Stripe event types, handler signatures
- Fix: Discriminated unions for event types, proper handler types
- Verification: All pass
- Commit: "types: eliminate any in webhooks.ts"

**File: service.ts (4 `any`)**
- Analysis: Method return types, repository interfaces
- Fix: Repository generics, proper return types
- Verification: All pass
- Commit: "types: eliminate any in service.ts"

**File: routes.ts (2 `any`)**
- Analysis: Request body types, response types
- Fix: Zod schemas for validation + inference
- Verification: All pass
- Commit: "types: eliminate any in routes.ts"

### CRITIC EVALUATION
```
All 41 `any` eliminated ✅
Typecheck: CLEAN (0 errors) ✅
Tests: 127 pass (0 new failures) ✅
Financial logic: UNCHANGED (verified by review) ✅
Commits: 5 atomic, each revertible ✅
Budget: $1.87 << $4.00
```

### LESSONS LEARNED
- "Per-file commits enable safe rollback and clear history"
- "Human review gate on financial code catches type changes that look correct but alter semantics"
- "Property-based tests essential for financial math type changes"
```

---

## Scenario 5: Autonomous Security Hardening

**Trigger:** "Scan codebase for OWASP Top 10 vulnerabilities and fix critical/high findings."

**Invocation:**
```
Execute autonomous workflow:
Goal: "Remediate OWASP Top 10 vulnerabilities in codebase"
Constraints:
- Budget: $10.00
- Priority: Critical → High → Medium
- Gates: Security review for each fix
- Verification: Security tests for each fix
```

**Execution Log:**
```
## Workflow Execution: OWASP Remediation

### PHASE 1: Scan & Prioritize
**Tool: SAST + Dependency Audit + Manual Review**
Findings:
1. CRITICAL: SQL Injection in user search (string interpolation)
2. CRITICAL: Path traversal in file upload (../ in filename)
3. HIGH: XSS in admin panel (unescaped user input)
4. HIGH: Broken auth — JWT no audience validation
5. MEDIUM: Info disclosure — stack traces in production
6. MEDIUM: Weak crypto — Math.random() for tokens
7. LOW: Missing security headers

### PHASE 2: Remediate (Parallel where independent)

**Critical 1: SQL Injection**
- Fix: Parameterized queries (Prisma)
- Tests: 5 injection attempts blocked
- Review: APPROVED

**Critical 2: Path Traversal**
- Fix: Path normalization + allowlist validation
- Tests: 10 traversal attempts blocked
- Review: APPROVED

**High 1: XSS**
- Fix: Auto-escaping template engine (replaced string concat)
- Tests: 15 XSS payloads neutralized
- Review: APPROVED

**High 2: JWT Audience**
- Fix: Validate `aud` claim matches service
- Tests: Cross-service token rejected
- Review: APPROVED

**Medium: Info Disclosure**
- Fix: Error boundary + sanitized production errors
- Review: APPROVED

**Medium: Weak Crypto**
- Fix: `crypto.randomBytes()` for all tokens
- Review: APPROVED

**Low: Security Headers**
- Fix: Helmet.js middleware
- Review: APPROVED

### PHASE 3: Regression & Verification
- Full test suite: 523 pass
- Security test suite: 47 new tests pass
- SAST re-scan: 0 critical/high, 0 new findings
- Dependency audit: 0 critical/high

### RESULT
```
Status: SUCCESS
Findings Fixed: 7 (2 critical, 2 high, 2 medium, 1 low)
Security Tests Added: 47
Cost: $6.23
Time: 52 min
Risk Reduction: CRITICAL: 2→0, HIGH: 2→0
```
```

---

## Advanced: Meta-Learning in Action

**Scenario:** Engine learns from previous workflows to optimize future ones.

```
## Learning Progression (Over 20 Workflows)

### Workflow 1-5: Naive Planning
- Over-estimated time by 3x
- Used premium models for everything
- No parallel execution
- Avg cost: $4.20, time: 45 min

### Workflow 6-10: Pattern Recognition
- Learned: codebase-intelligence + debugging can parallelize
- Learned: free models work for classification
- Learned: security review gate catches 40% of issues
- Avg cost: $2.10, time: 28 min

### Workflow 11-15: Optimization
- Learned: Test generation batches of 5-8 optimal
- Learned: Load test only needed for perf-critical changes
- Learned: Property-based tests catch type refactor bugs
- Avg cost: $1.35, time: 22 min

### Workflow 16-20: Mastery
- Dynamic model routing per subtask
- Predictive budget allocation
- Proactive correction (anticipates security findings)
- Avg cost: $0.87, time: 18 min
- Success rate: 95% (vs 70% initially)
```

---

## Configuration for Production

```yaml
agentic_workflow_engine:
  # Production hardening
  max_iterations: 15
  max_iterations_per_node: 3
  
  # Cost control
  default_total_budget_usd: 15.00
  budget_warning_threshold: 0.75
  hard_stop_at_budget: true
  
  # Quality gates (non-negotiable)
  quality_gates:
    test_pass_rate: 1.0
    typecheck_clean: true
    lint_clean: true
    security_scan_clean: true
    coverage_threshold: 0.80
  
  # Human governance
  required_human_gates:
    - "production_deploy"
    - "secret_rotation"
    - "data_migration"
    - "security_finding_critical"
    - "budget_exceeded"
    - "destructive_operation"
    - "schema_migration"
  
  # Observability
  trace_enabled: true
  metrics_enabled: true
  audit_log_path: ".workflow/audit.log"
  alert_on:
    - budget_warning
    - critical_finding
    - iteration_limit_approaching
    - human_gate_pending > 30min
  
  # Memory & Learning
  memory_enabled: true
  memory_retention_days: 180
  meta_learning_enabled: true
  optimization_interval: 10  # workflows
```

---

*This playbook demonstrates the agentic workflow engine's ability to autonomously execute complex goals with self-correction, quality gates, and continuous learning. Each workflow produces auditable evidence and reusable lessons.*