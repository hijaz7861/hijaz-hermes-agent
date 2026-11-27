---
name: human-needs-analyst
description: Analyze human needs, requirements, and pain points to inform system design and skill development. Translates user needs into actionable requirements and acceptance criteria.
version: 1.0.0
tags: [human, needs, analysis, requirements, user-experience, understanding]
dependencies: [human-feedback-collector, codebase-intelligence]
---

# Human Needs Analyst

## Objective
Analyze human needs, requirements, and pain points to inform system design and skill development. Translates user needs into actionable requirements and acceptance criteria that reflect real human problems.

## Trigger
- "Analyze user needs for feature X"
- "Understand stakeholder requirements for system Y"
- "Identify pain points in workflow Z"
- "Translate user feedback into requirements"

Anti-triggers: "Define requirements without human input" / "Assume user needs without validation" — those violate the human-centered design principle.

## Inputs
- Human feedback: from human-feedback-collector or direct input
- User personas: roles, goals, contexts, constraints
- Current system: existing features, workflows, limitations
- Business goals: objectives, success metrics, constraints
- Context: industry, domain, regulatory environment

## Outputs
- Needs analysis report: identified needs, pain points, requirements
- User stories: formatted requirements with acceptance criteria
- Priority matrix: needs ranked by impact and urgency
- Gap analysis: current system vs. human needs
- Recommendations: features, improvements, or new skills needed

## Procedure
1. **Collect human needs** (human-feedback-collector)
   - Gather feedback about user needs, goals, and pain points
   - Identify user personas and their contexts
   - Document constraints: technical, regulatory, resource

2. **Analyze needs**
   - Categorize needs: functional, non-functional, emotional, social
   - Identify pain points: where current system fails users
   - Map needs to user personas and contexts
   - Prioritize by: frequency, impact, urgency, feasibility

3. **Translate to requirements**
   - Write user stories: "As a [persona], I want [goal] so that [benefit]"
   - Define acceptance criteria: observable, measurable conditions
   - Identify dependencies and constraints
   - Note edge cases and exceptions

4. **Gap analysis**
   - Compare current system features against identified needs
   - Identify unmet needs and over-served areas
   - Document gaps: missing features, poor usability, performance issues
   - Rank gaps by impact on user satisfaction

5. **Generate recommendations**
   - Recommend features, improvements, or new skills to address gaps
   - Prioritize by: user impact, implementation effort, alignment with goals
   - Document trade-offs and alternatives

6. **Verify**
   - Review requirements with stakeholders (if available)
   - Validate against business goals and constraints
   - Confirm acceptance criteria are observable and measurable

7. **Report**
   - Produce needs analysis report: needs, stories, priorities, gaps, recommendations

## Safety & Approval Gates
- **Human needs validated**: Requirements confirmed with users or representatives
- **No assumptions**: All needs backed by feedback or evidence
- **Accessibility considered**: Needs of users with disabilities included
- **Approval required** before acting on recommendations that change system behavior

## Failure Handling
- No human feedback → Report "no human input available," recommend user research
- Contradictory needs → Report conflict, recommend stakeholder resolution
- Needs out of scope → Document as "out of scope," recommend separate initiative
- Cannot validate → Mark as "unverified," recommend user testing

## Completion Criteria
- Needs analysis report with categorized needs and pain points
- User stories with acceptance criteria
- Priority matrix with impact and urgency rankings
- Gap analysis with specific recommendations
- No assumptions without evidence
