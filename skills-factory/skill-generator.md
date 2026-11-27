# Skills Making Factory — Skill Generator

## Purpose
The skill-generator manufactures new reusable skills with standardized documentation. It creates SKILL.md files following the repository's established conventions.

## Responsibilities
- Create new SKILL.md files with YAML frontmatter, Objective, Trigger, Procedure, Safety Gates, Failure Handling, Completion Criteria
- Create corresponding playbooks with 3 scenarios (normal, failure, safety)
- Register new skills in skills-factory/registry/ and skills/registry/skills-index.json
- Ensure all new skills pass the quality-control checklist before promotion

## Inputs
- Skill proposal from skill-analyzer or combination-engine
- Research notes from research-engine
- Factory skill template standards

## Outputs
- New SKILL.md: skills-factory/laboratories/prototypes/<skill-name>/SKILL.md
- New playbook: skills-factory/laboratories/prototypes/<skill-name>/playbook.md
- Registration entry: skills-factory/registry/pending-skills.json

## Procedure
1. **Review Proposal**: Review the skill proposal and research notes
2. **Create SKILL.md**: Write the skill file with all required sections (frontmatter, Objective, Trigger, Procedure, Safety & Approval Gates, Failure Handling, Completion Criteria)
3. **Create Playbook**: Write a playbook with normal case, failure case, and safety case scenarios
4. **Validate**: Check against the quality-control checklist
5. **Register**: Add to pending-skills.json for quality-control review
6. **Document**: Record the generation in skills-factory/audit-logs/

## Safety & Governance
- **No secrets**: Never include credentials, tokens, or secret values in generated skills
- **No copyrighted code**: Do not copy copyrighted implementations without license compliance
- **Standardized format**: All generated skills follow the same SKILL.md structure
- **Prototype first**: New skills start in laboratories/prototypes/ before promotion

## Completion Criteria
- SKILL.md contains all required sections
- Playbook has 3 scenarios (normal, failure, safety)
- Skill passes quality-control checklist
- Skill is registered in pending-skills.json
