---
name: skill-documentation-enhancer
description: Enhances skill documentation by improving clarity, adding examples, clarifying procedures, and strengthening safety gates. Based on improvement plans, applies documentation improvements while maintaining skill integrity.
version: 1.0.0
tags: [skill-documentation, enhancement, clarity, examples, safety-gates, documentation-improvement]
dependencies: [skill-improvement-planner, skill-reader, skill-generator]
---

# Skill Documentation Enhancer

## Objective
Enhance skill documentation by improving clarity, adding examples, clarifying procedures, and strengthening safety gates. Applies improvement plans to skill documentation while maintaining skill integrity and following repository conventions.

## Trigger
- "Enhance documentation for skill X"
- "Improve clarity of skill Y's procedures"
- "Add examples to skill Z's playbook"
- "Strengthen safety gates in skill documentation"

Anti-triggers: "Change skill behavior without analysis" / "Modify skill without improvement plan" — those require separate skill-improvement-planner and quality-control steps.

## Inputs
- Skill to enhance: SKILL.md file and playbook
- Improvement plan: from skill-improvement-planner with specific changes
- Enhancement scope: documentation only, examples only, safety gates only, or all
- Style guidelines: repository conventions and style preferences

## Outputs
- Enhanced SKILL.md: improved documentation with changes applied
- Enhanced playbook: improved scenarios with examples and execution logs
- Change log: all changes made with before/after comparison
- Verification results: validation that changes follow conventions
- Enhancement report: what was improved, effort spent, outcomes

## Procedure
1. **Review improvement plan** (skill-improvement-planner)
   - Understand planned changes and their rationale
   - Identify which changes are documentation-only vs. structural
   - Verify plan has been approved for implementation

2. **Read current skill** (skill-reader)
   - Parse current SKILL.md and playbook
   - Extract current content for before/after comparison
   - Document current state for change log

3. **Apply documentation improvements**
   - Clarify ambiguous language: rewrite unclear sentences
   - Add examples: illustrative examples for procedures and scenarios
   - Improve structure: better headings, formatting, readability
   - Strengthen safety gates: clearer approval requirements, more specific failure modes
   - Add missing sections: complete incomplete sections per improvement plan

4. **Apply playbook enhancements**
   - Improve scenario descriptions with more detail
   - Add realistic execution logs with tool output
   - Enhance expected output formats
   - Add failure and safety scenarios if missing

5. **Validate changes**
   - Check against CONTRIBUTING.md validation checklist
   - Verify frontmatter still valid
   - Verify all required sections present
   - Verify playbook has 3 scenarios (normal, failure, safety)
   - Verify no secrets introduced

6. **Produce change log**
   - Document all changes with before/after text
   - Record rationale for each change
   - Note any deviations from improvement plan

7. **Report**
   - Produce enhancement report: changes made, effort, validation results

## Safety & Approval Gates
- **Implementation only of approved plans**: Does not create new changes, only implements approved plans
- **No secret logging**: Ensures no secrets introduced in documentation
- **Backward compatibility**: Changes must not break skill usage
- **Convention compliance**: All changes follow repository conventions

## Failure Handling
- No improvement plan → Report "no plan available," run skill-improvement-planner first
- Validation fails → Report validation issues, fix before completing
- Cannot apply change → Report specific change that failed, recommend manual review
- Skill file read-only → Report permission issue, request write access

## Completion Criteria
- Enhanced SKILL.md with all planned changes applied
- Enhanced playbook with improved scenarios
- Change log with all modifications documented
- Validation passed against CONTRIBUTING.md checklist
- No secrets introduced
- Enhancement report produced
