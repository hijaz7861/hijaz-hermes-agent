# Playbook: Dependency Duplicate Remover

*Practical examples for the `dependency-duplicate-remover` skill*

---

## Scenario 1: Consolidate duplicate lodash versions (happy path)

**Trigger:** "Remove duplicate lodash versions across package manifests."

**Invocation:**
```
Audit dependency manifests for duplicate lodash versions.
Consolidate to single version. Tests must pass after consolidation.
```

**Execution Log:**
```
## Dependency Deduplication: lodash

### Inventory
Manifests found:
- package.json: lodash 4.17.20
- package-lock.json: lodash 4.17.21
- subpackage/package.json: lodash 4.17.15
- subpackage/package-lock.json: lodash 4.17.20

### Conflicts Detected
| Manifest | Version | Location |
|----------|---------|----------|
| package.json | 4.17.20 | root |
| package-lock.json | 4.17.21 | root |
| subpackage/package.json | 4.17.15 | subpackage |
| subpackage/package-lock.json | 4.17.20 | subpackage |

### Consolidation Plan
Target version: 4.17.21 (latest, security patched)
Files to update: 3 (subpackage/package.json, both lockfiles)

### Applied Changes (with approval)
- subpackage/package.json: 4.17.15 → 4.17.21
- package-lock.json: updated to 4.17.21
- subpackage/package-lock.json: updated to 4.17.21

### Verification
- npm install: SUCCESS
- npm run build: SUCCESS
- npm test: 156 passed, 0 failed
- No duplicate lodash declarations remain

Exit code: 0.
```

**Expected Output:**
Dependency deduplication report with conflicts, consolidation plan, and verification results.

---

## Scenario 2: No compatible version (failure case)

**Trigger:** "Consolidate duplicate react versions across monorepo packages."

**Invocation:**
```
Remove duplicate react versions. Find compatible version for all packages.
```

**Execution Log:**
```
## Dependency Deduplication: react

### Inventory
Packages and versions:
- web-app/package.json: react 18.2.0
- mobile-app/package.json: react 17.0.2
- shared-components/package.json: react 16.14.0
- docs-site/package.json: react 18.2.0

### Conflicts
react 18.2.0 vs 17.0.2 vs 16.14.0 - 3 different major versions

### Compatibility Analysis
- react 18 requires react-dom 18, new concurrent features
- react 17 doesn't support concurrent features
- react 16 lacks hooks support used by web-app

### Options
1. Upgrade all to 18.2.0 (breaking for mobile-app, shared-components)
2. Keep 3 versions (no consolidation possible)
3. Upgrade shared-components to 17, keep web/docs at 18

### Decision
Option 3 selected: Partial consolidation

### Applied Changes
- shared-components/package.json: 16.14.0 → 17.0.2
- Verified: shared-components tests pass with react 17
- web-app and docs-site remain at 18.2.0
- mobile-app remains at 17.0.2

### Report
Consolidated: 1 package (shared-components)
Remaining versions: 2 (18.2.0, 17.0.2)
Cannot fully consolidate due to incompatibility
Exit code: 0.
```

**Expected Output:**
Dependency deduplication report showing partial consolidation with reasons.

---

## Scenario 3: Consolidation breaks build (safety case)

**Trigger:** "Consolidate duplicate express versions."

**Invocation:**
```
Remove duplicate express versions. Consolidate to 4.18.2.
Build and tests must pass after consolidation.
```

**Execution Log:**
```
## Dependency Deduplication: express

### Inventory
- api-gateway/package.json: express 4.17.1
- user-service/package.json: express 4.18.2
- payment-service/package.json: express 4.17.1

### Consolidation Applied
- api-gateway: 4.17.1 → 4.18.2
- payment-service: 4.17.1 → 4.18.2

### Verification (FAILED)
- api-gateway build: FAILED
- Error: express-validator 4.x incompatible with express 4.18.2
- payment-service build: SUCCESS

### Rollback Triggered
- Reverted api-gateway to 4.17.1
- Re-ran build: SUCCESS
- No changes remain

### Report
Deduplication: ROLLED BACK
Reason: build failure (dependency incompatibility)
Only payment-service consolidated (no issues)
Exit code: 1 (safety gate triggered, partial rollback).
```

**Expected Output:**
Deduplication report showing rollback due to build failure, with partial consolidation results.
