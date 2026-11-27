# Playbook: Secret Duplicate Remover

*Practical examples for the `secret-duplicate-remover` skill*

---

## Scenario 1: Consolidate duplicate API key (happy path)

**Trigger:** "Find and remove duplicate Stripe API key declarations."

**Invocation:**
```
Scan for duplicate Stripe secret key declarations across config files.
Consolidate to single secret store entry. NEVER print secret values.
```

**Execution Log:**
```
## Secret Deduplication: Stripe API Key

### Scan Results
Locations scanned: 12 files across 3 environments

### Duplicates Found
| Location | Type | Environment | Exposure |
|----------|------|-------------|----------|
| config/payments.yaml:15 | STRIPE_SECRET_KEY | production | Current file |
| .env.production:22 | STRIPE_SECRET_KEY | production | Current file |
| .git/refs/heads/main:3 | STRIPE_SECRET_KEY | production | Historical (commit a1b2c3d) |
| .github/workflows/deploy.yml:8 | STRIPE_SECRET_KEY | production | CI/CD file |

### Analysis
- config/payments.yaml and .env.production: Same secret key → TRUE DUPLICATE (current exposure)
- .github/workflows/deploy.yml: Same secret key → TRUE DUPLICATE (CI/CD exposure)
- .git history: Same secret key → HISTORICAL EXPOSURE (assume compromised)

### Consolidation Plan
1. Move secret to secret store (AWS Secrets Manager)
2. Remove from config/payments.yaml, .env.production, deploy.yml
3. Reference secret store entry in all locations
4. Rotate the secret (assume compromised due to git history exposure)

### Applied Changes (with approval)
- config/payments.yaml: removed STRIPE_SECRET_KEY, added reference to secret store
- .env.production: removed STRIPE_SECRET_KEY, added reference to secret store
- .github/workflows/deploy.yml: removed STRIPE_SECRET_KEY, added reference to secret store

### Verification
- Production app: loads secret from secret store successfully
- CI/CD pipeline: retrieves secret from secret store successfully
- No secret values printed anywhere in output

Exit code: 0.
```

**Expected Output:**
Secret deduplication report with locations only (no values), consolidation plan, and verification.

---

## Scenario 2: Secret in git history (safety case)

**Trigger:** "Scan git history for committed secrets."

**Invocation:**
```
Scan last 500 commits for committed secrets.
Report all findings with locations. Never print secret values.
```

**Execution Log:**
```
## Secret Deduplication: Git History Scan

### Scan Scope
- Repository: /workspace/app
- Scan depth: 500 commits
- Current branch: kilo/hearty-sequoia-b6b

### Findings
| Commit | File | Pattern | Severity | Exposure |
|--------|------|---------|----------|----------|
| current | src/config/production.yml:15 | Database password | CRITICAL | Current file |
| 3f4a2b1 | .env:8 | AWS secret key | HIGH | Historical only |
| 1a2b3c4 | config/secrets.yml:5 | Stripe test key | MEDIUM | Historical only |
| 7d8e9f0 | .gitignore:3 | None (false positive) | INFO | N/A |

### Analysis
- src/config/production.yml: Database password in current file → CRITICAL (active exposure)
- .env (commit 3f4a2b1): AWS secret key → HIGH (historical, assume compromised)
- config/secrets.yml (commit 1a2b3c4): Stripe test key → MEDIUM (historical)
- .gitignore: False positive (not a secret)

### Recommendations
1. ROTATE database password immediately (active exposure)
2. ROTATE AWS secret key (historical exposure, assume compromised)
3. ROTATE Stripe test key (historical exposure)
4. Remove secrets from git history (git filter-repo or BFG) - requires authorization
5. Add .gitignore for *.yml files containing secrets
6. Add pre-commit hook to block secret patterns

### Report
Secrets found: 3 (1 current, 2 historical)
No secret values printed anywhere in output
Exit code: 0.
```

**Expected Output:**
Secret deduplication report flagging secrets by location/severity only, with rotation recommendations.

---

## Scenario 3: Secret retrieval breaks after consolidation (safety case)

**Trigger:** "Remove duplicate JWT secret from config files."

**Invocation:**
```
Remove duplicate JWT secret declarations. Verify apps can still retrieve secrets.
```

**Execution Log:**
```
## Secret Deduplication: JWT Secret

### Findings
| Location | Type | Environment |
|----------|------|-------------|
| config/auth.yaml:23 | JWT_SECRET | production |
| .env.production:31 | JWT_SECRET | production |
| src/auth/tokens.ts:45 | JWT_SECRET (hardcoded fallback) | production |

### Analysis
- All three locations contain the same JWT secret → TRUE DUPLICATE
- src/auth/tokens.ts has hardcoded fallback → SECURITY RISK (should never hardcode)

### Consolidation Applied (with approval)
- Removed JWT_SECRET from config/auth.yaml (reference .env.production)
- Removed hardcoded JWT_SECRET from src/auth/tokens.ts (reference environment variable)

### Verification (FAILED)
- Auth service: FAILED to start
- Error: JWT_SECRET not found
- Root cause: Production environment doesn't have JWT_SECRET set as env var
- The .env.production file isn't loaded in production container

### Rollback Triggered
- Restored JWT_SECRET in config/auth.yaml
- Kept hardcoded fallback removal (security improvement)
- Re-verified: Auth service starts successfully
- Partial consolidation: 1 of 2 changes applied

### Report
Deduplication: PARTIAL
- config/auth.yaml: restored (production env var missing)
- src/auth/tokens.ts: removed hardcoded secret (security improvement kept)
Exit code: 1 (partial consolidation, one change reverted).
```

**Expected Output:**
Secret deduplication report showing partial consolidation with security improvement kept.
