# Skills Making Factory — Libraries

## Purpose
The libraries directory maintains separate skill libraries by maturity level: production, experimental, deprecated, and archived.

## Subdirectories

### production/
Skills that have passed quality control and are approved for use in production workflows. These are the stable, verified skills.

### experimental/
Skills that are under development or testing. These may be promoted to production or moved to failed-tests.

### deprecated/
Skills that have been superseded by newer versions but are kept for reference and rollback capability.

### archived/
Skills that are no longer maintained but preserved for historical reference.

## Governance
- **Production skills are immutable without authorization**: Cannot be overwritten without explicit approval
- **Version history maintained**: All versions kept for rollback capability
- **Deprecated skills not deleted**: Preserved for reference
- **Promotion requires quality control**: Skills move from experimental → production only after passing quality-control
