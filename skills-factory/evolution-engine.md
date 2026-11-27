# Skills Making Factory — Evolution Engine

## Purpose
The evolution-engine drives the continuous improvement cycle (DISCOVER → ANALYZE → COMBINE → CREATE → TEST → COMPARE → IMPROVE → DOCUMENT → REPEAT). It ensures the factory itself and all skills evolve over time based on measured evidence.

## Responsibilities
- Track skill versions and improvement history
- Detect when skills need re-evaluation or improvement
- Trigger re-testing of skills when dependencies change
- Maintain the evolution log (skills-factory/registry/evolution-log.md)
- Coordinate the recursive self-improvement of the factory

## Inputs
- Quality control decisions
- Test results and benchmark results
- Security scan reports
- Factory performance metrics
- User feedback and new requirements

## Outputs
- Evolution log entries: skills-factory/registry/evolution-log.md
- Version bumps for skills
- Re-evaluation triggers: skills-factory/registry/re-evaluation-queue.json
- Improvement history: skills-factory/reports/improvement-history.json

## Procedure
1. **Collect Signals**: Gather quality decisions, test results, benchmark results, security scans
2. **Detect Improvement Opportunities**: Identify skills that need updates based on test results, new requirements, or dependency changes
3. **Version Skills**: Bump versions according to semantic versioning (MAJOR for breaking, MINOR for new capability, PATCH for clarification)
4. **Trigger Re-evaluation**: Add skills to re-evaluation queue when dependencies change
5. **Log Evolution**: Write evolution log entries with version, changes, rationale
6. **Coordinate Recursive Improvement**: Feed factory improvements back into the factory components themselves

## Safety & Governance
- **Version history preserved**: All skill versions maintained for rollback capability
- **No destructive version changes**: MAJOR version bumps require explicit authorization
- **Evidence-based**: All evolution decisions backed by test evidence

## Completion Criteria
- Evolution log updated with all changes
- Version history maintained for all skills
- Re-evaluation queue processed
- Improvement history documented
