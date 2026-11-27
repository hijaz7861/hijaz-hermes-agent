# Playbook: Skill Template Generator

*Practical examples for the `skill-template-generator` skill*

---

## Scenario 1: Generate skill template for reconnaissance category (happy path)

**Trigger:** "Generate skill template for reconnaissance skills."

**Invocation:**
```
Generate SKILL.md and playbook template for a reconnaissance skill.
Category: reconnaissance. Target: skills that map and analyze codebases.
Use patterns from codebase-intelligence as reference.
```

**Execution Log:**
```
## Skill Template Generation: Reconnaissance Category

### Pattern Source
Analyzed skills: codebase-intelligence, codebase-intelligence
Common patterns:
- Section order: Objective → Trigger → Procedure → Safety → Failure → Completion
- Dependencies: codebase-intelligence (self-reference for category skills)
- Tags: reconnaissance, analysis, mapping
- Safety: Read-only by default, no secret logging

### SKILL.md Template Generated
---
name: [skill-name]
description: [One sentence description of what the skill does and when to use it.]
version: 1.0.0
tags: [reconnaissance, analysis, mapping]
dependencies: [codebase-intelligence]
---

# [Skill Name]

## Objective
[One paragraph describing the skill's purpose and when to use it.]

## Trigger
- "[Specific trigger phrase 1]"
- "[Specific trigger phrase 2]"
Anti-triggers: "[What this skill does NOT do]"

## Inputs
- [Input 1]: [Description]
- [Input 2]: [Description]

## Outputs
- [Output 1]: [Description]
- [Output 2]: [Description]

## Procedure
1. **[Step 1 name]**
   - [Sub-step]
   - [Sub-step]
2. **[Step 2 name]**
   - [Sub-step]
   ...

## Safety & Approval Gates
- **Read-only:** [Read-only statement]
- **No secret logging:** [Secret handling statement]
- **Approval required:** [When approval is needed]

## Failure Handling
- [Failure mode 1]: [Handling procedure]
- [Failure mode 2]: [Handling procedure]

## Completion Criteria
- [Observable criterion 1]
- [Observable criterion 2]

### Playbook Template Generated
Scenario 1: Normal case (happy path)
- Trigger: [Specific scenario]
- Invocation: [Exact invocation]
- Execution Log: [Template with expected output]
- Expected Output: [Description]

Scenario 2: Failure case
- Trigger: [Failure scenario]
- Invocation: [Exact invocation]
- Execution Log: [Template with error handling]
- Expected Output: [Description]

Scenario 3: Safety case
- Trigger: [Safety scenario]
- Invocation: [Exact invocation]
- Execution Log: [Template with gate triggered]
- Expected Output: [Description]

### Validation
- All required sections present: YES
- Frontmatter fields complete: YES
- Playbook has 3 scenarios: YES
- Follows repository conventions: YES

Exit code: 0.
```

**Expected Output:**
Generated SKILL.md template and playbook template with pattern references and usage instructions.

---

## Scenario 2: Unknown category (failure case)

**Trigger:** "Generate template for unknown category."

**Invocation:**
```
Generate skill template for category "quantum-computing".
This category does not exist in the skills repository.
```

**Execution Log:**
```
## Skill Template Generation: Unknown Category

### Category Analysis
Category "quantum-computing" not found in skills repository.
Existing categories: Reconnaissance, Remediation, Verification, Governance, Infrastructure, Meta, Orchestration, Performance Optimization, Software Engineering, Documentation, DevOps & Infrastructure, AI Agent Development, Multi-Agent Orchestration, Factory Engineering, Meta-Engineering.

### Options
1. Use closest existing category: "Research & Intelligence" (closest match for quantum computing)
2. Create new category "Quantum Computing" (requires category creation workflow)
3. Use generic template without category-specific patterns

### Decision
Option 1 selected: Use "Research & Intelligence" category patterns as base.

### SKILL.md Template Generated (using Research & Intelligence patterns)
---
name: [skill-name]
description: [One sentence description.]
version: 1.0.0
tags: [research, analysis, intelligence]
dependencies: []
---

# [Skill Name]

## Objective
[Paragraph describing purpose.]

## Trigger
- "[Specific trigger]"
Anti-triggers: "[What this skill does NOT do]"

## Procedure
1. Research the topic
2. Analyze findings
3. Document results
4. Report findings

## Safety & Approval Gates
- **Read-only:** Research only, no modifications
- **No secret logging:** Do not log sensitive information

## Failure Handling
- [Failure mode]: [Handling]

## Completion Criteria
- [Observable criterion]

### Warning
Category "quantum-computing" does not exist. Template uses closest match "Research & Intelligence".
Consider creating the category first using category-organizer skill.

Exit code: 0 (template generated with warning).
```

**Expected Output:**
Template generated using closest matching category, with warning about unknown category.

---

## Scenario 3: Template validation fails (safety case)

**Trigger:** "Generate template and validate against repository conventions."

**Invocation:**
```
Generate skill template and validate against CONTRIBUTING.md checklist.
```

**Execution Log:**
```
## Skill Template Generation: With Validation

### Template Generated
SKILL.md and playbook template created.

### Validation Results
| Check | Status | Details |
|-------|--------|---------|
| YAML frontmatter: name, description, version, tags | PASS | All fields present |
| All required sections present | PASS | Objective, Trigger, Procedure, Safety, Failure, Completion |
| No TODO/FIXME/placeholder | PASS | No placeholders found |
| Playbook has 3 scenarios | PASS | Normal, failure, safety scenarios present |
| Commands verified | FAIL | Command "hermes" not found in environment |
| References exist | PASS | All referenced skills exist |

### Validation Issue
Command "hermes" referenced in template invocation examples but not found in PATH.
This is expected — "hermes" is the Hermes CLI which may not be installed in all environments.

### Resolution
Template updated to mark "hermes" command as example only:
```
# Example invocation (requires Hermes CLI):
hermes run [skill-name] --goal "..."
```

### Re-validation
- All checks: PASS

Exit code: 0.
```

**Expected Output:**
Template generation report with validation results and issue resolution.
