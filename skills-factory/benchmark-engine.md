# Skills Making Factory — Benchmark Engine

## Purpose
The benchmark-engine measures skill performance across multiple dimensions: accuracy, reliability, execution time, resource consumption, maintainability, and security. It provides the quantitative data for comparative evaluation.

## Responsibilities
- Measure skill execution time and resource consumption
- Track accuracy (percent of acceptance criteria met)
- Track reliability (success/failure rate across repetitions)
- Measure maintainability (diff size, code clarity, documentation completeness)
- Measure security compliance (no secret leakage, gate enforcement)
- Produce benchmark results for the testing-engine

## Inputs
- Skill to benchmark
- Test scenario and inputs
- Number of repetitions (min 3)
- Metric definitions and thresholds

## Outputs
- Benchmark results: skills-factory/laboratories/benchmark-results/<skill-name>/benchmark-results.json
- Performance metrics: execution time, memory usage, model calls, cost
- Reliability metrics: success rate, failure modes
- Security metrics: secret detection results, gate violations

## Procedure
1. **Configure Benchmark**: Set up the test scenario, inputs, and metric thresholds
2. **Execute Repetitions**: Run the skill min 3 times on the identical scenario
3. **Measure Metrics**: Record execution time, resource consumption, accuracy, reliability
4. **Check Security**: Scan outputs for secret values, verify approval gates were respected
5. **Assess Maintainability**: Evaluate code clarity, documentation completeness, diff size
6. **Aggregate Results**: Compute averages, variances, and confidence intervals
7. **Write Results**: Save benchmark results to benchmark-results directory

## Safety & Governance
- **No destructive benchmarking**: Do not run skills that modify production without approval
- **Isolated environment**: Benchmark in isolated copies/worktrees
- **No secret logging**: Benchmark outputs must not contain credentials

## Completion Criteria
- Min 3 repetitions completed for statistical stability
- All six metrics measured or explicitly marked N/A
- Statistical significance assessed
- Results saved in valid JSON format
