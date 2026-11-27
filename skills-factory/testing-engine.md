# Skills Making Factory — Testing Engine

## Purpose
The testing-engine tests all new skills against their original versions and relevant existing skills. It implements the Continuous Testing & Comparative Evaluation cycle from the framework.

## Responsibilities
- Execute new skills on identical scenarios as their original/predecessor versions
- Compare results across accuracy, reliability, execution time, resource consumption, maintainability, and security
- Detect regressions and improvements
- Generate comparative evaluation records

## Inputs
- New skill from skill-generator or combination-engine
- Original/predecessor skill (if improving an existing skill)
- Test scenario and fixture repository
- Metrics definitions (accuracy, reliability, time, resources, maintainability, security)

## Outputs
- Test results: skills-factory/laboratories/benchmark-results/<skill-name>/test-results.json
- Comparative evaluation: skills-factory/registry/evaluation-history.json entries
- Regression report: skills-factory/reports/regression-report-<skill-name>.json

## Procedure
1. **Establish Baseline**: Run the original/predecessor skill on the test scenario
2. **Run New Skill**: Run the new skill on the identical scenario and inputs
3. **Compare Results**: Build comparison matrix (skill × metric × value)
4. **Compute Deltas**: Calculate new − baseline for each metric
5. **Assess Significance**: Run multiple repetitions (min 3) for statistical stability
6. **Detect Regressions**: Flag any metric where the new skill underperforms
7. **Record Evaluation**: Write evaluation record to evaluation-history.json
8. **Determine Outcome**: Adopt / Reject / Iterate based on results

## Safety & Governance
- **No destructive testing**: Do not run skills that modify production or spend money without explicit approval
- **Identical scenario**: Both skills must run on the exact same scenario and inputs
- **No secrets**: Test outputs must not contain credentials
- **Read-only by default**: Test in isolated copies/worktrees

## Completion Criteria
- Both skills run on identical scenario with identical inputs
- All six metrics measured (accuracy, reliability, time, resources, maintainability, security)
- Winner determination (adopt/reject/iterate) with evidence
- Security and safety findings recorded
