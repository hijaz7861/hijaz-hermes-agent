# Skills Making Factory — Security Engine

## Purpose
The security-engine performs security checks on all new and modified skills. It verifies that skills follow security best practices, do not leak secrets, respect approval gates, and handle sensitive data correctly.

## Responsibilities
- Scan skill files for hardcoded secrets, credentials, or tokens
- Verify that skills respect approval gates for destructive operations
- Check that skills do not log or expose sensitive data
- Validate privacy gates for data classification
- Ensure skills handle failure modes safely

## Inputs
- Skill file (SKILL.md) to check
- Playbook file to check
- Security policy configuration from skills-factory/factory-config/

## Outputs
- Security scan report: skills-factory/audit-logs/security-scan-<skill-name>.json
- Security pass/fail determination
- List of security findings with severity

## Procedure
1. **Scan for Secrets**: Search for API keys, passwords, tokens, private keys, connection strings in skill files
2. **Check Approval Gates**: Verify that skills requiring approval gates have them documented
3. **Check Privacy Gates**: Verify that skills handling confidential data have privacy gates
4. **Check Failure Modes**: Verify that skills have explicit failure handling (BLOCKED, ERROR, etc.)
5. **Check Destructive Operations**: Verify that skills modifying code require explicit approval
6. **Produce Report**: Write security scan report with pass/fail and findings

## Safety & Governance
- **No secrets in reports**: Security scan reports must not contain actual secret values
- **Hard fail on secrets**: Any skill containing unredacted secrets fails security check
- **Hard fail on missing gates**: Skills modifying code without approval gates fail security check

## Completion Criteria
- Security scan report produced with pass/fail determination
- All secret patterns checked
- All approval gates verified
- Security findings classified by severity
