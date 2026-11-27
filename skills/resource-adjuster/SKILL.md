---
name: resource-adjuster
description: Dynamically adjust resource allocations (CPU, memory, storage, replicas) based on usage patterns, performance metrics, and cost targets. Optimizes resource utilization without service disruption.
version: 1.0.0
tags: [adjustment, resource, scaling, optimization, cpu, memory, replicas]
dependencies: [observability-instrumenter, performance-profiler, environment-provisioner]
---

# Resource Adjuster

## Objective
Dynamically adjust resource allocations (CPU, memory, storage, replicas) based on usage patterns, performance metrics, and cost targets. Optimizes resource utilization without service disruption through measured, incremental changes.

## Trigger
- "Adjust CPU allocation for service X"
- "Optimize memory usage in deployment Y"
- "Right-size resources based on usage patterns"
- "Adjust replica count based on load"

Anti-triggers: "Scale resources without measurement" / "Make drastic resource changes without testing" — those violate safety principles.

## Inputs
- Target resource: deployment, database, service, or component
- Current allocation: CPU, memory, storage, replicas
- Usage metrics: CPU utilization, memory usage, storage I/O, request rate
- Performance targets: response time, error rate, throughput
- Cost targets: monthly budget, cost per request
- Adjustment limits: min/max values, step size, cooldown period

## Outputs
- Adjustment plan: current → target values, rationale, expected impact
- Adjustment log: changes made, timestamps, before/after metrics
- Verification: service health maintained, performance targets met
- Cost impact: estimated monthly cost change

## Procedure
1. **Collect usage metrics** (observability-instrumenter)
   - Query CPU, memory, storage, and network metrics over time window
   - Identify peak, average, and minimum utilization
   - Record resource contention and throttling events

2. **Analyze performance** (performance-profiler)
   - Identify resource bottlenecks and underutilization
   - Correlate resource usage with performance metrics
   - Determine if resources are over- or under-provisioned

3. **Design adjustments**
   - Calculate target values based on utilization targets (e.g., 70% CPU target)
   - Determine adjustment step size and cooldown period
   - Assess risk: low (minor), medium (significant), high (drastic)

4. **Apply adjustments** (requires approval for production)
   - Apply smallest effective change first
   - Monitor service health during and after adjustment
   - One resource at a time
   - For high-risk adjustments, use canary deployment

5. **Verify**
   - Confirm service health checks pass
   - Verify performance targets met (latency, error rate)
   - Confirm cost impact within budget
   - Roll back if performance degrades

6. **Report**
   - Produce adjustment report: before/after values, metrics, cost impact, verification

## Safety & Approval Gates
- **Approval required** for production resource adjustments
- **Adjustment limits enforced**: min/max values, step size, cooldown
- **One resource at a time**: no batching unrelated adjustments
- **Rollback**: revert if performance degrades or errors increase
- **No drastic changes without canary testing**

## Failure Handling
- Metrics unavailable → Mark as "insufficient data," recommend monitoring setup
- Adjustment breaks service → Revert immediately, report, do not proceed
- Performance degrades → Roll back, investigate root cause
- Cannot determine target values → Mark as "manual review," do not guess

## Completion Criteria
- Adjustment plan with current → target values
- Each adjustment verified with service health maintained
- Performance targets met after adjustment
- Cost impact documented
- No service disruption
