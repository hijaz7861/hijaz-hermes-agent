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
| `security-dependency-audit` | Security Engineering | Medium | Dependency audit with security focus — vulnerable packages, CVEs, secure remediation | `security-audit`, `dependency-management` |
| `performance-optimization` | Performance Optimization | Medium | Profile bottlenecks then refactor hot paths — verified performance gains with benchmarks | `performance-profiler`, `code-refactorer` |
| `architecture-documentation` | Documentation | Medium | Architecture map + synthesized docs from code — API reference, module overviews, data flow | `codebase-intelligence`, `documentation-synthesizer` |
| `performance-observability` | DevOps & Infrastructure | Medium | Instrument code + profile overhead — observability with measured performance impact | `observability-instrumenter`, `performance-profiler` |
| `secure-release` | Security Engineering | High | Release coordination with mandatory security audit gate — no release with unresolved CRITICAL/HIGH | `release-coordinator`, `security-audit` |
| `debug-performance` | Debugging | Medium | Debug performance defects — reproduce slowness, find root cause, fix with benchmark verification | `autonomous-debugging`, `performance-profiler` |
| `refactor-with-verification` | Software Engineering | Medium | Refactor with test verification — characterization tests, behavior-preserving transforms, test gate | `code-refactorer`, `autonomous-testing` |
| `security-review` | Security Engineering | High | Security-focused multi-agent review — adversarial review with security audit scan, severity classification | `multi-agent-review`, `security-audit` |
| `workflow-benchmarking` | Multi-Agent Orchestration | Medium | Benchmark multi-skill workflows — compare configurations, measure performance, identify bottlenecks | `workflow-orchestrator`, `skill-benchmarker` |
| `agentic-routing` | Multi-Agent Orchestration | Very High | Autonomous execution with model routing — each subtask routed to optimal model by task/privacy/cost | `agentic-workflow-engine`, `model-router` |
| `test-coverage-analyzer` | Testing & Quality Assurance | Medium | Analyze coverage gaps, recommend targeted tests, verify improvement | `codebase-intelligence`, `autonomous-testing` |
| `security-debugger` | Security Engineering | Medium | Debug security defects — reproduce, find root cause, fix with regression tests | `autonomous-debugging`, `security-audit` |
| `quality-gate-review` | Security Engineering | High | Gated code review — independent review + test validation before approval | `multi-agent-review`, `autonomous-testing` |
| `workflow-optimizer` | Performance Optimization | Medium | Optimize multi-skill workflows — measure performance, identify bottlenecks | `workflow-orchestrator`, `skill-benchmarker` |
| `autonomous-refactoring-planner` | Software Engineering | Very High | Autonomous refactoring planning and execution with self-correction | `agentic-workflow-engine`, `codebase-intelligence` |
| `api-contract-tester` | Testing & Quality Assurance | Medium | Validate API contracts — detect breaking changes, schema mismatches | `codebase-intelligence`, `autonomous-testing` |
| `incident-responder` | DevOps & Infrastructure | Medium | Incident response — reproduce, correlate observability, fix, monitor | `autonomous-debugging`, `observability-instrumenter` |
| `compliance-auditor` | Security Engineering | Medium | Compliance audit — GDPR, SOC2, HIPAA, PCI-DSS requirements | `security-audit`, `documentation-synthesizer` |
| `database-query-optimizer` | Performance Optimization | Medium | Optimize database queries — slow queries, N+1, missing indexes | `performance-profiler`, `code-refactorer` |
| `configuration-validator` | Security Engineering | Medium | Validate configuration — secrets, insecure defaults, drift | `codebase-intelligence`, `security-audit` |
| `api-version-manager` | Documentation | Medium | API version management — versions, deprecation, migration guides | `codebase-intelligence`, `documentation-synthesizer` |
| `error-budget-tracker` | DevOps & Infrastructure | Medium | Error budget tracking — SLO compliance, budget consumption, alerts | `autonomous-testing`, `observability-instrumenter` |
| `database-schema-linter` | Performance Optimization | Medium | Schema linting — missing indexes, constraints, unsafe types | `codebase-intelligence`, `security-audit` |
| `chaos-engineer` | DevOps & Infrastructure | Medium | Chaos engineering — failure injection, resilience verification | `performance-profiler`, `incident-responder` |
| `secret-scanner-historical` | Security Engineering | Medium | Historical secret scanning — git history, leaked credentials | `security-audit`, `codebase-intelligence` |
| `production-safety-engine` | DevOps & Infrastructure | Very High | Production safety — incident response, error budgets, chaos, secure release | `incident-responder`, `error-budget-tracker`, `chaos-engineer`, `secure-release` |
| `api-governance-platform` | Security Engineering | Very High | API governance — contract testing, version management, security review, quality gate | `api-contract-tester`, `api-version-manager`, `security-review`, `quality-gate-review` |
| `database-reliability-engine` | Performance Optimization | Very High | Database reliability — query optimization, schema linting, coverage analysis | `database-query-optimizer`, `database-schema-linter`, `test-coverage-analyzer` |
| `security-operations-center` | Security Engineering | Very High | Security operations — secret scanning, debugging, compliance, review, dependencies | `secret-scanner-historical`, `security-debugger`, `compliance-auditor`, `security-review`, `security-dependency-audit` |
| `developer-experience-platform` | Software Engineering | Very High | Developer experience — coverage analysis, verified refactoring, documentation | `test-coverage-analyzer`, `refactor-with-verification`, `architecture-documentation`, `code-refactorer` |

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

### security-dependency-audit
```
Trigger: "Audit dependencies for security vulnerabilities" / "Find vulnerable packages"
Input: Dependency manifests/lockfiles, security advisory feeds, severity threshold
Output: Vulnerable dependency report, CVE IDs, fix versions, prioritized remediation plan
Time: 5-20 min
Features: Dependency inventory + security scan, CVE/advisory IDs, severity ranking, approval-gated fixes
```

### performance-optimization
```
Trigger: "Optimize this code for performance" / "Profile and fix slow endpoint X"
Input: Target code, workload, performance target, constraints
Output: Baseline profile, bottleneck table, refactor plan, before/after benchmarks, verification
Time: 10-30 min
Features: Measurement-first profiling + behavior-preserving refactoring, test gate, rollback on regression
```

### architecture-documentation
```
Trigger: "Document this repository's architecture" / "Generate API docs from code"
Input: Target repo/module, format, audience, existing docs
Output: Architecture map, API reference, module overviews, coverage report, staleness report
Time: 5-15 min
Features: Code-as-source-of-truth, data flow mapping, real examples from tests, contradiction detection
```

### performance-observability
```
Trigger: "Instrument and profile service X" / "Add observability and measure overhead"
Input: Target code, telemetry type, overhead budget, destination
Output: Instrumentation diff, baseline/post profiles, overhead %, data-classification review
Time: 5-15 min
Features: Observability + profiling, overhead budget enforcement, no secret logging, data classification
```

### secure-release
```
Trigger: "Prepare secure release vX.Y.Z" / "Release with security audit gate"
Input: Target version, branch, commit range, security policy
Output: Release report, security findings, gate status, changelog, next steps
Time: Variable (minutes to hours)
Features: Release readiness + security audit, mandatory CRITICAL/HIGH gate, approval-gated version bump
```

### debug-performance
```
Trigger: "Debug why endpoint X is slow" / "Find performance regression in module Y"
Input: Performance issue, reproduction steps, environment, acceptable target
Output: Reproduction evidence, root cause, fix, regression test, before/after benchmarks
Time: 10-30 min
Features: Debugging + profiling, root-cause analysis, regression benchmark, rollback on failure
```

### refactor-with-verification
```
Trigger: "Refactor module X with full test verification" / "Extract method safely"
Input: Target code, transformation type, scope, test coverage requirement
Output: Refactor plan, characterization tests, diff, before/after test results, risk assessment
Time: 5-15 min
Features: Refactoring + test verification, behavior-preserving, test gate (pass before/after), rollback
```

### security-review
```
Trigger: "Security review this PR" / "Review auth module for security issues"
Input: Change diff/PR, security requirements, severity threshold for blocking
Output: Findings table, role reports, consolidated report, go/no-go decision
Time: 10-60 min
Features: Multi-agent review + security audit, adversarial review, severity classification, post-integration verification
```

### workflow-benchmarking
```
Trigger: "Benchmark this workflow configuration" / "Compare workflow A vs. workflow B"
Input: Workflow definitions, scenario, metrics, repetitions
Output: Evaluation report, comparison matrix, bottleneck analysis, adopt/reject/iterate decision
Time: 10-30 min
Features: Workflow execution + benchmarking, identical scenario comparison, statistical significance, bottleneck identification
```

### agentic-routing
```
Trigger: "Execute goal autonomously with optimal model routing" / "Agentic workflow with routing"
Input: High-level goal, task types per subtask, privacy classification, budget/latency targets
Output: GoalSpec, execution plan, routing decisions per subtask, execution result, audit trail
Time: Variable (minutes to hours)
Features: Agentic execution + model routing, per-subtask model selection, privacy gates, budget limits, self-correction
```

### test-coverage-analyzer
```
Trigger: "Analyze test coverage gaps in module X" / "Find untested code paths"
Input: Target code, coverage threshold, existing coverage data
Output: Coverage gap report, risk-classified gaps, test recommendations
Time: 5-15 min
Features: Codebase mapping + coverage analysis, risk classification, prioritized recommendations
```

### security-debugger
```
Trigger: "Debug SQL injection in endpoint X" / "Find auth bypass vulnerability"
Input: Security issue, reproduction steps, environment, acceptable target
Output: Reproduction evidence, root cause, fix, regression test, verification
Time: 10-30 min
Features: Debugging + security audit, root-cause analysis, regression benchmark, no secret logging
```

### quality-gate-review
```
Trigger: "Review PR #X with quality gate — tests must pass"
Input: Change diff/PR, acceptance criteria, test requirements, gate threshold
Output: Review findings, test evidence, gate decision (PASS/FAIL/BLOCKED)
Time: 10-60 min
Features: Multi-agent review + test validation, mandatory gate, cross-reference findings
```

### workflow-optimizer
```
Trigger: "Optimize this workflow for speed" / "Find bottlenecks in workflow X"
Input: Workflow definitions, scenario, performance target, repetitions
Output: Baseline profile, bottleneck analysis, optimized config, before/after results
Time: 10-30 min
Features: Workflow execution + benchmarking, bottleneck identification, statistical significance
```

### autonomous-refactoring-planner
```
Trigger: "Autonomously refactor module X" / "Plan and execute refactoring"
Input: Refactoring goal, constraints, behavior contract, quality thresholds
Output: GoalSpec, execution plan, routing decisions, execution result, lessons learned
Time: Variable (minutes to hours)
Features: Agentic planning + codebase mapping, per-subtask routing, self-correction, quality gates
```

### api-contract-tester
```
Trigger: "Validate API contracts for endpoint X" / "Check for breaking API changes"
Input: Contract spec (OpenAPI/GraphQL), target API, codebase, breaking change threshold
Output: Contract compliance report, breaking changes, schema mismatches, test results
Time: 5-20 min
Features: Codebase mapping + contract validation, breaking change detection, staging-only testing
```

### incident-responder
```
Trigger: "Respond to production incident #X" / "Debug the outage in service Y"
Input: Incident details, observability data, environment, rollback plan
Output: Incident timeline, root cause, fix, monitoring added, verification
Time: 15-60 min
Features: Debugging + observability, log/metric/trace correlation, monitoring for prevention
```

### compliance-auditor
```
Trigger: "Audit for GDPR compliance" / "Check SOC2 requirements for service X"
Input: Compliance framework, target code/config, data classification, existing docs
Output: Compliance gap report, data inventory, remediation plan, documentation
Time: 10-30 min
Features: Security audit + documentation synthesis, requirement mapping, gap classification
```

### database-query-optimizer
```
Trigger: "Optimize slow database queries in module X" / "Find N+1 query patterns"
Input: Target queries, database type, workload, performance target
Output: Query performance report, optimization recommendations, before/after benchmarks
Time: 10-30 min
Features: Profiling + refactoring, EXPLAIN ANALYZE verification, data integrity gate
```

### configuration-validator
```
Trigger: "Validate application configuration" / "Find hardcoded secrets in config"
Input: Config files, environment variables, code readers, environments
Output: Validation report, secret locations (redacted), drift analysis, remediation plan
Time: 5-15 min
Features: Codebase mapping + security audit, secret detection, environment drift detection
```

### api-version-manager
```
Trigger: "Manage API versioning for service X" / "Deprecate API v1 and migrate clients"
Input: API versions, deprecation policy, client usage data, breaking change definition
Output: Version inventory, breaking changes, deprecation timeline, migration guide
Time: 10-30 min
Features: Codebase mapping + documentation synthesis, version diffing, client compliance
```

### error-budget-tracker
```
Trigger: "Track error budget for service X" / "Monitor SLO compliance for API Y"
Input: SLO targets, time window, observability data, test results
Output: SLO compliance report, budget status, error rate trends, alert recommendations
Time: 5-15 min
Features: Testing + observability, SLO definition, budget calculation, alert thresholds
```

### database-schema-linter
```
Trigger: "Lint the database schema for service X" / "Check for missing indexes"
Input: Schema files, database type, naming conventions, security requirements
Output: Schema lint report, missing indexes/constraints, unsafe types, naming violations
Time: 5-15 min
Features: Codebase mapping + security audit, structural linting, security audit
```

### chaos-engineer
```
Trigger: "Run chaos experiment on service X" / "Test resilience under failure"
Input: Target, failure type, blast radius, safety thresholds, rollback plan
Output: Experiment hypothesis, results, resilience assessment, monitoring verification
Time: 15-60 min
Features: Profiling + incident response, failure injection, safety thresholds, auto-abort
```

### secret-scanner-historical
```
Trigger: "Scan git history for committed secrets" / "Find leaked credentials in history"
Input: Repository, scan depth, secret patterns, exclusions
Output: Secret findings report, exposure assessment, remediation recommendations
Time: 10-30 min
Features: Security audit + codebase mapping, commit history scanning, no secret output
```

### production-safety-engine
```
Trigger: "Ensure production safety for service X" / "Set up reliability monitoring"
Input: Services, SLO targets, observability data, release pipeline, safety thresholds
Output: Safety dashboard, incident response, chaos results, release report, improvement loop
Time: Variable (minutes to hours)
Features: 4-skill integration, SLO monitoring + chaos + incident response + secure release
```

### api-governance-platform
```
Trigger: "Establish API governance for service X" / "Validate API before release"
Input: API contract, versions, security requirements, quality gate criteria, deprecation policy
Output: Governance report: contract, version, security, quality, final go/no-go
Time: Variable (minutes to hours)
Features: 4-skill integration, contract testing + versioning + security review + quality gate
```

### database-reliability-engine
```
Trigger: "Ensure database reliability for service X" / "Database health check"
Input: Database, schema files, query files, test files, workload, performance target
Output: Reliability report: query perf, schema lint, coverage gaps, remediation plan
Time: Variable (minutes to hours)
Features: 3-skill integration, query optimization + schema linting + coverage analysis
```

### security-operations-center
```
Trigger: "Establish security operations for repository X" / "Full security assessment"
Input: Repository, compliance frameworks, dependency manifests, change scope, security policy
Output: Security ops report: secrets, vulnerabilities, compliance, review, dependencies
Time: Variable (minutes to hours)
Features: 5-skill integration, secret scanning + debugging + compliance + review + dependencies
```

### developer-experience-platform
```
Trigger: "Improve developer experience for module X" / "DX improvement"
Input: Target code, coverage threshold, refactoring goals, documentation format, quality thresholds
Output: DX report: coverage gaps, refactoring results, documentation, maintainability metrics
Time: Variable (minutes to hours)
Features: 4-skill integration, coverage analysis + verified refactoring + documentation
```

---

---

## Maintenance

- **Owner:** HIJAZ team
- **Review cycle:** Quarterly
- **Deprecation policy:** 2 major versions notice
- **Breaking changes:** Require major version bump in skill name (e.g., `codebase-intelligence-v2`)

---

*Generated from skill frontmatter and manual curation. Update when adding/modifying skills.*