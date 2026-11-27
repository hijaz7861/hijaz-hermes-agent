# Skills Making Factory — Factory Core

## Purpose
The factory-core is the central orchestration component of the Skills Making Factory. It coordinates all factory sub-components, manages the skill manufacturing pipeline, and ensures governance rules are followed.

## Responsibilities
- Route tasks to appropriate factory sub-components (discovery, analysis, generation, combination, testing, benchmarking, security, optimization, evolution, quality control)
- Track the lifecycle of each skill from discovery through production promotion
- Enforce factory governance rules (no overwriting production skills, no destructive operations without authorization, version history maintenance)
- Maintain the separation between experimental, production, deprecated, and archived libraries
- Generate factory status reports

## Inputs
- Skill manufacturing requests (new skill, improvement, combination, optimization)
- Existing skill inventory from skills/registry/skills-index.json
- Factory configuration from skills-factory/factory-config/
- Audit logs from skills-factory/audit-logs/

## Outputs
- Factory execution reports
- Skill lifecycle state transitions (experimental → production → deprecated → archived)
- Audit log entries
- Factory health metrics

## Procedure
1. **Receive Request**: Accept a skill manufacturing request with type (new/improve/combine/optimize/test), target skill(s), and acceptance criteria
2. **Validate Governance**: Check that the request does not violate factory rules (no destructive operations, no copyrighted code, no secrets)
3. **Route to Sub-components**: Dispatch to the appropriate factory engine based on request type
4. **Track Lifecycle**: Record the skill's state in the skills-factory/registry/
5. **Aggregate Results**: Collect outputs from all sub-components into a factory execution report
6. **Apply Quality Gate**: Only promote skills that pass quality-control to skills-factory/libraries/production/
7. **Update Registry**: Record the final state in skills-factory/registry/ and skills/registry/skills-index.json

## Safety & Governance
- **No destructive operations** without explicit user authorization
- **No overwriting** of working production skills with untested experiments
- **Version history** must be maintained for all changes
- **No secrets or credentials** in any factory file
- **Experimental and production libraries** must remain separate

## Completion Criteria
- All factory sub-components are operational
- Factory governance rules are enforced
- Skill lifecycle tracking is functional
- Audit logs are being written
