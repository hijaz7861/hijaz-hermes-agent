---
name: workflow-orchestrator
description: Compose and execute multi-skill workflows for complex end-to-end software engineering tasks. Use when a goal requires coordinated reconnaissance, remediation, verification, and governance across multiple skills.
---

# Workflow Orchestrator

## Objective
Execute complex multi-phase goals by dynamically composing skills, managing state, and producing auditable evidence — all while respecting approval gates and safety boundaries.

## When to Use
- End-to-end defect resolution: explore → diagnose → fix → review → test
- Feature implementation in unfamiliar codebases: map → design → implement → review → test
- Release validation pipelines: test → review → security-scan → deploy-gate
- Cross-module refactoring with independent verification
- Any task where a single skill is insufficient and coordination adds value

## Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    WORKFLOW ORCHESTRATOR                     │
├─────────────────────────────────────────────────────────────┤
│  Planner          │  Executor        │  State Manager       │
│  - Goal analysis  │  - Skill dispatch│  - Checkpointing     │
│  - Skill selection│  - Agent spawn   │  - Rollback points   │
│  - DAG construction│ - Result collect │  - Context passing   │
├─────────────────────────────────────────────────────────────┤
│  Governance       │  Evidence        │  Reporter            │
│  - Approval gates │  - Aggregation   │  - Consolidated log  │
│  - Policy check   │  - Verification  │  - Diff summary      │
│  - Audit trail    │  - Gap detection │  - Risk assessment   │
└─────────────────────────────────────────────────────────────┘
```

## Procedure

### 1. Goal Analysis & Planning
- Parse the high-level objective into discrete, verifiable outcomes
- Identify required capabilities and map to available skills (consult `SKILLS.md`)
- Construct a Directed Acyclic Graph (DAG) of skill invocations with:
  - Nodes: skill executions with explicit inputs/outputs
  - Edges: data dependencies and ordering constraints
  - Gates: approval checkpoints for high-risk transitions
- Estimate resource needs (time, model calls, agent sessions)
- **Output:** Execution plan with skill sequence, parallelization opportunities, and risk flags

### 2. Context Preparation
- Establish shared context bundle:
  - Repository root, branch, working-tree status
  - Relevant AGENTS.md, CONTRIBUTING, README
  - Acceptance criteria and success metrics
  - Security/privacy constraints
  - Budget limits (time, cost, model calls)
- Create isolated workspace per skill when needed (worktrees, sessions)
- Initialize evidence ledger for audit trail

### 3. Skill Dispatch & Execution
For each node in topological order:
1. **Validate preconditions** — inputs available, gates passed, budget remaining
2. **Select execution mode:**
   - `inline`: Run skill logic in current session (for lightweight skills)
   - `subagent`: Spawn dedicated session with scoped context (for heavy skills)
   - `parallel`: Launch independent nodes concurrently
3. **Inject context** — pass only required subset to each skill
4. **Execute with timeout** — enforce per-skill and cumulative budgets
5. **Collect results** — structured output, evidence, artifacts, errors
6. **Update state** — checkpoint progress, record decisions, track budget

### 4. Gate Evaluation
At each approval gate:
- Present aggregated evidence to user/approver
- Block until explicit approval for:
  - Destructive operations
  - Production deployment
  - Credential rotation
  - Irreversible migrations
  - External API calls with side effects
- Record approval/denial with timestamp and identity
- On denial: execute rollback to last safe checkpoint

### 5. Evidence Aggregation & Verification
- Merge evidence from all skills into unified report
- Cross-reference findings (e.g., debugging root cause ↔ test coverage)
- Detect gaps: untested paths, unreviewed files, missing approvals
- Verify completion criteria for each skill and overall goal
- Generate machine-readable summary (JSON) + human report (Markdown)

### 6. Final Report & Cleanup
- Produce consolidated report with:
  - Executive summary (goal, outcome, risk)
  - Skill-by-skill evidence with timestamps
  - Final diff (if code modified)
  - Test results matrix
  - Outstanding risks and limitations
  - Audit trail of all approvals and decisions
- Clean up ephemeral worktrees/sessions per policy
- Archive evidence ledger for traceability

## Workflow Templates

### Template: Bug Resolution Pipeline
```
Goal: "Fix the login timeout bug reported in #1234"

DAG:
  1. codebase-intelligence (target: auth/login flow)
     → outputs: architecture map, entry points, test baseline
  2. autonomous-debugging (input: map + error from #1234)
     → outputs: root cause, minimal fix, regression test
  3. [GATE: User approves fix]
  4. multi-agent-review (scope: auth module + tests)
     → outputs: findings, severity, remediation
  5. [GATE: Critical findings resolved]
  6. autonomous-testing (scope: auth + related integration)
     → outputs: test evidence, pass/fail matrix
  7. [GATE: All critical tests pass]
  8. Reporter: consolidated report
```

### Template: Feature Implementation
```
Goal: "Add OAuth2 provider support per SPEC-567"

DAG:
  1. codebase-intelligence (target: auth/integration patterns)
  2. model-router (task: code-generation, constraints: security)
  3. [PARALLEL]
     3a. Implementer subagent: write code + unit tests
     3b. Test analyst subagent: design integration test plan
  4. multi-agent-review (scope: new provider + tests)
  5. autonomous-testing (full auth suite + new integration)
  6. Reporter
```

### Template: Release Validation
```
Goal: "Validate v2.4.0 release candidate"

DAG:
  1. autonomous-testing (full suite + performance baseline)
  2. multi-agent-review (scope: changelog, migrations, config)
  3. [PARALLEL]
     3a. Security scan skill (if available)
     3b. Dependency audit skill (if available)
  4. [GATE: Release approval]
  5. Reporter + release notes generation
```

## State Management

### Checkpoint Format
```json
{
  "workflowId": "wf_abc123",
  "goal": "Fix login timeout #1234",
  "phase": "debugging",
  "completedNodes": ["codebase-intelligence"],
  "currentNode": "autonomous-debugging",
  "contextBundle": { ... },
  "evidenceLedger": [
    {"skill": "codebase-intelligence", "status": "completed", "outputRef": "..."}
  ],
  "budget": {"timeUsedMs": 45000, "modelCalls": 12, "costUsd": 0.03},
  "approvals": [],
  "checkpointTime": "2026-11-24T10:30:00Z"
}
```

### Rollback Procedure
1. Identify last clean checkpoint before failure/gate denial
2. Restore repository state (git checkout/worktree reset)
3. Invalidate downstream evidence
4. Resume from checkpoint with modified plan or escalate

## Safety & Approval Gates

| Gate | Trigger | Required Approval | Auto-Approve Condition |
|------|---------|-------------------|------------------------|
| Code modification | Any skill writes to repo | User | Never |
| Production deploy | Deploy step in DAG | User + ops | Never |
| Credential rotation | Skill requests secret change | User + security | Never |
| External mutation | API call with side effects | User | Read-only GET |
| Budget exceeded | Time/cost/calls > threshold | User | Never |
| Security finding | Critical severity in review | User + security | Never |

## Failure Handling

| Failure Type | Response |
|--------------|----------|
| Skill timeout | Retry once with extended budget, then mark blocked |
| Skill error | Capture error, attempt fallback skill, else block DAG |
| Gate denied | Rollback to checkpoint, report, await new instructions |
| Budget exhausted | Halt, report partial evidence, request budget increase |
| Context loss | Reconstruct from evidence ledger, replay from checkpoint |
| Concurrent conflict | Serialize conflicting nodes, retry with fresh context |

## Completion Criteria
- All DAG nodes completed or explicitly skipped with justification
- All approval gates passed (or workflow terminated at gate)
- Evidence ledger contains verifiable output for each completed node
- Consolidated report generated and archived
- No unresolved critical findings
- Budget within declared limits (or overage approved)

## Configuration

```yaml
# workflow-orchestrator config (optional, in runtime config)
workflow_orchestrator:
  default_time_budget_ms: 1800000      # 30 min
  default_cost_budget_usd: 5.00
  max_parallel_agents: 3
  checkpoint_interval_nodes: 2
  evidence_retention_days: 30
  auto_approve_read_only: true
  require_approval_for:
    - write
    - deploy
    - secret
    - external_write
```

## Integration Points

- **Skill Registry:** Reads `SKILLS.md` for capability routing
- **Model Router:** Uses `model-router` for subagent model selection
- **Board/Message Bus:** Coordinates multi-agent reviews
- **Worktree Manager:** Isolates parallel skill executions
- **Audit Log:** Structured event stream for compliance

## Example Invocation

```yaml
# User request
goal: "Resolve the memory leak in the WebSocket handler (issue #882)"
constraints:
  max_time_minutes: 45
  max_cost_usd: 3.00
  require_approval_before_write: true
```

**Orchestrator plans:**
1. `codebase-intelligence` → map WS handler, dependencies
2. `autonomous-debugging` → reproduce leak, find root cause
3. `multi-agent-review` → review fix (security: resource exhaustion)
4. `autonomous-testing` → load test + memory profile
5. Report

---

*This skill requires Hermes runtime with multi-session, worktree, and board support. Degrades gracefully to sequential inline execution when unavailable.*