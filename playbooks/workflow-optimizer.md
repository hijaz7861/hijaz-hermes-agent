# Playbook: Workflow Optimizer

*Practical examples for the `workflow-optimizer` skill*

---

## Scenario 1: Optimize bug-fix workflow (happy path)

**Trigger:** "Optimize the bug-resolution workflow for speed."

**Invocation:**
```
Optimize the bug-resolution workflow on issue #1847.
Current: sequential (map → debug → review → test)
Target: reduce execution time by 30% without quality loss.
3 repetitions each.
```

**Execution Log:**
```
## Workflow Optimization: Bug Resolution Workflow

### Baseline (sequential)
| Run | Total Time | Map | Debug | Review | Test | Gate Wait |
|-----|-----------|-----|-------|--------|------|-----------|
| 1 | 23 min | 4 | 12 | 3 | 4 | 0 |
| 2 | 24 min | 4 | 13 | 3 | 4 | 0 |
| 3 | 23 min | 4 | 12 | 3 | 4 | 0 |
| Avg | 23.3 min | 4 | 12.3 | 3 | 4 | 0 |

### Bottleneck Analysis
- Debug (12.3 min) and Review (3 min) run sequentially — but they're independent
- Review can start as soon as map is done (doesn't depend on debug)
- Potential parallel savings: ~3 min

### Optimized Configuration (parallel)
DAG: map → [debug, review] → test
| Run | Total Time | Map | Debug | Review | Test | Gate Wait |
|-----|-----------|-----|-------|--------|------|-----------|
| 1 | 16 min | 4 | 12 | 3 (parallel) | 4 | 0 |
| 2 | 17 min | 4 | 13 | 3 (parallel) | 4 | 0 |
| 3 | 16 min | 4 | 12 | 3 (parallel) | 4 | 0 |
| Avg | 16.3 min | 4 | 12.3 | 3 | 4 | 0 |

### Comparison Matrix
| Metric | Original | Optimized | Delta |
|--------|----------|-----------|-------|
| Total time (min) | 23.3 | 16.3 | -7 min (-30%) |
| Accuracy | 100% | 100% | 0% |
| Reliability | Pass | Pass | — |

### Result: ADOPT
30% faster, no quality regression, statistical significance confirmed.

Exit code: 0.
```

**Expected Output:**
Optimization report with baseline, bottleneck analysis, optimized DAG config, before/after comparison matrix, and adopt/reject/iterate decision.

---

## Scenario 2: Optimization reduces quality (reject case)

**Trigger:** "Optimize the testing workflow to run faster."

**Invocation:**
```
Optimize the PR testing workflow to reduce time.
Current: full test suite (sequential)
Proposal: skip slow integration tests
```

**Execution Log:**
```
## Workflow Optimization: PR Testing Workflow

### Baseline (full suite)
| Metric | Value |
|--------|-------|
| Total time | 12 min |
| Test pass rate | 100% |
| Coverage | 87% |

### Optimized (skip integration tests)
| Metric | Value |
|--------|-------|
| Total time | 6 min |
| Test pass rate | 100% |
| Coverage | 62% (-25%) |

### Quality Regression Detected
- Coverage dropped from 87% to 62% (-25 percentage points)
- Integration test paths no longer covered
- Risk: regressions in integration boundaries undetected

### Result: REJECT
Optimization is faster but reduces coverage by 25%.
Quality gate not met — coverage threshold not maintained.

### Improvements Required
1. Parallelize test execution instead of skipping tests
2. Run integration tests in parallel with unit tests
3. Use test selection (only run affected tests)

Exit code: 1 (quality regression, reject decision).
```

**Expected Output:**
Optimization report showing quality regression, reject decision, and required improvements.

---

## Scenario 3: Non-deterministic results (inconclusive case)

**Trigger:** "Benchmark workflow consistency. Run same workflow twice."

**Invocation:**
```
Benchmark the same workflow configuration twice, compare variance.
Scenario: codebase mapping on test-repo/
```

**Execution Log:**
```
## Workflow Optimization: Consistency Test

### Cycle 1
- Total time: 23.3 min (avg of 3)
- Accuracy: 100%

### Cycle 2
- Total time: 22.8 min (avg of 3)
- Accuracy: 100%

### Variance Analysis
- Time variance: 0.5 min (2.1% relative) — acceptable
- Accuracy: 0% variance
- Bottleneck identification: identical across both cycles

### Status: CONSISTENT
Variance within acceptable threshold (<10%).
Workflow produces consistent results.

Exit code: 0.
```

**Expected Output:**
Variance analysis between workflow cycles, consistency assessment, repetition recommendations.
