---
name: autonomous-refactoring-planner
description: Plan autonomous refactoring by combining the agentic workflow engine with codebase intelligence. Decomposes refactoring goals into subtasks, assigns skills, models, and gates, then executes with self-correction and verification.
version: 1.0.0
tags: [refactoring, planning, autonomous, agentic, codebase-analysis]
dependencies: [agentic-workflow-engine, codebase-intelligence]
---

# Autonomous Refactoring Planner

## Objective
Combine the agentic workflow engine with codebase intelligence to autonomously plan and execute refactoring initiatives. Decomposes refactoring goals into subtasks (map → analyze → refactor → test → verify), assigns optimal skills and models, and executes with self-correction and quality gates.

## Trigger
- "Autonomously refactor module X"
- "Plan and execute refactoring of component Y with safety gates"
- "Refactor codebase with agentic workflow and verification"
- "Improve maintainability of module Z autonomously"

Anti-triggers: "Refactor without a plan" / "Refactor without tests" — those are code-refactorer alone, not the autonomous planner.

## Inputs
- Refactoring goal: target module, transformation type, desired outcome
- Constraints: budget, time, privacy classification, approval requirements
- Behavior contract: what must remain unchanged (public API, outputs, side effects)
- Quality thresholds: test pass rate, typecheck clean, coverage minimum

## Outputs
- GoalSpec: decomposed refactoring subtasks with skill/model assignments per subtask
- Execution plan: DAG with dependency edges, gates, checkpoints
- Routing decisions: model selected per subtask with rationale, cost estimate, privacy gate
- Execution result: success/fail, iterations, total cost, lessons learned
- Refactor report: changes applied, before/after metrics, verification results

## Procedure
1. **Goal intake and decomposition** (agentic-workflow-engine)
   - Parse refactoring goal into GoalSpec: objective, success criteria, constraints, subtasks.
   - Subtasks: map codebase → analyze complexity → plan transformations → apply refactors → test → verify behavior.
   - Identify human gates: public API changes, behavior changes, destructive operations.

2. **Map the codebase** (codebase-intelligence)
   - Establish context: repo root, branch, working-tree status.
   - Map structure: modules, dependencies, entry points, public APIs.
   - Trace target: callers, dependents, trust boundaries, external integrations.
   - Establish baseline: test suite, lint, typecheck, build commands.

3. **Build execution plan** (agentic-workflow-engine)
   - Construct DAG: nodes = subtasks with assigned skills and model routes.
   - Edges = dependencies (map before analyze, analyze before refactor, refactor before test).
   - Gates = approval checkpoints for API changes, behavior changes, destructive ops.

4. **Route each subtask** (agentic-workflow-engine + model-router principles)
   - Map task type to skill: mapping → codebase-intelligence, analysis → reasoning model, refactoring → code-refactorer, testing → autonomous-testing.
   - Apply privacy gates: confidential code → local/private models only.
   - Rank models: capability fit → reliability → cost.

5. **Adaptive execution** (agentic-workflow-engine)
   - Execute plan with real-time adaptation; route each node through the model router.
   - Self-correction on failure: if refactor breaks tests, revert and retry with different approach.
   - Critic evaluation after each phase: verify behavior contract preserved.

6. **Verify** (agentic-workflow-engine + code-refactorer principles)
   - Run tests before and after each refactor; require 100% pass.
   - Run lint, typecheck, build; require clean.
   - Confirm behavior contract unchanged (same inputs → same outputs).

7. **Learning and memory** (agentic-workflow-engine)
   - Persist lessons: which transformations worked best for which code patterns.
   - Feed back to improve future refactoring plans.

8. **Report**
   - Produce refactoring report: GoalSpec, execution plan, routing decisions, result, lessons learned, before/after metrics.

## Safety & Approval Gates
- **Privacy gates are hard constraints:** confidential code never goes to unapproved providers.
- **Human gates required** for: public API changes, behavior changes, destructive operations, budget exceeded.
- **Budget hard limit:** execution stops at total_budget_usd.
- **Test gate:** Every refactor verified with tests passing before and after.
- **No model response treated as executable authorization.**

## Failure Handling
- Model rate limit → agentic engine falls back to next model in chain.
- Refactor breaks tests → self-correction: revert, analyze, retry with different approach.
- All models exhausted → raise clear failure, no silent degradation.
- Budget exceeded → halt, report partial evidence, request budget increase.
- Privacy gate violation → block, report, require re-classification.

## Completion Criteria
- All success criteria met with evidence (behavior preserved, tests pass).
- All quality gates passed (tests, lint, typecheck, security).
- Budget and time within limits.
- Human gates approved.
- Audit trail complete with all decisions logged.
- Lessons learned recorded.
