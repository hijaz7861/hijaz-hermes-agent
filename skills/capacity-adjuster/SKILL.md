---
name: capacity-adjuster
description: Adjust capacity planning parameters based on growth trends, usage forecasts, and resource constraints. Plans for future capacity needs and adjusts auto-scaling policies, quotas, and reservations.
version: 1.0.0
tags: [adjustment, capacity, planning, scaling, quotas, forecasting]
dependencies: [observability-instrumenter, resource-adjuster, environment-provisioner]
---

# Capacity Adjuster

## Objective
Adjust capacity planning parameters based on growth trends, usage forecasts, and resource constraints. Plans for future capacity needs and adjusts auto-scaling policies, quotas, and reservations to prevent outages and optimize costs.

## Trigger
- "Adjust auto-scaling policy for service X"
- "Tune capacity quotas for environment Y"
- "Plan capacity based on growth trends"
- "Adjust resource reservations based on forecasts"

Anti-triggers: "Scale capacity without growth data" / "Adjust quotas without usage analysis" — those violate measurement-first principles.

## Inputs
- Capacity parameter: auto-scaling thresholds, quotas, reservations, limits
- Current capacity and usage data
- Growth trends: usage increase over time, seasonal patterns
- Resource constraints: infrastructure limits, budget constraints
- Adjustment limits: min/max values, step size

## Outputs
- Adjustment plan: parameter, current → target, growth rationale
- Adjustment log: changes, timestamps, capacity impact
- Verification: capacity adequate for projected load, no outages
- Cost impact: estimated cost change from capacity adjustments

## Procedure
1. **Collect usage data** (observability-instrumenter)
   - Query resource usage trends over time
   - Identify growth patterns: linear, exponential, seasonal
   - Record peak usage and headroom

2. **Analyze capacity needs** (resource-adjuster)
   - Project future capacity based on growth trends
   - Identify constraints: infrastructure limits, budget
   - Calculate time-to-capacity exhaustion

3. **Design adjustments**
   - Calculate target values based on growth projections
   - Set auto-scaling thresholds with appropriate headroom
   - Adjust quotas and reservations to match projected needs
   - Document rollback values

4. **Apply adjustments** (requires approval for production)
   - Apply one capacity parameter change at a time
   - Monitor resource utilization after adjustment
   - Verify no outages or performance degradation
   - One change at a time

5. **Verify**
   - Confirm resource utilization within targets
   - Verify no outages or service degradation
   - Confirm cost impact within budget
   - Roll back if utilization exceeds targets or costs exceed budget

6. **Report**
   - Produce adjustment report: parameters, before/after values, capacity projections, cost impact

## Safety & Approval Gates
- **Approval required** for production capacity changes
- **Capacity gate**: adjustments verified with adequate headroom
- **One parameter at a time**: no batching unrelated changes
- **Rollback**: revert if utilization exceeds targets or outages occur
- **Budget constraint**: cost impact must be within approved budget

## Failure Handling
- Usage data unavailable → Mark as "insufficient data," recommend monitoring setup
- Adjustment causes outages → Revert immediately, report
- Cost exceeds budget → Roll back, report, request budget increase
- Cannot project growth → Mark as "manual review," do not guess

## Completion Criteria
- Adjustment plan with current → target values
- Each adjustment verified with adequate capacity headroom
- No outages or service degradation
- Cost impact within budget
- Rollback values documented
