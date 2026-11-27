# Playbook: Skill Suggestion Engine

*Practical examples for the `skill-suggestion-engine` skill*

---

## Scenario 1: Suggest skills for debugging task (happy path)

**Trigger:** "Suggest skills for debugging a slow API endpoint."

**Invocation:**
```
Suggest skills for task: "Debug slow API endpoint in payment service"
Context:
- Repository: Node.js API with Express
- Language: TypeScript
- Issue: p95 latency > 2 seconds on /api/payments
- Existing files: src/api/payments.ts, tests/payments.test.ts
- Time budget: 20 minutes
```

**Execution Log:**
```
## Skill Suggestion: Slow API Endpoint Debugging

### Request Analysis
- Task type: debugging, performance
- Key concepts: API endpoint, latency, payments, Node.js, TypeScript
- Context: p95 latency > 2s, specific endpoint, test files exist

### Skill Matching
| Skill | Confidence | Rationale |
|-------|------------|-----------|
| autonomous-debugging | 95% | Directly matches debugging task, reproduces and resolves defects |
| performance-profiler | 90% | Matches performance issue (slow endpoint), identifies bottlenecks |
| codebase-intelligence | 85% | Maps codebase to understand payment service structure |
| autonomous-testing | 80% | Tests payment endpoint, verifies fixes don't break tests |
| observability-instrumenter | 75% | Adds logging/metrics to identify slow paths |

### Skill Combinations
| Combination | Capability | Rationale |
|-------------|------------|-----------|
| codebase-intelligence → autonomous-debugging → performance-profiler | Full debugging pipeline | Map code → reproduce issue → find bottleneck |
| performance-profiler → autonomous-debugging → autonomous-testing | Fix and verify performance | Profile → debug → test fix |

### Execution Guidance
1. **autonomous-debugging** (confidence: 95%)
   - Command: hermes run autonomous-debugging --goal "Debug slow /api/payments endpoint"
   - Inputs: error description, reproduction steps, environment
   - Estimated time: 15 minutes
   - Approval needed: Yes (may modify code)

2. **performance-profiler** (confidence: 90%)
   - Command: hermes run performance-profiler --target src/api/payments.ts
   - Inputs: target file, workload, constraints
   - Estimated time: 10 minutes
   - Approval needed: No (read-only profiling)

### Report
- Top suggestion: autonomous-debugging (95% confidence)
- Best combination: codebase-intelligence → autonomous-debugging → performance-profiler
- All skills validated against context and constraints

Exit code: 0.
```

**Expected Output:**
Skill suggestion report with ranked skills, confidence scores, rationale, combinations, and execution guidance.

---

## Scenario 2: No skills match (failure case)

**Trigger:** "Suggest skills for unknown task type."

**Invocation:**
```
Suggest skills for task: "Calculate quantum physics equations"
Context:
- Repository: Python scientific computing
- Language: Python
- Task: quantum physics calculations
```

**Execution Log:**
```
## Skill Suggestion: Quantum Physics Calculations

### Request Analysis
- Task type: scientific computing, quantum physics
- Key concepts: quantum physics, equations, calculations, Python
- Context: Python scientific computing repository

### Skill Matching
| Skill | Confidence | Rationale |
|-------|------------|-----------|
| No skills matched | 0% | No skills in repository cover quantum physics calculations |

### Analysis
The skills repository contains skills for software engineering, debugging, testing, security, documentation, and DevOps. None cover quantum physics calculations or scientific computing domains.

### Recommendations
1. No existing skill matches this task
2. Consider creating a new skill using skill-creator
3. Use skill-template-generator to create a template for quantum physics skill
4. Consider manual computation or specialized scientific tools

### Report
- No matching skills found
- Exit code: 1
- Recommendation: Create new skill or use external tools

Exit code: 1.
```

**Expected Output:**
Skill suggestion report showing no matches with recommendations for creating new skills.

---

## Scenario 3: All suggestions require approval (safety case)

**Trigger:** "Suggest skills for code refactoring without approval."

**Invocation:**
```
Suggest skills for task: "Refactor authentication module"
Context:
- Repository: auth service
- Approval available: NO
- Changes allowed: read-only only
```

**Execution Log:**
```
## Skill Suggestion: Auth Module Refactoring

### Request Analysis
- Task type: refactoring, code modification
- Key concepts: authentication module, refactor
- Constraints: read-only only, no approval available

### Skill Matching
| Skill | Confidence | Approval Required |
|-------|------------|-------------------|
| code-refactorer | 90% | YES (modifies code) |
| autonomous-debugging | 85% | YES (may modify code) |
| codebase-intelligence | 95% | NO (read-only) |
| multi-agent-review | 80% | NO (review only) |
| skill-comprehension-analyzer | 75% | NO (read-only analysis) |

### Filtering (read-only constraint)
- code-refactorer: EXCLUDED (requires code modification approval)
- autonomous-debugging: EXCLUDED (may modify code)
- codebase-intelligence: INCLUDED (read-only mapping)
- multi-agent-review: INCLUDED (review only, no modifications)
- skill-comprehension-analyzer: INCLUDED (read-only analysis)

### Skill Suggestions (Read-Only)
1. **codebase-intelligence** (95% confidence)
   - Maps auth module structure, dependencies, entry points
   - No code changes, no approval needed
   - Command: hermes run codebase-intelligence --target src/auth/

2. **skill-comprehension-analyzer** (75% confidence)
   - Analyzes existing auth code quality and structure
   - Identifies improvement opportunities without modifying
   - Command: hermes run skill-comprehension-analyzer --skill src/auth/

3. **multi-agent-review** (80% confidence)
   - Reviews auth code for security and quality issues
   - Read-only review, no modifications
   - Command: hermes run multi-agent-review --scope src/auth/

### Report
- All code-modifying skills excluded due to approval constraint
- Read-only alternatives provided
- User can request approval for code-modifying skills if needed

Exit code: 0.
```

**Expected Output:**
Skill suggestion report with read-only alternatives and approval requirements clearly marked.
