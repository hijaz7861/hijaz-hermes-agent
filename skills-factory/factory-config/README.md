# Skills Making Factory — Factory Configuration

## Purpose
The factory-config directory contains configuration files that govern factory behavior, governance rules, and operational parameters.

## Files

### factory-config.json
Core factory configuration:
- Governance rules (no destructive operations, no secrets, version history, etc.)
- Quality control thresholds
- Benchmark repetition counts
- Security scan patterns
- Library promotion criteria

### governance-rules.json
The factory governance rules that all components must follow:
1. Never overwrite a working production skill with an untested experiment
2. Never delete original repository content without authorization
3. Never copy copyrighted or restricted code without respecting its license
4. Never introduce secrets or credentials into skill files
5. Never claim a skill is tested without actual test evidence
6. Maintain complete version history
7. Keep experimental and production libraries separate
8. Use isolated testing environments where possible
9. Require authorization for destructive repository operations and external publication
10. Ensure every production skill has documentation and reproducible tests

### capability-matrix.json
The factory's target capability matrix: what capabilities the skills ecosystem should cover.

## Governance
- **Configuration changes require review**: Changes to governance rules require explicit authorization
- **Factory-config is versioned**: All config changes tracked
