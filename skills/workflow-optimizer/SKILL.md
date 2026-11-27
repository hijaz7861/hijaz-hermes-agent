---
name: workflow-optimizer
description: Optimize multi-skill workflows by combining workflow orchestration with skill benchmarking. Measures workflow performance, identifies bottlenecks (slow skills, sequential vs parallel inefficiencies, gate wait times), and recommends optimized workflow configurations.
version: 1.0.0
tags: [workflow, optimization, benchmarking, orchestration, performance]
dependencies: [workflow-orchestrator, skill-benchmarker]
---

# Workflow Optimizer

## Objective
Combine workflow orchestration with skill benchmarking to measure end-to-end workflow performance, identify bottlenecks, and recommend optimized workflow configurations. Every optimization is verified with before/after workflow execution.

## Trigger
- "Optimize this workflow for speed"
- "Find bottlenecks in workflow X"
- "Compare sequential vs parallel workflow configuration"
- "Reduce workflow execution time for scenario Y"

Anti-triggers: "Run a workflow without measuring" / "Declare one workflow better without testing" — violates evidence-based optimization.

## Inputs
- Workflow definition(s): DAG, skill sequences, configurations, gates
- Scenario: task description, repository/fixture, inputs, acceptance criteria
- Performance target: time, cost, reliability threshold
- Repetitions: runs per configuration for statistical stability

## Outputs
- Performance baseline: workflow execution time, per-skill timing, gate wait times
- Bottleneck analysis: slow skills, sequential vs parallel inefficiencies, resource contention
- Optimized workflow configuration: reordered nodes, parallelized branches, adjusted timeouts
- Before/after verification: execution results comparing original vs optimized

## Procedure
1. **Execute baseline workflow** (workflow-orchestrator)
   - Run the current workflow on the scenario.
   - Record: total time, per-skill execution time, per-skill cost, gate wait times, success/fail.
   - Run min 3 repetitions for stability.

2. **Benchmark skills individually** (skill-benchmarker)
   - Measure each skill's accuracy, reliability, time, resource consumption on the scenario.
   - Identify slow or unreliable skills.

3. **Identify bottlenecks**
   - Sequential chains: long sequences that could be parallelized.
   - Gate wait times: human approval delays.
   - Slow skills: skills exceeding time budget.
   - Resource contention: skills competing for same resources.

4. **Design optimized configuration**
   - Parallelize independent branches (fan-out/fan-in).
   - Reorder nodes to start long-running skills early.
   - Adjust timeouts and retry policies based on measured data.
   - Combine sequential dependent skills where safe.

5. **Execute optimized workflow**
   - Run the optimized configuration on the identical scenario.
   - Record same metrics as baseline.

6. **Compare results** (skill-benchmarker)
   - Build comparison matrix: original vs optimized × metric × value.
   - Compute deltas; assess statistical significance.
   - Verify no accuracy/reliability regression.

7. **Report**
   - Produce optimization report: baseline, bottlenecks, optimized config, before/after results, recommendation.

## Safety & Approval Gates
- **No destructive optimization:** Do not run workflows that modify production or spend money without explicit approval.
- **No secret logging:** Benchmark outputs must not contain credentials.
- **Read-only by default:** Optimize in isolated copies/worktrees.
- **Quality gate:** Optimization must not reduce accuracy or reliability.

## Failure Handling
- Workflow errors → Record as failure, capture error, continue with other configurations.
- Non-deterministic results → Increase repetitions, mark variance.
- Optimization reduces quality → Reject, report regression, revert to original.
- Baseline unavailable → Run original workflow first to establish baseline.

## Completion Criteria
- Optimization report with baseline and optimized results.
- All metrics measured for both configurations.
- Statistical significance assessed.
- Recommendation (adopt/reject/iterate) with evidence.
- No quality regression in optimized configuration.
- No secret values in output.
