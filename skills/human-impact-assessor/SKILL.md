---
name: human-impact-assessor
description: Assess the human impact of system changes, skill deployments, and process modifications. Evaluates how changes affect users, teams, and stakeholders before implementation.
version: 1.0.0
tags: [human, impact, assessment, change-management, user-experience, understanding]
dependencies: [human-needs-analyst, human-feedback-collector, quality-control]
---

# Human Impact Assessor

## Objective
Assess the human impact of system changes, skill deployments, and process modifications. Evaluates how changes affect users, teams, and stakeholders before implementation to prevent negative consequences and ensure positive outcomes.

## Trigger
- "Assess human impact of change X"
- "Evaluate how deployment Y affects users"
- "Analyze stakeholder impact of process Z"
- "Assess human impact before releasing feature"

Anti-triggers: "Deploy without considering human impact" / "Assume no human impact" — those violate the human-centered safety principle.

## Inputs
- Proposed change: system modification, skill deployment, process modification
- Affected humans: users, teams, stakeholders, roles
- Current state: existing workflows, tools, processes
- Change details: what, when, how, who is affected
- Risk tolerance: acceptable disruption level

## Outputs
- Impact assessment: affected humans, impact type, severity, likelihood
- Risk matrix: impact vs. probability for each affected group
- Mitigation plan: actions to reduce negative impact
- Communication plan: who needs to know, when, what
- Go/no-go recommendation: proceed, proceed with mitigation, or delay

## Procedure
1. **Identify affected humans** (human-needs-analyst)
   - List all user roles, teams, and stakeholders affected
   - Document how each group uses the system/skill/process
   - Identify dependencies: who relies on whom

2. **Analyze impact types**
   - Workflow changes: new steps, removed steps, changed order
   - Skill requirements: new knowledge, new tools, retraining needed
   - Disruption: downtime, learning curve, temporary reduced productivity
   - Benefits: new capabilities, time savings, reduced errors
   - Risks: errors during transition, resistance, confusion

3. **Assess severity and likelihood**
   - Rate each impact: low, medium, high, critical
   - Assess probability: certain, likely, possible, unlikely
   - Plot on risk matrix: impact × probability

4. **Design mitigations**
   - Training: documentation, tutorials, hands-on sessions
   - Communication: announcements, FAQs, office hours
   - Phased rollout: pilot group, gradual expansion
   - Rollback: return to previous state if issues arise
   - Support: help desk, office hours, feedback channel

5. **Make recommendation**
   - Go: proceed with planned mitigations
   - Go with conditions: proceed only if specific mitigations completed
   - No-go: delay until impacts addressed
   - Document rationale for decision

6. **Verify**
   - Review assessment with affected stakeholders (if available)
   - Validate impact ratings against historical data
   - Confirm mitigation feasibility
   - Document assumptions and uncertainties

7. **Report**
   - Produce impact report: affected humans, risk matrix, mitigations, recommendation

## Safety & Approval Gates
- **Human impact considered**: No change deployed without impact assessment
- **Mitigation required**: High/critical impacts must have mitigations before deployment
- **Approval required** for changes with high/critical human impact
- **Rollback plan required**: Must be able to revert if impact exceeds expectations

## Failure Handling
- Affected humans unknown → Mark as "incomplete assessment," recommend stakeholder identification
- Impact cannot be assessed → Mark as "unknown," recommend pilot testing
- Stakeholders disagree → Document disagreement, recommend escalation
- No mitigation possible → Mark as "high risk," recommend delay

## Completion Criteria
- Impact assessment with affected humans and impact types
- Risk matrix with severity and likelihood
- Mitigation plan with specific actions
- Communication plan documented
- Go/no-go recommendation with rationale
