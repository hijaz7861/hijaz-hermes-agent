# Skills Making Factory — Quality Control

## Purpose
The quality-control component enforces quality gates before skills are promoted from experimental to production. It validates skills against the factory quality checklist.

## Responsibilities
- Validate new skills against the quality-control checklist
- Approve or reject skills for production promotion
- Maintain the production skills library (skills-factory/libraries/production/)
- Reject skills that fail quality gates with documented reasons

## Inputs
- New skill from skill-generator or combination-engine
- Test results from testing-engine
- Benchmark results from benchmark-engine
- Security scan report from security-engine

## Outputs
- Quality decision: skills-factory/registry/quality-decisions.json
- Production skill: skills-factory/libraries/production/<skill-name>/SKILL.md
- Rejection report: skills-factory/reports/rejection-report-<skill-name>.json

## Procedure
1. **Review Checklist**: Check all quality-control items (frontmatter, required sections, playbook, tests, security, no secrets, no TODO/FIXME)
2. **Review Test Results**: Confirm testing-engine results show adopt decision
3. **Review Benchmark Results**: Confirm benchmark results show no critical regressions
4. **Review Security Scan**: Confirm security-engine passed with no critical findings
5. **Make Decision**: Approve (promote to production), Reject (document reasons), or Request Changes
6. **Record Decision**: Write quality decision to quality-decisions.json
7. **Promote or Reject**: Copy approved skills to libraries/production/, write rejection reports for rejected skills

## Quality Control Checklist
- [ ] YAML frontmatter: name, description, version, tags
- [ ] All required sections: Objective, Trigger, Procedure, Safety Gates, Failure Handling, Completion Criteria
- [ ] Playbook created with 3 scenarios (normal, failure, safety)
- [ ] No TODO, FIXME, or placeholder commands
- [ ] All referenced tools/commands verified or marked as examples
- [ ] Approval gates for destructive operations
- [ ] No secret logging or printing
- [ ] Privacy gates for data classification
- [ ] Failure modes include BLOCKED for gates
- [ ] Completion criteria are observable
- [ ] Distinguishes verified vs hypothesized vs not-run

## Safety & Governance
- **No promotion without quality pass**: Skills cannot enter production without passing quality control
- **No overwriting production**: Cannot replace a working production skill without authorization
- **Documented decisions**: All quality decisions recorded with rationale

## Completion Criteria
- Quality decision recorded for every submitted skill
- Approved skills copied to libraries/production/
- Rejected skills documented with reasons
- Quality decisions registry updated
