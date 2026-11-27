# Playbook: Skill Launcher

*Practical examples for the `skill-launcher` skill*

---

## Scenario 1: Launch skill with valid inputs (happy path)

**Trigger:** "Launch codebase-intelligence skill on this repository."

**Invocation:**
```
Launch skill codebase-intelligence with inputs:
- Target: current repository (/workspace/app)
- Read scope: full structure
- Parse depth: detailed
Output format: structured JSON
```

**Execution Log:**
```
## Skill Launch: codebase-intelligence

### Validation
- Skill exists: skills/codebase-intelligence/SKILL.md ✅
- Version: 1.0.0, compatible ✅
- Dependencies: none required ✅

### Input Validation
- Target: /workspace/app (valid path) ✅
- Read scope: full structure (valid) ✅
- Parse depth: detailed (valid) ✅

### Execution Context
- Repository: /workspace/app
- Branch: kilo/hearty-sequoia-b6b
- User permissions: read access ✅
- Time budget: 30 minutes ✅

### Safety Gates Check
- Approval required: No (read-only skill) ✅
- Privacy gates: No confidential data ✅
- Resource limits: Within budget ✅

### Execution
- Skill invoked with validated inputs
- Execution time: 4.2 minutes
- Tool calls: 23 (glob, grep, read, etc.)
- Output collected: structured JSON

### Output Validation
- Output format: valid JSON ✅
- All expected fields present: ✅
- No secrets in output: ✅

### Audit Trail Recorded
- Skill: codebase-intelligence
- Inputs: {target: "/workspace/app", scope: "full", depth: "detailed"}
- Output: architecture map with 12 sections
- Execution time: 4.2 min
- Timestamp: 2026-11-27T10:30:00Z

### Report
- Skill executed successfully
- Exit code: 0
- Output: architecture map saved to output directory
- Audit trail: complete

Exit code: 0.
```

**Expected Output:**
Skill launch report with execution result, evidence log, performance metrics, and audit trail.

---

## Scenario 2: Input validation fails (failure case)

**Trigger:** "Launch skill with invalid inputs."

**Invocation:**
```
Launch skill autonomous-debugging with inputs:
- Target: /nonexistent/path
- Error: ""
```

**Execution Log:**
```
## Skill Launch: autonomous-debugging

### Validation
- Skill exists: skills/autonomous-debugging/SKILL.md ✅

### Input Validation (FAILED)
- Target: /nonexistent/path → INVALID (path does not exist)
- Error: "" → INVALID (empty string, required field)

### Validation Errors
1. Target path /nonexistent/path does not exist
2. Error field is empty, required field

### Execution Blocked
- Skill NOT executed
- Reason: input validation failed
- User notified with specific validation errors

### Report
- Skill launch blocked due to invalid inputs
- Exit code: 1
- Fix: Provide valid target path and non-empty error description

Exit code: 1.
```

**Expected Output:**
Skill launch report showing validation errors and blocked execution with specific error messages.

---

## Scenario 3: Safety gate violation (safety case)

**Trigger:** "Launch skill that modifies production code without approval."

**Invocation:**
```
Launch skill code-refactorer on production repository.
Target: /production/repo
Changes: modify source files
Approval: none provided
```

**Execution Log:**
```
## Skill Launch: code-refactorer

### Validation
- Skill exists: skills/code-refactorer/SKILL.md ✅
- Inputs: valid ✅

### Safety Gates Check
- Approval required: YES (code modification skill)
- Approval provided: NO
- Gate: BLOCKED

### Execution Blocked
- Skill NOT executed
- Reason: safety gate violation
- Gate: Approval required for code modification
- User notified: "This skill modifies code. Explicit approval required."

### Alternative Suggestions
- Use codebase-intelligence for read-only analysis (no approval needed)
- Request approval for code-refactorer execution
- Use skill-suggestion-engine to find read-only alternatives

### Report
- Skill launch blocked due to safety gate violation
- Exit code: 1
- No changes made to production repository
- Audit trail: gate violation recorded

Exit code: 1.
```

**Expected Output:**
Skill launch report showing safety gate violation, blocked execution, and alternative suggestions.
