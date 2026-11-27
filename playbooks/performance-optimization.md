# Playbook: Performance Optimization

*Practical examples for the `performance-optimization` skill*

---

## Scenario 1: Slow API endpoint optimization (happy path)

**Trigger:** "Optimize the /api/reports endpoint — it's taking 2.5 seconds."

**Invocation:**
```
Profile and optimize src/api/reports.ts. Identify bottlenecks, refactor hot paths,
verify with before/after benchmarks. Target: reduce p95 latency by 40%.
```

**Execution Log:**
```
## Performance Optimization: /api/reports endpoint

### Baseline Profile (performance-profiler)
Environment: Node 20, staging DB
Baseline p95 latency: 2,450ms (5 iterations)
Top bottlenecks:
1. buildReportQuery (src/api/reports.ts:42) — 49% of time — N+1 queries
2. formatRow (src/api/reports.ts:78) — 22% of time — string concat in loop

### Optimization Plan
| Priority | Bottleneck | Refactor | Impact | Effort | Risk |
|----------|-----------|----------|--------|--------|------|
| P0 | buildReportQuery | Replace N+1 with batch query | ~45% | Moderate | Medium |
| P1 | formatRow | Array join instead of concat | ~16% | Trivial | Low |

### Applied Changes (with user approval)
1. src/api/reports.ts:42 — Replaced 300 individual queries with single JOIN query
2. src/api/reports.ts:78 — Replaced string concatenation with array + join

### Verification (before/after benchmarks)
| Metric | Before | After | Change |
|--------|--------|-------|--------|
| p95 latency | 2,450ms | 1,180ms | -52% |
| CPU per request | 850ms | 420ms | -51% |
| Memory per request | 85MB | 72MB | -15% |

Tests: all pass (47 tests). Typecheck: clean. No new bottlenecks detected.

Exit code: 0.
```

**Expected Output:**
Optimization report with baseline profile, bottleneck table, refactor plan, before/after benchmarks, and verification results.

---

## Scenario 2: No measurable improvement (failure case)

**Trigger:** "Optimize the helper utility in src/lib/utils.ts."

**Invocation:**
```
Profile src/lib/utils.ts and optimize any bottlenecks found.
```

**Execution Log:**
```
## Performance Optimization: src/lib/utils.ts

### Baseline Profile
- formatDate(): 2ms per call (negligible)
- validateInput(): 1ms per call (negligible)
- No function exceeds 5% of total time

### Analysis
No significant bottlenecks identified. All functions are already optimal.
The utility is not a performance hot path.

### Result
No optimizations applied. No measurable improvement possible.
Recommendation: Focus optimization efforts elsewhere (the reports endpoint at 2,450ms).

Exit code: 0 (no bottlenecks found, correctly reported).
```

**Expected Output:**
Report stating no bottlenecks found, no optimizations applied, with recommendation to focus elsewhere.

---

## Scenario 3: Optimization breaks tests (safety case)

**Trigger:** "Optimize the parser in src/lib/parser.ts. Apply changes after approval."

**Invocation:**
```
Profile src/lib/parser.ts. Recommend optimizations. Do NOT apply without approval.
```

**Execution Log:**
```
## Performance Optimization: src/lib/parser.ts

### Profile Results
- parseToken(): regex matching at src/lib/parser.ts:145 — 60% of time
- Recommendation: Precompile regex outside the loop

### Approval Gate
User approval requested. Decision: APPROVED — apply regex precompilation only.

### Applied Change
- src/lib/parser.ts: Moved regex instantiation outside parseToken() loop

### Verification
- Before: 2,100ms (avg of 5 runs)
- After: 1,350ms (avg of 5 runs) — 36% improvement
- Tests: ALL PASS (parser + integration tests)
- Typecheck: CLEAN
- Rollback state: recorded (pre-optimization git commit)

Exit code: 0.
```

**Expected Output:**
Report showing profile results, approval gate, applied change, before/after benchmarks, and verification.
