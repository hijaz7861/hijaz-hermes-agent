---
name: skill-template-generator
description: Generates standardized skill templates (SKILL.md and playbook) based on analyzed patterns from existing skills. Creates new skill templates following repository conventions and best practices.
version: 1.0.0
tags: [skill-template, generation, standardization, SKILL.md, playbook, template-creation]
dependencies: [skill-reader, skill-pattern-recognizer, skill-generator]
---

# Skill Template Generator

## Objective
Generate standardized skill templates (SKILL.md and playbook) based on analyzed patterns from existing skills. Creates new skill templates following repository conventions, best practices, and discovered patterns.

## Trigger
- "Generate skill template for category X"
- "Create SKILL.md template based on pattern Y"
- "Generate playbook template for skill type Z"
- "Create standardized skill template"

Anti-triggers: "Create complete skill without human input" / "Generate skill without pattern analysis" — those require separate skill creation workflows, not template generation.

## Inputs
- Skill category: target category for the template
- Skill type: type of skill (reconnaissance, remediation, verification, etc.)
- Pattern source: existing skills to base template on (optional)
- Template scope: SKILL.md only, playbook only, or both
- Custom sections: additional sections to include (optional)

## Outputs
- SKILL.md template: frontmatter, Objective, Trigger, Procedure, Safety Gates, Failure Handling, Completion Criteria
- Playbook template: 3 scenarios (normal, failure, safety) with execution log format
- Pattern references: which patterns from which skills were used
- Template validation: confirmation that template follows repository conventions
- Usage instructions: how to fill in the template for a specific skill

## Procedure
1. **Analyze pattern source** (skill-pattern-recognizer)
   - Identify common patterns in target category
   - Extract common section structures and procedures
   - Identify common safety gates and failure modes
   - Extract common tags and dependencies for category

2. **Design template structure**
   - Create SKILL.md template with all required sections
   - Create playbook template with 3 scenario types
   - Include placeholder text with guidance for each section
   - Add pattern-based suggestions for each section

3. **Generate SKILL.md template**
   - YAML frontmatter with category-appropriate defaults
   - Objective section with placeholder and guidance
   - Trigger section with anti-trigger examples
   - Procedure section with numbered steps and decision point placeholders
   - Safety & Approval Gates section with category-appropriate gates
   - Failure Handling section with common failure modes
   - Completion Criteria section with observable criteria placeholders

4. **Generate playbook template**
   - Scenario 1: Normal case (happy path) with execution log
   - Scenario 2: Failure case with error handling
   - Scenario 3: Safety case with gate triggered
   - Each scenario: trigger, invocation, execution log, expected output

5. **Validate template**
   - Check against CONTRIBUTING.md validation checklist
   - Verify all required sections present
   - Verify frontmatter fields complete
   - Verify playbook has 3 scenarios

6. **Report**
   - Produce template generation report: template created, patterns used, validation results

## Safety & Approval Gates
- **Template only**: Does not create complete skills, only templates
- **No secret logging**: Templates include guidance to avoid secrets
- **Pattern-based**: Templates based on actual patterns, not assumptions
- **Convention-compliant**: Templates follow repository conventions

## Failure Handling
- No pattern source → Report "no pattern source," recommend skill inventory first
- Unknown category → Report "unknown category," recommend category analysis first
- Template validation fails → Report validation issues, recommend fixes
- No output directory → Report "no output directory," specify output path

## Completion Criteria
- SKILL.md template with all required sections
- Playbook template with 3 scenarios
- Pattern references documented
- Template validation passed
- Usage instructions provided
