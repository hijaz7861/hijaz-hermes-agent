---
name: workflow-benchmarking
description: Benchmark multi-skill workflows — combining workflow orchestration with skill benchmarking to measure end-to-end workflow performance, compare workflow configurations, and identify optimization opportunities.
version: 1.0.0
tags: [benchmarking, orchestration, evaluation, workflow, performance]
dependencies: [workflow-orchestrator, skill-benchmarker]
---

# Workflow Benchmarking

## Objective
Combine workflow orchestration with skill benchmarking to execute and measure multi-skill workflows. Compares different workflow configurations on identical scenarios, measuring accuracy, reliability, execution time, resource consumption, and security to determine optimal workflow design.

## Trigger
- "Benchmark this workflow configuration"
- "Compare workflow A vs. workflow B on scenario X"
- "Measure end-to-end workflow performance"
- "Optimize multi-skill workflow execution"

Anti-triggers: "Run a workflow without measuring" / "Declare one workflow better without testing" — violates evidence-based evaluation.

## Inputs
- Workflow definitions to compare (DAGs, skill sequences, configurations)
- Scenario: task description, repository/fixture, inputs, acceptance criteria
- Metrics: accuracy, reliability, execution time, resource consumption, maintainability, security
- Repetitions: number of runs per workflow for statistical stability

## Outputs
- Workflow evaluation report: per-workflow results, comparison matrix
- Performance differences: deltas between workflow configurations
- Bottleneck identification: slow skills, sequential vs. parallel inefficiencies
- Recommendation: adopt, reject, or iterate workflow design

## Procedure
1. **Define the evaluation** (skill-benchmarker)
   - Select workflow definitions and versions to compare.
   - Define scenario: exact task, inputs, expected outputs, acceptance criteria.
   - Select metrics and measurement methods; set repetitions (min 3).

2. **Execute workflows** (workflow-orchestrator)
   - Run each workflow on the identical scenario and inputs.
   - Orchestrator manages skill dispatch, state, gates, and evidence collection.
   - Record all metrics per workflow run.

3. **Establish baseline** (skill-benchmarker)
   - Run the reference/original workflow first; archive as baseline.

4. **Compare results** (skill-benchmarker)
   - Build comparison matrix: workflow × metric × value.
   - Compute deltas; assess statistical significance.
   - Identify improvements and regressions.

5. **Identify bottlenecks**
   - Per-skill timing: which skills dominate execution time.
   - Sequential vs. parallel: opportunities for parallelization.
   - Gate wait times: human approval delays.

6. **Evaluate security & safety**
   - Check for secret exposure in workflow outputs/logs.
   - Verify approval gates were respected.
   - Record safety findings.

7. **Determine outcome**
   - Adopt/Reject/Iterate with rationale and evidence.
   - Record decision in evaluation history.

8. **Report**
   - Produce benchmarking report: original workflow, new workflow, scenario, results, differences, final status.

## Safety & Approval Gates
- **No destructive benchmarking:** Do not run workflows that modify production or spend money without explicit approval.
- **No secret logging:** Benchmark outputs must not contain credentials.
- **Read-only by default:** Benchmark in isolated copies/worktrees.

## Failure Handling
- Workflow errors → Record as failure, capture error, continue with other workflows.
- Non-deterministic results → Increase repetitions, mark variance.
- Baseline unavailable → Run once to establish baseline, mark as "initial measurement."
- Skill timeout within workflow → Record, attempt fallback, else mark blocked.

## Completion Criteria
- Evaluation record with all required fields.
- Both workflows run on identical scenario with identical inputs.
- All six metrics measured (or explicitly marked N/A).
- Winner determination (adopt/reject/iterate) with evidence.
- Security and safety findings recorded.
