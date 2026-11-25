# Playbook: Model Router

*Practical examples for the `model-router` skill*

---

## Scenario 1: Task Classification & Routing

**Trigger:** "Route this task: 'Write a complex GraphQL resolver with auth'"

**Invocation:**
```
Classify and route: "Write a complex GraphQL resolver with auth checks, pagination, and N+1 prevention"
Constraints: 
- Code generation task
- Needs strong reasoning
- Context: ~2000 lines of related code
- Budget: <$0.50
- No sensitive data
```

**Execution Log:**
```
## Routing Decision: GraphQL Resolver Generation

### Task Classification
- **Primary:** Code generation (GraphQL, TypeScript)
- **Secondary:** Security (auth checks), Performance (N+1)
- **Complexity:** High (multi-concern, requires reasoning)
- **Context needed:** ~2000 lines (schema, existing resolvers, auth patterns)

### Constraint Analysis
| Constraint | Value | Impact |
|------------|-------|--------|
| Data sensitivity | Low (public schema) | Any provider OK |
| Context length | ~8k tokens (2000 lines × 4) | Needs 16k+ context |
| Latency target | <30s | Excludes slow models |
| Budget | $0.50 | Excludes premium models |
| Tool support | Required (file read/write) | Must support function calling |

### Provider Catalog (Live Check)
| Provider | Model | Context | Input/$1M | Output/$1M | Tools | Status |
|----------|-------|---------|-----------|------------|-------|--------|
| Anthropic | claude-3.5-sonnet | 200k | $3.00 | $15.00 | ✅ | ✅ Available |
| OpenAI | gpt-4o | 128k | $2.50 | $10.00 | ✅ | ✅ Available |
| OpenRouter | deepseek/deepseek-coder | 128k | $0.14 | $0.28 | ✅ | ✅ Available |
| OpenRouter | meta-llama/llama-3.1-70b | 128k | $0.59 | $0.79 | ✅ | ✅ Available |
| Local | codellama-34b | 16k | $0.00 | $0.00 | ⚠️ Limited | ✅ Running |

### Ranking (Task Fit → Reliability → Latency → Cost)
| Rank | Model | Score | Rationale |
|------|-------|-------|-----------|
| 1 | **claude-3.5-sonnet** | 94/100 | Best reasoning for complex code, 200k context, tools |
| 2 | **gpt-4o** | 88/100 | Strong code gen, 128k context, slightly cheaper |
| 3 | **deepseek-coder** | 82/100 | Excellent code model, very cheap, 128k context |
| 4 | **llama-3.1-70b** | 75/100 | Good reasoning, cheap, but less reliable on TS |
| 5 | **codellama-34b (local)** | 60/100 | Free, but 16k context too small, limited tools |

### Routing Decision
```
SELECTED: anthropic/claude-3.5-sonnet
FALLBACK: openai/gpt-4o
BUDGET CHECK: ~2500 input + 1500 output tokens = $0.031 << $0.50
CONTEXT CHECK: 8k tokens << 200k limit
TOOL CHECK: Full function calling support
```

### Fallback Chain
1. claude-3.5-sonnet (primary)
2. gpt-4o (if Anthropic rate limited)
3. deepseek-coder (if both unavailable, cost-optimized)
4. FAIL (if all unavailable — do not silently degrade)

### Execution Result
```
$ route-task "Write GraphQL resolver..." --model=claude-3.5-sonnet
✓ Task routed to claude-3.5-sonnet
✓ Context prepared (1,847 lines, 7,388 tokens)
✓ Generation completed in 12.3s
✓ Output validated (TypeScript compiles, tests pass)
✓ Cost: $0.028 (1,847 input + 1,423 output tokens)
```
```

---

## Scenario 2: Privacy-Gated Routing

**Trigger:** "Route this: 'Analyze this production database schema for optimization' — contains real table names, indexes, query patterns."

**Invocation:**
```
Route task with sensitive data:
- Input: Production DB schema (real table names, PII columns, query logs)
- Task: Analysis/reasoning
- Constraint: Data must not leave VPC
- Budget: $2.00
```

**Execution Log:**
```
## Routing Decision: Production Schema Analysis

### Privacy Gate Evaluation
```
Data classification: CONFIDENTIAL (production schema + query patterns)
Policy: "Confidential data → approved local/self-hosted only"
```

### Eligible Models (Privacy Filter Applied)
| Provider | Model | Privacy | Eligible? |
|----------|-------|---------|-----------|
| Anthropic | claude-3.5-sonnet | Cloud | ❌ REJECTED |
| OpenAI | gpt-4o | Cloud | ❌ REJECTED |
| OpenRouter | *any* | Cloud | ❌ REJECTED |
| Local (VPC) | llama-3.1-70b-instruct | **Local** | ✅ APPROVED |
| Local (VPC) | codellama-34b | **Local** | ✅ APPROVED |
| Local (VPC) | deepseek-coder-33b | **Local** | ✅ APPROVED |

### Ranking (Privacy-First)
| Rank | Model | Context | Capability | Notes |
|------|-------|---------|------------|-------|
| 1 | **llama-3.1-70b-instruct (local)** | 128k | Strong reasoning | Best for analysis |
| 2 | **deepseek-coder-33b (local)** | 16k | Code-focused | Context may be tight |
| 3 | **codellama-34b (local)** | 16k | Code gen | Weak on analysis |

### Routing Decision
```
SELECTED: local/llama-3.1-70b-instruct
REASON: Only model meeting privacy + context + capability
CONTEXT CHECK: Schema ~15k tokens << 128k limit
COST: $0.00 (local inference)
LATENCY: ~45s (local GPU, batch size 1)
```

### Policy Enforcement
- **BLOCKED:** 3 cloud models rejected by privacy gate
- **AUDIT:** Routing decision logged with privacy rationale
- **FALLBACK:** None (policy prohibits cloud fallback for confidential data)
```

---

## Scenario 3: Cost-Optimized Batch Routing

**Trigger:** "Route 500 classification tasks — minimize cost."

**Invocation:**
```
Route batch of 500 tasks:
- Task type: Classification (spam/not-spam)
- Input: Short text (<200 chars each)
- Output: JSON {label, confidence}
- Budget: $0.10 total
- Latency: Not critical (async batch)
```

**Execution Log:**
```
## Routing Decision: Batch Classification (500 tasks)

### Task Analysis
- **Type:** Classification (binary, structured output)
- **Per-task tokens:** ~100 input + 20 output
- **Total tokens:** 50k input + 10k output
- **Complexity:** Low (simple classification)
- **Reliability needed:** High (production filter)

### Cost Comparison
| Model | Input/$1M | Output/$1M | Est. Cost (60k tokens) | Quality |
|-------|-----------|------------|------------------------|---------|
| gpt-4o-mini | $0.15 | $0.60 | **$0.014** | Excellent |
| gemini-1.5-flash | $0.075 | $0.30 | **$0.007** | Excellent |
| claude-3-haiku | $0.25 | $1.25 | $0.025 | Good |
| llama-3.1-8b (local) | $0.00 | $0.00 | **$0.00** | Good |
| deepseek-chat (OpenRouter) | $0.14 | $0.28 | $0.011 | Good |

### Routing Decision
```
SELECTED: google/gemini-1.5-flash (via OpenRouter)
REASON: Best cost/quality for classification, structured output support
ESTIMATED COST: $0.007 << $0.10 budget
FALLBACK: openai/gpt-4o-mini
STRUCTURED OUTPUT: JSON schema enforced
BATCH API: Used for 50% cost reduction
```

### Execution
```
$ route-batch classify-spam --model=gemini-1.5-flash --batch-api
✓ 500 tasks submitted to batch API
✓ Completed in 4.2 minutes
✓ Actual cost: $0.0068
✓ Accuracy: 99.2% (validated on 50 labeled samples)
✓ All outputs valid JSON per schema
```
```

---

## Scenario 4: Long-Context Repository Analysis

**Trigger:** "Analyze this entire 50k-line codebase for architectural patterns."

**Invocation:**
```
Route long-context analysis:
- Input: 50,000 lines TypeScript (~200k tokens)
- Task: Architecture analysis, pattern detection, risk identification
- Output: Structured report (Markdown + JSON)
- Budget: $1.00
```

**Execution Log:**
```
## Routing Decision: Full-Repo Analysis (200k tokens)

### Context Challenge
- 200k tokens exceeds most model limits
- Strategy: Targeted retrieval + long-context model

### Eligible Models (Context ≥ 200k)
| Provider | Model | Context | Cost (200k in + 10k out) |
|----------|-------|---------|---------------------------|
| Anthropic | claude-3.5-sonnet | 200k | $0.75 |
| Google | gemini-1.5-pro | 1M | $0.35 |
| OpenRouter | gemini-1.5-pro | 1M | $0.35 |
| OpenRouter | claude-3-opus | 200k | $2.50 |

### Routing Decision
```
SELECTED: google/gemini-1.5-pro (via OpenRouter)
REASON: 1M context handles full repo, best cost for long context
STRATEGY: 
  1. Send full repo (200k tokens) in single prompt
  2. Request structured JSON + Markdown output
  3. Use prompt caching for repeat analyses
ESTIMATED COST: $0.35 (well within $1.00 budget)
```

### Alternative: Retrieval-Augmented (if context too large)
```
If repo > 1M tokens:
  1. codebase-intelligence skill → extract key files (entry points, config, types)
  2. Send ~50k tokens to claude-3.5-sonnet
  3. Cost: ~$0.20
```

### Execution
```
$ route-task "Analyze architecture..." --model=gemini-1.5-pro --cache-prompt
✓ Full repo sent (198,432 tokens)
✓ Analysis completed in 67s
✓ Output: 2,847 tokens (JSON + Markdown)
✓ Actual cost: $0.34 (prompt cache hit on 2nd run: $0.08)
✓ Findings: 12 patterns, 7 risks, 3 recommendations
```
```

---

## OpenRouter Integration Config

```yaml
# model-router config with OpenRouter
model_router:
  providers:
    anthropic:
      api_base: "https://api.anthropic.com"
      models:
        - id: claude-3.5-sonnet
          context: 200000
          pricing: { input: 3.00, output: 15.00 }
        - id: claude-3-haiku
          context: 200000
          pricing: { input: 0.25, output: 1.25 }
    
    openai:
      api_base: "https://api.openai.com/v1"
      models:
        - id: gpt-4o
          context: 128000
          pricing: { input: 2.50, output: 10.00 }
        - id: gpt-4o-mini
          context: 128000
          pricing: { input: 0.15, output: 0.60 }
    
    openrouter:
      api_base: "https://openrouter.ai/api/v1"
      api_key_env: "OPENROUTER_API_KEY"
      models:
        # Free models
        - id: meta-llama/llama-3.1-8b-instruct:free
          context: 128000
          pricing: { input: 0.00, output: 0.00 }
          tags: [free]
        - id: mistralai/mistral-7b-instruct:free
          context: 32000
          pricing: { input: 0.00, output: 0.00 }
          tags: [free]
        - id: google/gemma-2-9b-it:free
          context: 8000
          pricing: { input: 0.00, output: 0.00 }
          tags: [free]
        
        # Cheap paid
        - id: deepseek/deepseek-chat
          context: 128000
          pricing: { input: 0.14, output: 0.28 }
        - id: deepseek/deepseek-coder
          context: 128000
          pricing: { input: 0.14, output: 0.28 }
        - id: google/gemini-1.5-flash
          context: 1000000
          pricing: { input: 0.075, output: 0.30 }
        - id: meta-llama/llama-3.1-70b-instruct
          context: 128000
          pricing: { input: 0.59, output: 0.79 }
        
        # Premium
        - id: anthropic/claude-3.5-sonnet
          context: 200000
          pricing: { input: 3.00, output: 15.00 }
        - id: openai/gpt-4o
          context: 128000
          pricing: { input: 2.50, output: 10.00 }
        - id: google/gemini-1.5-pro
          context: 1000000
          pricing: { input: 1.25, output: 5.00 }
    
    local:
      api_base: "http://localhost:11434/v1"  # Ollama
      api_key_env: ""  # Not needed
      models:
        - id: llama-3.1-70b-instruct
          context: 128000
          pricing: { input: 0.00, output: 0.00 }
          tags: [local, private]
        - id: deepseek-coder-33b
          context: 16000
          pricing: { input: 0.00, output: 0.00 }
          tags: [local, private, code]
        - id: codellama-34b
          context: 16000
          pricing: { input: 0.00, output: 0.00 }
          tags: [local, private, code]

  routing_policy:
    # Privacy gates
    data_classification:
      public: [anthropic, openai, openrouter, local]
      internal: [openrouter, local]
      confidential: [local]
      restricted: [local]  # Air-gapped only
    
    # Task-type preferences
    task_preferences:
      code_generation:
        primary: [deepseek-coder, claude-3.5-sonnet, gpt-4o]
        budget_fallback: [deepseek-chat, gemini-1.5-flash]
      reasoning:
        primary: [claude-3.5-sonnet, gpt-4o, gemini-1.5-pro]
        budget_fallback: [llama-3.1-70b, deepseek-chat]
      classification:
        primary: [gemini-1.5-flash, gpt-4o-mini]
        budget_fallback: [llama-3.1-8b-free, gemma-2-9b-free]
      long_context:
        primary: [gemini-1.5-pro, claude-3.5-sonnet]
        budget_fallback: [gemini-1.5-flash]
    
    # Hard constraints
    max_cost_per_task_usd: 5.00
    max_latency_seconds: 120
    require_tools: true
    require_structured_output: true
    retry_budget: 3
    circuit_breaker_threshold: 5
```

---

## Tips for Effective Use

1. **Classify data sensitivity first** — Drives provider eligibility
2. **Use OpenRouter for model diversity** — Single API, 100+ models
3. **Leverage free tiers** — Llama-3.1-8b, Gemma-2-9b, Mistral-7b for low-stakes
4. **Enable prompt caching** — 50-90% cost reduction on repeat analyses
5. **Batch API for classification** — 50% cost reduction
6. **Local models for confidential data** — Zero egress, full control