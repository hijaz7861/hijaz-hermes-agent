# HIJAZ Hermes Agent Skills

[![Skills](https://img.shields.io/badge/skills-53-brightgreen)](SKILLS.md)
[![Playbooks](https://img.shields.io/badge/playbooks-8-blue)](playbooks/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![Hermes](https://img.shields.io/badge/Hermes-compatible-purple)](https://github.com/hijaz/hermes)
[![Contributions](https://img.shields.io/badge/contributions-welcome-orange)](CONTRIBUTING.md)

A practical, production-ready skill pack for turning Hermes into a **disciplined autonomous software-engineering agent**.

> **Philosophy:** Evidence-based, safety-first, human-governed. Skills don't replace engineering judgment — they amplify it with structure, verification, and auditability.

---

## 🎯 Quick Start

### 1. Install Skills
```bash
# Workspace install (recommended)
mkdir -p .agents/skills
cp -r skills/* .agents/skills/

# Or user-wide (check your Hermes config for exact path)
cp -r skills/* ~/.hermes/skills/
```

### 2. Verify Installation
```bash
# List available skills
hermes skills list

# Should show:
# codebase-intelligence    Map repositories before editing
# autonomous-debugging     Reproduce, diagnose, fix defects
# autonomous-testing       Risk-based test design & execution
# multi-agent-review       Independent review for critical changes
# model-router             Select optimal model per task
# skill-creator            Design, validate, maintain skills
# workflow-orchestrator    Compose skills into complex workflows
```

### 3. Run Your First Skill
```bash
# Explore a new repository
hermes run codebase-intelligence --goal "Map this repository"

# Fix a bug with full verification
hermes run workflow-orchestrator --goal "Fix the login timeout bug #1234"

# Create a custom skill for your team's workflow
hermes run skill-creator --goal "Create skill for our API contract testing"
```

---

## 🧠 Included Skills

| Skill | Category | Complexity | Description |
|-------|----------|------------|-------------|
| [`codebase-intelligence`](skills/codebase-intelligence/SKILL.md) | Reconnaissance | ⭐ | Build evidence-based repo map before editing |
| [`autonomous-debugging`](skills/autonomous-debugging/SKILL.md) | Remediation | ⭐⭐ | Reproduce, diagnose, fix defects with regression tests |
| [`autonomous-testing`](skills/autonomous-testing/SKILL.md) | Verification | ⭐⭐ | Risk-based test design, execution, evidence |
| [`multi-agent-review`](skills/multi-agent-review/SKILL.md) | Governance | ⭐⭐⭐ | Independent review roles: Coordinator, Implementer, Reviewer, Test Analyst |
| [`model-router`](skills/model-router/SKILL.md) | Infrastructure | ⭐ | Route tasks to optimal model (OpenRouter, local, cloud) |
| [`advanced-model-router`](skills/advanced-model-router/SKILL.md) | Infrastructure | ⭐⭐ | Free/paid tier routing, privacy gates, fallback chains, batch API |
| [`skill-creator`](skills/skill-creator/SKILL.md) | Meta | ⭐⭐ | Turn recurring workflows into maintainable skills |
| [`workflow-orchestrator`](skills/workflow-orchestrator/SKILL.md) | Orchestration | ⭐⭐⭐ | Compose skills into DAGs with gates, checkpoints, audit trails |
| [`agentic-workflow-engine`](skills/agentic-workflow-engine/SKILL.md) | Orchestration | ⭐⭐⭐⭐ | Autonomous loops, self-correction, meta-learning, critic evaluation |
| [`security-audit`](skills/security-audit/SKILL.md) | Governance | ⭐⭐ | Secrets scan, dependency audit, insecure config, trust boundaries |
| [`dependency-management`](skills/dependency-management/SKILL.md) | Remediation | ⭐⭐ | Audit, patch, and verify dependency updates with rollback |
| [`release-coordinator`](skills/release-coordinator/SKILL.md) | Orchestration | ⭐⭐⭐ | Release readiness, changelog, version bumps, gated approval |
| [`performance-profiler`](skills/performance-profiler/SKILL.md) | Performance Optimization | ⭐⭐ | Identify bottlenecks via measurement, recommend optimizations, verify with benchmarks |
| [`code-refactorer`](skills/code-refactorer/SKILL.md) | Software Engineering | ⭐⭐ | Safe behavior-preserving transformations with test verification |
| [`documentation-synthesizer`](skills/documentation-synthesizer/SKILL.md) | Documentation | ⭐⭐ | Generate API docs, README sections, docstrings from code |
| [`observability-instrumenter`](skills/observability-instrumenter/SKILL.md) | DevOps & Infrastructure | ⭐⭐ | Add structured logging, metrics, tracing, health checks |
| [`skill-benchmarker`](skills/skill-benchmarker/SKILL.md) | AI Agent Development | ⭐⭐ | Evaluate and compare skill performance against baselines |
| [`security-dependency-audit`](skills/security-dependency-audit/SKILL.md) | Security Engineering | ⭐⭐ | Dependency audit with security focus — vulnerable packages, CVEs, secure remediation |
| [`performance-optimization`](skills/performance-optimization/SKILL.md) | Performance Optimization | ⭐⭐ | Profile bottlenecks then refactor hot paths — verified performance gains with benchmarks |
| [`architecture-documentation`](skills/architecture-documentation/SKILL.md) | Documentation | ⭐⭐ | Architecture map + synthesized docs from code — API reference, module overviews, data flow |
| [`performance-observability`](skills/performance-observability/SKILL.md) | DevOps & Infrastructure | ⭐⭐ | Instrument code + profile overhead — observability with measured performance impact |
| [`secure-release`](skills/secure-release/SKILL.md) | Security Engineering | ⭐⭐⭐ | Release coordination with mandatory security audit gate — no release with unresolved CRITICAL/HIGH |
| [`debug-performance`](skills/debug-performance/SKILL.md) | Debugging | ⭐⭐ | Debug performance defects — reproduce slowness, find root cause, fix with benchmark verification |
| [`refactor-with-verification`](skills/refactor-with-verification/SKILL.md) | Software Engineering | ⭐⭐ | Refactor with test verification — characterization tests, behavior-preserving transforms, test gate |
| [`security-review`](skills/security-review/SKILL.md) | Security Engineering | ⭐⭐⭐ | Security-focused multi-agent review — adversarial review with security audit scan, severity classification |
| [`workflow-benchmarking`](skills/workflow-benchmarking/SKILL.md) | Multi-Agent Orchestration | ⭐⭐ | Benchmark multi-skill workflows — compare configurations, measure performance, identify bottlenecks |
| [`agentic-routing`](skills/agentic-routing/SKILL.md) | Multi-Agent Orchestration | ⭐⭐⭐⭐ | Autonomous execution with model routing — each subtask routed to optimal model by task/privacy/cost |
| [`test-coverage-analyzer`](skills/test-coverage-analyzer/SKILL.md) | Testing & Quality Assurance | ⭐⭐ | Analyze coverage gaps, recommend targeted tests, verify improvement |
| [`security-debugger`](skills/security-debugger/SKILL.md) | Security Engineering | ⭐⭐ | Debug security defects — reproduce, find root cause, fix with regression tests |
| [`quality-gate-review`](skills/quality-gate-review/SKILL.md) | Security Engineering | ⭐⭐⭐ | Gated code review — independent review + test validation before approval |
| [`workflow-optimizer`](skills/workflow-optimizer/SKILL.md) | Performance Optimization | ⭐⭐ | Optimize multi-skill workflows — measure performance, identify bottlenecks |
| [`autonomous-refactoring-planner`](skills/autonomous-refactoring-planner/SKILL.md) | Software Engineering | ⭐⭐⭐⭐ | Autonomous refactoring planning and execution with self-correction |
| [`api-contract-tester`](skills/api-contract-tester/SKILL.md) | Testing & Quality Assurance | ⭐⭐ | Validate API contracts — detect breaking changes, schema mismatches |
| [`incident-responder`](skills/incident-responder/SKILL.md) | DevOps & Infrastructure | ⭐⭐ | Incident response — reproduce, correlate observability, fix, monitor |
| [`compliance-auditor`](skills/compliance-auditor/SKILL.md) | Security Engineering | ⭐⭐ | Compliance audit — GDPR, SOC2, HIPAA, PCI-DSS requirements |
| [`database-query-optimizer`](skills/database-query-optimizer/SKILL.md) | Performance Optimization | ⭐⭐ | Optimize database queries — slow queries, N+1, missing indexes |
| [`configuration-validator`](skills/configuration-validator/SKILL.md) | Security Engineering | ⭐⭐ | Validate configuration — secrets, insecure defaults, drift |
| [`api-version-manager`](skills/api-version-manager/SKILL.md) | Documentation | ⭐⭐ | API version management — versions, deprecation, migration guides |
| [`error-budget-tracker`](skills/error-budget-tracker/SKILL.md) | DevOps & Infrastructure | ⭐⭐ | Error budget tracking — SLO compliance, budget consumption, alerts |
| [`database-schema-linter`](skills/database-schema-linter/SKILL.md) | Performance Optimization | ⭐⭐ | Schema linting — missing indexes, constraints, unsafe types |
| [`chaos-engineer`](skills/chaos-engineer/SKILL.md) | DevOps & Infrastructure | ⭐⭐ | Chaos engineering — failure injection, resilience verification |
| [`secret-scanner-historical`](skills/secret-scanner-historical/SKILL.md) | Security Engineering | ⭐⭐ | Historical secret scanning — git history, leaked credentials |
| [`production-safety-engine`](skills/production-safety-engine/SKILL.md) | DevOps & Infrastructure | ⭐⭐⭐⭐ | Production safety — incident response, error budgets, chaos, secure release |
| [`api-governance-platform`](skills/api-governance-platform/SKILL.md) | Security Engineering | ⭐⭐⭐⭐ | API governance — contract testing, version management, security review, quality gate |
| [`database-reliability-engine`](skills/database-reliability-engine/SKILL.md) | Performance Optimization | ⭐⭐⭐⭐ | Database reliability — query optimization, schema linting, coverage analysis |
| [`security-operations-center`](skills/security-operations-center/SKILL.md) | Security Engineering | ⭐⭐⭐⭐ | Security operations — secret scanning, debugging, compliance, review, dependencies |
| [`developer-experience-platform`](skills/developer-experience-platform/SKILL.md) | Software Engineering | ⭐⭐⭐⭐ | Developer experience — coverage analysis, verified refactoring, documentation |
| [`factory-core`](skills-factory/factory-core.md) | Factory Engineering | ⭐⭐⭐⭐ | Central orchestration, lifecycle management, governance enforcement |
| [`discovery-engine`](skills-factory/discovery-engine.md) | Factory Engineering | ⭐⭐ | Skill scanning, capability mapping, gap detection |
| [`research-engine`](skills-factory/research-engine.md) | Factory Engineering | ⭐⭐ | Best practice research, procedure verification |
| [`skill-analyzer`](skills-factory/skill-analyzer.md) | Factory Engineering | ⭐⭐ | Quality assessment, gap detection, improvement prioritization |
| [`skill-generator`](skills-factory/skill-generator.md) | Factory Engineering | ⭐⭐ | Standardized skill creation, playbook generation |
| [`combination-engine`](skills-factory/combination-engine.md) | Factory Engineering | ⭐⭐⭐ | Multi-skill combination, synergy validation |
| [`testing-engine`](skills-factory/testing-engine.md) | Factory Engineering | ⭐⭐ | Comparative evaluation, adopt/reject/iterate |
| [`benchmark-engine`](skills-factory/benchmark-engine.md) | Factory Engineering | ⭐⭐ | Multi-metric measurement, statistical significance |
| [`security-engine`](skills-factory/security-engine.md) | Factory Engineering | ⭐⭐ | Secret detection, gate verification, privacy check |
| [`optimization-engine`](skills-factory/optimization-engine.md) | Factory Engineering | ⭐⭐ | Bottleneck identification, before/after benchmarking |
| [`evolution-engine`](skills-factory/evolution-engine.md) | Factory Engineering | ⭐⭐ | Version tracking, improvement history |
| [`quality-control`](skills-factory/quality-control.md) | Factory Engineering | ⭐⭐⭐ | Checklist validation, production promotion |
| [`meta-skills-factory`](skills-factory/meta-skills-factory/SKILL.md) | Meta-Engineering | ⭐⭐⭐⭐⭐ | Recursive self-improvement, factory component optimization |
| [`skill-launcher`](skills/skill-launcher/SKILL.md) | Factory Engineering | ⭐⭐⭐ | Launches skills with context, parameters, execution tracking |
| [`skill-suggestion-engine`](skills/skill-suggestion-engine/SKILL.md) | Factory Engineering | ⭐⭐⭐ | Suggests relevant skills based on intent, context, and usage |

---

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                         HIJAZ HERMES SKILL ECOSYSTEM                         │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  ┌──────────────┐    ┌──────────────┐    ┌──────────────┐    ┌──────────┐  │
│  │  RECONNAISSANCE  │    │  REMEDIATION   │    │  VERIFICATION  │    │ GOVERNANCE │  │
│  │              │    │              │    │              │    │          │  │
│  │ codebase-    │    │ autonomous-  │    │ autonomous-  │    │ multi-   │  │
│  │ intelligence │───▶│ debugging    │───▶│ testing      │───▶│ agent    │  │
│  │              │    │              │    │              │    │ review   │  │
│  └──────────────┘    └──────────────┘    └──────────────┘    └──────────┘  │
│        │                    │                    │                    │       │
│        │                    │                    │                    │       │
│        ▼                    ▼                    ▼                    ▼       │
│  ┌──────────────────────────────────────────────────────────────────────┐   │
│  │                 ORCHESTRATION LAYER                                  │   │
│  │  ┌─────────────────────┐  ┌─────────────────────────────────────┐   │   │
│  │  │ WORKFLOW ORCHESTRATOR│  │      AGENTIC WORKFLOW ENGINE       │   │   │
│  │  │  ┌─────────┐        │  │  ┌─────────┐ ┌─────────┐ ┌───────┐  │   │   │
│  │  │  │ Planner │        │  │  │ Planner │ │Executor │ │Critic │  │   │   │
│  │  │  │(DAG)    │        │  │  │(Goal    │ │(Skills) │ │(Eval) │  │   │   │
│  │  │  │Executor │        │  │  │Spec)    │ │         │ │       │  │   │   │
│  │  │  │(Subagent)       │  │  │Corrector│ │Memory   │ │Loop   │  │   │   │
│  │  │  │State    │        │  │  │(Self-   │ │(Vector) │ │Control│  │   │   │
│  │  │  │Manager  │        │  │  │Fix)     │ │         │ │       │  │   │   │
│  │  │  │Gates    │        │  │  └─────────┘ └─────────┘ └───────┘  │   │   │
│  │  │  │(Approval)       │  │                                        │   │   │
│  │  │  │Reporter │        │  └─────────────────────────────────────┘   │   │
│  │  │  │(Audit)  │        │                                            │   │   │
│  │  │  └─────────┘        │                                            │   │   │
│  │  └─────────────────────┘                                            │   │
│  └──────────────────────────────────────────────────────────────────────┘   │
│        │                    │                    │                    │       │
│        ▼                    ▼                    ▼                    ▼       │
│  ┌──────────────┐    ┌──────────────┐    ┌──────────────┐    ┌──────────┐  │
│  │ INFRASTRUCTURE │    │    META      │    │  PLAYBOOKS   │    │ REGISTRY │  │
│  │              │    │              │    │              │    │          │  │
│  │ model-router │    │ skill-creator│    │ 8 guides     │    │ SKILLS.md│  │
│  │ advanced-    │    │              │    │ (examples)   │    │ (index)  │  │
│  │ model-router │    └──────────────┘    └──────────────┘    └──────────┘  │
│  │ (OpenRouter, │                                                            │
│  │  local, cloud)│                                                           │
│  └──────────────┘                                                            │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Data Flow Example: Bug Fix

```
User Goal: "Fix payment reconciliation silent failure"
                    │
                    ▼
┌─────────────────────────────────────────────────────────────────┐
│ WORKFLOW ORCHESTRATOR                                           │
│ 1. PLAN: Build DAG from goal                                    │
│    codebase-intelligence → autonomous-debugging → review → test │
└─────────────────────────────────────────────────────────────────┘
                    │
        ┌───────────┼───────────┐
        ▼           ▼           ▼
┌───────────────┐ ┌───────────┐ ┌───────────┐
│ codebase-     │ │ autonomous│ │ model-    │
│ intelligence  │ │ debugging │ │ router    │
│ (subagent)    │ │ (subagent)│ │ (inline)  │
│               │ │           │ │           │
│ Output: Map   │ │ Output:   │ │ Selects:  │
│ - Entry pts   │ │ - Root    │ │ claude-3.5│
│ - Risk areas  │ │   cause   │ │ sonnet    │
│ - Test base   │ │ - Fix     │ │           │
│               │ │ - Test    │ │           │
└───────────────┘ └───────────┘ └───────────┘
        │           │           
        │           ▼           
        │    ┌─────────────┐    
        │    │ GATE: User  │    
        │    │ approves    │    
        │    │ fix?        │    
        │    └──────┬──────┘    
        │           │ YES       
        ▼           ▼           
┌─────────────────────────────┐
│ multi-agent-review          │
│ (Coordinator + Reviewer     │
│  + Test Analyst)            │
│                             │
│ Output: Findings + Verdict  │
└─────────────┬───────────────┘
              │
              ▼
┌─────────────────────────────┐
│ autonomous-testing          │
│ (Full suite + regression)   │
│                             │
│ Output: Evidence + Report   │
└─────────────┬───────────────┘
              │
              ▼
┌─────────────────────────────┐
│ REPORTER                    │
│ Consolidated audit trail    │
│ - Executive summary         │
│ - Skill-by-skill evidence   │
│ - Final diff                │
│ - Risk assessment           │
└─────────────────────────────┘
```

---

## 📚 Playbooks

Each skill has a detailed playbook with real-world scenarios:

| Playbook | Scenarios Covered |
|----------|-------------------|
| [`codebase-intelligence`](playbooks/codebase-intelligence.md) | New repo onboarding, feature trace, risk assessment, security audit prep |
| [`autonomous-debugging`](playbooks/autonomous-debugging.md) | Flaky test diagnosis, production crash analysis, silent data corruption |
| [`autonomous-testing`](playbooks/autonomous-testing.md) | Pre-merge validation, release candidate validation, AI code verification, regression generation |
| [`multi-agent-review`](playbooks/multi-agent-review.md) | Security-critical PR, cross-module refactor, AI-generated code review |
| [`model-router`](playbooks/model-router.md) | Task classification, privacy-gated routing, cost-optimized batch, long-context analysis |
| [`advanced-model-router`](playbooks/advanced-model-router.md) | Free tier first, confidential data routing, batch classification, long context, adaptive fallback |
| [`skill-creator`](playbooks/skill-creator.md) | Create from workflow, improve existing, composite skill design |
| [`workflow-orchestrator`](playbooks/workflow-orchestrator.md) | End-to-end bug fix, feature implementation, release validation, safe refactoring |
| [`agentic-workflow-engine`](playbooks/agentic-workflow-engine.md) | Autonomous bug fix with self-correction, iterative coverage, feature with gates, safe refactoring, security hardening |

---

## 🔧 Advanced Features

### Multi-Provider Model Routing (OpenRouter + Local + Cloud)

```yaml
# model-router config excerpt
providers:
  openrouter:
    api_base: "https://openrouter.ai/api/v1"
    models:
      # FREE tier
      - id: meta-llama/llama-3.1-8b-instruct:free
        pricing: { input: 0, output: 0 }
      - id: mistralai/mistral-7b-instruct:free
        pricing: { input: 0, output: 0 }
      # CHEAP paid
      - id: deepseek/deepseek-coder
        pricing: { input: 0.14, output: 0.28 }
      - id: google/gemini-1.5-flash
        pricing: { input: 0.075, output: 0.30 }
      # PREMIUM
      - id: anthropic/claude-3.5-sonnet
        pricing: { input: 3.00, output: 15.00 }
  
  local:  # Ollama, vLLM, etc.
    api_base: "http://localhost:11434/v1"
    models:
      - id: llama-3.1-70b-instruct
        tags: [private, local]
        pricing: { input: 0, output: 0 }
```

**Privacy Gates:** Confidential data → local models only. Public data → any provider.

### Autonomous Workflow Loops

```yaml
# Iterative test improvement
loop:
  max_iterations: 5
  condition: "{{coverage.percent}} < 80"
  body:
    - skill: autonomous-testing
      input: { target_coverage: 80, gaps: "{{coverage.gaps}}" }
    - skill: codebase-intelligence
      input: { target: "test_coverage" }
```

### Skill Composition Patterns

See [`SKILL-COMPOSITION.md`](SKILL-COMPOSITION.md) for 10 patterns:
- Sequential Pipeline
- Parallel Fan-Out/In
- Conditional Branching
- Iterative Refinement
- Human-in-the-Loop Gates
- Composite Skills
- Adapters
- Fallback Chains
- Observability Wrappers

---

## 🛡️ Safety & Governance

| Principle | Implementation |
|-----------|----------------|
| **Evidence-based** | Every claim backed by tool output (test results, diffs, logs) |
| **Minimal changes** | Smallest safe fix, regression test required |
| **Human gates** | Approval required for writes, deploys, secrets, budget |
| **Audit trail** | Structured logs for every skill execution |
| **No silent failures** | Explicit pass/fail/blocked, no degraded fallbacks |
| **Secret safety** | Never logs credentials, routes confidential data to local models |

---

## 📦 Repository Structure

```
.
├── AGENTS.md                    # Repository instructions for agents
├── CONTRIBUTING.md              # Contribution guide
├── LICENSE                      # MIT License
├── README.md                    # This file
├── SKILLS.md                    # Skill registry & index
├── SKILL-COMPOSITION.md         # Composition patterns guide
├── playbooks/                   # Detailed usage guides
│   ├── codebase-intelligence.md
│   ├── autonomous-debugging.md
│   ├── autonomous-testing.md
│   ├── multi-agent-review.md
│   ├── model-router.md
│   ├── skill-creator.md
│   └── workflow-orchestrator.md
│   ├── advanced-model-router.md
│   ├── agentic-workflow-engine.md
│   ├── security-audit.md
│   ├── dependency-management.md
│   └── release-coordinator.md
│   ├── performance-profiler.md
│   ├── code-refactorer.md
│   ├── documentation-synthesizer.md
│   ├── observability-instrumenter.md
│   ├── skill-benchmarker.md
│   └── secure-release.md
│   ├── security-dependency-audit.md
│   ├── performance-optimization.md
│   ├── architecture-documentation.md
│   ├── performance-observability.md
│   ├── debug-performance.md
│   ├── refactor-with-verification.md
│   ├── security-review.md
│   └── workflow-benchmarking.md
│   ├── test-coverage-analyzer.md
│   ├── security-debugger.md
│   ├── quality-gate-review.md
│   ├── workflow-optimizer.md
│   ├── autonomous-refactoring-planner.md
│   ├── api-contract-tester.md
│   ├── incident-responder.md
│   ├── compliance-auditor.md
│   ├── database-query-optimizer.md
│   ├── configuration-validator.md
│   ├── api-version-manager.md
│   ├── error-budget-tracker.md
│   ├── database-schema-linter.md
│   ├── chaos-engineer.md
│   ├── secret-scanner-historical.md
│   ├── production-safety-engine.md
│   ├── api-governance-platform.md
│   ├── database-reliability-engine.md
│   ├── security-operations-center.md
│   └── developer-experience-platform.md
└── skills/                      # Skill definitions
    ├── codebase-intelligence/
    ├── autonomous-debugging/
    ├── autonomous-testing/
    ├── multi-agent-review/
    ├── model-router/
    ├── skill-creator/
    └── workflow-orchestrator/
    ├── advanced-model-router/
    ├── agentic-workflow-engine/
    ├── security-audit/
    ├── dependency-management/
    ├── release-coordinator/
    ├── performance-profiler/
    ├── code-refactorer/
    ├── documentation-synthesizer/
    ├── observability-instrumenter/
    ├── skill-benchmarker/
    ├── security-dependency-audit/
    ├── performance-optimization/
    ├── architecture-documentation/
    ├── performance-observability/
    ├── secure-release/
    ├── debug-performance/
    ├── refactor-with-verification/
    └── security-review/
    └── workflow-benchmarking/
    ├── test-coverage-analyzer/
    ├── security-debugger/
    ├── quality-gate-review/
    ├── workflow-optimizer/
    ├── autonomous-refactoring-planner/
    ├── api-contract-tester/
    ├── incident-responder/
    ├── compliance-auditor/
    ├── database-query-optimizer/
    ├── configuration-validator/
    ├── api-version-manager/
    ├── error-budget-tracker/
    ├── database-schema-linter/
    ├── chaos-engineer/
    ├── secret-scanner-historical/
    ├── production-safety-engine/
    ├── api-governance-platform/
    ├── database-reliability-engine/
    ├── security-operations-center/
    └── developer-experience-platform/
├── skills-factory/                # Skills Making Factory
│   ├── README.md                  # Factory overview
│   ├── factory-core.md            # Core orchestration
│   ├── discovery-engine.md        # Skill scanning & gap detection
│   ├── research-engine.md         # Best practice research
├── skill-analyzer.md              # Skill quality analysis
├── skill-generator.md             # New skill manufacturing
├── combination-engine.md          # Skill combination (A+B=C)
├── testing-engine.md              # Comparative testing
├── benchmark-engine.md            # Performance benchmarking
├── security-engine.md             # Security checks
├── optimization-engine.md         # Skill optimization
├── evolution-engine.md            # Continuous improvement
├── quality-control.md             # Quality gates
├── meta-skills-factory.md         # Factory self-improvement
├── meta-skills-factory-playbook.md # Factory playbook
├── meta-skills-factory/           # Meta-skill definition
│   └── SKILL.md
├── laboratories/
│   ├── experiments/
│   ├── prototypes/
│   ├── failed-tests/
│   └── benchmark-results/
├── libraries/
│   ├── production/
│   ├── experimental/
│   ├── deprecated/
│   └── archived/
├── registry/
│   ├── skill-inventory.json
│   ├── quality-decisions.json
│   ├── pending-skills.json
│   └── pending-combinations.json
├── reports/
├── audit-logs/
└── factory-config/
    ├── factory-config.json
    ├── governance-rules.json
    └── capability-matrix.json
```

---

## 🤝 Contributing

See [`CONTRIBUTING.md`](CONTRIBUTING.md) for:
- Skill design principles
- Validation checklist
- Testing requirements
- Release process

---

## 📄 License

MIT License — see [`LICENSE`](LICENSE) for details.

---

## 🔗 Related

- [Hermes Agent Framework](https://github.com/hijaz/hermes) — Runtime for these skills
- [OpenRouter](https://openrouter.ai) — 100+ models, one API

---

*Built with discipline. Used in production. Evolved by feedback.*