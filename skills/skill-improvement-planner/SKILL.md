---
name: skill-improvement-planner
description: Plans improvements to existing skills based on comprehension analysis, pattern recognition, and quality assessment. Identifies specific changes needed and creates improvement plans with prioritized actions.
version: 1.0.0
tags: [skill-improvement, planning, enhancement, quality-improvement, skill-evolution]
dependencies: [skill-comprehension-analyzer, skill-pattern-recognizer, quality-control, evolution-engine]
---

# Skill Improvement Planner

## Objective
Plan improvements to existing skills based on comprehension analysis, pattern recognition, and quality assessment. Identifies specific changes needed and creates improvement plans with prioritized actions, estimated effort, and expected outcomes.

## Trigger
- "Plan improvements for skill X"
- "Identify improvements needed for skill Y"
- "Create improvement plan for skill Z"
- "Plan skill quality enhancements"

Anti-triggers: "Implement improvements without planning" / "Change skill without analysis" — those violate the plan-first principle.

## Inputs
- Skill to improve: SKILL.md file and playbook
- Comprehension analysis: results from skill-comprehension-analyzer
- Pattern analysis: results from skill-pattern-recognizer
- Quality assessment: results from quality-control or skill-benchmarker
- Improvement goals: specific areas to improve (clarity, safety, completeness, etc.)
- Constraints: time budget, approval requirements, backward compatibility

## Outputs
- Improvement plan: prioritized actions with descriptions, effort estimates, and expected outcomes
- Change list: specific changes to SKILL.md and playbook
- Priority ranking: actions ranked by impact and effort
- Risk assessment: risks of each change and mitigation strategies
- Rollback plan: how to revert changes if needed
- Success criteria: how to measure improvement success

## Procedure
1. **Analyze current skill** (skill-comprehension-analyzer)
   - Review comprehension analysis results
   - Identify quality gaps and improvement areas
   - Document current score and dimension breakdown

2. **Identify improvement opportunities**
   - Compare against quality standards (CONTRIBUTING.md checklist)
   - Compare against patterns from similar skills (skill-pattern-recognizer)
   - Identify missing sections, unclear language, missing safety gates
   - Identify outdated commands, tools, or references

3. **Prioritize improvements**
   - Rank by impact (how much quality improves) and effort (how hard to implement)
   - Critical: missing safety gates, unclear procedures, missing completion criteria
   - High: vague language, missing examples, unclear triggers
   - Medium: style improvements, additional examples, better formatting
   - Low: minor wording, cosmetic changes

4. **Design specific changes**
   - For each improvement: describe current state, proposed change, expected outcome
   - Identify exact text to add, modify, or remove
   - Estimate effort for each change (minutes/hours)
   - Identify dependencies between changes

5. **Create improvement plan**
   - Order changes by dependency and priority
   - Group related changes into phases
   - Estimate total effort
   - Identify approval requirements for each change

6. **Assess risks**
   - Identify changes that could reduce quality if done incorrectly
   - Identify changes that could break backward compatibility
   - Plan mitigation for each risk
   - Create rollback plan

7. **Define success criteria**
   - How to measure improvement (quality score increase, section completeness)
   - Validation steps (quality-control re-run, comprehension re-analysis)
   - Acceptance thresholds

8. **Report**
   - Produce improvement plan document with all actions, priorities, and criteria

## Safety & Approval Gates
- **Plan only**: Does not implement changes, only plans them
- **Approval required** before implementing any changes
- **Backward compatibility**: Changes must not break existing skill usage
- **Rollback plan**: Must include how to revert changes

## Failure Handling
- Skill not found → Report "skill not found," verify path
- No comprehension analysis → Report "no analysis available," run skill-comprehension-analyzer first
- No quality standards → Report "no standards available," use CONTRIBUTING.md checklist
- Cannot estimate effort → Mark as "unknown effort," recommend expert estimation

## Completion Criteria
- Improvement plan with prioritized actions
- Change list with specific text modifications
- Priority ranking with impact and effort estimates
- Risk assessment with mitigation strategies
- Rollback plan documented
- Success criteria defined
