# Skills Making Factory — Combination Engine

## Purpose
The combination-engine combines existing skills (A + B + C = New Skill) to create integrated capabilities that none of the individual skills can provide alone. This implements the Skill Combination & Innovation Engine from the framework.

## Responsibilities
- Identify compatible skill combinations that produce new capabilities
- Design composite skill architectures combining 2+ existing skills
- Generate composite SKILL.md files and playbooks
- Document the combination rationale and expected synergy
- Test composite skills against their component skills

## Inputs
- Skill inventory from discovery-engine
- Capability gap analysis
- Combination proposals from skill-analyzer
- Factory combination matrix

## Outputs
- Composite SKILL.md: skills-factory/laboratories/prototypes/<composite-name>/SKILL.md
- Composite playbook: skills-factory/laboratories/prototypes/<composite-name>/playbook.md
- Combination rationale document: skills-factory/laboratories/prototypes/<composite-name>/combination-rationale.md
- Registration entry: skills-factory/registry/pending-combinations.json

## Procedure
1. **Identify Candidates**: Review skill inventory for complementary capabilities
2. **Design Combination**: Determine how skills A, B, C integrate to produce new capability
3. **Validate Synergy**: Confirm the combination produces something none of the components can do alone
4. **Create Composite Skill**: Write SKILL.md and playbook for the composite skill
5. **Document Rationale**: Record why this combination was chosen and what new capability it enables
6. **Register**: Add to pending-combinations.json for quality-control review

## Safety & Governance
- **No meaningless combinations**: Every combination must produce a distinct, reusable capability
- **Component attribution**: Composite skills must credit their component skills
- **No secrets**: Composite skills must not introduce secret handling beyond what components already do

## Completion Criteria
- Composite SKILL.md created with all required sections
- Combination rationale documented
- At least 2 component skills clearly integrated
- New capability identified that components cannot provide alone
