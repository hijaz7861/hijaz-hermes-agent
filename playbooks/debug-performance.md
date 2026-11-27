# Playbook: Debug Performance

*Practical examples for the `debug-performance` skill*

---

## Scenario 1: Slow endpoint debug and fix (happy path)

**Trigger:** "Debug why /api/reports is slow — reproduce, diagnose, fix, benchmark."

**Invocation:**
```
Debug the /api/reports performance issue. Reproduce the slowness,
find root cause, apply fix, verify with before/after benchmarks.
Target: p95 latency under 1 second.
```

**Execution Log:**
```
## Debug Performance: /api/reports endpoint

### Capture the failure (autonomous-debugging)
- Observed: p95 latency 2,450ms, target <1,000ms
- Reproduction: 10 concurrent requests to /api/reports with large dataset
- Deterministic: Yes, reproduces every time

### Performance baseline (performance-profiler)
- Top bottleneck: buildReportQuery (src/api/reports.ts:42) — 49% of time
- Root cause: N+1 query pattern (300 separate queries for related data)

### Hypotheses confirmed
1. N+1 queries in buildReportQuery — CONFIRMED by profiler
2. String concatenation in formatRow — CONFIRMED (secondary, 22%)

### Fix applied (autonomous-debugging)
- src/api/reports.ts:42 — Replaced N+1 queries with single batch JOIN query

### Regression test added
- tests/performance/reports.test.ts: "batch query replaces N+1"
  - Fails before fix (2,450ms), passes after (1,180ms)

### Verification (performance-profiler)
| Metric | Before | After |
|--------|--------|-------|
| p95 latency | 2,450ms | 1,180ms |
| Queries per request | 301 | 1 |

- Full test suite: PASS (89 tests)
- Typecheck: CLEAN
- No regressions

Exit code: 0.
```

**Expected Output:**
Debug report with reproduction evidence, root cause, fix, before/after benchmarks, regression test, and verification.

---

## Scenario 2: Cannot reproduce (failure case)

**Trigger:** "Debug intermittent slowness in the billing job."

**Invocation:**
```
Debug the intermittent billing job slowness. It happens occasionally at 2AM.
```

**Execution Log:**
```
## Debug Performance: billing job intermittent slowness

### Capture the failure
- Observed: billing job occasionally takes 30+ minutes (normal: 5 minutes)
- Time: occurs at 2AM, intermittent (1 in 10 runs)
- Reproduction: NOT deterministic — cannot reproduce on demand

### Hypotheses (labeled as unconfirmed)
1. Stripe API rate limiting at 2AM (other jobs running) — UNCONFIRMED
2. Database connection pool exhaustion — UNCONFIRMED
3. Large data volume on certain days — UNCONFIRMED

### Performance profiling
- Profiled during normal run: 5 minutes, no bottlenecks
- Cannot profile during slow run (not reproducible)

### Status
- Cannot reproduce deterministically
- Continuing with labeled hypotheses only
- Recommendation: Add structured logging to capture next occurrence

Exit code: 0 (investigation ongoing, hypotheses documented, no fix applied).
```

**Expected Output:**
Report stating non-reproducible issue, labeled hypotheses, profiling results from normal run, and recommendations for capturing next occurrence.

---

## Scenario 3: Fix breaks tests (safety case)

**Trigger:** "Fix the memory leak in the WebSocket handler. Apply after approval."

**Invocation:**
```
Debug WebSocket memory leak. Reproduce, find root cause, apply fix.
Request approval before applying code changes.
```

**Execution Log:**
```
## Debug Performance: WebSocket memory leak

### Reproduction
- Simulated 10,000 WebSocket connections
- Memory growth: 2KB per message (confirmed leak)
- Root cause: Missing cleanup in onClose handler (src/ws/handler.ts:88)

### Approval Gate
Decision: APPROVED — apply fix only.

### Fix Applied
- src/ws/handler.ts:88 — Added connection cleanup in onClose handler

### Verification (performance-profiler)
- Before: 2KB/message memory growth
- After: <10 bytes/message — leak fixed
- Regression test: added (fails before, passes after)
- Full test suite: PASS
- No regressions

Exit code: 0.
```

**Expected Output:**
Report with reproduction evidence, root cause, approval gate status, fix, before/after memory benchmarks, regression test, and verification.
