---
name: resource-duplicate-remover
description: Detect and remove duplicate cloud resources, infrastructure components, and services across environments. Consolidates redundant resources to reduce costs and complexity.
version: 1.0.0
tags: [duplicate, removal, resources, cloud, infrastructure, deduplication, cost-optimization]
dependencies: [environment-provisioner, infrastructure-as-code-generator]
---

# Resource Duplicate Remover

## Objective
Detect and remove duplicate cloud resources, infrastructure components, and services across environments. Consolidates redundant resources to reduce costs, complexity, and attack surface.

## Trigger
- "Remove duplicate cloud resources across environments"
- "Consolidate redundant infrastructure components"
- "Deduplicate deployed services and resources"
- "Find and remove duplicate cloud resources"

Anti-triggers: "Delete resources without verification" / "Remove production resources without approval" — those violate safety principles.

## Inputs
- Cloud resources: instances, databases, storage buckets, load balancers, etc.
- Infrastructure definitions: Terraform, CloudFormation, or similar
- Environment mapping: which resources belong to which environment
- Usage data: which resources are actively used

## Outputs
- Duplicate report: duplicate resources, locations, environments, estimated cost savings
- Consolidation plan: which resources to keep, which to remove
- Updated infrastructure definitions
- Verification: applications function after consolidation

## Procedure
1. **Inventory resources** (environment-provisioner)
   - Scan cloud resources across environments
   - Read infrastructure definitions
   - List resources with types, locations, configurations

2. **Detect duplicates**
   - Same service deployed in multiple environments unnecessarily
   - Duplicate storage buckets with same data
   - Duplicate load balancers serving same backend
   - Duplicate databases with same schema

3. **Classify duplicates**
   - True duplicates: same purpose, same data, can consolidate
   - Environment-specific: needed in each environment (dev, staging, prod)
   - Redundant backups: intentional duplicates for disaster recovery

4. **Plan consolidation**
   - For true duplicates: determine single resource to keep
   - For environment-specific: keep separate but standardize configuration
   - Map all applications referencing the affected resources

5. **Apply consolidation** (requires approval for production)
   - Remove duplicate resources
   - Update application references
   - Update infrastructure definitions
   - One resource at a time

6. **Verify**
   - Confirm applications function after consolidation
   - Verify no broken references
   - Test in each environment
   - Roll back any consolidation that breaks functionality

7. **Report**
   - Produce deduplication report: duplicates found, removed, cost savings, verification results

## Safety & Approval Gates
- **Approval required** before removing production resources
- **Functionality gate**: consolidation verified with applications working
- **One resource at a time**: no batching unrelated changes
- **Rollback**: recreate removed resources if functionality breaks
- **No disaster recovery backups removed**: intentional duplicates preserved

## Failure Handling
- Resource API error → Skip, mark as unanalyzable, continue
- Consolidation breaks functionality → Revert (recreate resource), report
- Cannot determine if duplicate is intentional → Mark as "manual review," do not remove
- No duplicates found → Report "no duplicate resources detected"

## Completion Criteria
- Duplicate report with resources and locations
- Each consolidation verified with applications functioning
- No true duplicate resources remain
- Environment-specific resources preserved
- Estimated cost savings documented
