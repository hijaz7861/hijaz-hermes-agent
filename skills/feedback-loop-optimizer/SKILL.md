---
name: feedback-loop-optimizer
description: Optimize feedback loops between humans and systems for continuous improvement. Analyzes feedback collection, analysis, action, and measurement cycles to reduce latency and improve improvement velocity.
version: 1.0.0
tags: [human, feedback-loop, optimization, continuous-improvement, velocity, learning]
dependencies: [human-feedback-collector, evolution-engine, skill-benchmarker]
---

# Feedback Loop Optimizer

## Objective
Optimize feedback loops between humans and systems for continuous improvement. Analyzes feedback collection, analysis, action, and measurement cycles to reduce latency and improve improvement velocity.

## Trigger
- "Optimize feedback loop for feature X"
- "Improve improvement velocity for system Y"
- "Reduce time from feedback to action"
- "Optimize continuous improvement cycle"

Anti-triggers: "Skip feedback steps for speed" / "Make changes without measuring impact" — those violate the continuous improvement principle.

## Inputs
- Feedback loop stages: collection, analysis, action, measurement
- Current latency: time from feedback to action, action to measurement
- Improvement velocity: improvements per time period
- Bottlenecks: slow stages, manual steps, approval delays
- Measurement criteria: improvement rate, latency, cycle time

## Outputs
- Loop analysis: current cycle time, bottlenecks, improvement velocity
- Optimization plan: specific changes to speed up each stage
- Implemented changes: automated steps, reduced approvals, faster measurement
- Velocity metrics: improvements per week/month, cycle time reduction
- Recommendations: further optimizations, tooling needs

## Procedure
1. **Map feedback loop** (human-feedback-collector)
   - Document each stage: collect → analyze → act → measure
   - Identify participants and tools at each stage
   - Record current cycle times for each stage

2. **Identify bottlenecks**
   - Find slowest stages: collection delays, analysis backlog, approval delays
   - Identify manual steps that could be automated
   - Find approval gates that slow action
   - Document measurement gaps: missing metrics, slow reporting

3. **Design optimizations**
   - Automate collection: integrate with existing tools
   - Streamline analysis: templates, checklists, automated categorization
   - Reduce approvals: delegate authority, set SLA for approvals
   - Accelerate measurement: real-time dashboards, automated benchmarks

4. **Apply optimizations** (evolution-engine)
   - Implement one optimization at a time
   - Measure cycle time before and after
   - Verify improvement velocity increases
   - One optimization at a time

5. **Verify**
   - Measure cycle time: feedback to action, action to measurement
   - Count improvements: number of changes implemented per period
   - Verify quality: improvements don't introduce regressions
   - Roll back if velocity decreases or quality drops

6. **Report**
   - Produce optimization report: cycle times, velocity, changes made, recommendations

## Safety & Approval Gates
- **Quality gate**: optimizations must not reduce improvement quality
- **Approval required** for changing approval workflows
- **One optimization at a time**: no batching unrelated changes
- **Rollback**: revert if velocity decreases or quality drops
- **No skipping stages**: all feedback loop stages must remain

## Failure Handling
- Loop data unavailable → Mark as "insufficient data," recommend instrumentation
- Optimization slows loop → Revert immediately, report
- Cannot measure velocity → Mark as "inconclusive," recommend better metrics
- Approval bottleneck → Document, recommend delegation or SLA

## Completion Criteria
- Loop analysis with cycle times and bottlenecks
- Optimization plan with specific changes
- Velocity metrics before and after
- Quality maintained (no regressions)
- Recommendations for further optimization
