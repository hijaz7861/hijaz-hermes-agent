# Skills Making Factory — Discovery Engine

## Purpose
The discovery-engine scans the existing skills repository, maps all available skills, identifies their capabilities, dependencies, and gaps. It serves as the "Knowledge Discovery" layer of the factory.

## Responsibilities
- Scan all skills in skills/*/SKILL.md
- Map skill capabilities, categories, dependencies, and versions
- Identify capability gaps against the factory's target capability matrix
- Detect skill weaknesses and improvement opportunities
- Produce a discovery report for the skill-analyzer

## Inputs
- Path to skills directory (skills/)
- Registry file (skills/registry/skills-index.json)
- Dependency graph (skills/registry/skill-dependencies.json)
- Capability matrix requirements

## Outputs
- Discovery report: skills-factory/reports/discovery-report.json
- Skill inventory map: skills-factory/registry/skill-inventory.json
- Gap analysis: skills-factory/reports/gap-analysis.json

## Procedure
1. **Scan Skills**: Read all SKILL.md files in skills/*/
2. **Extract Metadata**: Parse YAML frontmatter (name, description, version, tags, dependencies)
3. **Map Capabilities**: Record what each skill can do (reads_code, runs_commands, modifies_code, spawns_agents, selects_models, creates_skills, produces_reports)
4. **Identify Dependencies**: Build the dependency graph from each skill's dependencies field
5. **Detect Gaps**: Compare current capabilities against the factory's target capability matrix
6. **Identify Weaknesses**: Flag skills with missing playbooks, outdated versions, or missing dependencies
7. **Generate Report**: Write discovery report, skill inventory, and gap analysis

## Safety & Governance
- **Read-only**: Discovery engine only reads existing files, never modifies them
- **No secrets**: Discovery reports exclude any secret values found in skill files

## Completion Criteria
- All 37+ existing skills are mapped in the inventory
- Gap analysis identifies at least 5 missing capability areas
- Discovery report is valid JSON
