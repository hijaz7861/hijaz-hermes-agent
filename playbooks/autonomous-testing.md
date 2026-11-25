# Playbook: Autonomous Testing

*Practical examples for the `autonomous-testing` skill*

---

## Scenario 1: Pre-Merge Validation

**Trigger:** "Test this PR before merge — it touches auth and billing."

**Invocation:**
```
Validate PR #234 (auth: add MFA, billing: proration fixes):
- Run affected unit tests
- Run integration tests for auth + billing
- Check lint, typecheck, build
- Report pass/fail/blocked with evidence
```

**Execution Log:**
```
## Test Report: PR #234

### Change Summary
- `src/modules/auth/mfa.ts` (new) — TOTP + backup codes
- `src/modules/auth/routes.ts` — 3 new routes
- `src/modules/billing/proration.ts` — fixed edge case
- `tests/unit/auth/mfa.test.ts` (new) — 12 tests
- `tests/integration/billing/proration.test.ts` — 5 tests updated

### Baseline (main branch)
```
$ pnpm test --reporter=dot 2>&1 | tail -5
✓ 234 passed
✗ 0 failed
Duration: 12.3s
```

### Test Execution on PR

| Phase | Command | Exit | Duration | Result |
|-------|---------|------|----------|--------|
| Lint | `pnpm lint` | 0 | 3.2s | ✅ Pass |
| Typecheck | `pnpm typecheck` | 0 | 4.1s | ✅ Pass |
| Build | `pnpm build` | 0 | 6.8s | ✅ Pass |
| Unit (auth) | `pnpm test tests/unit/auth/` | 0 | 2.1s | ✅ 47 passed |
| Unit (billing) | `pnpm test tests/unit/billing/` | 0 | 1.8s | ✅ 31 passed |
| Integration (auth) | `pnpm test tests/integration/auth/` | 0 | 8.4s | ✅ 23 passed |
| Integration (billing) | `pnpm test tests/integration/billing/` | 0 | 6.2s | ✅ 18 passed |
| E2E (critical) | `pnpm test:e2e --project=chromium` | 0 | 42.1s | ✅ 12 passed |

### Coverage Impact
| Module | Before | After | Delta |
|--------|--------|-------|-------|
| auth/mfa.ts | N/A | 94% | +94% |
| billing/proration.ts | 78% | 91% | +13% |
| Overall | 87.2% | 88.1% | +0.9% |

### Risk Assessment
- **New attack surface:** MFA endpoints — covered by 12 unit + 5 integration tests
- **Proration logic:** Financial calc — covered by 8 unit + 5 integration (edge cases added)
- **No migration** — schema unchanged
- **No config changes** — env vars unchanged

### Verdict: ✅ APPROVE
All checks pass. Coverage increased. No new failures. Ready for merge.

### Evidence Artifacts
- `test-report-pr-234.json` — machine-readable results
- `coverage-pr-234/` — HTML coverage report
- `e2e-screenshots-pr-234/` — Playwright traces
```

---

## Scenario 2: Release Candidate Validation

**Trigger:** "Validate v2.4.0-rc.1 for production release."

**Invocation:**
```
Full release validation for v2.4.0-rc.1:
- Complete test suite (unit, integration, e2e)
- Performance baseline comparison
- Security scan (dependencies, SAST)
- Migration dry-run
- Rollback test
```

**Execution Log:**
```
## Release Validation: v2.4.0-rc.1

### Test Suite
| Suite | Tests | Passed | Failed | Skipped | Duration |
|-------|-------|--------|--------|---------|----------|
| Unit | 412 | 412 | 0 | 0 | 18.3s |
| Integration | 127 | 127 | 0 | 0 | 47.2s |
| E2E (3 browsers) | 45 | 45 | 0 | 0 | 2m 14s |
| Contract (Pact) | 23 | 23 | 0 | 0 | 8.1s |

### Performance Baseline (vs v2.3.0)
| Endpoint | v2.3.0 p95 | v2.4.0 p95 | Delta | Verdict |
|----------|------------|------------|-------|---------|
| GET /api/users/me | 42ms | 38ms | -9.5% | ✅ Better |
| POST /api/auth/login | 89ms | 95ms | +6.7% | ⚠️ Within 10% |
| POST /api/billing/checkout | 234ms | 241ms | +3.0% | ✅ OK |
| GET /api/teams/:id/members | 156ms | 148ms | -5.1% | ✅ Better |

### Security Scan
```
$ pnpm audit --audit-level=high
✓ 0 vulnerabilities (high/critical)

$ pnpm dlx @github/codeql-cli analyze --format=sarif
✓ 0 new findings
✓ 2 pre-existing low: logged for tracking
```

### Migration Dry-Run
```
$ pnpm migrate:dry-run --to=v2.4.0
✓ 3 migrations pending
✓ All reversible (down scripts present)
✓ Estimated downtime: <30s (index creation concurrent)
✓ Tested on staging clone: 12s
```

### Rollback Test
```
$ pnpm deploy:staging v2.4.0-rc.1
✓ Deployed in 42s

$ pnpm test:smoke --env=staging
✓ 15/15 passed

$ pnpm rollback:staging v2.3.0
✓ Rolled back in 18s
✓ Data integrity verified
✓ Smoke tests pass on v2.3.0
```

### Known Limitations
1. E2E tests don't cover Stripe webhook retry scenarios (mock only)
2. Load test limited to 100 RPS (staging capacity)
3. No chaos engineering in pipeline yet

### Verdict: ✅ RELEASE APPROVED
All gates pass. Performance within threshold. Security clean. Migration reversible. Rollback verified.

### Sign-Off
- QA Lead: ✅ (automated evidence)
- Security: ✅ (scan clean)
- Platform: ✅ (rollback tested)
- Product: ⏳ (manual feature verification)
```

---

## Scenario 3: Agent-Generated Code Verification

**Trigger:** "The AI wrote a new rate limiter. Verify it works correctly."

**Invocation:**
```
Verify agent-generated rate limiter in src/shared/rate-limiter.ts:
- Unit tests for token bucket algorithm
- Integration test with Redis backend
- Concurrency test (1000 parallel requests)
- Edge cases: burst, refill, clock skew, Redis failure
- Property-based tests for invariants
```

**Execution Log:**
```
## Verification: Agent-Generated Rate Limiter

### Code Under Test
- `src/shared/rate-limiter.ts` — TokenBucket + RedisTokenBucket
- Generated by: code-generation agent (model: claude-3.5-sonnet)
- Claimed: "Production-ready, handles all edge cases"

### Test Plan Execution

#### 1. Unit Tests (Algorithm Correctness)
```
$ pnpm test tests/unit/shared/rate-limiter.test.ts
✓ 28/28 passed
```
| Test | Purpose |
|------|---------|
| `allows up to capacity` | Basic allowance |
| `rejects over capacity` | Hard limit |
| `refills over time` | Token regeneration |
| `burst then refill` | Burst handling |
| `exact capacity boundary` | Off-by-one |
| `zero capacity` | Edge case |
| `negative capacity throws` | Input validation |

#### 2. Integration Tests (Redis Backend)
```
$ pnpm test tests/integration/shared/rate-limiter-redis.test.ts
✓ 15/15 passed
```
| Test | Purpose |
|------|---------|
| `distributed rate limiting` | Multi-instance |
| `Redis connection failure` | Graceful degrade |
| `key expiry cleanup` | Memory management |
| `atomic operations` | Race conditions |

#### 3. Concurrency Stress Test
```typescript
// tests/stress/rate-limiter-concurrency.test.ts
const results = await Promise.all(
  Array(1000).fill(null).map(() => limiter.consume('user-1'))
);
const allowed = results.filter(r => r.allowed).length;
expect(allowed).toBe(100); // capacity = 100
```
```
$ pnpm test tests/stress/rate-limiter-concurrency.test.ts
✓ 1/1 passed (1000 parallel, 100 allowed, 900 rejected)
Duration: 1.2s
```

#### 4. Property-Based Tests (fast-check)
```typescript
// tests/property/rate-limiter.properties.test.ts
test('invariant: allowed + rejected === total requests', () => {
  fc.assert(fc.property(fc.nat(1000), fc.nat(100), (requests, capacity) => {
    const limiter = new TokenBucket(capacity, 10); // 10/sec refill
    let allowed = 0, rejected = 0;
    for (let i = 0; i < requests; i++) {
      if (limiter.consume('key').allowed) allowed++; else rejected++;
    }
    expect(allowed + rejected).toBe(requests);
  }));
});
```
```
$ pnpm test tests/property/rate-limiter.properties.test.ts
✓ 5000 properties tested, 0 failures
```

#### 5. Clock Skew & Edge Cases
| Scenario | Test | Result |
|----------|------|--------|
| System time jumps forward | `setSystemTime(+1hr)` | ✅ Refills correctly |
| System time jumps backward | `setSystemTime(-1hr)` | ✅ No negative tokens |
| Redis latency spike (500ms) | `chaos.latency(500ms)` | ✅ Local fallback works |
| Redis returns stale data | `mock.staleData()` | ✅ Version check rejects |

### Issues Found & Fixed

| Issue | Severity | Fix |
|-------|----------|-----|
| No validation on `capacity <= 0` | Medium | Added `if (capacity <= 0) throw` |
| Refill rate not validated | Low | Added `if (refillRate <= 0) throw` |
| Redis key collision possible | Low | Added namespace prefix `rl:` |
| No metrics export | Info | Added `getStats()` method |

### Verdict: ✅ VERIFIED WITH FIXES
Agent code functionally correct. 4 issues found (0 critical), all fixed with tests. Ready for production.

### Evidence
- `verification-report-rate-limiter.json` — full results
- `fixed-rate-limiter.patch` — applied fixes
- Property test seed: `0x7f3a1` (reproducible)
```

---

## Scenario 4: Regression Test Generation

**Trigger:** "We fixed bug #882 (memory leak). Generate regression tests."

**Invocation:**
```
Generate and run regression tests for fixed memory leak in WebSocket handler:
- Test that reproduces original leak pattern
- Test that verifies fix (no leak)
- Long-running test (10k messages)
- Memory profiling integration
```

**Execution Log:**
```
## Regression Tests: WebSocket Memory Leak (#882)

### Original Bug
- Leak: 2KB/connection/message in `ws-handler.ts:145`
- Cause: Event listener not removed on disconnect
- Fixed: Added `cleanup()` call in `onClose` handler

### Generated Tests

#### 1. Reproduction Test (fails before fix)
```typescript
test('REPRODUCTION: memory grows unbounded without cleanup', async () => {
  const server = createTestServer();
  const client = connect(server);
  
  // Send 1000 messages
  for (let i = 0; i < 1000; i++) {
    client.send(JSON.stringify({ type: 'ping', seq: i }));
  }
  
  const memBefore = process.memoryUsage().heapUsed;
  await waitForMessages(client, 1000);
  const memAfter = process.memoryUsage().heapUsed;
  
  // Before fix: ~2MB growth
  // After fix: <50KB growth
  expect(memAfter - memBefore).toBeLessThan(50_000);
});
```

#### 2. Long-Running Stability Test
```typescript
test('STABILITY: 10k messages over 60s, no leak', async () => {
  const server = createTestServer({ messageLimit: 10000 });
  const client = connect(server);
  
  const snapshots = [];
  for (let batch = 0; batch < 10; batch++) {
    for (let i = 0; i < 1000; i++) {
      client.send(JSON.stringify({ type: 'data', batch, seq: i }));
    }
    await waitForMessages(client, 1000);
    global.gc(); // Force GC
    snapshots.push(process.memoryUsage().heapUsed);
  }
  
  // Memory should stabilize, not grow linearly
  const growth = snapshots[9] - snapshots[0];
  expect(growth).toBeLessThan(100_000); // <100KB over 10k msgs
});
```

#### 3. Concurrent Connections Test
```typescript
test('CONCURRENT: 100 connections, 100 msgs each', async () => {
  const server = createTestServer();
  const clients = Array(100).fill(null).map(() => connect(server));
  
  await Promise.all(clients.map((c, i) => 
    Promise.all(Array(100).fill(null).map((_, j) => 
      c.send(JSON.stringify({ conn: i, seq: j }))
    ))
  ));
  
  await waitForAllMessages(clients, 100);
  
  global.gc();
  const mem = process.memoryUsage().heapUsed;
  expect(mem).toBeLessThan(50_000_000); // <50MB total
});
```

### Execution Results
```
$ pnpm test tests/regression/websocket-memory-leak.test.ts
✓ REPRODUCTION: memory grows unbounded without cleanup (would fail pre-fix)
✓ STABILITY: 10k messages over 60s, no leak
✓ CONCURRENT: 100 connections, 100 msgs each
✓ CLEANUP: listeners removed on disconnect
✓ ERROR HANDLING: cleanup on transport error

Duration: 78.4s
Memory peak: 42MB (stable)
```

### CI Integration
```yaml
# .github/workflows/regression.yml
- name: WebSocket Memory Regression
  run: |
    pnpm test tests/regression/websocket-memory-leak.test.ts
    # Fail if memory growth > threshold
    node scripts/check-memory-growth.js --threshold=100KB
```

### Verdict: ✅ REGRESSION PROTECTED
5 tests cover leak pattern, fix verification, stability, concurrency, error paths. Integrated in CI.

---

## Tips for Effective Use

1. **Define acceptance criteria first** — "What must pass for merge?"
2. **Ask for risk-based prioritization** — Critical paths first
3. **Request evidence format** — JSON + human report
4. **Use for agent code** — Always verify AI-generated code
5. **Baseline everything** — Compare against main branch