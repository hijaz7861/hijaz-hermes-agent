---
name: deployment-environment-validator
description: Validate deployments before and after promotion to target environments. Ensures deployments meet quality gates, security requirements, and performance criteria before allowing traffic.
version: 1.0.0
tags: [deployment, validation, environment, promotion, gates, verification]
dependencies: [autonomous-testing, security-audit, quality-gate-review]
---

# Deployment Environment Validator

## Objective
Validate deployments before and after promotion to target environments. Ensures deployments meet quality gates, security requirements, and performance criteria before allowing traffic to reach the new version.

## Trigger
- "Validate deployment to staging environment"
- "Verify production deployment readiness"
- "Check deployment passes quality gates before promotion"
- "Validate post-deployment health in environment X"

Anti-triggers: "Deploy without validation" / "Skip quality gates for emergency deployment" — those violate deployment safety principles (except break-glass with documentation).

## Inputs
- Deployment artifact: container image, binary, or package
- Target environment: development, staging, production
- Quality gates: test coverage, lint, typecheck, security scan thresholds
- Performance criteria: latency, error rate, throughput thresholds
- Rollback criteria: conditions that trigger automatic rollback

## Outputs
- Pre-deployment validation: artifact scan, gate check, readiness report
- Post-deployment validation: health check, smoke test, performance check
- Deployment decision: approve, reject, or rollback
- Validation report: gates passed/failed, performance metrics, issues
- Rollback execution: triggered, completed, verified (if needed)

## Procedure
1. **Validate deployment artifact** (autonomous-testing)
   - Scan artifact for vulnerabilities and secrets
   - Verify artifact signature and integrity
   - Check artifact against approved build
   - Verify dependencies and versions

2. **Run pre-deployment quality gates** (quality-gate-review)
   - Run test suite: unit, integration, end-to-end
   - Run lint, typecheck, build
   - Run security scan: dependencies, SAST, secrets
   - Verify coverage threshold met

3. **Deploy to target environment**
   - Execute deployment (rolling, blue-green, or canary)
   - Monitor deployment progress
   - Capture deployment metrics (time, errors, rollbacks)

4. **Run post-deployment validation** (autonomous-testing + observability-instrumenter)
   - Health checks: service endpoints responding
   - Smoke tests: critical user journeys
   - Performance checks: latency, error rate, throughput
   - Observability: logs, metrics, traces normal

5. **Make deployment decision**
   - Approve: all gates passed, health checks green
   - Reject: gates failed, do not promote
   - Rollback: post-deployment issues detected, revert to previous version

6. **Report**
   - Produce validation report: gates, health checks, performance, decision

## Safety & Approval Gates
- **Production deployment requires manual approval** after validation
- **Quality gates cannot be bypassed** without documented break-glass
- **Rollback is automatic** on critical post-deployment failures
- **All deployment decisions logged** with rationale

## Failure Handling
- Pre-deployment gate failure → Block deployment, report failures, do not proceed
- Post-deployment health check failure → Trigger rollback, report, investigate
- Performance degradation → Rollback if above threshold, report
- Security scan failure → Block deployment, report vulnerabilities

## Completion Criteria
- Pre-deployment validation completed with results
- Post-deployment validation completed with results
- Deployment decision documented (approve/reject/rollback)
- Rollback executed if needed (with verification)
- No secret values in output
