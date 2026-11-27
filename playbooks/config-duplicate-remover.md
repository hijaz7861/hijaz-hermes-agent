# Playbook: Config Duplicate Remover

*Practical examples for the `config-duplicate-remover` skill*

---

## Scenario 1: Consolidate duplicate API URL config (happy path)

**Trigger:** "Remove duplicate API URL configuration across environment files."

**Invocation:**
```
Find and remove duplicate API_URL configuration across .env files.
Consolidate to single source of truth. Verify config loads in all environments.
```

**Execution Log:**
```
## Config Deduplication: API_URL

### Inventory
Files scanned: 6 (.env.development, .env.staging, .env.production, config.yaml, settings.py, docker-compose.yml)

### Duplicates Found
| Key | File | Value | Environment |
|-----|------|-------|-------------|
| API_URL | .env.development | https://api.dev.example.com | development |
| API_URL | .env.staging | https://api.staging.example.com | staging |
| API_URL | .env.production | https://api.example.com | production |
| api_url | config.yaml | https://api.example.com | production |
| API_ENDPOINT | settings.py | https://api.example.com | production |

### Analysis
- API_URL in .env.production, api_url in config.yaml, API_ENDPOINT in settings.py → all point to production API → TRUE DUPLICATE
- API_URL in .env.development/.env.staging → different environments → LEGITIMATE DIFFERENCE

### Consolidation Plan
- Remove api_url from config.yaml (reference .env.production instead)
- Remove API_ENDPOINT from settings.py (reference .env.production instead)
- Keep .env.development and .env.staging as-is (environment-specific)

### Applied Changes (with approval)
- config.yaml: removed api_url entry
- settings.py: removed API_ENDPOINT, added reference to .env.production

### Verification
- Development: config loads successfully
- Staging: config loads successfully
- Production: config loads successfully
- No missing keys detected

Exit code: 0.
```

**Expected Output:**
Config deduplication report with duplicates, consolidation plan, and multi-environment verification.

---

## Scenario 2: Legitimate environment differences (failure case)

**Trigger:** "Remove duplicate database configuration across environments."

**Invocation:**
```
Deduplicate database configuration in .env files.
```

**Execution Log:**
```
## Config Deduplication: Database Configuration

### Inventory
Files scanned: 3 (.env.development, .env.staging, .env.production)

### Findings
| Key | Development | Staging | Production |
|-----|-------------|---------|------------|
| DB_HOST | localhost | db.staging.internal | db.production.internal |
| DB_PORT | 5432 | 5432 | 5432 |
| DB_NAME | app_dev | app_staging | app_production |
| DB_USER | dev_user | staging_user | prod_user |

### Analysis
- DB_PORT: same value (5432) across all environments → TRUE DUPLICATE
- DB_HOST, DB_NAME, DB_USER: different values → LEGITIMATE ENVIRONMENT DIFFERENCES

### Decision
- DB_PORT: Can consolidate (same value)
- DB_HOST, DB_NAME, DB_USER: Must remain environment-specific

### Status
Only DB_PORT is a true duplicate. Consolidating single key provides minimal benefit.
Recommendation: Leave as-is, consolidation not worth the risk.

Exit code: 0 (no changes made, analysis complete).
```

**Expected Output:**
Config deduplication report distinguishing true duplicates from legitimate environment differences.

---

## Scenario 3: Consolidation breaks config loading (safety case)

**Trigger:** "Remove duplicate feature flag configuration."

**Invocation:**
```
Deduplicate FEATURE_FLAGS across config files. Verify apps load correctly.
```

**Execution Log:**
```
## Config Deduplication: Feature Flags

### Inventory
Files: config/features.yaml, .env.production, .env.staging, docker-compose.yml

### Duplicate Found
- FEATURE_NEW_DASHBOARD: true (config/features.yaml)
- FEATURE_NEW_DASHBOARD: true (.env.production)
- FEATURE_NEW_DASHBOARD: false (.env.staging)

### Analysis
- config/features.yaml and .env.production: same value (true) → TRUE DUPLICATE
- .env.staging: different value (false) → LEGITIMATE (staging tests new feature)

### Consolidation Applied (with approval)
- Removed FEATURE_NEW_DASHBOARD from .env.production (reference config/features.yaml instead)

### Verification (FAILED)
- Production app: FAILED to start
- Error: FEATURE_NEW_DASHBOARD not found in environment
- Root cause: Production code reads from .env, not config/features.yaml

### Rollback Triggered
- Restored FEATURE_NEW_DASHBOARD in .env.production
- Re-verified: Production app starts successfully
- No changes remain

### Report
Deduplication: ROLLED BACK
Reason: config loading failure (wrong config source)
No changes applied to repository
Exit code: 1 (safety gate triggered, rollback completed).
```

**Expected Output:**
Config deduplication report showing rollback due to config loading failure.
