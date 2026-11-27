---
name: skill-comprehension-analyzer
description: Deeply analyzes skill content to understand intent, quality, completeness, and effectiveness. Evaluates skill procedures, safety gates, and completion criteria to assess how well a skill is designed and how effectively it can be executed.
version: 1.0.0
tags: [skill-comprehension, analysis, quality, effectiveness, intent, evaluation]
dependencies: [skill-reader, skill-analyzer, quality-control]
---

# Skill Comprehension Analyzer

## Objective
Deeply analyze skill content to understand intent, quality, completeness, and effectiveness. Evaluates skill procedures, safety gates, and completion criteria to assess how well a skill is designed and how effectively it can be executed by an agent or human.

## Trigger
- "Analyze skill X's quality and completeness"
- "Understand intent of skill Y"
- "Evaluate skill Z's safety gates and procedures"
- "Assess skill effectiveness and quality"

Anti-triggers: "Rewrite skill without analysis" / "Judge skill without reading" — those violate the comprehension-first principle.

## Inputs
- Skill file: SKILL.md to analyze
- Skill playbook: associated playbook for scenario verification
- Quality criteria: completeness, clarity, safety, testability, portability
- Comparison baseline: reference skills or standards (optional)

## Outputs
- Comprehension report: intent summary, quality score, completeness rating
- Procedure analysis: step clarity, decision points, tool references, actionable items
- Safety analysis: gate coverage, approval requirements, risk coverage
- Completion criteria analysis: observability, measurability, testability
- Quality issues: missing sections, vague language, unclear steps, missing gates
- Improvement recommendations: specific changes to improve skill quality
- Effectiveness score: overall rating (0-100) with breakdown

## Procedure
1. **Read skill structure** (skill-reader)
   - Parse frontmatter, sections, procedures, safety gates
   - Extract all skill content for analysis
   - Identify missing or incomplete sections

2. **Analyze intent**
   - Determine skill's primary purpose from description and trigger
   - Identify target audience and use cases
   - Determine skill boundaries (what it does and doesn't do)
   - Assess alignment between trigger and procedure

3. **Analyze procedure quality**
   - Evaluate step clarity: are steps specific and actionable?
   - Identify decision points: are conditional branches clear?
   - Check tool references: are all referenced tools available?
   - Assess step ordering: is the sequence logical?
   - Identify vague or ambiguous language

4. **Analyze safety gates**
   - Check for approval gates on destructive operations
   - Verify no-secret logging rules
   - Check privacy gate coverage
   - Verify failure mode coverage (BLOCKED, ERROR, etc.)
   - Assess rollback procedures

5. **Analyze completion criteria**
   - Check if criteria are observable and measurable
   - Verify criteria cover all procedure outcomes
   - Assess testability of criteria
   - Identify vague or untestable criteria

6. **Compare against quality standards**
   - Check against CONTRIBUTING.md validation checklist
   - Compare with high-quality reference skills
   - Identify deviations from standards

7. **Generate recommendations**
   - Specific changes to improve clarity, safety, completeness
   - Missing sections to add
   - Vague language to clarify
   - Additional safety gates to include

8. **Calculate effectiveness score**
   - Weight dimensions: completeness (30%), clarity (25%), safety (25%), testability (20%)
   - Produce overall score (0-100) with breakdown

9. **Report**
   - Produce comprehension report with scores, issues, recommendations

## Safety & Approval Gates
- **Read-only analysis**: Does not modify skill files
- **No secret logging**: Redacts any secrets found in skill content
- **Objective assessment**: Based on observable criteria, not opinion
- **No automated changes**: Analysis only, modifications require separate authorization

## Failure Handling
- Skill file unreadable → Report "cannot read skill," verify file access
- Missing frontmatter → Report "incomplete skill structure," list missing fields
- Unclear procedure → Mark sections as "unclear," recommend rewrite
- No safety gates → Flag as "critical gap," recommend immediate addition

## Completion Criteria
- Intent summary with purpose and boundaries
- Quality score with dimension breakdown
- Procedure analysis with clarity and tool references
- Safety analysis with gate coverage
- Completion criteria analysis with observability rating
- Improvement recommendations with specific changes
- Effectiveness score (0-100)
