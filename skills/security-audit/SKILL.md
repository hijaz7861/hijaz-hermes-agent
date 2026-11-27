---
name: security-audit
description: Audit a repository for security issues: secrets in code, vulnerable dependencies, weak configuration, and exposed trust boundaries. Use before merges, releases, or when handling sensitive data.
version: 1.0.0
tags: [governance, security, audit, secrets, dependencies]
---

# Security Audit

## Objective
Produce an evidence-based security findings report for a repository. Identify committed secrets, vulnerable/outdated dependencies, insecure configuration, and exposed trust boundaries. Never modify code without explicit approval; never log or exfiltrate secrets.

## Trigger
- "Security audit this repo" / "Run a security audit"
- "Check for secrets in code"
- "Audit dependencies for vulnerabilities before release"
- "Review configuration for insecure settings"

Anti-triggers: "Fix all vulnerabilities" / "Patch dependencies automatically" — those require explicit approval and are handled by dependency-management or a separate remediation workflow.

## Procedure
1. **Scope the audit**
   - Record repository root, branch, and working-tree status.
   - Identify areas handling secrets, authentication, payments, personal data, or external service integrations.
   - List configuration files that control access, TLS, CORS, CSP, and cookie settings.

2. **Scan for secrets**
   - Search for common secret patterns: API keys, tokens, private keys, passwords, connection strings.
   - Check `.env*`, `config*.*`, `secrets*`, CI/CD files, and commit history (bounded: most recent 50 commits).
   - Flag any candidate; do not print the secret value in output. Record file, line, and a redacted snippet only.

3. **Audit dependencies**
   - Inspect dependency manifests and lockfiles (package.json, requirements.txt, go.mod, Cargo.toml, etc.).
   - Identify outdated, unmaintained, or known-vulnerable packages where a vulnerability database or advisory feed is available.
   - Record package, current version, fixed version (if known), and severity.

4. **Review configuration and trust boundaries**
   - Check for: disabled TLS/HTTPS, permissive CORS (`*` origins), weak cookie flags (no `HttpOnly`/`Secure`), exposed debug endpoints, hardcoded credentials, world-writable permissions on sensitive files.
   - Map data flow across trust boundaries (external input → validation → business logic → persistence/output).

5. **Consolidate findings**
   - Classify each finding: CRITICAL / HIGH / MEDIUM / LOW / INFO.
   - Include: finding, file:line, evidence (redacted), risk rationale, recommended remediation, and whether user approval is required before fixing.

6. **Report**
   - Write a Markdown findings report with an executive summary, findings table, and remediation priority order.
   - State clearly which findings were verified vs. hypothesized vs. could not be checked.

## Safety & Approval Gates
- **Read-only:** Do not modify source, configuration, or dependencies. Findings only.
- **No secret output:** Never print secret values, tokens, or keys. Record only location and redacted context.
- **Approval required before any remediation:** Patching, dependency updates, or config changes need explicit user approval.
- **No network exfiltration:** Do not send code, secrets, or repository contents to external scanning services unless the user approves.

## Failure Handling
- Vulnerability feed unavailable → Record as hypothesis, note "could not verify", continue.
- Encrypted/binary file blocks scan → Skip, list as unscanned, continue.
- No secrets found → Report "no committed secrets detected" (does not guarantee absence).
- Approval denied for remediation → Stop, report findings only, exit 0.

## Completion Criteria
- Findings report produced with at least an executive summary and findings table.
- Every finding has a location (file:line where applicable) and a severity.
- Secrets, if any, are never printed in plaintext.
- Verified findings are separated from hypotheses and unchecked areas.
