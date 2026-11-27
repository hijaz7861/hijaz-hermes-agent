# Skills Making Factory — Registry

## Purpose
The registry directory maintains the factory's internal registries: skill inventory, quality decisions, pending submissions, and evaluation history.

## Files

### skill-inventory.json
Inventory of all skills known to the factory, with capabilities, dependencies, versions, and maturity levels.

### quality-decisions.json
Records of all quality-control decisions (approve/reject/request-changes) with rationale.

### pending-skills.json
New skills awaiting quality-control review.

### pending-combinations.json
New skill combinations awaiting quality-control review.

### evolution-log.md
Complete history of all skill versions, changes, and improvements.

## Governance
- **Registry is the source of truth**: All skill states tracked here
- **No unauthorized modifications**: Registry changes only through factory components
- **Version history preserved**: All changes recorded for auditability
