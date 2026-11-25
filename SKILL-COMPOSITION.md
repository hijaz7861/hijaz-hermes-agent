# Skill Composition Patterns

*Advanced patterns for combining HIJAZ Hermes skills into powerful workflows*

---

## Composition Philosophy

Skills are **composable primitives**, not monolithic workflows. The orchestrator skill (`workflow-orchestrator`) provides the runtime for composition, but understanding patterns helps you design effective workflows manually or via the orchestrator.

---

## Pattern 1: Sequential Pipeline (Linear)

**Structure:** `Skill A → Skill B → Skill C → ...`

**Use when:** Each step depends on the previous step's output.

### Canonical Example: Bug Fix Pipeline
```
codebase-intelligence 
  → autonomous-debugging 
  → multi-agent-review 
  → autonomous-testing
```

**Data Flow:**
```
Repo Map → Root Cause + Fix → Review Findings → Test Evidence → Final Report
```

**Orchestrator Config:**
```yaml
dag:
  - id: map
    skill: codebase-intelligence
    input: { target: "auth/login" }
  - id: debug
    skill: autonomous-debugging
    input: { map: "{{map.output}}", error: "login timeout" }
    depends_on: [map]
  - id: review
    skill: multi-agent-review
    input: { diff: "{{debug.output.fix}}" }
    depends_on: [debug]
    gate: approval_required
  - id: test
    skill: autonomous-testing
    input: { scope: "auth", fix: "{{debug.output.fix}}" }
    depends_on: [review]
```

---

## Pattern 2: Parallel Fan-Out (Map)

**Structure:** `Skill A → [Skill B1, Skill B2, Skill B3] → Skill C`

**Use when:** Multiple independent analyses can run simultaneously.

### Canonical Example: Security Audit
```
codebase-intelligence
  → [static-analysis, dependency-audit, secret-scan, config-review]
  → multi-agent-review (consolidate)
  → autonomous-testing (security tests)
```

**Data Flow:**
```
Repo Map → [4 Parallel Security Scans] → Consolidated Findings → Review → Security Tests
```

**Orchestrator Config:**
```yaml
dag:
  - id: map
    skill: codebase-intelligence
    input: { target: "security" }
  - id: static
    skill: static-analysis      # hypothetical skill
    input: { map: "{{map.output}}" }
    depends_on: [map]
  - id: deps
    skill: dependency-audit     # hypothetical skill
    input: { map: "{{map.output}}" }
    depends_on: [map]
  - id: secrets
    skill: secret-scan          # hypothetical skill
    input: { map: "{{map.output}}" }
    depends_on: [map]
  - id: config
    skill: config-review        # hypothetical skill
    input: { map: "{{map.output}}" }
    depends_on: [map]
  - id: consolidate
    skill: multi-agent-review
    input: 
      findings: 
        - "{{static.output}}"
        - "{{deps.output}}"
        - "{{secrets.output}}"
        - "{{config.output}}"
    depends_on: [static, deps, secrets, config]
```

---

## Pattern 3: Parallel Fan-In (Reduce)

**Structure:** `[Skill A1, Skill A2] → Skill B`

**Use when:** Multiple independent inputs feed into a single synthesis step.

### Canonical Example: PR Review Preparation
```
[codebase-intelligence (PR changes), autonomous-testing (affected tests)] 
  → multi-agent-review
```

**Data Flow:**
```
[Change Map, Test Baseline] → Reviewer has full context
```

---

## Pattern 4: Conditional Branching

**Structure:** `Skill A → (Condition) → Skill B | Skill C`

**Use when:** Next step depends on analysis results.

### Canonical Example: Smart Debugging
```
codebase-intelligence
  → autonomous-debugging
  → (root_cause.severity == "critical") 
       ? multi-agent-review 
       : autonomous-testing
```

**Orchestrator Config:**
```yaml
dag:
  - id: map
    skill: codebase-intelligence
  - id: debug
    skill: autonomous-debugging
    depends_on: [map]
  - id: review
    skill: multi-agent-review
    depends_on: [debug]
    condition: "{{debug.output.root_cause.severity}} == 'critical'"
  - id: test
    skill: autonomous-testing
    depends_on: [debug]
    condition: "{{debug.output.root_cause.severity}} != 'critical'"
```

---

## Pattern 5: Iterative Refinement (Loop)

**Structure:** `while (condition) { Skill A → Skill B }`

**Use when:** Repeated application until quality threshold met.

### Canonical Example: Test Coverage Improvement
```
while (coverage < 80%) {
  autonomous-testing (generate tests for uncovered)
  → codebase-intelligence (map new coverage)
}
```

**Orchestrator Config:**
```yaml
loop:
  max_iterations: 5
  condition: "{{coverage.output.percent}} < 80"
  body:
    - id: test_gen
      skill: autonomous-testing
      input: { target_coverage: 80, gaps: "{{coverage.output.gaps}}" }
    - id: coverage
      skill: codebase-intelligence
      input: { target: "test_coverage" }
      depends_on: [test_gen]
```

---

## Pattern 6: Human-in-the-Loop (Gated)

**Structure:** `Skill A → [GATE: Human Approval] → Skill B`

**Use when:** Critical decisions require human judgment.

### Canonical Example: Production Deployment
```
autonomous-testing (full suite)
  → [GATE: Release Approval]
  → deploy (hypothetical skill)
  → rollback-test
```

**Gate Types:**
| Gate Type | Trigger | Resolver |
|-----------|---------|----------|
| `approval` | Any write/deploy | User |
| `security_review` | Critical findings | Security team |
| `budget_check` | Cost > 80% | Orchestrator (auto) |
| `policy_check` | Confidential data | Policy engine |

---

## Pattern 7: Composite Skill (Encapsulation)

**Structure:** Single skill that internally sequences other skills.

**Use when:** Pattern is reusable, should be invokable as one unit.

### Example: `test-planning` Skill (from playbooks)
```
Internally:
  1. codebase-intelligence (map impact)
  2. autonomous-testing (prioritize risks)
  3. Produce test plan document

Externally:
  invoke test-planning → get test plan
```

**Benefits:**
- Single entry point
- Hidden complexity
- Versioned as unit
- Discoverable in skill registry

---

## Pattern 8: Skill Adapter (Translation)

**Structure:** Wrapper that translates between skill interfaces.

**Use when:** Skills have incompatible input/output formats.

### Example: Legacy Tool Integration
```
legacy-linter (outputs custom format)
  → adapter (transforms to standard format)
  → multi-agent-review (consumes standard format)
```

**Adapter Pattern:**
```typescript
// Adapter skill fragment
function adaptLegacyLintOutput(legacyOutput: LegacyFormat): StandardFindings {
  return {
    findings: legacyOutput.issues.map(i => ({
      file: i.path,
      line: i.line,
      severity: mapSeverity(i.level),
      message: i.message,
      rule: i.ruleId
    }))
  };
}
```

---

## Pattern 9: Fallback Chain (Resilience)

**Structure:** `Skill A (primary) → [on failure] → Skill B (fallback) → Skill C (last resort)`

**Use when:** Primary approach may fail, need graceful degradation.

### Canonical Example: Model Routing with Fallbacks
```
model-router (primary: claude-3.5-sonnet)
  → [on rate_limit] → model-router (fallback: gpt-4o)
  → [on rate_limit] → model-router (fallback: deepseek-coder)
  → [on all_fail] → FAIL (no silent degradation)
```

---

## Pattern 10: Observability Wrapper (Instrumentation)

**Structure:** `Skill A → [Instrument] → Skill A'`

**Use when:** Need metrics, tracing, audit without modifying skill.

### Example: Instrumented Debugging
```
autonomous-debugging
  → wrapper adds:
    - Start/end timestamps
    - Token usage tracking
    - Decision logging
    - Cost attribution
  → outputs enriched evidence
```

---

## Composition Matrix

| Pattern | Complexity | Parallelism | Human Gates | Reusability |
|---------|------------|-------------|-------------|-------------|
| Sequential | Low | None | Optional | High (as composite) |
| Fan-Out | Medium | High | Optional | Medium |
| Fan-In | Medium | Medium | Optional | Medium |
| Conditional | Medium | Low | Optional | High |
| Iterative | High | Low | Optional | Medium |
| Gated | Low | None | **Required** | High |
| Composite | Low | Hidden | Hidden | **Highest** |
| Adapter | Low | None | None | Medium |
| Fallback | Medium | Sequential | None | Medium |
| Observability | Low | None | None | High |

---

## Anti-Patterns to Avoid

| Anti-Pattern | Problem | Solution |
|--------------|---------|----------|
| **God Workflow** | Single workflow does everything | Decompose into composable skills |
| **Implicit Coupling** | Skills share hidden state | Explicit input/output contracts |
| **No Checkpointing** | Failure loses all progress | Checkpoint every 1-2 skills |
| **Silent Fallback** | Degraded quality unnoticed | Explicit fallback logging, alerts |
| **Unbounded Loops** | Infinite iteration | Max iterations + progress metric |
| **Skip Gates** | Safety bypassed | Gates enforced by orchestrator |
| **Monolithic Skills** | Hard to reuse, test | Keep skills small, focused |

---

## Designing Composable Skills

### 1. Explicit Contracts
```yaml
# Every skill declares:
inputs:
  - name: repo_map
    type: CodebaseMap
    required: true
  - name: target_symbol
    type: string
    required: false
outputs:
  - name: root_cause
    type: RootCause
    required: true
  - name: fix
    type: CodeChange
    required: false
```

### 2. Idempotency
```yaml
# Skills should be safely re-runnable
idempotency_key: "{{workflow_id}}-{{skill_name}}-{{input_hash}}"
```

### 3. Progress Reporting
```yaml
# Long skills emit progress
progress:
  - stage: "analyzing"
    percent: 30
    message: "Tracing data flow..."
  - stage: "complete"
    percent: 100
```

### 4. Failure Modes
```yaml
# Explicit failure types
failure_modes:
  - REPRODUCIBLE: "Can reproduce, needs fix"
  - HYPOTHESIS: "Cannot reproduce, has hypotheses"
  - BLOCKED: "Missing input, awaiting gate"
  - ERROR: "Unexpected error, see logs"
```

---

## Orchestrator DSL Reference

```yaml
# Full workflow definition
workflow:
  id: "bug-fix-{{issue_number}}"
  name: "Bug Fix Pipeline"
  version: "1.0"
  
  # Global settings
  settings:
    max_parallel: 3
    default_timeout_ms: 1800000
    checkpoint_interval: 1
    evidence_dir: ".workflow/evidence"
  
  # Input parameters
  parameters:
    - name: issue_number
      type: string
      required: true
    - name: target_branch
      type: string
      default: "main"
  
  # DAG nodes
  nodes:
    - id: map
      skill: codebase-intelligence
      input:
        target: "area from issue {{issue_number}}"
      output: [repo_map]
    
    - id: debug
      skill: autonomous-debugging
      input:
        map: "{{repo_map}}"
        issue: "{{issue_number}}"
      depends_on: [map]
      output: [root_cause, fix, regression_test]
      timeout_ms: 600000
    
    - id: review
      skill: multi-agent-review
      input:
        diff: "{{fix}}"
        scope: "{{root_cause.affected_files}}"
      depends_on: [debug]
      gate:
        type: approval
        required: true
        message: "Review fix for issue {{issue_number}}"
      output: [findings, approval]
    
    - id: test
      skill: autonomous-testing
      input:
        scope: "{{root_cause.affected_files}}"
        regression_test: "{{regression_test}}"
      depends_on: [review]
      output: [test_results]
    
    - id: report
      skill: reporter  # built-in
      input:
        workflow_id: "{{workflow.id}}"
        evidence: ["{{map}}", "{{debug}}", "{{review}}", "{{test}}"]
      depends_on: [test]
      output: [final_report]
  
  # Outputs
  outputs:
    - final_report
    - fix
    - test_results
```

---

## Running Compositions

### Via Orchestrator Skill
```bash
# Direct invocation
hermes run workflow-orchestrator --goal "Fix issue #1847" --config workflow-bug-fix.yaml

# With parameters
hermes run workflow-orchestrator --goal "Release v3.0.0" \
  --param version=3.0.0-rc.2 \
  --param skip_security_scan=false
```

### Manual Composition (Ad-hoc)
```bash
# Step by step with context passing
map=$(hermes run codebase-intelligence --target "billing/reconciliation")
debug=$(hermes run autonomous-debugging --map "$map" --error "silent failure")
# ... human reviews debug output ...
review=$(hermes run multi-agent-review --diff "$debug.fix")
test=$(hermes run autonomous-testing --scope "billing" --fix "$debug.fix")
```

---

## Best Practices Summary

1. **Start simple** — Sequential pipeline first, add parallelism when needed
2. **Explicit contracts** — Every skill input/output documented
3. **Checkpoint often** — Every 1-2 skills minimum
4. **Gate critical transitions** — Never auto-approve writes/deploys
5. **Observe everything** — Metrics, costs, decisions, timestamps
6. **Compose, don't monolith** — Reusable skills > one big workflow
7. **Test compositions** — Run workflow-orchestrator on test scenarios
8. **Version workflows** — Track workflow definitions like code