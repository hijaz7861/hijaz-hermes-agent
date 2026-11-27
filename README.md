# HIJAZ Hermes Agent Skills

[![Skills](https://img.shields.io/badge/skills-17-brightgreen)](SKILLS.md)
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
│   └── skill-benchmarker.md
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
    └── skill-benchmarker/
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