# Skills Making Factory — Research Engine

## Purpose
The research-engine researches relevant open-source implementations, technical documentation, and best practices for new skill designs. It ensures skills are built on verified engineering practices rather than assumptions.

## Responsibilities
- Research technical specifications for new skill domains
- Verify that proposed skill procedures align with industry best practices
- Document sources and references for each new skill design
- Cross-reference new skills against existing implementations

## Inputs
- Skill design proposal from skill-analyzer or combination-engine
- Target domain (e.g., "database reliability", "API governance")
- Required capabilities and constraints

## Outputs
- Research report: skills-factory/reports/research-report-<skill-name>.json
- Verified procedures: skills-factory/laboratories/prototypes/<skill-name>/research-notes.md
- Source citations and references

## Procedure
1. **Analyze Request**: Review the skill design proposal for domain, requirements, and constraints
2. **Research Domain**: Gather information on industry best practices, tools, and methodologies for the target domain
3. **Verify Procedures**: Confirm that each proposed step in the skill procedure is technically valid and achievable
4. **Document Sources**: Record all references, documentation URLs, and implementation examples
5. **Produce Research Report**: Document findings, verified procedures, and source citations

## Safety & Governance
- **No copyrighted code**: Research must not copy copyrighted implementations without respecting licenses
- **No secrets**: Research reports must not contain credentials or secret values
- **Verified only**: Only include procedures that have been verified as technically achievable

## Completion Criteria
- Research report produced with at least 3 verified sources
- All proposed skill procedures verified as achievable
- Source citations documented
