# Playbook: Autonomous Refactoring Planner

*Practical examples for the `autonomous-refactoring-planner` skill*

---

## Scenario 1: Autonomous module refactoring (happy path)

**Trigger:** "Autonomously refactor the auth module for maintainability."

**Invocation:**
```
Autonomously refactor src/auth/ for maintainability.
Constraints: Budget $5, Time 20min, Privacy INTERNAL
Quality: 100% tests pass, typecheck clean, behavior preserved.
Human gate: public API changes require approval.
```

**Execution Log:**
```
## Autonomous Refactoring: src/auth/

### Goal Decomposition (agentic-workflow-engine)
Subtasks:
1. map_auth (codebase-intelligence) — task: long_context, privacy: INTERNAL
2. analyze_complexity (reasoning model) — task: reasoning, privacy: INTERNAL
3. plan_transformations (code-refactorer) — task: code_generation, privacy: INTERNAL
4. apply_refactors (code-refactorer) — task: code_generation, privacy: INTERNAL
5. run_tests (autonomous-testing) — task: code_generation, privacy: INTERNAL
6. verify_behavior (autonomous-testing) — task: reasoning, privacy: INTERNAL

### Model Routing Decisions
| Subtask | Task Type | Privacy | Model | Cost Est. |
|---------|-----------|---------|-------|-----------|
| map_auth | long_context | INTERNAL | gemini-1.5-flash | $0.02 |
| analyze_complexity | reasoning | INTERNAL | deepseek-coder | $0.03 |
| plan_transformations | code_generation | INTERNAL | deepseek-coder | $0.02 |
| apply_refactors | code_generation | INTERNAL | deepseek-coder | $0.02 |
| run_tests | code_generation | INTERNAL | deepseek-coder | $0.02 |
| verify_behavior | reasoning | INTERNAL | deepseek-coder | $0.02 |

### Execution Results
- Total cost: $0.13 (within $5 budget)
- Total time: 11 min (within 20 min)
- Iterations: 2
- Self-corrections: 1 (reverted refactor that changed public signature)
- Human gates passed: 0 (no public API changes needed)
- Result: SUCCESS

### Refactor Summary
- Extract method: validateCredentials() from authenticate()
- Extract method: generateToken() from issueToken()
- Inline: unused helper function
- Complexity reduced: 14 → 9 (authenticate)

### Verification
- Tests: 100% pass before and after each refactor
- Typecheck: CLEAN
- Behavior contract: preserved (same inputs → same outputs)

Exit code: 0.
```

**Expected Output:**
Refactoring report with GoalSpec, per-subtask routing decisions, execution result, refactor summary, and verification.

---

## Scenario 2: Public API change requires human gate (safety case)

**Trigger:** "Refactor the billing module. Public API may change."

**Invocation:**
```
Autonomously refactor src/billing/ for maintainability.
Human gate: any public API change requires explicit approval.
```

**Execution Log:**
```
## Autonomous Refactoring: src/billing/

### Goal Decomposition
Subtasks:
1. map_billing (codebase-intelligence)
2. analyze_complexity (reasoning)
3. plan_transformations (code-refactorer)
4. apply_refactors (code-refactorer) ← HUMAN GATE if API changes
5. run_tests (autonomous-testing)
6. verify_behavior (autonomous-testing)

### Human Gate Triggered
Subtask plan_transformations identified a public API change:
- calculateTotal() signature: (amount: number) → (amount: number, taxRate: number)
- This is a breaking change to the public API

### Gate Decision
- Human approval REQUIRED for public API change
- Decision: PENDING — awaiting user approval
- Execution halted at gate

### Report
Refactoring: HALTED at human gate.
Reason: public API change detected (calculateTotal signature).
No refactors applied pending approval.
Next: User approves or rejects API change, then resume execution.
Exit code: 0 (halted at gate, not failed).
```

**Expected Output:**
Report showing human gate triggered, public API change identified, execution halted pending approval, no changes applied.

---

## Scenario 3: Budget exceeded (failure case)

**Trigger:** "Autonomously refactor the entire codebase. Budget $1."

**Invocation:**
```
Autonomously refactor src/ for maintainability.
Constraints: Budget $1, Time 15min
```

**Execution Log:**
```
## Autonomous Refactoring: src/ (Full Codebase)

### Budget Tracking
- Iteration 1: map + analyze — $0.45 used
- Iteration 2: plan + apply (auth module) — $0.35 used
- Iteration 3: plan + apply (billing module) — $0.30 used
- Total: $1.10 — BUDGET EXCEEDED ($1.00 limit)

### Execution Halted
- Status: BUDGET_EXCEEDED
- Completed: auth module refactored (tests pass)
- Partial: billing module plan created, not applied
- No further model calls permitted

### Report
- Workflow halted at budget limit
- Partial results: auth module refactored successfully
- Billing module: plan created, application pending
- Recommendation: increase budget or reduce scope to single module

Exit code: 1 (budget exceeded, execution halted).
```

**Expected Output:**
Report showing budget tracking, halt at limit, partial results (auth done, billing pending), and recommendations.
