# Contributing to HIJAZ Hermes Skills

Thank you for contributing! This guide ensures skills remain **discoverable, actionable, bounded, safe, testable, and portable**.

---

## 🎯 Skill Design Principles

### 1. Single Responsibility
Each skill does **one thing well**. If you find "and" in the description, split it.

```
❌ "Debug and test and deploy"
✅ "autonomous-debugging" — reproduces, diagnoses, fixes
✅ "autonomous-testing" — designs, executes, reports tests
✅ "workflow-orchestrator" — composes skills into workflows
```

### 2. Explicit Contracts
Every skill declares inputs, outputs, and failure modes in its frontmatter and procedure.

```yaml
# Required frontmatter
---
name: skill-name
description: One sentence, specific trigger + outcome
version: 1.0.0
tags: [category, keyword]
---

# Procedure must define:
inputs:
  - name: repo_root
    type: string
    required: true
outputs:
  - name: architecture_map
    type: CodebaseMap
    required: true
failure_modes:
  - CANNOT_REPRODUCE: "Issue not reproducible, hypotheses listed"
  - BLOCKED: "Awaiting approval/gate"
```

### 3. Bounded Scope
Skills **never** claim capabilities they don't have.

```
❌ "Fixes any bug automatically"
✅ "Fixes demonstrated root cause with smallest safe patch. Plausible edit ≠ verified fix."
```

### 4. Safety First
- **Approval gates** for destructive actions
- **No secrets** in logs, outputs, or prompts
- **Privacy gates** for data classification
- **Budget limits** with hard stops

### 5. Testable & Verifiable
- Completion criteria are **observable**, not aspirational
- Playbook examples show real tool output
- Regression tests included in fix procedures

---

## 📝 Creating a New Skill

### Step 1: Check for Duplicates
Search `SKILLS.md` and existing skills. Is there a skill that covers 80% of your use case? **Extend it** instead.

### Step 2: Define the Trigger
```markdown
## Trigger
- "User says: 'X'"
- "Situation: Y occurs"
- "Anti-trigger: 'Z' — NOT this skill"
```

### Step 3: Write the Skill
Use the template in `skills/skill-creator/SKILL.md` as reference.

**Required sections:**
1. YAML frontmatter (`name`, `description`, `version`, `tags`)
2. Objective (one paragraph)
3. Trigger/Use Cases
4. Procedure (numbered steps with decision points)
5. Safety & Approval Gates
6. Failure Handling
7. Completion Criteria (observable)

### Step 4: Create a Playbook
Add `playbooks/your-skill.md` with **3+ scenarios**:
- Normal case (happy path)
- Failure case (graceful handling)
- Safety case (gate triggered)

Each scenario shows:
- Invocation (what user says)
- Execution log (tool calls, output)
- Expected output format

### Step 5: Validate
Run the validation checklist (see below).

### Step 6: Update Registry
Add entry to `SKILLS.md`:
- Catalog table
- Category
- Composition patterns
- Capability matrix
- Quick reference card

---

## ✅ Validation Checklist

Before submitting a skill, verify:

### Structure
- [ ] YAML frontmatter: `name`, `description`, `version`, `tags`
- [ ] All required sections present
- [ ] No `TODO`, `FIXME`, or placeholder commands

### Correctness
- [ ] Every referenced tool/command verified in target runtime
- [ ] Every file path exists or is clearly marked as example
- [ ] No contradictions between sections
- [ ] No vague phrases ("do everything", "handle appropriately")

### Safety
- [ ] Approval gates for: writes, deploys, secrets, external mutations, budget
- [ ] No secret logging/printing
- [ ] Privacy gates for data classification
- [ ] Failure modes include `BLOCKED` for gates

### Testability
- [ ] Completion criteria are observable (exit codes, artifacts, reports)
- [ ] Distinguishes verified vs hypothesized vs not-run
- [ ] Playbook includes 3 scenarios with tool evidence

### Portability
- [ ] No hardcoded paths (use `repository_root`, `config_dir`)
- [ ] No assumed connectors (document required runtime capabilities)
- [ ] Degrades gracefully when optional features unavailable

### Documentation
- [ ] Playbook created with 3 scenarios
- [ ] `SKILLS.md` updated
- [ ] Quick reference card added

---

## 🧪 Testing Skills

### Unit Testing (Skill Logic)
```bash
# Validate frontmatter
yq '.name, .description' skills/your-skill/SKILL.md

# Check references
grep -oP '`[^`]+`' skills/your-skill/SKILL.md | sort -u | xargs -I{} which {}
```

### Integration Testing (Runtime)
```bash
# Test in isolated workspace
mkdir -p /tmp/skill-test
cd /tmp/skill-test
git clone <test-repo>
cd <test-repo>

# Run skill via Hermes
hermes run your-skill --goal "Test scenario from playbook"

# Verify output matches playbook
diff expected-output.md actual-output.md
```

### Playbook Validation
Each playbook scenario must be **reproducible**:
1. Set up test repository (or use fixture)
2. Run exact invocation from playbook
3. Verify output matches documented structure
4. Check all evidence artifacts produced

---

## 🔄 Improving Existing Skills

### Types of Improvements
| Type | Example | Process |
|------|---------|---------|
| **Bug fix** | Incorrect command in procedure | Direct fix + test |
| **Clarification** | Ambiguous step | Rewrite step + add example |
| **Extension** | Add TypeScript support to debugging | Follow "Creating New Skill" for delta |
| **Safety** | Add missing approval gate | Add gate + update failure modes |
| **Performance** | Reduce token usage in model-router | Benchmark before/after |

### Change Process
1. Open issue describing the gap
2. Reference playbook scenario that fails
3. Make minimal change
4. Update playbook if behavior changes
5. Re-run validation checklist
6. Update `SKILLS.md` if metadata changes

---

## 📦 Release Process

### Versioning
Skills use **semantic versioning** in frontmatter:
- `MAJOR`: Breaking procedure change (rename, remove step, change contract)
- `MINOR`: New capability, backward compatible (add step, new output)
- `PATCH`: Clarification, bug fix, playbook update

### Release Checklist
- [ ] Version bumped in frontmatter
- [ ] `CHANGELOG.md` updated (per skill or root)
- [ ] All validation checks pass
- [ ] Playbook scenarios verified
- [ ] `SKILLS.md` registry updated
- [ ] Tagged: `skill-name-v1.2.0`

---

## 🏷️ Skill Categories & Tags

Use consistent tags for discovery:

| Category | Tags |
|----------|------|
| Reconnaissance | `reconnaissance`, `analysis`, `mapping` |
| Remediation | `remediation`, `debugging`, `fix` |
| Verification | `verification`, `testing`, `quality` |
| Governance | `governance`, `review`, `security` |
| Infrastructure | `infrastructure`, `routing`, `models` |
| Meta | `meta`, `skill-creation`, `maintenance` |
| Orchestration | `orchestration`, `workflow`, `composition` |

---

## 📋 Pull Request Template

```markdown
## Skill: [name]

### Change Type
- [ ] New skill
- [ ] Bug fix
- [ ] Enhancement
- [ ] Documentation only

### Description
[What changed and why]

### Validation
- [ ] Frontmatter valid
- [ ] All commands verified
- [ ] Playbook scenarios tested
- [ ] SKILLS.md updated
- [ ] Version bumped (if applicable)

### Testing
- Test repo: [link or description]
- Command run: `hermes run skill-name --goal "..."`
- Output verified: [how]

### Safety
- [ ] No new secret exposure
- [ ] Approval gates appropriate
- [ ] Failure modes cover new paths
```

---

## 🎖️ Recognition

Contributors are recognized in:
- Skill frontmatter `owner` field
- `CONTRIBUTORS.md` (root)
- Release notes

---

## ❓ Questions?

- Check existing skills for patterns
- Review `skill-creator` skill for meta-guidance
- Open a discussion issue for design questions
- Playbooks are the ground truth — if skill and playbook disagree, **playbook wins**

---

*Quality over quantity. One well-tested skill > ten aspirational ones.*