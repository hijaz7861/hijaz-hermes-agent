---
name: secret-scanner-historical
description: Scan git history for committed secrets by combining security auditing with codebase intelligence. Searches commit history for API keys, passwords, tokens, and other secrets that were committed and may still be accessible in the repository history.
version: 1.0.0
tags: [secrets, security, git, history, audit, remediation]
dependencies: [security-audit, codebase-intelligence]
---

# Secret Scanner Historical

## Objective
Combine security auditing with codebase intelligence to scan git history for committed secrets. Identifies API keys, passwords, tokens, private keys, and connection strings that were committed to the repository and may still be accessible in the git history, even if removed from current files.

## Trigger
- "Scan git history for committed secrets"
- "Find leaked credentials in repository history"
- "Audit git history for secrets in module X"
- "Historical secret scan before making repo public"

Anti-triggers: "Rotate all secrets automatically" / "Rewrite git history" — those are separate remediation tasks requiring careful planning, not just scanning.

## Inputs
- Repository: git repository with commit history
- Scan depth: number of commits to scan (default: last 500, or all)
- Secret patterns: API key formats, password patterns, token patterns, private key headers
- Exclusions: files or patterns to skip (vendored dependencies, test fixtures)

## Outputs
- Secret findings report: commit, file, line, pattern type, severity, redacted context
- Secret inventory: unique secrets found, locations across history
- Exposure assessment: secrets still in current files vs. only in history
- Remediation recommendations: rotate secrets, remove from history, use secret manager
- Risk assessment: likelihood of exposure, potential impact

## Procedure
1. **Establish scan scope** (codebase-intelligence)
   - Record repository root, current branch, latest commit.
   - Identify .git directory and commit history depth.
   - Identify file types to scan: source code, config files, CI/CD files, documentation.
   - Identify exclusions: node_modules, vendor directories, test fixtures, generated files.

2. **Scan commit history** (security-audit)
   - Use git log to iterate through commits (bounded by scan depth).
   - For each commit, scan added/modified files for secret patterns.
   - Pattern types: AWS keys, GitHub tokens, private keys (BEGIN RSA/EC/OPENSSH), database connection strings, generic password patterns, Stripe keys, Slack tokens.
   - Record: commit hash, author, date, file, line, pattern type, redacted context.

3. **Check current files** (codebase-intelligence)
   - Scan current working tree for the same secrets.
   - Determine: secret still present in current code vs. only in history.
   - If still present: CRITICAL (active exposure).
   - If only in history: HIGH (historical exposure, still accessible via git).

4. **Assess exposure risk**
   - Repository public/private: public repos have higher exposure risk.
   - Secret type: production vs. test/staging secrets.
   - Secret age: older secrets more likely to have been rotated.
   - Secret validity: unknown without testing (never test real secrets).

5. **Generate remediation recommendations**
   - Rotate all exposed secrets (assume compromised).
   - Remove secrets from current files; use environment variables or secret manager.
   - Remove secrets from git history (git filter-repo or BFG) — requires careful planning.
   - Add .gitignore for sensitive files.
   - Add pre-commit hooks to prevent future commits.

6. **Report**
   - Produce secret scan report: findings table, exposure assessment, remediation plan.

## Safety & Approval Gates
- **Read-only scanning:** No history rewriting or secret rotation without explicit approval.
- **No secret output:** Secret values NEVER printed; only location and redacted context.
- **Approval required** before rotating secrets or rewriting git history.
- **Assume compromised:** Any secret found in history should be treated as compromised.

## Failure Handling
- Git history unavailable → Mark as "no git history," scan current files only.
- Large repository → Limit scan depth, mark as "partial scan."
- Encrypted files → Skip, mark as "encrypted, cannot scan."
- Binary files → Skip, mark as "binary, not scanned."
- No secrets found → Report "no secrets detected" (does not guarantee absence).

## Completion Criteria
- Secret findings report with commit, file, pattern type, severity, redacted context.
- Exposure assessment: current vs. historical presence.
- Remediation recommendations: rotate, remove, use secret manager, add pre-commit hooks.
- Risk assessment: public/private repo, secret type, age.
- No secret values printed anywhere in output.
