# Playbook: Agentic Routing

*Practical examples for the `agentic-routing` skill*

---

## Scenario 1: Autonomous bug fix with model routing (happy path)

**Trigger:** "Fix the WebSocket memory leak autonomously with optimal model routing."

**Invocation:**
```
Execute autonomous workflow: "Fix WebSocket memory leak #882"
Constraints: Budget $5, Time 30min, Privacy INTERNAL
Route each subtask to optimal model.
```

**Execution Log:**
```
## Agentic Routing: WebSocket Memory Leak Fix

### Goal Decomposition (agentic-workflow-engine)
Subtasks:
1. map_ws_handler (codebase-intelligence) — task: long_context, privacy: INTERNAL
2. debug_leak (autonomous-debugging) — task: reasoning, privacy: INTERNAL
3. apply_fix (code edit) — task: code_generation, privacy: INTERNAL
4. security_review (multi-agent-review) — task: reasoning, privacy: CONFIDENTIAL
5. regression_test (autonomous-testing) — task: code_generation, privacy: INTERNAL

### Model Routing Decisions (model-router)
| Subtask | Task Type | Privacy | Selected Model | Cost Est. | Rationale |
|---------|-----------|---------|---------------|-----------|-----------|
| map_ws_handler | long_context | INTERNAL | gemini-1.5-flash | $0.02 | 1M context, cheap |
| debug_leak | reasoning | INTERNAL | deepseek-coder | $0.03 | Strong coding, low cost |
| apply_fix | code_generation | INTERNAL | deepseek-coder | $0.02 | Coding=9, tools |
| security_review | reasoning | CONFIDENTIAL | local/llama-3.1-70b | $0.00 | Privacy gate: local only |
| regression_test | code_generation | INTERNAL | deepseek-coder | $0.02 | Coding=9 |

### Execution Results
- Total cost: $0.09 (within $5 budget)
- Total time: 14 min (within 30 min)
- Iterations: 2
- Self-corrections: 1 (switched idempotency key to UUID v7)
- Human gates passed: 1 (security review)
- Result: SUCCESS

### Audit Trail
All routing decisions logged with model, cost, latency, rationale.
Privacy gates enforced: confidential data never left local environment.

Exit code: 0.
```

**Expected Output:**
Execution report with goal decomposition, per-subtask routing decisions, costs, latencies, result, audit trail, and lessons learned.

---

## Scenario 2: Privacy gate blocks model (safety case)

**Trigger:** "Fix the authentication bug. Confidential data — use local models only."

**Invocation:**
```
Execute autonomous workflow: "Fix auth bug"
Constraint: Privacy CONFIDENTIAL — no cloud models.
```

**Execution Log:**
```
## Agentic Routing: Auth Bug Fix (Confidential)

### Privacy Gate Enforcement (model-router)
Subtask: debug_auth (reasoning, CONFIDENTIAL)
- Cloud models (claude-3.5-sonnet, gpt-4o): BLOCKED by privacy gate
- OpenRouter models: BLOCKED by privacy gate
- Local models: llama-3.1-70b (Ollama) — ALLOWED

### Routing Decision
- Selected: local/llama-3.1-70b (Ollama, FREE)
- Fallback: local/deepseek-coder-33b (Ollama, FREE)
- Cost: $0.00

### Execution Result
- Debug completed using local model
- Root cause found: missing input validation
- Fix applied and tested
- No confidential data left the environment

Exit code: 0.
```

**Expected Output:**
Report showing privacy gate enforcement, local model selection, zero cost, and successful execution without data leaving environment.

---

## Scenario 3: Budget exceeded (failure case)

**Trigger:** "Autonomously refactor the entire auth module. Budget $1."

**Invocation:**
```
Execute autonomous workflow: "Refactor auth module"
Constraints: Budget $1, Time 20min
```

**Execution Log:**
```
## Agentic Routing: Auth Module Refactor

### Budget Tracking
- Iteration 1: map + debug — $0.45 used
- Iteration 2: apply fixes — $0.35 used
- Iteration 3: review + test — $0.25 used
- Total: $1.05 — BUDGET EXCEEDED ($1.00 limit)

### Execution Halted
- Status: BUDGET_EXCEEDED
- Partial results: map and debug complete, fixes partially applied
- No further model calls permitted

### Report
- Workflow halted at budget limit
- Partial evidence archived
- Rollback to last checkpoint available
- Recommendation: increase budget or reduce scope

Exit code: 1 (budget exceeded, execution halted).
```

**Expected Output:**
Report showing budget tracking, halt at limit, partial results, and recommendations.
