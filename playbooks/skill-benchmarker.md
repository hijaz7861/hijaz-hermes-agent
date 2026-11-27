# Playbook: Skill Benchmarker

*Practical examples for the `skill-benchmarker` skill*

---

## Scenario 1: Compare new skill vs. manual approach (happy path)

**Trigger:** "Benchmark the performance-profiler against manual profiling on the reports endpoint."

**Invocation:**
```
Benchmark performance-profiler vs. manual profiling.
Scenario: Profile src/api/reports.ts, identify top 3 bottlenecks.
Metrics: accuracy, time, completeness. 3 repetitions each.
```

**Execution Log:**
```
## Skill Benchmark: performance-profiler vs. Manual Profiling

### Evaluation Setup
- Original: Manual profiling (developer reads code, adds timers)
- New: performance-profiler skill
- Scenario: Profile src/api/reports.ts, identify top 3 bottlenecks
- Fixture: test-repo/ (sample Node.js API)
- Repetitions: 3 runs each
- Metrics: accuracy (% correct bottlenecks), time (wall clock), completeness (all hotspots found)

### Baseline Results (Manual Profiling)
| Run | Accuracy | Time (min) | Bottlenecks Found | Notes |
|-----|----------|------------|-------------------|-------|
| 1 | 67% | 18 | 2 of 3 | Missed N+1 query |
| 2 | 67% | 22 | 2 of 3 | Missed string concat |
| 3 | 100% | 15 | 3 of 3 | — |
| Average | 78% | 18.3 | 2.3 of 3 | High variance |

### New Skill Results (performance-profiler)
| Run | Accuracy | Time (min) | Bottlenecks Found | Notes |
|-----|----------|------------|-------------------|-------|
| 1 | 100% | 4 | 3 of 3 | All found, file:line provided |
| 2 | 100% | 5 | 3 of 3 | — |
| 3 | 100% | 4 | 3 of 3 | — |
| Average | 100% | 4.3 | 3 of 3 | Low variance |

### Comparison Matrix
| Metric | Manual | performance-profiler | Delta |
|--------|--------|---------------------|-------|
| Accuracy | 78% | 100% | +22% |
| Time (min) | 18.3 | 4.3 | -14 min (-77%) |
| Bottlenecks found | 2.3 | 3.0 | +0.7 |
| Variance | High | Low | — |
| Security | Pass | Pass | — |

### Result: ADOPT
performance-profiler outperforms manual profiling on all metrics:
- 22% higher accuracy
- 77% faster
- Consistent results (low variance)
- No security issues

Exit code: 0.
```

**Expected Output:**
Evaluation record with comparison matrix, deltas, and adopt/reject/iterate decision.

---

## Scenario 2: New skill has regression (reject case)

**Trigger:** "Benchmark the code-refactorer against manual refactoring on the orders module."

**Invocation:**
```
Benchmark code-refactorer vs. manual refactoring.
Scenario: Extract method from processOrder in src/billing/orders.ts.
Metrics: accuracy, test pass rate, behavior preservation.
```

**Execution Log:**
```
## Skill Benchmark: code-refactorer vs. Manual Refactoring

### Evaluation Setup
- Original: Manual refactoring (developer edits, runs tests)
- New: code-refactorer skill
- Scenario: Extract validateOrder, calculateTotal, persistOrder from processOrder
- Fixture: test-repo/ (billing module with 12 tests)
- Repetitions: 3 runs each

### Baseline Results (Manual Refactoring)
| Run | Test Pass Rate | Behavior Preserved | Time (min) |
|-----|---------------|-------------------|------------|
| 1 | 100% | Yes | 8 |
| 2 | 100% | Yes | 10 |
| 3 | 100% | Yes | 9 |
| Average | 100% | Yes | 9 |

### New Skill Results (code-refactorer)
| Run | Test Pass Rate | Behavior Preserved | Time (min) |
|-----|---------------|-------------------|------------|
| 1 | 83% | No | 6 |
| 2 | 100% | Yes | 7 |
| 3 | 83% | No | 6 |
| Average | 89% | Partial | 6.3 |

### Regression Details
- Run 1: Missing caller update in src/billing/jobs.ts → 2 tests fail
- Run 3: Same missing caller → 2 tests fail
- Root cause: code-refactorer missed one of 3 callers

### Comparison Matrix
| Metric | Manual | code-refactorer | Delta |
|--------|--------|-----------------|-------|
| Test pass rate | 100% | 89% | -11% |
| Behavior preserved | Yes | Partial | Regression |
| Time (min) | 9 | 6.3 | -2.7 (-30%) |
| Reliability | Consistent | Inconsistent | — |

### Result: REJECT
code-refactorer is faster but has a critical reliability regression (missed caller).
Must fix caller-discovery before adoption.

### Identified Weaknesses
- Caller discovery incomplete (missed src/billing/jobs.ts)
- No cross-file reference validation

### Improvements Required
1. Add cross-file caller analysis to refactor plan phase
2. Verify all references updated before reporting completion
3. Re-run benchmark after fix

Exit code: 1 (regression detected, reject decision).
```

**Expected Output:**
Evaluation record showing regression, adopt/reject/iterate decision, weaknesses, and required improvements.

---

## Scenario 3: Non-deterministic results (inconclusive case)

**Trigger:** "Benchmark skill-benchmarker itself on a simple task. Results vary between runs."

**Invocation:**
```
Benchmark skill-benchmarker's own measurement consistency.
Scenario: Run same benchmark twice, compare results.
Metric: result variance between runs.
```

**Execution Log:**
```
## Skill Benchmark: skill-benchmarker Consistency Test

### Evaluation Setup
- Skill: skill-benchmarker (self-benchmark)
- Scenario: Benchmark performance-profiler on reports endpoint (same as Scenario 1)
- Repetitions: 2 full benchmark cycles
- Metric: variance in accuracy and time measurements

### Cycle 1 Results
performance-profiler: Accuracy 100%, Time 4.3 min (avg of 3)

### Cycle 2 Results
performance-profiler: Accuracy 100%, Time 4.1 min (avg of 3)

### Variance Analysis
- Accuracy: 0% variance (consistent)
- Time: 0.2 min variance (4.7% relative) — acceptable
- Bottleneck identification: identical across both cycles

### Status: INCONCLUSIVE — but acceptable
Variance is within acceptable threshold (<10%).
skill-benchmarker produces consistent results for this scenario.

### Recommendation
For high-stakes evaluations, use 5+ repetitions to reduce variance further.
Document variance in all evaluation records.

Exit code: 0 (inconclusive but within thresholds).
```

**Expected Output:**
Variance analysis between benchmark cycles, consistency assessment, recommendations for repetition count.
