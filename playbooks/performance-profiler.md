# Playbook: Performance Profiler

*Practical examples for the `performance-profiler` skill*

---

## Scenario 1: Slow API endpoint investigation (happy path)

**Trigger:** "The /api/reports endpoint is slow — profile it and find bottlenecks."

**Invocation:**
```
Profile src/api/reports.ts. Identify bottlenecks in the reports endpoint. 
Use the staging database with a representative query workload. 
Report top 5 bottlenecks with file:line and optimization recommendations.
```

**Execution Log:**
```
## Performance Profile: /api/reports endpoint

### Baseline Measurement
Environment: Node 20, staging DB, 10 concurrent requests
Baseline p95 latency: 2,450ms (5 iterations, std dev 120ms)
Baseline memory: 85MB peak per request

### Profiling Results
Tool: Node.js CPU profiler (`node --prof`), 30-second profile under load

Top 5 bottlenecks:
| # | Function | File:Line | Self Time | Total Time | Calls | % of Total |
|---|----------|-----------|-----------|------------|-------|------------|
| 1 | buildReportQuery | src/api/reports.ts:42 | 890ms | 1,200ms | 100 | 49% |
| 2 | formatRow | src/api/reports.ts:78 | 540ms | 540ms | 50,000 | 22% |
| 3 | fetchRelatedData | src/api/reports.ts:55 | 310ms | 420ms | 300 | 17% |
| 4 | serializeJSON | src/api/reports.ts:102 | 180ms | 180ms | 100 | 7% |
| 5 | dbConnectionPool.acquire | node_modules/pg | 90ms | 110ms | 100 | 4% |

### Bottleneck Analysis
1. **buildReportQuery (CRITICAL)** — N+1 query pattern: 300 separate queries for related data. Should use a single JOIN or batch fetch. Estimated savings: ~1,100ms (45%).
2. **formatRow (HIGH)** — String concatenation in a hot loop (50,000 iterations). Should use array join or template literals. Estimated savings: ~400ms (16%).
3. **fetchRelatedData (MEDIUM)** — No prepared statement; query re-parsed each call. Estimated savings: ~80ms (3%).

### Prioritized Recommendations
| Priority | Optimization | Impact | Effort | Risk |
|----------|-------------|--------|--------|------|
| P0 | Replace N+1 with batch query in buildReportQuery | ~45% latency reduction | Moderate | Medium |
| P1 | Optimize formatRow string building | ~16% latency reduction | Trivial | Low |
| P2 | Use prepared statements in fetchRelatedData | ~3% latency reduction | Trivial | Low |

### Verification (after P0 + P1 applied, with approval)
- p95 latency: 2,450ms → 1,180ms (52% improvement)
- Memory: 85MB → 72MB
- All existing tests pass
- No new bottlenecks detected

Exit code: 0.
```

**Expected Output:**
A performance report with baseline measurements, bottleneck table (file:line, metric, severity), prioritized recommendations with impact/effort/risk, and before/after benchmark verification.

---

## Scenario 2: Profiler unavailable (failure case)

**Trigger:** "Profile this Python module. cProfile is not installed."

**Invocation:**
```
Profile src/data/processor.py. Find bottlenecks. cProfile may not be available.
```

**Execution Log:**
```
## Performance Profile: src/data/processor.py

### Tool Check
- `cProfile`: not installed → unavailable
- `py-spy`: not installed → unavailable
- Fallback: Manual timing instrumentation with `time.perf_counter()`

### Manual Instrumentation Results
Instrumented: load_data(), transform(), validate(), save()

| Function | Avg Time (ms) | Calls | % of Total |
|----------|---------------|-------|------------|
| load_data | 1,200 | 1 | 48% |
| transform | 950 | 1 | 38% |
| validate | 300 | 1 | 12% |
| save | 50 | 1 | 2% |

### Limitations
- No per-line granularity (manual instrumentation only)
- No memory/allocation data
- No call-stack context
- Results marked as "approximate — profiler unavailable"

### Recommendations
1. Install `cProfile` or `py-spy` for detailed profiling
2. Investigate `load_data()` — likely I/O bottleneck (48% of time)
3. Investigate `transform()` — likely CPU bottleneck (38% of time)

Exit code: 0 (incomplete profile, clearly reported with limitations).
```

**Expected Output:**
A report stating profiling is incomplete due to missing tooling, providing approximate measurements from manual instrumentation, with clear limitations and next steps.

---

## Scenario 3: Optimization breaks tests (safety case)

**Trigger:** "Optimize the hot loop in src/lib/parser.ts. Apply changes after approval."

**Invocation:**
```
Profile src/lib/parser.ts. Recommend optimizations. Do NOT apply code changes without approval.
```

**Execution Log:**
```
## Performance Profile: src/lib/parser.ts

### Profiling Results
- parseToken(): 2,100ms total, 60% in regex matching at src/lib/parser.ts:145
- Suggested optimization: Precompile regex outside loop

### Approval Gate
User approval requested before applying code change.
Decision: APPROVED — apply regex precompilation only.

### Applied Change
- src/lib/parser.ts: Moved regex instantiation outside parseToken() loop

### Verification
- Before: 2,100ms (avg of 5 runs)
- After: 1,350ms (avg of 5 runs) — 36% improvement
- Test suite: ALL PASS (parser tests + integration)
- Typecheck: CLEAN
- No regressions detected

Exit code: 0.
```

**Expected Output:**
A report showing the optimization recommendation, the approval gate, before/after benchmarks, and verification that tests pass after the change.
