# Playbook: Skill Reader

*Practical examples for the `skill-reader` skill*

---

## Scenario 1: Read complete skill structure (happy path)

**Trigger:** "Read the complete structure of skill security-audit."

**Invocation:**
```
Read skill security-audit/SKILL.md completely. Extract frontmatter, all sections, procedure steps, safety gates, dependencies, and playbook references. Output structured JSON.
```

**Execution Log:**
```
## Skill Reading: security-audit

### Frontmatter Extracted
{
  "name": "security-audit",
  "description": "Audit a repository for security issues: secrets in code, vulnerable dependencies, weak configuration, and exposed trust boundaries.",
  "version": "1.0.0",
  "tags": ["governance", "security", "audit", "secrets", "dependencies"],
  "dependencies": ["codebase-intelligence"],
  "capabilities": ["reads_code", "produces_reports"],
  "min_hermes_version": "1.0.0",
  "protocol_version": 1
}

### Sections Identified (7 sections)
1. Objective - "Produce an evidence-based security findings report..."
2. Trigger - 3 triggers listed, 1 anti-trigger
3. Procedure - 6 steps with sub-steps
4. Safety & Approval Gates - 4 gates listed
5. Failure Handling - 5 failure modes documented
6. Completion Criteria - 5 criteria listed
7. (Playbook reference: playbooks/security-audit.md)

### Procedure Steps
1. Scope the audit (sub-steps: record root, identify areas, list config files)
2. Scan for secrets (sub-steps: search patterns, check files, check commit history)
3. Audit dependencies (sub-steps: inspect manifests, identify outdated packages)
4. Review configuration (sub-steps: check TLS, CORS, cookies, trust boundaries)
5. Consolidate findings (sub-steps: classify severity, include location and rationale)
6. Report (sub-steps: write Markdown report, state verified vs hypothesized)

### Safety Gates
- Read-only: Do not modify source, configuration, or dependencies
- No secret output: Never print secret values
- Approval required before any remediation
- No network exfiltration unless user approves

### Dependencies
Direct: codebase-intelligence
Playbook: playbooks/security-audit.md (3 scenarios)

### Verification
- All 7 required sections present
- Frontmatter complete (all required fields)
- Procedure steps: 6 main steps with 18 sub-steps
- Safety gates: 4 gates documented
- No secrets found in skill file

Exit code: 0.
```

**Expected Output:**
Structured JSON/YAML representation of skill structure with frontmatter, sections, procedures, safety gates, dependencies, and playbook references.

---

## Scenario 2: Skill with missing sections (failure case)

**Trigger:** "Read skill with incomplete structure."

**Invocation:**
```
Read skill draft/SKILL.md. Identify missing sections and incomplete frontmatter.
```

**Execution Log:**
```
## Skill Reading: draft/SKILL.md

### Frontmatter (INCOMPLETE)
{
  "name": "draft",
  "description": "A skill for doing things."
  // Missing: version, tags, dependencies, capabilities
}

### Sections Identified (3 of 7 required)
1. Objective - PRESENT
2. Trigger - PRESENT
3. Procedure - PRESENT (but only 2 steps, no sub-steps)
4. Safety & Approval Gates - MISSING
5. Failure Handling - MISSING
6. Completion Criteria - MISSING
7. Playbook reference - MISSING

### Issues Found
- Frontmatter missing: version, tags, dependencies, capabilities, min_hermes_version, protocol_version
- Missing sections: Safety & Approval Gates, Failure Handling, Completion Criteria, Playbook reference
- Procedure steps lack sub-steps and decision points
- No safety gates documented (critical gap)
- No failure handling documented
- No completion criteria defined

### Recommendations
1. Add missing frontmatter fields
2. Add Safety & Approval Gates section
3. Add Failure Handling section
4. Add Completion Criteria section
5. Add playbook reference
6. Expand procedure with sub-steps and decision points

Exit code: 1 (incomplete skill structure).
```

**Expected Output:**
Reading report identifying missing sections and incomplete frontmatter with specific recommendations.

---

## Scenario 3: Secret detected in skill file (safety case)

**Trigger:** "Read skill that contains a hardcoded secret."

**Invocation:**
```
Read skill legacy/SKILL.md. Check for any hardcoded secrets or credentials.
```

**Execution Log:**
```
## Skill Reading: legacy/SKILL.md

### Frontmatter
{
  "name": "legacy",
  "description": "Legacy skill with hardcoded credentials."
  "version": "1.0.0"
}

### Secret Detection
SCAN RESULTS:
- File: legacy/SKILL.md, Line 23: API_KEY = "sk-1234567890abcdef" (REDACTED)
- File: legacy/SKILL.md, Line 45: password = "admin123" (REDACTED)
- File: legacy/SKILL.md, Line 67: connection_string = "postgres://user:pass@host:5432/db" (REDACTED)

### Safety Action
SECRET VALUES NOT PRINTED. Locations recorded only.

### Recommendations
1. Remove hardcoded secrets from skill file
2. Use environment variables or secret references instead
3. Rotate exposed credentials (assume compromised)
4. Add pre-commit hook to block secret patterns

### Report
Secrets found: 3 locations
No secret values printed anywhere in output
Exit code: 0 (secrets detected and redacted).
```

**Expected Output:**
Reading report flagging secret locations only (no values), with remediation recommendations.
