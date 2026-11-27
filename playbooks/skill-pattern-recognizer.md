# Playbook: Skill Pattern Recognizer

*Practical examples for the `skill-pattern-recognizer` skill*

---

## Scenario 1: Identify common patterns across security skills (happy path)

**Trigger:** "Find patterns across security-related skills."

**Invocation:**
```
Analyze skills security-audit, security-debugger, security-review, dependency-management for common patterns.
Identify structural, procedure, safety, and combination patterns.
```

**Execution Log:**
```
## Skill Pattern Recognition: Security Skills

### Skills Analyzed (4)
- security-audit
- security-debugger  
- security-review
- dependency-management

### Common Structural Patterns
| Pattern | Frequency | Example Skills |
|---------|-----------|----------------|
| Section order: Objective → Trigger → Procedure → Safety → Failure → Completion | 4/4 | All 4 skills |
| Frontmatter fields: name, description, version, tags, dependencies | 4/4 | All 4 skills |
| Dependencies include codebase-intelligence | 3/4 | security-audit, security-debugger, dependency-management |

### Common Procedure Patterns
| Pattern | Frequency | Description |
|---------|-----------|-------------|
| Read-only analysis first, then act | 4/4 | All skills analyze before modifying |
| Verification step included | 4/4 | All skills verify results after action |
| Rollback on failure | 3/4 | security-audit, security-debugger, dependency-management |

### Common Safety Patterns
| Pattern | Frequency | Description |
|---------|-----------|-------------|
| Approval required before code changes | 4/4 | All skills require approval |
| No secret logging | 4/4 | All skills redact secret values |
| Read-only by default | 4/4 | All skills start as read-only |

### Combination Opportunities
| Skills | Combined Capability | Rationale |
|--------|-------------------|-----------|
| security-audit + dependency-management | Security dependency audit | Both audit dependencies, combine for security-focused audit |
| security-debugger + security-audit | Security incident response | Debug findings from security audit |
| security-review + security-audit | Security review with audit scan | Review changes with security scan |

### Anti-Patterns Found
| Pattern | Frequency | Skills |
|---------|-----------|--------|
| Vague trigger language | 0/4 | None (all have specific triggers) |
| Missing safety gates | 0/4 | None (all have safety gates) |
| Unclear completion criteria | 0/4 | None (all have observable criteria) |

### Pattern Strength
- Strongest pattern: Read-only analysis first (4/4 = 100%)
- Second strongest: No secret logging (4/4 = 100%)
- Third strongest: Approval required before changes (4/4 = 100%)

Exit code: 0.
```

**Expected Output:**
Pattern report with identified patterns, frequency, examples, combination opportunities, and anti-patterns.

---

## Scenario 2: No common patterns found (failure case)

**Trigger:** "Find patterns across unrelated skills."

**Invocation:**
```
Analyze skills codebase-intelligence, observability-instrumenter, agentic-routing for common patterns.
These skills have different purposes and domains.
```

**Execution Log:**
```
## Skill Pattern Recognition: Unrelated Skills

### Skills Analyzed (3)
- codebase-intelligence (Reconnaissance)
- observability-instrumenter (DevOps & Infrastructure)
- agentic-routing (Multi-Agent Orchestration)

### Common Structural Patterns
| Pattern | Frequency | Skills |
|---------|-----------|--------|
| Section order: Objective → Trigger → Procedure → Safety → Failure → Completion | 3/3 | All 3 skills |
| Frontmatter fields present | 3/3 | All 3 skills |

### Common Procedure Patterns
| Pattern | Frequency | Skills |
|---------|-----------|--------|
| No common procedure patterns found | 0/3 | None |

### Common Safety Patterns
| Pattern | Frequency | Skills |
|---------|-----------|--------|
| Approval required before changes | 2/3 | observability-instrumenter, agentic-routing |
| No secret logging | 3/3 | All 3 skills |

### Combination Opportunities
| Skills | Combined Capability | Rationale |
|---------|-------------------|-----------|
| codebase-intelligence + observability-instrumenter | Code observability | Map code then instrument it |
| observability-instrumenter + agentic-routing | Observable agentic execution | Instrument code then route agentically |
| codebase-intelligence + agentic-routing | Intelligent agentic planning | Map code then plan routes |

### Anti-Patterns Found
None found.

### Pattern Strength
- Weakest commonality: Only structural patterns shared (section order, frontmatter)
- No procedure patterns shared (different domains, different procedures)
- Limited combination value (3 possible combinations, but each serves different purpose)

Exit code: 0.
```

**Expected Output:**
Pattern report showing limited commonality between unrelated skills, with only structural patterns shared.

---

## Scenario 3: Anti-patterns detected (safety case)

**Trigger:** "Find anti-patterns in skill set."

**Invocation:**
```
Scan skills for anti-patterns: vague triggers, missing safety gates, unclear completion criteria.
```

**Execution Log:**
```
## Skill Pattern Recognition: Anti-Pattern Detection

### Skills Analyzed (5)
- skill-a, skill-b, skill-c, skill-d, skill-e

### Anti-Patterns Found
| Pattern | Frequency | Skills | Severity |
|---------|-----------|--------|----------|
| Vague trigger: "Handle things appropriately" | 2/5 | skill-a, skill-c | HIGH |
| Missing Safety & Approval Gates section | 1/5 | skill-b | CRITICAL |
| Missing Failure Handling section | 2/5 | skill-b, skill-d | HIGH |
| Completion criteria not observable: "Done when it works" | 2/5 | skill-c, skill-e | HIGH |
| Unclear trigger: too broad ("Fix code issues") | 1/5 | skill-d | MEDIUM |
| No tool references in procedure | 3/5 | skill-a, skill-b, skill-e | MEDIUM |

### Detailed Findings
1. skill-b: Missing Safety & Approval Gates section — CRITICAL — no approval gates for code modifications
2. skill-c: Vague trigger + unobservable criteria — HIGH — cannot determine when skill applies or when done
3. skill-e: Vague trigger + no tool references + unobservable criteria — HIGH — multiple issues

### Recommendations
1. skill-b: Add Safety & Approval Gates section immediately
2. skill-c: Rewrite trigger to be specific, rewrite completion criteria to be observable
3. skill-e: Complete rewrite of trigger, procedure, and completion criteria
4. All skills: Add specific tool references to procedures

### Pattern Frequency
- Most common anti-pattern: Missing tool references (3/5 = 60%)
- Most severe anti-pattern: Missing safety gates (1/5 = 20%, but CRITICAL severity)

Exit code: 1 (anti-patterns detected).
```

**Expected Output:**
Pattern report identifying anti-patterns with frequency, severity, and specific recommendations.
