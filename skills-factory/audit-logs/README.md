# Skills Making Factory — Audit Logs

## Purpose
The audit-logs directory maintains a complete, immutable audit trail of all factory operations: security scans, factory executions, quality decisions, and skill lifecycle transitions.

## Log Types

### security-scan-<skill-name>.json
Security engine scan results for each skill.

### factory-execution-<timestamp>.log
Log of each factory pipeline execution: components invoked, skills processed, decisions made.

### quality-decision-<timestamp>.json
Quality control decisions with rationale.

### lifecycle-transition-<timestamp>.json
Skill state transitions (experimental → production → deprecated → archived).

## Governance
- **Immutable**: Audit logs are never modified or deleted
- **Complete**: Every factory action is logged
- **No secrets**: Audit logs exclude credentials and secret values
