---
name: production-environment-guardian
description: Protect production environments from unauthorized changes. Enforces change approval, monitors for drift, validates deployments, and provides emergency rollback capabilities.
version: 1.0.0
tags: [production, protection, governance, rollback, monitoring, safety]
dependencies: [release-coordinator, security-audit, observability-instrumenter]
---

# Production Environment Guardian

## Objective
Protect production environments from unauthorized changes. Enforces change approval, monitors for configuration drift, validates deployments, and provides emergency rollback capabilities to maintain production stability and security.

## Trigger
- "Protect production environment from changes"
- "Enforce production change approval process"
- "Monitor production for configuration drift"
- "Emergency rollback production deployment"

Anti-triggers: "Bypass production approval process" / "Make direct production changes without review" — those are strictly prohibited.

## Inputs
- Production environment: current state, configuration, deployed version
- Change requests: proposed changes, justification, rollback plan
- Approval workflow: approvers, escalation paths, time limits
- Monitoring data: logs, metrics, traces, health checks
- Rollback procedures: previous version, data migration reversal

## Outputs
- Change approval log: requests, decisions, approvers, timestamps
- Drift detection report: differences between expected and actual state
- Deployment validation: pre/post-deployment checks, pass/fail
- Rollback execution: triggered, completed, verified
- Production status report: health, recent changes, active alerts

## Procedure
1. **Establish protection rules**
   - Define change approval workflow (who can approve, what requires approval)
   - Define protected resources (databases, production services, security configs)
   - Define drift detection schedule and thresholds
   - Define rollback procedures and triggers

2. **Monitor for changes**
   - Track configuration changes (IaC, environment variables, secrets)
   - Track deployment changes (image tags, versions, feature flags)
   - Track infrastructure changes (scaling, networking, security groups)
   - Compare against expected state from version control

3. **Enforce change approval**
   - Review change requests against protection rules
   - Require approvals for protected resources
   - Log all decisions with approvers and timestamps
   - Block unauthorized changes

4. **Validate deployments**
   - Pre-deployment: verify tests pass, security scan clean, approval obtained
   - Post-deployment: verify health checks, error rates, performance
   - Rollback if validation fails

5. **Detect and respond to drift**
   - Compare actual state vs. expected state
   - Classify drift: intentional (approved change) vs. unintentional (drift)
   - Remediate unintentional drift
   - Report all drift findings

6. **Execute rollback (emergency)**
   - Trigger rollback on critical issues
   - Restore previous version and configuration
   - Verify rollback completion
   - Document incident and lessons learned

7. **Report**
   - Produce protection report: changes, approvals, drift, rollbacks, status

## Safety & Approval Gates
- **No production changes without documented approval**
- **Emergency rollback can be triggered by on-call without prior approval**
- **All production changes logged and auditable**
- **No direct production access** without break-glass procedure

## Failure Handling
- Approval workflow failure → Block change, escalate to manager
- Drift detection failure → Report, manual review required
- Deployment validation failure → Rollback automatically
- Rollback failure → Alert on-call, manual intervention required

## Completion Criteria
- Protection rules established and enforced
- All production changes logged with approvals
- Drift detection running and reporting
- Rollback procedures tested and documented
- Production status report available
