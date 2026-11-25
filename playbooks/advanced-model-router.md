# Playbook: Advanced Model Router

*Practical examples for the `advanced-model-router` skill*

---

## Scenario 1: Free Tier First — Code Generation

**Trigger:** "Write a React component for user avatar upload — use free model if good enough."

**Invocation:**
```
Route task: Code generation (React TypeScript component)
Constraints: 
- Privacy: INTERNAL (proprietary component library)
- Budget: $0.20
- Needs: Tools (file write), structured output (component + tests)
- Quality threshold: 85% of best model
```

**Execution Log:**
```
## Routing Decision: React Avatar Component

### Task Classification
- Type: code_generation
- Needs: coding=required, tools=required, structured_output=preferred
- Context: ~5 files (component library patterns)
- Estimated tokens: 3,000 in + 1,500 out

### Privacy Gate (INTERNAL)
Allowed: openrouter, local
Blocked: direct anthropic, direct openai (cloud)

### Free Model Evaluation (OpenRouter)
| Model | Coding | Tools | Structured | Context | Est. Cost | Quality Score |
|-------|--------|-------|------------|---------|-----------|---------------|
| meta-llama/llama-3.1-8b-instruct:free | 6 | ✅ | ⚠️ | 128k | $0.00 | 62 |
| mistralai/mistral-7b-instruct:free | 5 | ✅ | ❌ | 32k | $0.00 | 55 |
| google/gemma-2-9b-it:free | 6 | ✅ | ⚠️ | 8k | $0.00 | 58 |
| microsoft/phi-3-mini-128k-instruct:free | 5 | ✅ | ⚠️ | 128k | $0.00 | 53 |

**Best free: llama-3.1-8b-instruct:free (62/100)**
**Quality threshold: 85% of best paid (deepseek-coder: 87) = 74**
**Result: FREE models BELOW threshold (62 < 74)**

### Budget Model Evaluation
| Model | Coding | Tools | Structured | Context | Est. Cost | Quality Score |
|-------|--------|-------|------------|---------|-----------|---------------|
| deepseek/deepseek-coder | 9 | ✅ | ✅ | 128k | $0.04 | 87 |
| google/gemini-1.5-flash | 8 | ✅ | ✅ | 1M | $0.02 | 82 |
| meta-llama/llama-3.1-70b-instruct | 7 | ✅ | ✅ | 128k | $0.08 | 78 |

### Routing Decision
```
SELECTED: deepseek/deepseek-coder (OpenRouter)
REASON: Meets quality threshold (87), within budget ($0.04 << $0.20), 
        supports tools + structured output, 128k context
FALLBACK: google/gemini-1.5-flash
FALLBACK: meta-llama/llama-3.1-70b-instruct
ESTIMATED COST: $0.035
```

### Execution
```
$ route-task "React avatar upload component" --model=deepseek/deepseek-coder
✓ Component generated: AvatarUpload.tsx (TypeScript, 87 lines)
✓ Tests generated: AvatarUpload.test.tsx (12 tests)
✓ TypeScript compiles: ✅
✓ Tests pass: 12/12
✓ Actual cost: $0.032
✓ Latency: 6.2s
```

---

## Scenario 2: Confidential Data — Local Only

**Trigger:** "Analyze this production database schema for optimization — contains real customer PII columns."

**Invocation:**
```
Route task: Schema analysis (reasoning, long context)
Constraints:
- Privacy: CONFIDENTIAL (PII in column names, data patterns)
- Budget: $2.00
- Context: ~50k tokens (full schema + sample queries)
- No data leaves VPC
```

**Execution Log:**
```
## Routing Decision: Production Schema Analysis

### Privacy Gate (CONFIDENTIAL)
ALLOWED TAGS: ["local", "private", "airgapped"]
BLOCKED: All cloud providers (OpenRouter, Anthropic, OpenAI, Google)

### Local Model Evaluation (Ollama)
| Model | Reasoning | Context | Tags | Status |
|-------|-----------|---------|------|--------|
| llama-3.1-70b-instruct | 8 | 128k | [local, private, reasoning] | ✅ RUNNING |
| deepseek-coder-33b | 7 | 16k | [local, private, coding] | ✅ RUNNING |
| codellama-34b | 6 | 16k | [local, private, coding] | ✅ RUNNING |
| llama-3.1-8b-instruct | 5 | 128k | [local, private, fast] | ✅ RUNNING |

### Routing Decision
```
SELECTED: local/llama-3.1-70b-instruct (Ollama)
REASON: Only model with reasoning=8 + 128k context + privacy tags
CONTEXT CHECK: 50k tokens << 128k limit
COST: $0.00 (local inference)
ESTIMATED LATENCY: ~45s (local GPU)
```

### Execution
```
$ route-task "Analyze production schema..." --model=local/llama-3.1-70b-instruct
✓ Analysis complete (2,400 token response)
✓ Found: 12 missing indexes, 3 N+1 query patterns, 1 PII exposure risk
✓ Zero data egress verified
✓ Actual latency: 41s
✓ Cost: $0.00
```

---

## Scenario 3: Batch Classification — Cost Optimized

**Trigger:** "Classify 10,000 support tickets — spam vs legitimate — minimize cost."

**Invocation:**
```
Route batch: 10,000 classification tasks
Constraints:
- Type: classification (binary, structured JSON output)
- Privacy: PUBLIC (anonymized tickets)
- Budget: $0.50 total
- Output: JSON {label, confidence} per item
- Can use batch API (50% discount)
```

**Execution Log:**
```
## Routing Decision: Batch Ticket Classification

### Task Profile
- 10,000 items × ~150 tokens = 1.5M input tokens
- ~20 tokens output each = 200k output tokens
- Total: 1.7M tokens
- Structured output REQUIRED

### Model Comparison (with Batch API)
| Model | Input/$1M | Output/$1M | Batch Discount | Est. Cost | Quality |
|-------|-----------|------------|----------------|-----------|---------|
| google/gemini-1.5-flash | $0.075 | $0.30 | 50% | **$0.071** | 85 |
| deepseek/deepseek-chat | $0.14 | $0.28 | 50% | $0.147 | 82 |
| gpt-4o-mini | $0.15 | $0.60 | 50% | $0.172 | 88 |
| llama-3.1-8b-free | $0.00 | $0.00 | N/A | $0.00 | 65 |

### Routing Decision
```
SELECTED: google/gemini-1.5-flash (OpenRouter, Batch API)
REASON: Best cost/quality for classification, structured output native,
        1M context handles large batches, 50% batch discount
FALLBACK: deepseek/deepseek-chat (batch)
ESTIMATED COST: $0.071 << $0.50 budget
```

### Execution
```
$ route-batch classify-tickets --model=gemini-1.5-flash --batch-api --items=10000
✓ Batch submitted (job_id: batch_abc123)
✓ Completed in 8.3 minutes
✓ Results: 10,000 JSON objects, all valid schema
✓ Accuracy: 99.1% (validated on 200 labeled sample)
✓ Actual cost: $0.068
✓ Cost per 1k: $0.0068
```

---

## Scenario 4: Long Context — Full Repo Analysis

**Trigger:** "Analyze this 80k-line monorepo for architectural debt — find circular deps, god classes, testing gaps."

**Invocation:**
```
Route task: Architecture analysis (reasoning, very long context)
Constraints:
- Privacy: INTERNAL (proprietary codebase)
- Budget: $2.00
- Context: ~300k tokens (entire codebase)
- Output: Structured report (Markdown + JSON)
```

**Execution Log:**
```
## Routing Decision: Monorepo Architecture Analysis

### Context Challenge
- 300k tokens exceeds most model limits (128k standard)
- Need 1M+ context model OR retrieval-augmented approach

### Eligible Models (Context ≥ 300k)
| Model | Context | Cost (300k in + 10k out) | Quality |
|-------|---------|---------------------------|---------|
| google/gemini-1.5-pro | 1M | $0.40 | 92 |
| google/gemini-1.5-flash | 1M | $0.08 | 85 |
| anthropic/claude-3.5-sonnet | 200k | ❌ EXCEEDS | 95 |
| gpt-4o | 128k | ❌ EXCEEDS | 90 |

### Routing Decision
```
SELECTED: google/gemini-1.5-pro (OpenRouter)
REASON: Only model with 1M context within budget, high reasoning
ALTERNATIVE: Retrieval-augmented with claude-3.5-sonnet (200k context)
  - codebase-intelligence extracts key 50k tokens
  - Then route to claude-3.5-sonnet
  - Cost: ~$0.20, slightly lower quality
ESTIMATED COST: $0.40 (well within $2.00)
PROMPT CACHING: Enabled (repeat analyses 80% cheaper)
```

### Execution
```
$ route-task "Analyze monorepo architecture..." --model=gemini-1.5-pro --cache-prompt
✓ Full repo sent (298,432 tokens)
✓ Analysis completed in 112s
✓ Output: 5,200 tokens (JSON + Markdown)
✓ Findings: 23 circular deps, 7 god classes, 34% test gaps, 12 security issues
✓ Actual cost: $0.38 (prompt cache hit on 2nd run: $0.07)
```

---

## Scenario 5: Adaptive Fallback Chain

**Trigger:** "Generate complex SQL migration — primary model rate limited."

**Invocation:**
```
Route task: SQL generation (coding, reasoning)
Constraints:
- Privacy: INTERNAL
- Budget: $1.00
- Needs: High reliability (production migration)
```

**Execution Log:**
```
## Routing Decision: SQL Migration Generation

### Primary Chain
1. deepseek/deepseek-coder (OpenRouter) — coding=9, $0.14/$0.28
2. google/gemini-1.5-flash (OpenRouter) — coding=8, $0.075/$0.30
3. anthropic/claude-3.5-sonnet (OpenRouter) — coding=9, $3/$15
4. local/llama-3.1-70b (Ollama) — coding=7, FREE

### Execution with Fallback
```
$ route-task "Generate SQL migration..." --model=auto
✓ Attempt 1: deepseek/deepseek-coder
✗ RATE_LIMITED (429) after 2.1s
✓ Circuit breaker: deepseek marked degraded
✓ Attempt 2: google/gemini-1.5-flash (fallback 1)
✓ SUCCESS in 4.3s
✓ Cost: $0.018
✓ Migration generated, syntax validated
```

### Fallback Telemetry
```json
{
  "primary": "deepseek/deepseek-coder",
  "attempt": 0,
  "error": "rate_limit",
  "fallback_used": "google/gemini-1.5-flash",
  "fallback_attempt": 1,
  "total_latency_ms": 6400,
  "total_cost": 0.018,
  "circuit_breaker_state": {
    "deepseek/deepseek-coder": "half_open",
    "google/gemini-1.5-flash": "closed"
  }
}
```

---

## Scenario 6: Dynamic Free Tier Upgrade

**Trigger:** "Classify these 500 log lines — use free model, but upgrade if accuracy < 95%."

**Invocation:**
```
Route with quality gate:
- Task: Classification (500 items)
- Primary: Free model (llama-3.1-8b-free)
- Quality gate: Validate on 50 labeled samples
- If accuracy < 95% → auto-upgrade to budget model
```

**Execution Log:**
```
## Routing Decision: Log Classification with Quality Gate

### Phase 1: Free Model Attempt
```
SELECTED: meta-llama/llama-3.1-8b-instruct:free
EXECUTION: 500 classifications in 3.2s, $0.00
VALIDATION: 50 labeled samples → 91% accuracy
QUALITY GATE: FAILED (91% < 95%)
```

### Phase 2: Auto-Upgrade
```
TRIGGER: Quality gate failure
UPGRADE TO: google/gemini-1.5-flash (budget)
RE-EXECUTION: 500 classifications in 4.1s
VALIDATION: 50 labeled samples → 98% accuracy
QUALITY GATE: PASSED
COST: $0.004
```

### Final Result
```
MODEL USED: google/gemini-1.5-flash (upgraded from free)
ACCURACY: 98%
COST: $0.004
TIME: 7.3s total
AUTO-UPGRADE: ✅ Triggered and logged
```
```

---

## Configuration Tips

### Enable Free Tier Aggressive Mode
```yaml
cost_optimization:
  free_tier_threshold: 0.80  # Lower = more free usage
  auto_upgrade_on_quality_gate: true
  quality_gate_sample_size: 50
  quality_gate_threshold: 0.95
```

### Privacy-First Configuration
```yaml
routing_policy:
  privacy_gates:
    CONFIDENTIAL: ["local", "private"]  # Strict
  # Override per-task if needed (with approval)
  allow_privacy_override: false
```

### Local Model Setup (Ollama)
```bash
# Pull models for private/confidential workloads
ollama pull llama-3.1-70b-instruct    # Best reasoning
ollama pull deepseek-coder-33b        # Best coding
ollama pull llama-3.1-8b-instruct     # Fast, free

# Verify
ollama list
```

---

## Monitoring & Alerts

```yaml
telemetry:
  alerts:
    - name: "budget_80%"
      condition: "cumulative_cost > 0.8 * budget"
      action: "warn"
    - name: "fallback_activated"
      condition: "fallback_attempt > 0"
      action: "log"
    - name: "free_model_quality_gate_fail"
      condition: "free_model_accuracy < threshold"
      action: "auto_upgrade"
    - name: "circuit_breaker_open"
      condition: "circuit_breaker_state == open"
      action: "alert_oncall"
```

---

*This playbook demonstrates the advanced model router's ability to balance cost, quality, privacy, and reliability automatically. All routing decisions are auditable and reproducible.*