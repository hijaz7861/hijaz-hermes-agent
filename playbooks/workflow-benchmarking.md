# Playbook: Workflow Benchmarking

*Practical examples for the `workflow-benchmarking` skill*

---

## Scenario 1: Compare two workflow configurations (happy path)

**Trigger:** "Compare workflow A vs. workflow B on the bug-fix scenario."

**Invocation:**
```
Benchmark two bug-resolution workflows on issue #1847.
Workflow A: sequential (map → debug → review → test)
Workflow B: parallel (map → [debug, review] → test)
Metrics: accuracy, time, reliability. 3 repetitions each.
```

**Execution Log:**
```
## Workflow Benchmark: Bug Resolution Workflows

### Evaluation Setup
- Scenario: Fix payment reconciliation bug (#1847)
- Fixture: test-repo/ (billing module)
- Repetitions: 3 runs each
- Metrics: accuracy, reliability, execution time, resource use, maintainability, security

### Workflow A (Sequential)
| Run | Accuracy | Time (min) | Reliability | Security |
|-----|----------|------------|-------------|----------|
| 1 | 100% | 22 | Pass | Pass |
| 2 | 100% | 24 | Pass | Pass |
| 3 | 100% | 23 | Pass | Pass |
| Average | 100% | 23.0 | Pass | Pass |

### Workflow B (Parallel)
| Run | Accuracy | Time (min) | Reliability | Security |
|-----|----------|------------|-------------|----------|
| 1 | 100% | 14 | Pass | Pass |
| 2 | 100% | 13 | Pass | Pass |
| 3 | 100% | 15 | Pass | Pass |
| Average | 100% | 14.0 | Pass | Pass |

### Comparison Matrix
| Metric | Workflow A | Workflow B | Delta |
|--------|-----------|-----------|-------|
| Accuracy | 100% | 100% | 0% |
| Time (min) | 23.0 | 14.0 | -9 min (-39%) |
| Reliability | Pass | Pass | — |
| Security | Pass | Pass | — |

### Bottleneck Analysis
- Workflow A: sequential review waits for debug (8 min idle)
- Workflow B: debug and review run in parallel (saves 8 min)

### Result: ADOPT Workflow B
Same accuracy and security, 39% faster, no reliability regression.

Exit code: 0.
```

**Expected Output:**
Benchmarking report with comparison matrix, deltas, bottleneck analysis, and adopt/reject/iterate decision.

---

## Scenario 2: Regression in new workflow (reject case)

**Trigger:** "Benchmark the new parallel testing workflow."

**Invocation:**
```
Benchmark parallel testing workflow vs. sequential.
Scenario: test PR #234 (auth + billing changes).
```

**Execution Log:**
```
## Workflow Benchmark: Parallel vs. Sequential Testing

### Sequential (Baseline)
- Test pass rate: 100%
- Time: 12 min
- All gates passed

### Parallel (New)
- Test pass rate: 92% (flaky test in auth module)
- Time: 6 min
- Flaky test: auth/mfa.test.ts — intermittent timeout

### Regression Details
- Parallel execution caused test contention on shared DB connection
- 2 tests failed due to timeout, not logic errors

### Comparison Matrix
| Metric | Sequential | Parallel | Delta |
|--------|-----------|----------|-------|
| Test pass rate | 100% | 92% | -8% |
| Time (min) | 12 | 6 | -6 (-50%) |
| Reliability | Pass | Fail | Regression |

### Result: REJECT
Parallel workflow is faster but has reliability regression (flaky tests).
Must fix test isolation before adoption.

### Improvements Required
1. Fix test isolation (separate DB connections per test)
2. Add retry logic for flaky tests
3. Re-run benchmark after fix

Exit code: 1 (regression detected, reject decision).
```

**Expected Output:**
Benchmarking report showing regression, reject decision, weaknesses, and required improvements.

---

## Scenario 3: Non-deterministic results (inconclusive case)

**Trigger:** "Benchmark the same workflow twice. Results vary between runs."

**Invocation:**
```
Benchmark workflow consistency. Run same workflow twice, compare variance.
```

**Execution Log:**
```
## Workflow Benchmark: Consistency Test

### Cycle 1
- Accuracy: 100%
- Time: 23.0 min (avg of 3)

### Cycle 2
- Accuracy: 100%
- Time: 22.4 min (avg of 3)

### Variance Analysis
- Accuracy: 0% variance
- Time: 0.6 min variance (2.6% relative) — acceptable
- Findings identical across both cycles

### Status: INCONCLUSIVE but acceptable
Variance within threshold (<10%). Workflow produces consistent results.

### Recommendation
For high-stakes evaluations, use 5+ repetitions to reduce variance.

Exit code: 0 (consistent within acceptable variance).
```

**Expected Output:**
Variance analysis between benchmark cycles, consistency assessment, repetition recommendations.
