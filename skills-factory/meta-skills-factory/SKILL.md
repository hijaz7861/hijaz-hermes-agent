---
name: meta-skills-factory
description: Meta-skill that improves the Skills Making Factory itself. Analyzes factory performance, identifies improvements to factory components, creates better skill-manufacturing capabilities, and enables recursive self-improvement of the engineering ecosystem.
version: 1.0.0
tags: [meta, factory, self-improvement, factory-optimization, manufacturing-pipeline]
dependencies: [factory-core, evolution-engine, optimization-engine, quality-control, benchmark-engine, testing-engine]
---

# Meta-Skills Factory

## Objective
Improve the Skills Making Factory's own ability to manufacture better skills. The Meta-Skills Factory analyzes factory performance metrics, identifies weaknesses in factory components, proposes and tests factory improvements, and enables recursive self-improvement of the entire skills engineering ecosystem. It is part of the initial architecture (not a later add-on) to provide a path toward a continuously self-improving system.

## Trigger
- "Improve the factory's skill creation success rate"
- "Optimize the manufacturing pipeline"
- "Make the factory better at creating skills"
- "Meta-improvement: enhance factory components"

Anti-triggers: "Create a new individual skill" / "Fix a bug in a skill" — those are handled by the factory's regular components, not the meta-factory.

## Inputs
- Factory performance metrics (skill creation success rate, test pass rate, regression rate)
- Component performance data (testing-engine, benchmark-engine, quality-control results)
- Factory governance rule compliance data
- User feedback on factory-produced skills
- Existing factory component documentation (factory-core.md, discovery-engine.md, etc.)

## Outputs
- Factory improvement report: skills-factory/reports/factory-improvement-report.json
- Factory component improvements: updated factory-*.md files
- New factory capabilities: additional factory sub-components or enhanced existing ones
- Meta-evaluation: comparison of factory performance before/after improvements

## Procedure
### Phase 1: Measure Factory Performance
Collect factory performance metrics: skill creation success rate, test pass rate, regression rate, capability improvements, reusability, execution efficiency, security compliance, maintenance requirements. Establish a baseline by running the factory on standard skill creation tasks.

### Phase 2: Analyze Factory Weaknesses
Evaluate each factory component (discovery, analysis, generation, combination, testing, benchmarking, security, quality control). Detect components with high failure rates, slow execution, or poor output quality. Analyze the quality of skills produced by the factory. Prioritize factory improvements by impact.

### Phase 3: Design Factory Improvements
Propose specific changes to factory components to improve effectiveness. Design new factory sub-components that would improve skill manufacturing. Validate designs against factory governance rules.

### Phase 4: Implement and Test Improvements
Apply improvements to factory component documentation and configuration. Run testing-engine to verify improved factory still produces quality skills. Run benchmark-engine to measure before/after performance. Confirm no regression in skill quality.

### Phase 5: Promote and Document
Verify factory improvements pass quality control. Update factory component files with approved improvements. Record factory improvements in evolution log. Produce factory improvement report with before/after metrics.

## Safety & Approval Gates
- **Factory governance rules apply to itself**: The Meta-Skills Factory must follow the same governance rules it enforces (10 rules in skills-factory/factory-config/governance-rules.json)
- **No destructive factory changes**: Cannot modify factory-core or governance-rules without explicit authorization
- **Evidence-based**: All factory improvements backed by before/after performance measurements
- **Recursive improvement limit**: Avoid uncontrolled recursive creation; every factory iteration must have a measurable objective and quality threshold

## Failure Handling
- Factory improvement reduces skill quality → Revert factory changes, report regression
- Factory component fails after improvement → Rollback to previous component version
- Authorization denied → Stop, report findings only, no factory changes
- Insufficient test evidence → Mark improvement as "unverified," require testing

## Completion Criteria
- Factory improvement report produced with before/after metrics
- At least one factory component improved with evidence
- No regression in skill creation quality
- Factory governance rules still enforced after improvements
- Evolution log updated with factory improvement entries
