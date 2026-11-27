---
name: skill-benchmarker
description: Evaluate and compare skill performance against baselines. Measures accuracy, reliability, execution time, resource consumption, maintainability, and security. Required for the continuous testing and comparative evaluation cycle.
version: 1.0.0
tags: [evaluation, benchmarking, comparison, quality-assurance, metrics]
---

# Skill Benchmarker

## Objective
Run controlled comparisons between skills (old vs. new, or skill A vs. skill B) on identical scenarios. Produce reproducible evidence of which skill performs better across accuracy, reliability, speed, resource use, maintainability, and security.

## Trigger
- "Compare skill A vs. skill B on scenario X"
- "Benchmark the new performance-profiler against manual profiling"
- "Evaluate if skill X is better than its predecessor"
- "Run comparative evaluation of skills on task Y"
- "Measure skill performance regression after change"

Anti-triggers: "Declare skill X better without testing" / "Benchmark on unrepresentative synthetic data" — those violate the evidence-based principle.

## Inputs
- Skills to compare: names and versions
- Scenario: task description, repository/fixture, inputs, acceptance criteria
- Baseline: previous measurement or predecessor skill results
- Metrics: accuracy, reliability, execution time, resource consumption, maintainability, security
- Repetitions: number of runs for statistical stability

## Outputs
- Evaluation report: per-skill results, comparison matrix, statistical significance
- Winner determination: which skill performed better, on which metrics
- Regression detection: where the new skill underperforms
- Recommendation: adopt, reject, or iterate

## Procedure
1. **Define the evaluation**
   - Select skills and versions to compare.
   - Define the scenario: exact task, inputs, expected outputs, acceptance criteria.
   - Select metrics and measurement methods for each.
   - Set repetitions (min 3 runs per skill per scenario for stability).
   - Define pass/fail thresholds per metric.

2. **Establish baseline**
   - Run the predecessor/original skill on the scenario.
   - Record all metrics: accuracy (% criteria met), reliability (success/fail), time (wall clock), resources (memory, calls), maintainability (diff size, clarity), security (secret exposure, gate compliance).
   - Archive baseline results as reference.

3. **Run the new skill**
   - Run the candidate skill on the identical scenario and inputs.
   - Record all metrics using the same methods.
   - Ensure identical environment (same repo state, same dependencies).

4. **Compare results**
   - Build comparison matrix: skill × metric × value.
   - Compute deltas: new − baseline for each metric.
   - Assess statistical significance across repetitions.
   - Identify improvements (positive deltas) and regressions (negative deltas).

5. **Evaluate security & safety**
   - Check for secret exposure in outputs/logs.
   - Verify approval gates were respected.
   - Confirm no destructive actions without authorization.
   - Record safety findings as pass/fail/blocked.

6. **Determine outcome**
   - Adopt: new skill is better or equal on all critical metrics, no regressions.
   - Reject: new skill has critical regressions or safety issues.
   - Iterate: mixed results; improve new skill and re-benchmark.
   - Record decision with rationale and evidence.

7. **Report**
   - Write evaluation record: original skill, new skill, scenario, results, differences, weaknesses, improvements, final status.

## Safety & Approval Gates
- **No destructive benchmarking:** Do not run skills that modify production or spend money during benchmarks unless explicitly approved.
- **No secret logging:** Benchmark outputs must not contain credentials.
- **Read-only by default:** Benchmark in isolated copies/worktrees.

## Failure Handling
- Skill errors during benchmark → Record as failure, capture error, continue with other skills.
- Non-deterministic results → Increase repetitions, mark variance, do not declare winner on noisy data.
- Scenario not applicable to a skill → Mark as "not applicable," exclude from comparison.
- Baseline unavailable → Run skill once to establish baseline, mark as "initial measurement."

## Completion Criteria
- Evaluation record produced with all required fields.
- Both skills run on identical scenario with identical inputs.
- All six metrics measured (or explicitly marked N/A with justification).
- Winner determination (adopt/reject/iterate) with evidence.
- Security and safety findings recorded.
