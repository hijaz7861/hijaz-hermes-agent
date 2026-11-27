# Playbook: Skill Comprehension Analyzer

*Practical examples for the `skill-comprehension-analyzer` skill*

---

## Scenario 1: Complete skill quality analysis (happy path)

**Trigger:** "Analyze skill code-refactorer for quality and completeness."

**Invocation:**
```
Analyze skill code-refactorer/SKILL.md for quality, completeness, safety, and testability. Provide effectiveness score and improvement recommendations.
```

**Execution Log:**
```
## Skill Comprehension Analysis: code-refactorer

### Intent Summary
Primary purpose: Perform safe, behavior-preserving code transformations with test verification.
Target audience: Developers performing refactoring tasks.
Boundaries: Behavior-preserving only; no behavior change without explicit authorization.
Trigger-procedure alignment: TRIGGER and PROCEDURE are well-aligned.

### Quality Assessment
| Dimension | Score | Details |
|-----------|-------|---------|
| Completeness | 95% | All 7 sections present, frontmatter complete |
| Clarity | 88% | Steps are specific, some decision points could be clearer |
| Safety | 92% | Approval gates present, no-secret logging, rollback documented |
| Testability | 85% | Completion criteria observable, tests mentioned |

### Procedure Analysis
- Total steps: 6 main steps with 18 sub-steps
- Decision points: 3 (insufficient test coverage, test failure, caller missed)
- Tool references: 4 (codebase-intelligence, autonomous-testing, lint, typecheck)
- Step ordering: LOGICAL (analyze → baseline → design → apply → verify → report)
- Vague language: 0 instances found

### Safety Analysis
- Approval gates: 4 (behavior change, public API, test gate, rollback)
- No-secret logging: Documented
- Privacy gates: Not applicable (code refactoring)
- Failure modes: 5 (insufficient coverage, test failure, typecheck failure, caller missed, rollback)
- Rollback procedure: Documented (pre-refactor state recording)

### Completion Criteria Analysis
- Observable: YES (tests pass before/after, lint clean, behavior contract preserved)
- Measurable: YES (test pass rate, typecheck status)
- Testable: YES (all criteria can be verified)
- Complete: YES (covers all procedure outcomes)

### Effectiveness Score: 90/100
Breakdown: Completeness 95% (30%), Clarity 88% (25%), Safety 92% (25%), Testability 85% (20%)

### Improvement Recommendations
1. Add more specific examples for each refactoring type
2. Clarify decision point for "caller missed" scenario
3. Add example of behavior contract documentation
4. Add example rollback scenario in playbook

Exit code: 0.
```

**Expected Output:**
Comprehension report with intent summary, quality scores, procedure/safety/completion analysis, effectiveness score, and improvement recommendations.

---

## Scenario 2: Skill with vague language (failure case)

**Trigger:** "Analyze skill with vague procedure language."

**Invocation:**
```
Analyze skill vague-skill/SKILL.md. Identify vague language and unclear steps.
```

**Execution Log:**
```
## Skill Comprehension Analysis: vague-skill

### Intent Summary
Primary purpose: Unclear from description ("Do things with code").
Target audience: Unknown.
Boundaries: Not clearly defined.
Trigger-procedure alignment: POOR (trigger says "fix bugs" but procedure says "refactor code").

### Quality Assessment
| Dimension | Score | Details |
|-----------|-------|---------|
| Completeness | 60% | Missing Safety & Approval Gates, Failure Handling |
| Clarity | 45% | Multiple vague phrases, unclear steps |
| Safety | 30% | No approval gates, no secret handling |
| Testability | 20% | Completion criteria not observable |

### Vague Language Found
| Location | Text | Issue |
|----------|------|-------|
| Trigger | "Handle code issues appropriately" | Too broad, no specific trigger |
| Procedure Step 3 | "Fix the problems" | No specific problems identified |
| Procedure Step 4 | "Test as needed" | No criteria for when testing is needed |
| Safety | "Be careful with secrets" | No specific secret handling procedure |
| Completion | "Done when it works" | Not observable or measurable |

### Missing Sections
- Safety & Approval Gates: MISSING (critical gap)
- Failure Handling: MISSING
- Completion Criteria: PRESENT but not observable

### Recommendations
1. Rewrite trigger to be specific and measurable
2. Define specific problems to fix in procedure
3. Add Safety & Approval Gates section
4. Add Failure Handling section
5. Rewrite completion criteria to be observable and measurable
6. Add specific tool references and commands

### Effectiveness Score: 45/100

Exit code: 1 (low quality skill).
```

**Expected Output:**
Comprehension report identifying vague language, missing sections, and low effectiveness score with specific recommendations.

---

## Scenario 3: High-quality skill as reference (safety case)

**Trigger:** "Analyze skill autonomous-debugging as a reference for quality."

**Invocation:**
```
Analyze skill autonomous-debugging/SKILL.md as a high-quality reference. Document best practices observed.
```

**Execution Log:**
```
## Skill Comprehension Analysis: autonomous-debugging (Reference)

### Intent Summary
Primary purpose: Reproduce and resolve software defects using controlled experiments, root-cause analysis and regression verification.
Target audience: Software engineers debugging defects.
Boundaries: Fix demonstrated root cause with smallest safe patch; no behavior change without authorization.
Trigger-procedure alignment: EXCELLENT.

### Quality Assessment
| Dimension | Score | Details |
|-----------|-------|---------|
| Completeness | 100% | All 7 sections present, frontmatter complete with all fields |
| Clarity | 95% | Steps are specific, decision points clear, tool references verified |
| Safety | 98% | Approval gates, no-secret logging, rollback, escalation all documented |
| Testability | 95% | Completion criteria observable and measurable, regression test required |

### Best Practices Observed
1. **Clear trigger definition**: Specific triggers and anti-triggers listed
2. **Numbered procedure**: 7 steps with clear sub-steps and decision points
3. **Tool references**: Specific commands (tsc --noEmit, test runners) mentioned
4. **Safety gates**: Escalation and approval section with specific triggers
5. **Regression test requirement**: Explicitly requires regression test before fix
6. **Observable completion criteria**: "Original failure no longer reproducible" + "regression check protects behavior"
7. **Error handling**: Separate verified fixes from hypotheses
8. **Report structure**: Separate verified from hypothesized findings

### Effectiveness Score: 97/100

### Recommended as Reference Skill
This skill serves as an excellent reference for:
- Procedure structure and clarity
- Safety gate documentation
- Completion criteria observability
- Regression test requirements
- Error handling and hypothesis separation

Exit code: 0.
```

**Expected Output:**
Comprehension report identifying best practices and recommending the skill as a reference for quality.
