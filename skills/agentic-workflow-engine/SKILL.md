---
name: agentic-workflow-engine
description: Autonomous workflow engine with self-correcting loops, continuous improvement, goal decomposition, and adaptive execution. Executes complex goals by dynamically planning, executing, evaluating, and iterating until success criteria met.
version: 1.0.0
tags: [orchestration, autonomous, loops, self-correction, adaptive, agentic]
---

# Agentic Workflow Engine

## Objective
Execute high-level goals autonomously by decomposing into tasks, executing with skills, evaluating results, and iterating — with self-correction, learning, and human governance at critical checkpoints.

## Core Concept: The Autonomy Loop

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                        AGENTIC AUTONOMY LOOP                                 │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│   ┌─────────┐    ┌─────────┐    ┌─────────┐    ┌─────────┐    ┌─────────┐  │
│   │  GOAL   │───▶│ PLAN    │───▶│ EXECUTE │───▶│EVALUATE │───▶│ DECIDE  │  │
│   │  INTAKE │    │ (DAG)   │    │(Skills) │    │(Critic) │    │         │  │
│   └─────────┘    └─────────┘    └─────────┘    └─────────┘    └────┬────┘  │
│                                                                       │       │
│                              ┌───────────────────────────────────────┘       │
│                              ▼                                                 │
│                    ┌─────────────────┐                                        │
│                    │  CONTINUE?      │                                        │
│                    │  - Success?     │                                        │
│                    │  - Budget left? │                                        │
│                    │  - Iterations?  │                                        │
│                    │  - Human gate?  │                                        │
│                    └────────┬────────┘                                        │
│                             │                                                 │
│                    YES ────▶│────▶ NO                                         │
│                             ▼                                                 │
│                    ┌─────────────────┐                                        │
│                    │  COMPLETE       │                                        │
│                    │  - Report       │                                        │
│                    │  - Artifacts    │                                        │
│                    │  - Lessons      │                                        │
│                    └─────────────────┘                                        │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

## Procedure

### 1. Goal Intake & Decomposition
Parse high-level goal into structured specification:

```python
def decompose_goal(goal: str, context: Context) -> GoalSpec:
    # Use reasoning model to break down
    decomposition = reason_about_goal(goal, context)
    
    return GoalSpec(
        objective=goal,
        success_criteria=decomposition.criteria,  # Observable, measurable
        constraints=decomposition.constraints,    # Budget, time, privacy, approvals
        subtasks=decomposition.subtasks,          # Ordered, with dependencies
        acceptance_tests=decomposition.tests,     # How to verify each subtask
        risk_factors=decomposition.risks,         # What could go wrong
        human_gates=decomposition.gates           # Where human approval needed
    )
```

**Input:** Natural language goal + repository context
**Output:** `GoalSpec` with measurable criteria, subtask DAG, constraints

### 2. Dynamic Planning (DAG Construction)
Build executable plan from goal spec:

```python
def build_execution_plan(spec: GoalSpec, skills: SkillRegistry) -> ExecutionPlan:
    nodes = []
    for subtask in spec.subtasks:
        # Match subtask to best skill(s)
        skill_matches = skills.match(subtask)
        primary_skill = select_best_skill(skill_matches, spec.constraints)
        
        node = PlanNode(
            id=subtask.id,
            skill=primary_skill.name,
            input=map_inputs(subtask, spec),
            success_criteria=subtask.criteria,
            fallback_skills=[s.name for s in skill_matches[1:3]],
            timeout=subtask.estimated_time * 2,
            budget=subtask.estimated_cost,
            retry_policy=RetryPolicy(max_retries=2),
            human_gate=subtask.id in spec.human_gates
        )
        nodes.append(node)
    
    # Add edges from dependencies
    edges = build_dependency_edges(spec.subtasks)
    
    return ExecutionPlan(nodes=nodes, edges=edges, spec=spec)
```

### 3. Adaptive Execution
Execute plan with real-time adaptation:

```python
async def execute_plan(plan: ExecutionPlan, context: Context) -> ExecutionResult:
    state = ExecutionState(
        plan=plan,
        completed=set(),
        failed=set(),
        results={},
        budget_used=0.0,
        iterations=0,
        lessons_learned=[]
    )
    
    while not is_complete(state):
        # Get ready nodes (dependencies satisfied)
        ready = get_ready_nodes(state)
        
        # Execute in parallel (up to max_parallel)
        for node_batch in batch(ready, max_parallel=3):
            results = await execute_batch(node_batch, state, context)
            
            for node_id, result in results.items():
                state.results[node_id] = result
                state.budget_used += result.cost
                
                if result.success:
                    state.completed.add(node_id)
                    # Learn from success
                    state.lessons_learned.append(
                        Lesson(node=node_id, type="success", insight=result.insight)
                    )
                else:
                    state.failed.add(node_id)
                    # Self-correction attempt
                    correction = await attempt_correction(node_id, result, state, context)
                    if correction:
                        # Re-plan with correction
                        state = apply_correction(state, correction)
                    else:
                        # Escalate or fail
                        if node_id in plan.critical_path:
                            return ExecutionResult(
                                status="FAILED",
                                reason=f"Critical node {node_id} failed",
                                state=state
                            )
        
        # Check budget, time, iteration limits
        if state.budget_used > plan.total_budget:
            return ExecutionResult(status="BUDGET_EXCEEDED", state=state)
        if state.iterations > plan.max_iterations:
            return ExecutionResult(status="MAX_ITERATIONS", state=state)
        
        state.iterations += 1
    
    return ExecutionResult(status="SUCCESS", state=state)
```

### 4. Self-Correction Engine
When a node fails, automatically diagnose and fix:

```python
async def attempt_correction(node_id: str, result: NodeResult, 
                              state: ExecutionState, context: Context) -> Correction | None:
    failure = result.error
    
    # Classify failure type
    failure_type = classify_failure(failure)
    
    corrections = {
        FailureType.MODEL_ERROR: correct_model_selection,
        FailureType.SKILL_TIMEOUT: correct_timeout_or_scope,
        FailureType.VALIDATION_FAILED: correct_input_or_criteria,
        FailureType.DEPENDENCY_MISSING: correct_dependency_order,
        FailureType.PERMISSION_DENIED: correct_approval_gate,
        FailureType.BUDGET_EXCEEDED: correct_scope_or_model,
    }
    
    corrector = corrections.get(failure_type)
    if not corrector:
        return None  # Unknown failure, escalate
    
    correction = await corrector(node_id, failure, state, context)
    
    if correction and correction.confidence > 0.7:
        return correction
    return None
```

**Correction Strategies:**
| Failure Type | Correction |
|--------------|------------|
| Model error (rate limit, quality) | Switch to fallback model, simplify prompt |
| Timeout | Reduce scope, increase timeout, use faster model |
| Validation failed | Fix input data, relax criteria, add preprocessing |
| Dependency missing | Reorder DAG, add missing prerequisite |
| Permission denied | Request approval, use alternative approach |
| Budget exceeded | Switch to cheaper model, reduce scope, batch |

### 5. Critic Evaluation (Quality Gate)
After each major phase, evaluate quality:

```python
async def evaluate_phase(phase_results: Dict[str, NodeResult], 
                          spec: GoalSpec) -> Evaluation:
    # Use critic model (different from executor)
    critic_prompt = f"""
    Goal: {spec.objective}
    Success criteria: {spec.success_criteria}
    Phase results: {phase_results}
    
    Evaluate:
    1. Are success criteria met? (evidence)
    2. Any quality issues? (security, correctness, completeness)
    3. Any gaps? (missing tests, unhandled edge cases)
    4. Risk assessment for proceeding
    """
    
    evaluation = await call_critic_model(critic_prompt)
    
    return Evaluation(
        passed=evaluation.passes_criteria,
        issues=evaluation.issues,
        gaps=evaluation.gaps,
        risk_level=evaluation.risk,
        recommendation=evaluation.recommendation  # CONTINUE / REVISE / ESCALATE
    )
```

### 6. Learning & Memory
Persist lessons across executions:

```python
class AgentMemory:
    def __init__(self, storage: MemoryStore):
        self.store = storage
    
    async def record_lesson(self, lesson: Lesson):
        # Store with embeddings for retrieval
        embedding = embed(lesson.insight)
        await self.store.upsert(
            key=f"lesson:{lesson.id}",
            value=lesson,
            vector=embedding,
            metadata={
                "skill": lesson.skill,
                "failure_type": lesson.failure_type,
                "success": lesson.type == "success"
            }
        )
    
    async def retrieve_relevant(self, context: str, k: int = 5) -> List[Lesson]:
        embedding = embed(context)
        return await self.store.query(vector=embedding, top_k=k)
    
    async def get_best_practices(self, skill: str) -> List[str]:
        lessons = await self.store.query(
            filter={"skill": skill, "success": True},
            limit=10
        )
        return [l.insight for l in lessons]
```

## Autonomous Loop Patterns

### Pattern 1: Iterative Refinement (Test-Driven)
```
Goal: "Achieve 90% test coverage for auth module"

Loop:
  1. Measure current coverage
  2. Identify top 3 uncovered areas
  3. Generate tests for each (parallel)
  4. Run tests, measure new coverage
  5. If coverage < 90% and budget remains → repeat
  6. Else → complete
```

### Pattern 2: Bug Fix with Verification
```
Goal: "Fix memory leak in WebSocket handler"

Loop:
  1. Reproduce leak (autonomous-debugging)
  2. Apply minimal fix
  3. Run regression test (must fail before, pass after)
  4. Run load test (10k messages, memory stable)
  5. If leak persists → analyze, refine fix, repeat
  6. If fixed → security review → complete
```

### Pattern 3: Feature Implementation with Quality Gates
```
Goal: "Implement OAuth2 device flow per RFC 8628"

Loop (per endpoint):
  1. Write implementation + unit tests
  2. Static analysis (security, types)
  3. Integration test
  4. If any gate fails → fix, repeat step
  5. Security review (multi-agent-review)
  6. If findings → fix, repeat
  7. E2E test
  8. All pass → next endpoint
```

### Pattern 4: Refactoring with Safety
```
Goal: "Replace all 'any' types with proper types"

Loop (per module, topological order):
  1. Analyze module: count 'any', infer types
  2. Apply fixes (generics, interfaces, narrowing)
  3. Run tsc --noEmit (must be clean)
  4. Run module tests (must pass)
  5. If failures → revert, analyze, retry with different approach
  6. Human review gate
  7. Next module
```

## Configuration

```yaml
agentic_workflow_engine:
  # Loop control
  max_iterations: 10
  max_iterations_per_node: 3
  iteration_timeout_minutes: 30
  
  # Parallelism
  max_parallel_nodes: 3
  max_parallel_subagents: 2
  
  # Budgets
  default_total_budget_usd: 20.00
  default_time_budget_minutes: 60
  budget_warning_threshold: 0.8
  
  # Models
  planner_model: "claude-3.5-sonnet"      # Best reasoning
  executor_model: "auto"                   # Routed per task
  critic_model: "claude-3.5-sonnet"        # Independent critic
  corrector_model: "claude-3.5-sonnet"     # Self-correction
  
  # Memory
  memory_enabled: true
  memory_store: "vector"  # or "sqlite", "redis"
  memory_retention_days: 90
  max_lessons_per_skill: 50
  
  # Human gates (required)
  required_human_gates:
    - "production_deploy"
    - "secret_rotation"
    - "data_migration"
    - "security_finding_critical"
    - "budget_exceeded"
    - "destructive_operation"
  
  # Auto-approval (for read-only)
  auto_approve:
    - "code_analysis"
    - "test_execution"
    - "report_generation"
    - "documentation"
  
  # Quality thresholds
  quality_gates:
    test_pass_rate: 1.0          # 100% required
    typecheck_clean: true
    lint_clean: true
    security_scan_clean: true
    coverage_threshold: 0.80
  
  # Self-correction
  self_correction_enabled: true
  max_corrections_per_node: 2
  correction_confidence_threshold: 0.7
  
  # Critic
  critic_enabled: true
  critic_frequency: "phase"  # "node", "phase", "completion"
  
  # Observability
  trace_enabled: true
  trace_storage: "file"  # or "jaeger", "zipkin"
  metrics_enabled: true
```

## Execution Example

```python
# User invokes:
goal = """
Fix the payment reconciliation bug (#1847) end-to-end:
- Root cause fix
- Monitoring/alerting
- Regression tests
- Documentation update
"""

# Engine executes:

# ITERATION 1
# Plan: [map → debug → review → test → monitor → docs]
# Execute: map (success), debug (success: found 3 issues)
# Critic: "Debug found root causes but fix not yet applied"
# Decision: CONTINUE

# ITERATION 2
# Execute: fix applied (3 changes), review (security: 1 critical found)
# Critic: "Critical security finding: idempotency key collision"
# Correction: Switch to UUID v7 for idempotency keys
# Decision: REVISE (apply correction)

# ITERATION 3
# Execute: fix corrected, re-review (passed), test (all pass)
# Execute: monitoring added, docs updated
# Critic: "All success criteria met. Memory leak fixed, alerting works, tests pass."
# Decision: COMPLETE

# Result:
{
  "status": "SUCCESS",
  "iterations": 3,
  "total_cost": 1.23,
  "total_time_minutes": 18,
  "nodes_executed": 8,
  "corrections_applied": 1,
  "human_gates_passed": 1,
  "final_report": "...",
  "lessons_learned": [
    "Idempotency keys must use UUID v7, not timestamps",
    "Reconciliation jobs need distributed locks",
    "Silent failures require explicit alerting"
  ]
}
```

## Advanced: Meta-Learning

The engine improves over time by learning from executions:

```python
class MetaLearner:
    async def optimize_routing(self, history: List[Execution]) -> RoutingPolicy:
        # Analyze which models worked best for which tasks
        # Update task_preferences in model-router config
        
    async def optimize_planning(self, history: List[Execution]) -> PlanningHeuristics:
        # Learn typical task durations, failure patterns
        # Improve time/budget estimates
        
    async def optimize_corrections(self, history: List[Execution]) -> CorrectionStrategies:
        # Learn which corrections work for which failure types
        # Update correction confidence thresholds
```

## Safety & Governance

| Guardrail | Implementation |
|-----------|----------------|
| **Budget hard limit** | Execution stops at `total_budget_usd`, no partial spend |
| **Time hard limit** | Execution stops at `time_budget_minutes` |
| **Iteration limit** | Max 10 iterations total, 3 per node |
| **Human gates** | Required gates cannot be auto-approved |
| **Destructive ops** | Explicit approval per operation |
| **Circuit breakers** | Per-model, per-skill failure thresholds |
| **Audit trail** | Every decision, correction, gate logged |
| **Rollback** | Checkpointed state, can revert to any iteration |

## Completion Criteria
- All success criteria met with evidence
- All quality gates passed (tests, lint, typecheck, security)
- Budget and time within limits
- Human gates approved
- Audit trail complete
- Lessons learned recorded
- Artifacts delivered (code, tests, docs, reports)

---

*This is the highest-level orchestration skill. It uses all other skills as tools. Requires Hermes runtime with subagent, worktree, board, and vector memory support.*