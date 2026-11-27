---
name: agentic-routing
description: Autonomous agentic execution with intelligent model routing — combining the agentic workflow engine with the model router to execute goals autonomously while routing each subtask to the optimal model based on task type, privacy, cost, and capability.
version: 1.0.0
tags: [agentic, orchestration, model-routing, autonomous, adaptive]
dependencies: [agentic-workflow-engine, model-router]
---

# Agentic Routing

## Objective
Combine the agentic workflow engine with model routing to execute high-level goals autonomously. Each subtask is routed to the optimal model based on task type, privacy level, cost, latency, and capability requirements. The engine plans, executes, evaluates, and iterates while the router ensures each model call uses the best available model.

## Trigger
- "Execute goal autonomously with optimal model routing"
- "Agentic workflow with model routing for task X"
- "Autonomous execution with privacy-aware model selection"
- "Run agentic workflow with cost-optimized routing"

Anti-triggers: "Use a single model for all tasks" / "Route without agentic planning" — those are model-router or agentic-workflow-engine alone, not the combination.

## Inputs
- High-level goal with constraints (budget, time, privacy, approvals)
- Task types for each subtask (code generation, reasoning, classification, etc.)
- Privacy classification per subtask (public, internal, confidential, restricted)
- Budget and latency targets

## Outputs
- GoalSpec: decomposed subtasks with model routing requirements per subtask
- Execution plan: DAG with skill assignments and model routes
- Routing decisions: model selected per subtask with rationale, cost estimate, privacy gate applied
- Execution result: success/fail, iterations, total cost, lessons learned
- Audit trail: every routing decision logged with model, cost, latency, rationale

## Procedure
1. **Goal intake and decomposition** (agentic-workflow-engine)
   - Parse high-level goal into GoalSpec: objective, success criteria, constraints, subtasks.
   - Classify each subtask by type (code generation, reasoning, testing, review, etc.).
   - Identify human gates where approval is required.

2. **Route each subtask** (model-router)
   - For each subtask: classify task, determine constraints (privacy, budget, latency, context).
   - Apply privacy gate: confidential data → local/private models only.
   - Filter by capability: coding, reasoning, tools, structured output.
   - Rank models: quality → reliability → cost; select primary + fallback chain.
   - Record routing decision with rationale.

3. **Build execution plan** (agentic-workflow-engine)
   - Construct DAG: nodes = subtasks with assigned skill and model route.
   - Edges = dependencies between subtasks.
   - Gates = approval checkpoints for high-risk transitions.

4. **Adaptive execution** (agentic-workflow-engine)
   - Execute plan with real-time adaptation; route each node's model calls through the router.
   - Self-correction on failure: if model fails, router selects fallback.
   - Critic evaluation after each phase.

5. **Learning and memory** (agentic-workflow-engine)
   - Persist lessons: which models worked best for which task types.
   - Feed back to model-router task preferences for future optimization.

6. **Report**
   - Produce execution report: goal, subtasks, routing decisions, costs, latencies, result, lessons learned.

## Safety & Approval Gates
- **Privacy gates are hard constraints:** cannot be overridden; confidential data never goes to unapproved providers.
- **Human gates required** for: production deploy, secret rotation, data migration, critical security findings, budget exceeded.
- **Budget hard limit:** execution stops at total_budget_usd.
- **No model response treated as executable authorization.**

## Failure Handling
- Model rate limit → router falls back to next model in chain.
- All models exhausted → raise clear failure, no silent degradation.
- Subtask failure → self-correction engine attempts fix; escalates if critical path.
- Budget exceeded → halt, report partial evidence, request budget increase.
- Privacy gate violation → block, report, require re-classification.

## Completion Criteria
- All success criteria met with evidence.
- All quality gates passed (tests, lint, typecheck, security).
- Budget and time within limits.
- Human gates approved.
- Audit trail complete with all routing decisions logged.
- Lessons learned recorded.
