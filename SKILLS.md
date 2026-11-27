# HIJAZ Hermes Skills Registry

Central index of all available skills with metadata for discovery, routing, and composition.

---

## Skill Catalog

| Skill | Category | Complexity | Primary Use Case | Dependencies |
|-------|----------|------------|------------------|--------------|
| `codebase-intelligence` | Reconnaissance | Low | Map unknown repos before editing | None |
| `autonomous-debugging` | Remediation | Medium | Reproduce, diagnose, fix defects | `codebase-intelligence` |
| `autonomous-testing` | Verification | Medium | Risk-based test design & execution | `codebase-intelligence` |
| `multi-agent-review` | Governance | High | Independent review for critical changes | `codebase-intelligence` |
| `model-router` | Infrastructure | Low | Select optimal model per task | None |
| `skill-creator` | Meta | Medium | Design, validate, maintain skills | None |
| `workflow-orchestrator` | Orchestration | High | Compose skills into complex workflows | All |
| `advanced-model-router` | Infrastructure | Medium | Intelligent routing with OpenRouter, free/paid tiers, privacy gates, fallback chains | `model-router` |
| `agentic-workflow-engine` | Orchestration | Very High | Autonomous goal execution with self-correction, learning, adaptive loops | All + vector memory |
| `security-audit` | Governance | Medium | Secrets scan, dependency audit, insecure config, trust boundaries | `codebase-intelligence` |
| `dependency-management` | Remediation | Medium | Audit, patch, and verify dependency updates with rollback | `codebase-intelligence` |
| `release-coordinator` | Orchestration | High | Release readiness, changelog, version bumps, gated approval | All |
| `performance-profiler` | Performance Optimization | Medium | Identify bottlenecks via measurement, recommend optimizations, verify with benchmarks | `codebase-intelligence` |
| `code-refactorer` | Software Engineering | Medium | Safe behavior-preserving transformations with test verification | `codebase-intelligence`, `autonomous-testing` |
| `documentation-synthesizer` | Documentation | Medium | Generate API docs, README sections, docstrings from code | `codebase-intelligence` |
| `observability-instrumenter` | DevOps & Infrastructure | Medium | Add structured logging, metrics, tracing, health checks | `codebase-intelligence` |
| `skill-benchmarker` | AI Agent Development | Medium | Evaluate and compare skill performance against baselines | `skill-creator` |

---

## Category Definitions

| Category | Purpose | Typical Trigger |
|----------|---------|-----------------|
| **Reconnaissance** | Build evidence-based understanding before action | New repo, unknown feature, onboarding |
| **Remediation** | Fix defects with verified root-cause analysis | Bug reports, failing tests, crashes |
| **Verification** | Prove correctness and catch regressions | Pre-merge, release, agent-generated code |
| **Governance** | Independent review for high-stakes changes | Security, cross-module, complex changes |
| **Infrastructure** | Optimize model selection and routing | Multi-provider, cost/latency optimization |
| **Meta** | Create and maintain the skill ecosystem | New recurring workflows, skill gaps |
| **Orchestration** | Chain skills for end-to-end workflows | Complex multi-phase tasks |
| **Performance Optimization** | Identify bottlenecks, measure, and optimize code performance | Slow endpoints, high CPU/memory, latency issues |
| **Software Engineering** | Improve code structure without changing behavior | Refactoring, code quality, maintainability |
| **Documentation** | Generate and synchronize docs from source code | Stale docs, missing API reference, onboarding |
| **DevOps & Infrastructure** | Manage releases, dependencies, observability, and model routing | Deployments, dependency updates, monitoring, routing |
| **AI Agent Development** | Create, evaluate, and benchmark agent skills | New skill creation, skill comparison, quality assurance |

---

## Skill Composition Patterns

### Pattern 1: Investigate → Fix → Verify
```
codebase-intelligence → autonomous-debugging → autonomous-testing
```
**Use for:** Bug reports in unfamiliar codebases

### Pattern 2: Analyze → Review → Test
```
codebase-intelligence → multi-agent-review → autonomous-testing
```
**Use for:** Security-sensitive or cross-module changes

### Pattern 3: Route → Execute → Review
```
model-router → [target skill] → multi-agent-review
```
**Use for:** Cost-optimized execution with quality gate

### Pattern 4: Full Lifecycle
```
codebase-intelligence → autonomous-debugging → multi-agent-review → autonomous-testing
```
**Use for:** Production-critical defect resolution

---

## Routing Rules (for workflow-orchestrator)

| Task Type | Primary Skill | Fallback | Review Required |
|-----------|---------------|----------|-----------------|
| "Explore this repo" | codebase-intelligence | — | No |
| "Fix this bug" | autonomous-debugging | codebase-intelligence | If security/critical |
| "Test this change" | autonomous-testing | — | No |
| "Review this PR" | multi-agent-review | — | Yes (built-in) |
| "Which model for X?" | advanced-model-router | model-router | No |
| "Create a skill for X" | skill-creator | — | No |
| "Do X end-to-end" | workflow-orchestrator | — | Yes |
| "Do X autonomously with self-correction" | agentic-workflow-engine | workflow-orchestrator | Yes (critical gates) |
| "Route with free tier / privacy gates" | advanced-model-router | model-router | No |

---

## Capability Matrix

| Capability | codebase-intelligence | autonomous-debugging | autonomous-testing | multi-agent-review | model-router | skill-creator | workflow-orchestrator | advanced-model-router | agentic-workflow-engine |
|------------|----------------------|---------------------|-------------------|-------------------|--------------|---------------|----------------------|----------------------|------------------------|
| Reads code | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ✅ | ❌ | ✅ |
| Runs commands | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ✅ | ❌ | ✅ |
| Modifies code | ❌ | ✅ | ❌ | ❌ | ❌ | ✅ | Via delegation | ❌ | Via delegation |
| Spawns agents | ❌ | ❌ | ❌ | ✅ | ❌ | ❌ | ✅ | ❌ | ✅ |
| Selects models | ❌ | ❌ | ❌ | ❌ | ✅ | ❌ | ✅ | ✅ | ✅ |
| Creates skills | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ | ❌ | ❌ | ❌ |
| Produces reports | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Free tier routing | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ | ✅ |
| Privacy gates | ❌ | ❌ | ❌ | ❌ | Basic | ❌ | ❌ | ✅ | ✅ |
| Self-correction | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ |
| Meta-learning | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ |
| Autonomous loops | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ |

---

## Installation Matrix

| Skill | Required Runtime | Optional Enhancements |
|-------|------------------|----------------------|
| codebase-intelligence | File read, grep, glob | LSP, call graph |
| autonomous-debugging | Test runner, debugger | Replay, time-travel |
| autonomous-testing | Test framework, CI | Coverage, mutation |
| multi-agent-review | Multi-session, board | Separate worktrees |
| model-router | Provider metadata API | Local model registry |
| skill-creator | YAML validator | Skill test harness |
| workflow-orchestrator | All above | State machine, DAG runner |
| advanced-model-router | OpenRouter API, Ollama/vLLM | Prometheus, vector DB |
| agentic-workflow-engine | All above + vector memory | Prometheus, Jaeger, alerting |

---

## Version Compatibility

| Skill | Min Hermes Version | Protocol Version |
|-------|-------------------|------------------|
| codebase-intelligence | 1.0.0 | 1 |
| autonomous-debugging | 1.0.0 | 1 |
| autonomous-testing | 1.0.0 | 1 |
| multi-agent-review | 1.1.0 | 1 |
| model-router | 1.0.0 | 1 |
| skill-creator | 1.0.0 | 1 |
| workflow-orchestrator | 1.2.0 | 2 |
| advanced-model-router | 1.2.0 | 2 |
| agentic-workflow-engine | 1.3.0 | 3 |

---

## Quick Reference Cards

### codebase-intelligence
```
Trigger: "Map this repository" / "Find where X is implemented"
Input: Repo root, optional target symbol
Output: Architecture map, entry points, risk areas, test baseline
Time: 2-10 min
```

### autonomous-debugging
```
Trigger: "Fix this bug" / "Why does X fail?"
Input: Error, reproduction steps, repo access
Output: Root cause, minimal fix, regression test, verification
Time: 5-30 min
```

### autonomous-testing
```
Trigger: "Test this change" / "Verify release readiness"
Input: Change diff, acceptance criteria, repo access
Output: Test plan, execution evidence, pass/fail/blocked report
Time: 3-20 min
```

### multi-agent-review
```
Trigger: "Review this change" / "Security audit this PR"
Input: Diff/scope, acceptance criteria, repo access
Output: Consolidated findings, severity, remediation, go/no-go
Time: 10-60 min
```

### model-router
```
Trigger: "Route this task" / "Which model for X?"
Input: Task classification, constraints, provider catalog
Output: Selected model, fallback chain, routing rationale
Time: <1 sec
```

### skill-creator
```
Trigger: "Create a skill for X" / "Improve this skill"
Input: Workflow description, runtime capabilities
Output: Validated SKILL.md, test cases, maintenance notes
Time: 10-30 min
```

### workflow-orchestrator
```
Trigger: "Do X end-to-end" / "Run the full pipeline"
Input: High-level goal, repo access, constraints
Output: Executed workflow, aggregated evidence, final report
Time: Variable (minutes to hours)
```

### advanced-model-router
```
Trigger: "Route this task" / "Which model for X?" (enhanced)
Input: Task classification, constraints, privacy level, budget
Output: Selected model, fallback chain, routing rationale, cost estimate
Time: <1 sec
Features: Free tier first, privacy gates, batch API, prompt caching, circuit breakers
```

### agentic-workflow-engine
```
Trigger: "Do X autonomously" / "Achieve goal Y end-to-end"
Input: High-level goal, constraints, success criteria
Output: Executed workflow with self-correction, lessons learned, artifacts
Time: Variable (minutes to hours)
Features: Autonomous loops, self-correction, critic evaluation, meta-learning, vector memory
```

### performance-profiler
```
Trigger: "Profile this code for performance" / "Find bottlenecks in X"
Input: Target file/module/function, workload, constraints
Output: Bottleneck report, optimization recommendations, before/after benchmarks
Time: 5-20 min
Features: Measurement-first profiling, impact-ranked recommendations, before/after verification, rollback on regression
```

### code-refactorer
```
Trigger: "Refactor this module" / "Extract method from X" / "Rename Y"
Input: Target code, transformation type, scope, constraints
Output: Refactor plan, diff, verification results, behavior contract
Time: 5-15 min
Features: Behavior-preserving only, test gate (pass before and after), one transformation at a time, rollback on failure
```

### documentation-synthesizer
```
Trigger: "Generate API docs for X" / "Update README with Y" / "Sync docs with code"
Input: Target code, format, audience, existing docs
Output: Generated documentation, coverage report, staleness report
Time: 5-15 min
Features: Code-as-source-of-truth, no invented behavior, real examples from tests, contradiction detection
```

### observability-instrumenter
```
Trigger: "Add logging to X" / "Instrument Y for metrics" / "Add tracing to Z"
Input: Target code, telemetry type, destination, constraints
Output: Instrumentation diff, configuration, data-classification review, overhead estimate
Time: 5-15 min
Features: No secret logging, structured JSON, overhead budget, data classification, build/test verification
```

### skill-benchmarker
```
Trigger: "Compare skill A vs. skill B" / "Benchmark skill X on scenario Y"
Input: Skills to compare, scenario, metrics, repetitions
Output: Evaluation report, comparison matrix, winner determination, regression detection
Time: 10-30 min
Features: Identical scenario for both skills, six metrics (accuracy, reliability, time, resources, maintainability, security), adopt/reject/iterate decision
```

### security-audit
```
Trigger: "Security audit this repo" / "Check for secrets in code"
Input: Repository root, optional focus area (secrets, dependencies, config)
Output: Findings report with severity, location (file:line), remediation priority
Time: 5-20 min
Features: Secret detection (redacted), vulnerability audit, config/trust-boundary review, no secret output
```

### dependency-management
```
Trigger: "Update dependencies" / "Patch vulnerable dependencies"
Input: Dependency manifests/lockfiles, optional allow-list of packages
Output: Dependency report, applied updates, pending approvals, rollback state
Time: 3-15 min
Features: Vulnerability detection, minimal patch/minor updates, test-verified, rollback on failure
```

### release-coordinator
```
Trigger: "Prepare release vX.Y.Z" / "Release readiness check"
Input: Target version, branch, release criteria
Output: Release report, changelog, gate status (passed/failed/blocked)
Time: Variable (minutes to hours)
Features: Readiness checks, changelog assembly, approval-gated version bump, no deploy/publish
```

---

## Maintenance

- **Owner:** HIJAZ team
- **Review cycle:** Quarterly
- **Deprecation policy:** 2 major versions notice
- **Breaking changes:** Require major version bump in skill name (e.g., `codebase-intelligence-v2`)

---

*Generated from skill frontmatter and manual curation. Update when adding/modifying skills.*