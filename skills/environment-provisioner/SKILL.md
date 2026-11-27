---
name: environment-provisioner
description: Provision development, staging, testing, and production environments with consistent configuration. Creates isolated environments matching production specifications.
version: 1.0.0
tags: [environment, provisioning, dev, staging, production, infrastructure]
dependencies: [codebase-intelligence, observability-instrumenter]
---

# Environment Provisioner

## Objective
Provision consistent, isolated environments (development, staging, testing, production) that match production specifications. Every environment is created from infrastructure-as-code definitions, ensuring reproducibility and preventing configuration drift.

## Trigger
- "Provision a development environment"
- "Create staging environment matching production"
- "Set up test environment for PR #X"
- "Provision production environment for release vX.Y.Z"

Anti-triggers: "Modify production environment directly" / "Manually configure environment" — those bypass IaC and violate consistency principles.

## Inputs
- Environment type: development, staging, testing, production
- Infrastructure definition: Terraform, CloudFormation, or similar IaC templates
- Environment variables and secrets (redacted)
- Resource limits: compute, memory, storage, network
- Target platform: AWS, GCP, Azure, local, Kubernetes

## Outputs
- Provisioned environment with connection details
- Environment configuration snapshot
- Resource inventory: compute, storage, network, services
- Provisioning log: time, resources created, costs
- Verification: health checks passed, environment ready

## Procedure
1. **Validate infrastructure definition** (codebase-intelligence)
   - Read IaC templates (Terraform, CloudFormation, etc.)
   - Validate template syntax and resource definitions
   - Identify required providers, modules, and dependencies
   - Check for hardcoded secrets or credentials

2. **Plan provisioning**
   - Calculate required resources based on environment type
   - Development: minimal resources, cost-optimized
   - Staging: production-like, full feature set
   - Testing: ephemeral, tear-down after use
   - Production: high availability, monitoring, backups

3. **Apply infrastructure** (requires approval for production)
   - Run `terraform apply` or equivalent
   - Create resources in dependency order
   - Apply environment-specific configuration
   - Configure networking, security groups, access controls

4. **Configure environment**
   - Set environment variables (secrets redacted)
   - Configure service endpoints and connections
   - Apply observability instrumentation (logs, metrics, tracing)
   - Configure health checks and readiness probes

5. **Verify environment**
   - Run health checks on all services
   - Verify connectivity between components
   - Confirm observability is working
   - Document environment endpoints and credentials (redacted)

6. **Report**
   - Produce provisioning report: environment details, resources, costs, verification results

## Safety & Approval Gates
- **Approval required** for production environment provisioning
- **No secrets in output**: Credentials and keys redacted from all reports
- **Read-only for development/staging**: No production data in non-production environments
- **Rollback plan**: Document how to tear down environment if provisioning fails

## Failure Handling
- IaC syntax errors → Report errors, stop provisioning, do not proceed
- Resource quota exceeded → Report, suggest resource reduction, do not create partial environment
- Provider authentication failure → Report, request credentials, do not proceed
- Health check failure → Report, mark environment as unhealthy, do not mark ready

## Completion Criteria
- Environment provisioned and verified ready
- All health checks passing
- Observability configured and reporting
- Provisioning report with resource inventory and costs
- No secret values in output
