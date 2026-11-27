# Playbook: Resource Duplicate Remover

*Practical examples for the `resource-duplicate-remover` skill*

---

## Scenario 1: Remove duplicate S3 buckets (happy path)

**Trigger:** "Find and remove duplicate S3 buckets across environments."

**Invocation:**
```
Scan for duplicate S3 buckets containing backup data.
Consolidate to single bucket. Verify applications still function.
```

**Execution Log:**
```
## Resource Deduplication: S3 Buckets

### Inventory
S3 buckets found across 3 environments:

| Bucket | Environment | Purpose | Size | Last Accessed |
|--------|-------------|---------|------|---------------|
| app-backups-dev | development | Daily backups | 50GB | 2 days ago |
| app-backups-staging | staging | Daily backups | 48GB | 2 days ago |
| app-backups-prod | production | Daily backups | 500GB | 2 days ago |
| app-backups-archive | production | Archive (6 months+) | 2TB | 30 days ago |

### Analysis
- app-backups-dev and app-backups-staging: Same purpose (daily backups), different environments → LEGITIMATE
- app-backups-prod: Production backups → MUST KEEP
- app-backups-archive: Disaster recovery → MUST KEEP (intentional duplicate for DR)

### Decision
No true duplicates found. All buckets serve distinct purposes or environments.
Recommendation: No consolidation needed.

Exit code: 0 (no duplicates detected).
```

**Expected Output:**
Resource deduplication report showing legitimate environment separation and intentional DR duplicates.

---

## Scenario 2: Consolidate duplicate load balancers (happy path)

**Trigger:** "Remove duplicate load balancers in staging environment."

**Invocation:**
```
Find duplicate load balancers in staging. Consolidate to single LB. Verify applications function.
```

**Execution Log:**
```
## Resource Deduplication: Load Balancers

### Inventory
Load balancers in staging:

| LB | Environment | Target | Port | Cost/Month |
|----|-------------|--------|------|------------|
| lb-staging-a | staging | api-staging | 443 | $18 |
| lb-staging-b | staging | api-staging | 443 | $18 |

### Analysis
- Both LBs point to same target (api-staging) on same port (443) → TRUE DUPLICATE
- Combined cost: $36/month

### Consolidation Plan
- Keep: lb-staging-a
- Remove: lb-staging-b
- Update DNS: point api.staging.example.com to lb-staging-a
- Update applications: reference single LB

### Applied Changes (with approval)
- Removed lb-staging-b
- Updated DNS record
- Verified application connectivity

### Verification
- api.staging.example.com: responds correctly
- All staging applications: connect successfully
- Cost savings: $18/month

Exit code: 0.
```

**Expected Output:**
Resource deduplication report with cost savings and verification results.

---

## Scenario 3: Cannot remove DR backup (safety case)

**Trigger:** "Remove duplicate database backups."

**Invocation:**
```
Find and remove duplicate database backups.
```

**Execution Log:**
```
## Resource Deduplication: Database Backups

### Inventory
Database backups found:

| Backup | Source | Frequency | Retention | Last Run |
|--------|--------|-----------|-----------|----------|
| prod-db-daily | production-db | Daily | 7 days | 2 hours ago |
| prod-db-weekly | production-db | Weekly | 4 weeks | 5 days ago |
| prod-db-dr-us-east | production-db | Daily | 30 days | 2 hours ago |
| prod-db-dr-eu-west | production-db | Daily | 30 days | 2 hours ago |

### Analysis
- prod-db-dr-us-east and prod-db-dr-eu-west: Same source, same frequency → APPEARS DUPLICATE
- However: These are cross-region disaster recovery backups → INTENTIONAL DUPLICATE
- Removing either would violate disaster recovery requirements

### Decision
DO NOT REMOVE. Cross-region backups are intentional for disaster recovery compliance.
Removing would create single point of failure.

### Report
Duplicates found: 2 (cross-region DR backups)
Action: None (intentional duplicates)
Reason: Disaster recovery requirement
Exit code: 0 (no changes made, intentional duplicates preserved).
```

**Expected Output:**
Resource deduplication report identifying intentional DR duplicates that must be preserved.
