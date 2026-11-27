# Playbook: Skill Documentation Enhancer

*Practical examples for the `skill-documentation-enhancer` skill*

---

## Scenario 1: Enhance documentation with examples and clarity (happy path)

**Trigger:** "Enhance documentation for skill legacy-skill based on improvement plan."

**Invocation:**
```
Apply improvement plan to skill legacy-skill/SKILL.md.
Add examples, clarify procedures, strengthen safety gates.
Validate against CONTRIBUTING.md checklist.
```

**Execution Log:**
```
## Skill Documentation Enhancement: legacy-skill

### Changes Applied

| Change | Location | Before | After |
|--------|----------|--------|-------|
| Clarify trigger language | Trigger section | "Handle code issues appropriately" | "Fix bugs in function X, resolve errors in module Y" |
| Add example to procedure | Procedure Step 2 | "Run tests" | "Run tests: `npm test tests/unit/` — expect 47 tests to pass" |
| Strengthen safety gate | Safety section | "Be careful" | "Approval required before modifying code. No secret logging." |
| Add failure mode | Failure Handling | (missing) | "Test failure: Revert changes, report error, do not proceed" |
| Clarify completion criteria | Completion Criteria | "Done when it works" | "Original failure no longer reproducible, regression test passes" |

### Playbook Enhancements
- Added normal case scenario with execution log
- Added failure case scenario with error handling
- Added safety case scenario with gate triggered

### Validation Results
| Check | Status |
|-------|--------|
| YAML frontmatter valid | PASS |
| All required sections present | PASS |
| No TODO/FIXME/placeholder | PASS |
| Playbook has 3 scenarios | PASS |
| No secrets introduced | PASS |
| Follows repository conventions | PASS |

### Change Log
- 5 documentation changes applied
- 3 playbook scenarios enhanced
- 1 safety gate strengthened
- 0 behavior changes made

### Verification
- Skill still usable for its intended purpose
- No backward compatibility issues
- All conventions followed

Exit code: 0.
```

**Expected Output:**
Enhanced skill documentation with change log and validation results.

---

## Scenario 2: No improvement plan available (failure case)

**Trigger:** "Enhance skill without improvement plan."

**Invocation:**
```
Enhance skill unknown-skill/SKILL.md.
No improvement plan provided.
```

**Execution Log:**
```
## Skill Documentation Enhancement: unknown-skill

### Error
No improvement plan available for skill unknown-skill.

### Required Prerequisite
Run skill-improvement-planner on unknown-skill first to generate an improvement plan.

### Manual Enhancement Option
If enhancement must proceed without a plan:
1. Read skill file manually
2. Identify documentation issues
3. Apply improvements based on best practices
4. Document all changes manually

### Status
BLOCKED — Cannot implement changes without approved improvement plan.

Exit code: 1 (missing prerequisite).
```

**Expected Output:**
Enhancement report showing blocked status with prerequisite requirements.

---

## Scenario 3: Validation fails (safety case)

**Trigger:** "Enhance skill but validation finds issues."

**Invocation:**
```
Apply improvement plan to skill broken-skill/SKILL.md.
Validate against CONTRIBUTING.md checklist.
```

**Execution Log:**
```
## Skill Documentation Enhancement: broken-skill

### Changes Applied
- Clarified trigger language (PASS)
- Added procedure examples (PASS)
- Strengthened safety gates (PASS)

### Validation Results
| Check | Status | Issue |
|-------|--------|-------|
| YAML frontmatter valid | FAIL | Version field missing |
| All required sections present | FAIL | Failure Handling section missing |
| No TODO/FIXME/placeholder | PASS | None found |
| Playbook has 3 scenarios | FAIL | Only 2 scenarios present |
| No secrets introduced | PASS | None found |
| Follows repository conventions | FAIL | Missing sections and version |

### Changes Rolled Back
All changes reverted to pre-enhancement state.

### Required Fixes Before Enhancement
1. Add version field to frontmatter
2. Add Failure Handling section
3. Add third playbook scenario (safety case)
4. Re-run skill-improvement-planner to update plan

### Report
Enhancement: BLOCKED
Validation failures must be fixed before enhancement can proceed.
No changes remain in skill file.

Exit code: 1 (validation failed, changes rolled back).
```

**Expected Output:**
Enhancement report showing validation failures and rollback, with required fixes listed.
