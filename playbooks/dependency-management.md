# Playbook: Dependency Management

*Practical examples for the `dependency-management` skill*

---

## Scenario 1: Patch vulnerable dependencies (happy path)

**Trigger:** "Patch the high-severity vulnerability in lodash and update outdated packages."

**Invocation:**
```
Audit and patch dependencies. Priority: vulnerabilities first. Apply patch/minor updates only; major version bumps need approval.
```

**Execution Log:**
```
## Dependency Management: acme-web

### Inventory
Manifest: package.json + package-lock.json
Direct dependencies: 24
Transitive dependencies: 148
Package manager: npm

### Detection
Tool: `npm audit` (available)
Findings:
1. `lodash` 4.17.20 — Prototype Pollution — HIGH — fixed in 4.17.21
2. `ansi-regex` 5.0.1 — ReDoS — MODERATE — fixed in 6.0.1 (major bump)

### Prioritization
- P0: lodash → 4.17.21 (patch, security fix, low risk)
- P1: ansi-regex → 6.0.1 (major bump, security, breaking-change risk — approval required)
- P2: `chalk` 4.1.2 → 5.3.0 (minor, ESM-only, breaking — approval required)

### Applied (with user approval)
- `lodash` 4.17.20 → 4.17.21
- Verification: `npm install`, `npm run build`, `npm test` — all pass
- Vulnerability resolved: `npm audit` reports 0 issues for lodash

### Pending (approval required)
- `ansi-regex` 5.0.1 → 6.0.1 (major, not applied)
- `chalk` 4.1.2 → 5.3.0 (minor but breaking, not applied)

### Report
Applied: 1 (lodash). Pending: 2. Remaining risk: 0 known unpatched vulns after applied patch.
Lockfile state recorded for rollback.
Exit code: 0.
```

**Expected Output:**
A dependency report listing audited packages, applied updates (with verification), pending updates awaiting approval, and remaining risk. Build and test results included.

---

## Scenario 2: Update breaks tests (failure case)

**Trigger:** "Update all outdated dependencies."

**Invocation:**
```
Update outdated packages. Do not proceed if tests fail.
```

**Execution Log:**
```
## Dependency Management: acme-api

### Proposed Updates
- `express` 4.18.1 → 4.19.2 (minor)
- `mongoose` 6.10.0 → 7.5.0 (major)

### Applied (with approval)
- `express` 4.18.1 → 4.19.2 — applied
- `mongoose` 6.10.0 → 7.5.0 — applied

### Verification (FAILED)
- `npm install` — success
- `npm run build` — success
- `npm test` — FAILURE: 12 tests fail (mongoose API change)
  - Test: userSchema.virtual — TypeError: ... is not a function

### Rollback
- Reverted package.json and package-lock.json to pre-update state.
- Re-ran `npm install` + `npm test` — all pass (baseline restored).

### Report
- Applied then reverted: mongoose 6.10.0 → 7.5.0 (broke tests)
- Successfully applied: express 4.18.1 → 4.19.2
- Remaining: mongoose update pending investigation
Exit code: 1 (update introduced test failures; reverted).
```

**Expected Output:**
A report showing the failed update, the rollback performed, and what remains pending. Tests pass after rollback.

---

## Scenario 3: Audit tool unavailable (failure case)

**Trigger:** "Check for outdated dependencies. `npm audit` not available."

**Invocation:**
```
Inventory dependencies in package.json. No network access to registry.
```

**Execution Log:**
```
## Dependency Management: acme-cli

### Tool Check
- `npm audit`: unavailable (no network)
- Fallback: manifest + lockfile inspection only

### Inventory (local data only)
- `typescript` 4.9.5 (lockfile) — latest unknown (no network)
- `esbuild` 0.17.19 — latest unknown
- No local vulnerability data available

### Findings
- All version comparisons marked "unverified — no network access"
- No fixes proposed without current-version data

### Report
- Audited: 18 direct dependencies
- Verified vulnerabilities: 0 (cannot verify without tool/network)
- Proposed updates: 0
- Note: Re-run with `npm audit` and network access for full audit.
Exit code: 0 (incomplete audit, clearly reported).
```

**Expected Output:**
A report stating the audit is incomplete due to missing tooling/network, listing only what could be observed locally, with no unverified changes proposed.
