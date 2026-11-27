---
name: infrastructure-as-code-generator
description: Generate infrastructure-as-code (Terraform, CloudFormation, Pulumi) definitions for cloud infrastructure. Creates modular, reusable IaC with security best practices and environment-specific variables.
version: 1.0.0
tags: [iac, terraform, cloudformation, infrastructure, cloud, provisioning]
dependencies: [environment-provisioner, security-audit]
---

# Infrastructure-as-Code Generator

## Objective
Generate infrastructure-as-code (Terraform, CloudFormation, Pulumi) definitions for cloud infrastructure. Creates modular, reusable IaC with security best practices and environment-specific variables for consistent, auditable infrastructure management.

## Trigger
- "Create Terraform configuration for infrastructure X"
- "Generate CloudFormation template for service Y"
- "Create IaC for multi-environment deployment"
- "Generate infrastructure code for cloud resources"

Anti-triggers: "Apply IaC to production without review" / "Hardcode credentials in IaC" — those violate safety and security principles.

## Inputs
- Infrastructure requirements: compute, storage, network, database, services
- Cloud provider: AWS, GCP, Azure, or multi-cloud
- Environment variables: region, instance types, sizes (per environment)
- Security requirements: encryption, access controls, network isolation
- Compliance requirements: GDPR, SOC2, HIPAA, PCI-DSS

## Outputs
- IaC definition files: .tf, .yaml, or .ts files
- Module structure: reusable modules for common patterns
- Variable definitions: environment-specific, with defaults and validation
- Outputs: resource IDs, endpoints, connection strings (redacted)
- Security configuration: encryption, IAM policies, network security groups

## Procedure
1. **Analyze infrastructure requirements**
   - Identify resources needed: VPC, subnets, compute, storage, database
   - Identify networking requirements: public/private subnets, security groups
   - Identify security requirements: encryption, IAM, network isolation

2. **Design IaC modules**
   - Create reusable modules: networking, compute, database, security
   - Parameterize modules for environment differences
   - Define inputs and outputs for each module

3. **Generate IaC code**
   - Write provider configuration and version constraints
   - Create resource definitions with security best practices
   - Define variables with types, defaults, and validation rules
   - Create outputs for cross-module references

4. **Apply security best practices**
   - Encryption at rest and in transit for all storage
   - IAM least-privilege policies
   - Network security groups with least-permissive rules
   - No hardcoded credentials or secrets

5. **Validate IaC**
   - Run `terraform validate` or equivalent
   - Check for security misconfigurations
   - Validate variable types and constraints
   - Run `terraform plan` to preview changes (dry-run)

6. **Report**
   - Produce IaC report: modules, resources, security configuration, validation results

## Safety & Approval Gates
- **No hardcoded secrets**: Use variable references or secret managers
- **IaC changes require review** before applying to production
- **Dry-run required**: `terraform plan` before `terraform apply`
- **Encryption mandatory** for all storage resources

## Failure Handling
- IaC syntax error → Report, fix, revalidate
- Provider authentication failure → Report, request credentials
- Resource quota exceeded → Report, suggest reduction
- Security misconfiguration → Report, fix before applying

## Completion Criteria
- IaC definition files created and validated
- Modules parameterized for environment differences
- Security best practices applied (encryption, IAM, network)
- Dry-run validation passed
- No secret values in IaC code
