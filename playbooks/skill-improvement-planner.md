# Playbook: Skill Improvement Planner

*Practical examples for the `skill-improvement-planner` skill*

---

## Scenario 1: Plan improvements for skill with low quality score (happy path)

**Trigger:** "Plan improvements for skill legacy-skill based on comprehension analysis."

**Invocation:**
```
Create improvement plan for skill legacy-skill.
Comprehension analysis shows: Completeness 60%, Clarity 45%, Safety 30%, Testability 20%.
Focus on safety gates and completion criteria first.
```

**Execution Log:**
```
## Skill Improvement Plan: legacy-skill

### Current State
- Effectiveness Score: 45/100
- Completeness: 60% (missing Safety & Approval Gates, Failure Handling)
- Clarity: 45% (vague language in 4 places)
- Safety: 30% (no approval gates, no secret handling)
- Testability: 20% (completion criteria not observable)

### Improvement Actions (Prioritized)

| Priority | Action | Effort | Impact | Dependencies |
|----------|--------|--------|--------|--------------|
| P0 | Add Safety & Approval Gates section | 30 min | HIGH | None |
| P0 | Add Failure Handling section | 30 min | HIGH | Safety gates |
| P0 | Rewrite completion criteria to be observable | 45 min | HIGH | None |
| P1 | Rewrite vague trigger to be specific | 20 min | HIGH | None |
| P1 | Clarify procedure steps 3 and 4 | 45 min | MEDIUM | Trigger rewrite |
| P2 | Add specific tool references | 30 min | MEDIUM | None |
| P2 | Add examples for each procedure step | 60 min | LOW | Procedure clarification |
| P3 | Improve formatting and style | 30 min | LOW | All above |

### Total Estimated Effort: 4.5 hours

### Change Details

**P0 - Add Safety & Approval Gates:**
- Current: No safety section exists
- Proposed: Add section with approval gates for code changes, no-secret logging rule, rollback procedure
- Expected: Skill can be safely used for code modifications

**P0 - Add Failure Handling:**
- Current: No failure handling section
- Proposed: Add section with failure modes (reproduction failure, test failure, build failure) and handling procedures
- Expected: Skill handles failures gracefully

**P0 - Rewrite completion criteria:**
- Current: "Done when it works" (not observable)
- Proposed: "Original failure no longer reproducible," "Regression test passes," "Tests pass before and after"
- Expected: Criteria are observable and measurable

**P1 - Rewrite trigger:**
- Current: "Handle code issues appropriately" (too broad)
- Proposed: "Fix bug in function X," "Resolve error Y in module Z"
- Expected: Clear trigger conditions

### Risk Assessment
- All changes are documentation-only, no behavior changes
- Low risk of breaking existing skill usage
- Rollback: Revert to previous version if issues arise

### Success Criteria
- Effectiveness score increases from 45/100 to 80+/100
- All CONTRIBUTING.md checklist items pass
- Quality-control approval obtained
- Comprehension re-analysis shows improvement

Exit code: 0.
```

**Expected Output:**
Improvement plan with prioritized actions, effort estimates, risk assessment, and success criteria.

---

## Scenario 2: No comprehension analysis available (failure case)

**Trigger:** "Plan improvements without analysis data."

**Invocation:**
```
Create improvement plan for skill unknown-skill.
No comprehension analysis available.
```

**Execution Log:**
```
## Skill Improvement Plan: unknown-skill

### Error
No comprehension analysis available for skill unknown-skill.

### Required Prerequisite
Run skill-comprehension-analyzer on unknown-skill/SKILL.md first to establish baseline quality metrics.

### Manual Analysis Option
If comprehension analysis cannot be run, manual review required:
1. Read skill file manually
2. Compare against CONTRIBUTING.md checklist
3. Document missing sections and issues
4. Create improvement plan based on manual findings

### Status
BLOCKED — Cannot create data-driven improvement plan without comprehension analysis.

Exit code: 1 (missing prerequisite).
```

**Expected Output:**
Improvement plan report showing blocked status with prerequisite requirements.

---

## Scenario 3: High-quality skill with minimal improvements (safety case)

**Trigger:** "Plan improvements for high-quality skill autonomous-debugging."

**Invocation:**
```
Create improvement plan for skill autonomous-debugging.
Current effectiveness score: 97/100.
```

**Execution Log:**
```
## Skill Improvement Plan: autonomous-debugging

### Current State
- Effectiveness Score: 97/100
- Completeness: 100%
- Clarity: 95%
- Safety: 98%
- Testability: 95%

### Improvement Actions (Minimal)

| Priority | Action | Effort | Impact | Dependencies |
|----------|--------|--------|--------|--------------|
| P3 | Add example for each procedure step | 60 min | LOW | None |
| P3 | Add more specific tool version references | 30 min | LOW | None |
| P3 | Add performance notes for large codebases | 45 min | LOW | None |

### Total Estimated Effort: 2.25 hours

### Analysis
Skill is already high quality (97/100). Remaining improvements are cosmetic or additive.
No critical or high-priority improvements needed.

### Recommendation
Do not prioritize improvements for this skill. Focus efforts on lower-quality skills instead.
If improvements are made, they should be additive only (examples, notes) — no structural changes needed.

### Success Criteria
- If improvements made: Effectiveness score remains 97+/100
- No regression in any dimension
- All existing functionality preserved

Exit code: 0.
```

**Expected Output:**
Improvement plan showing minimal improvements for already high-quality skill, with recommendation to focus elsewhere.
