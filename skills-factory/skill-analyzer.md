# Skills Making Factory — Skill Analyzer

## Purpose
The skill-analyzer analyzes existing skills for weaknesses, gaps, and improvement opportunities. It determines what new skills are needed and what existing skills need enhancement.

## Responsibilities
- Analyze skill quality, completeness, and test coverage
- Detect capability gaps not covered by existing skills
- Identify skills that need improvement (outdated, missing sections, weak procedures)
- Recommend new skill designs based on gap analysis
- Prioritize improvement opportunities

## Inputs
- Discovery report from discovery-engine
- Skill inventory from skills-factory/registry/skill-inventory.json
- Gap analysis from skills-factory/reports/gap-analysis.json
- Factory capability matrix requirements

## Outputs
- Skill analysis report: skills-factory/reports/skill-analysis-report.json
- Improvement recommendations: skills-factory/reports/improvement-recommendations.json
- New skill proposals: skills-factory/laboratories/prototypes/<skill-name>/proposal.md

## Procedure
1. **Review Discovery**: Analyze the discovery report for missing capabilities
2. **Assess Quality**: Evaluate each skill against the factory quality checklist (frontmatter, required sections, playbook, tests)
3. **Detect Gaps**: Identify capability areas with no existing skill coverage
4. **Prioritize**: Rank improvement opportunities by impact, feasibility, and urgency
5. **Propose**: Generate new skill proposals with name, purpose, dependencies, and procedure outline
6. **Report**: Write analysis report and improvement recommendations

## Safety & Governance
- **Read-only analysis**: Skill analyzer does not modify existing skills
- **Evidence-based**: All recommendations must cite specific evidence from discovery data

## Completion Criteria
- Analysis report produced with quality assessment for all skills
- At least 3 new skill proposals generated
- Improvement recommendations prioritized by impact
