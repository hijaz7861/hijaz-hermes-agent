# Skills Making Factory

## Overview

The Skills Making Factory is an autonomous skills engineering ecosystem that transforms the existing HIJAZ Hermes skills collection into an evolving, self-improving engineering intelligence system. It implements the **DISCOVER → ANALYZE → COMBINE → CREATE → TEST → COMPARE → IMPROVE → DOCUMENT → REPEAT** cycle from the framework.

## Factory Architecture

### Core Components

| Component | Purpose |
|-----------|---------|
| **factory-core** | Central orchestration; coordinates all sub-components, manages skill lifecycle, enforces governance |
| **discovery-engine** | Scans existing skills, maps capabilities, identifies gaps |
| **research-engine** | Researches best practices, verifies procedures, documents sources |
| **skill-analyzer** | Analyzes skill quality, detects gaps, proposes improvements |
| **skill-generator** | Manufactures new skills with standardized documentation |
| **combination-engine** | Combines existing skills (A+B+C=New) for integrated capabilities |
| **testing-engine** | Tests new skills against originals, comparative evaluation |
| **benchmark-engine** | Measures performance across 6 metrics |
| **security-engine** | Security checks: no secrets, approval gates, privacy |
| **optimization-engine** | Improves existing skills based on benchmark results |
| **evolution-engine** | Continuous improvement cycle, version tracking |
| **quality-control** | Quality gates before production promotion |
| **meta-skills-factory** | Improves the factory itself (recursive self-improvement) |

### Directory Structure

```
skills-factory/
├── factory-core.md              # Core orchestration
├── discovery-engine.md          # Skill scanning & gap detection
├── research-engine.md           # Best practice research
├── skill-analyzer.md            # Skill quality analysis
├── skill-generator.md           # New skill manufacturing
├── combination-engine.md        # Skill combination (A+B=C)
├── testing-engine.md            # Comparative testing
├── benchmark-engine.md          # Performance benchmarking
├── security-engine.md           # Security checks
├── optimization-engine.md       # Skill optimization
├── evolution-engine.md          # Continuous improvement
├── quality-control.md           # Quality gates
├── meta-skills-factory.md       # Factory self-improvement
├── laboratories/
│   ├── experiments/             # Volatile experiments
│   ├── prototypes/              # Candidates for production
│   ├── failed-tests/            # Failed skills (preserved)
│   └── benchmark-results/       # Test results
├── libraries/
│   ├── production/              # Approved production skills
│   ├── experimental/            # Under development
│   ├── deprecated/              # Superseded but kept
│   └── archived/                # Historical reference
├── registry/
│   ├── skill-inventory.json     # All known skills
│   ├── quality-decisions.json   # QC decisions
│   ├── pending-skills.json      # Awaiting QC review
│   ├── pending-combinations.json # Awaiting QC review
│   └── evolution-log.md         # Complete change history
├── reports/                     # Factory reports
├── audit-logs/                  # Immutable audit trail
└── factory-config/
    ├── factory-config.json      # Core configuration
    ├── governance-rules.json    # 10 factory rules
    └── capability-matrix.json   # Target capabilities
```

## Factory Governance Rules (10 rules)

1. Never overwrite a working production skill with an untested experiment.
2. Never delete original repository content without authorization.
3. Never copy copyrighted or restricted code without respecting its license.
4. Never introduce secrets or credentials into skill files.
5. Never claim a skill is tested without actual test evidence.
6. Maintain complete version history.
7. Keep experimental and production libraries separate.
8. Use isolated testing environments where possible.
9. Require authorization for destructive repository operations and external publication.
10. Ensure every production skill has documentation and reproducible tests.

## Factory Performance Metrics

- Skill creation success rate
- Test pass rate
- Regression rate
- Capability improvements
- Reusability
- Execution efficiency
- Security compliance
- Maintenance requirements

## Relationship to Existing Skills Repository

The factory operates alongside the existing `skills/` directory (37 skills) and `skills/registry/`. The factory's production library (`skills-factory/libraries/production/`) can promote skills to the main `skills/` directory after quality control approval.
