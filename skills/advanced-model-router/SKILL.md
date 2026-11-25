---
name: advanced-model-router
description: Intelligent model routing with OpenRouter integration, free/paid tier selection, privacy gates, cost optimization, and autonomous fallback chains. Use for all model selection decisions in multi-provider environments.
version: 2.0.0
tags: [infrastructure, routing, models, openrouter, cost-optimization, privacy]
---

# Advanced Model Router

## Objective
Select the optimal model for every task by continuously evaluating capability, cost, latency, privacy, and availability — with autonomous fallback, budget enforcement, and audit trails.

## Key Capabilities
- **OpenRouter Integration**: 100+ models via single API, unified pricing
- **Free Tier First**: Automatic preference for free models when quality permits
- **Privacy Gates**: Confidential data → local/private models only
- **Cost Optimization**: Per-task budgets, batch API, prompt caching
- **Autonomous Fallback**: Rate limit → next provider → circuit breaker
- **Capability Matching**: Reasoning, coding, context, tools, structured output
- **Audit Trail**: Every routing decision logged with rationale

## Architecture

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                         ADVANCED MODEL ROUTER                                │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  ┌─────────────┐    ┌─────────────┐    ┌─────────────┐    ┌─────────────┐  │
│  │  CLASSIFIER │    │  CONSTRAINT │    │   PROVIDER  │    │   POLICY    │  │
│  │             │    │  RESOLVER   │    │  REGISTRY   │    │   ENGINE    │  │
│  │ - Task type │    │             │    │             │    │             │  │
│  │ - Complexity│    │ - Privacy   │    │ - OpenRouter│    │ - Privacy   │  │
│  │ - Modality  │    │ - Budget    │    │ - Anthropic │    │ - Budget    │  │
│  │ - Tools?    │    │ - Latency   │    │ - OpenAI    │    │ - Capability│  │
│  │ - Struct.?  │    │ - Context   │    │ - Google    │    │ - Fallback  │  │
│  └──────┬──────┘    └──────┬──────┘    └──────┬──────┘    └──────┬──────┘  │
│         │                  │                  │                  │         │
│         └──────────────────┼──────────────────┼──────────────────┘         │
│                            ▼                  ▼                            │
│                 ┌─────────────────────────────────────┐                   │
│                 │         ROUTING DECISION ENGINE      │                   │
│                 │  1. Filter by privacy gate            │                   │
│                 │  2. Filter by capability requirements │                   │
│                 │  3. Filter by budget                  │                   │
│                 │  4. Rank: quality → reliability → cost│                   │
│                 │  5. Select primary + fallback chain   │                   │
│                 └──────────────────┬────────────────────┘                   │
│                                    │                                       │
│                                    ▼                                       │
│                 ┌─────────────────────────────────────┐                   │
│                 │         EXECUTION LAYER              │                   │
│                 │  - Primary model call                │                   │
│                 │  - Retry with exponential backoff    │                   │
│                 │  - Fallback on rate_limit/error      │                   │
│                 │  - Circuit breaker per provider      │                   │
│                 │  - Cost/latency tracking             │                   │
│                 └─────────────────────────────────────┘                   │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

## Procedure

### 1. Task Classification
Analyze the request to determine requirements:

```python
def classify_task(request: TaskRequest) -> TaskProfile:
    return TaskProfile(
        # Capability requirements
        needs_reasoning = detect_reasoning(request),
        needs_coding = detect_coding(request),
        needs_long_context = estimate_tokens(request) > 32000,
        needs_tools = request.tools is not None,
        needs_structured_output = request.response_schema is not None,
        needs_vision = has_images(request),
        
        # Constraints
        privacy_level = classify_data_sensitivity(request.data),
        max_cost_usd = request.budget or get_default_budget(request.type),
        max_latency_s = request.latency_target or get_default_latency(request.type),
        min_context = estimate_tokens(request) + 4000,  # output buffer
    )
```

**Task Types & Default Profiles:**
| Task Type | Reasoning | Coding | Context | Tools | Structured | Typical Budget |
|-----------|-----------|--------|---------|-------|------------|----------------|
| Code Generation | High | **Required** | Medium | Required | Preferred | $0.50 |
| Code Review | **Required** | High | Medium | Optional | Required | $1.00 |
| Reasoning/Analysis | **Required** | Low | High | Optional | Preferred | $1.00 |
| Classification | Low | None | Low | None | **Required** | $0.10 |
| Extraction | Medium | None | Medium | None | **Required** | $0.10 |
| Translation | Medium | None | Low | None | Preferred | $0.10 |
| Summarization | Medium | None | High | None | Preferred | $0.20 |
| Chat/Assistant | Medium | Low | Medium | Optional | Optional | $0.20 |

### 2. Privacy Gate (Hard Filter)
**Confidential data NEVER leaves approved environment.**

```python
def apply_privacy_gate(models: List[Model], privacy: PrivacyLevel) -> List[Model]:
    allowed_tags = {
        PrivacyLevel.PUBLIC:      ["cloud", "openrouter", "local"],
        PrivacyLevel.INTERNAL:    ["openrouter", "local"],
        PrivacyLevel.CONFIDENTIAL: ["local", "private"],
        PrivacyLevel.RESTRICTED:  ["local", "airgapped"],
    }
    return [m for m in models if any(tag in m.tags for tag in allowed_tags[privacy])]
```

**Data Classification Rules:**
- `PUBLIC`: Documentation, public APIs, general knowledge
- `INTERNAL`: Internal code, configs, non-sensitive logs
- `CONFIDENTIAL`: PII, credentials, financial data, customer data
- `RESTRICTED`: Production secrets, encryption keys, regulated data

### 3. Capability Filter
Match model capabilities to task requirements:

```python
def filter_by_capability(models: List[Model], profile: TaskProfile) -> List[Model]:
    return [m for m in models if
        (not profile.needs_reasoning or m.capabilities.reasoning >= 8) and
        (not profile.needs_coding or m.capabilities.coding >= 8) and
        (not profile.needs_long_context or m.context_window >= profile.min_context) and
        (not profile.needs_tools or m.supports_tools) and
        (not profile.needs_structured_output or m.supports_structured_output) and
        (not profile.needs_vision or m.supports_vision)
    ]
```

### 4. Budget Filter
```python
def filter_by_budget(models: List[Model], profile: TaskProfile) -> List[Model]:
    estimated_input = profile.estimated_input_tokens
    estimated_output = profile.estimated_output_tokens
    
    return [m for m in models if
        (m.pricing.input * estimated_input / 1_000_000) +
        (m.pricing.output * estimated_output / 1_000_000) <= profile.max_cost_usd
    ]
```

### 5. Ranking Algorithm
```python
def rank_models(models: List[Model], profile: TaskProfile) -> List[RankedModel]:
    scored = []
    for m in models:
        # Quality score (0-100)
        quality = (
            m.capabilities.reasoning * 0.3 +
            m.capabilities.coding * 0.25 +
            m.capabilities.instruction_following * 0.2 +
            m.capabilities.reliability * 0.15 +
            (10 if m.supports_structured_output else 0) * 0.1
        )
        
        # Cost score (lower = better, normalized)
        est_cost = estimate_cost(m, profile)
        cost_score = 100 * (1 - min(est_cost / profile.max_cost_usd, 1.0))
        
        # Latency score (lower = better)
        latency_score = 100 * (1 - min(m.avg_latency_ms / profile.max_latency_ms, 1.0))
        
        # Reliability (uptime, error rate)
        reliability = m.reliability_score
        
        # Composite (weights adjustable per task type)
        weights = get_weights(profile.task_type)
        composite = (
            quality * weights.quality +
            cost_score * weights.cost +
            latency_score * weights.latency +
            reliability * weights.reliability
        )
        
        scored.append(RankedModel(model=m, score=composite, est_cost=est_cost))
    
    return sorted(scored, key=lambda x: x.score, reverse=True)
```

### 6. Fallback Chain Construction
```python
def build_fallback_chain(ranked: List[RankedModel], profile: TaskProfile) -> FallbackChain:
    primary = ranked[0]
    fallbacks = ranked[1:4]  # Top 3 alternatives
    
    # Ensure fallbacks meet same privacy + capability constraints
    fallbacks = [f for f in fallbacks if
        f.model.privacy_tags == primary.model.privacy_tags and
        meets_capability(f.model, profile)
    ]
    
    return FallbackChain(
        primary=primary.model,
        fallbacks=[f.model for f in fallbacks],
        max_retries=3,
        retry_policy=RetryPolicy(
            base_delay=1.0,
            max_delay=30.0,
            exponential_base=2.0,
            jitter=0.1,
            retry_on=["rate_limit", "timeout", "5xx", "circuit_open"]
        ),
        circuit_breaker=CircuitBreaker(
            failure_threshold=5,
            recovery_timeout=60,
            half_open_requests=3
        )
    )
```

### 7. Execution with Telemetry
```python
async def execute_with_fallback(chain: FallbackChain, request: TaskRequest) -> ModelResponse:
    for attempt, model in enumerate([chain.primary] + chain.fallbacks):
        chain.circuit_breaker.check(model.id)
        
        try:
            start = time.time()
            response = await call_model(model, request)
            latency = time.time() - start
            
            # Record success
            chain.circuit_breaker.record_success(model.id)
            telemetry.record(
                model=model.id,
                latency=latency,
                cost=estimate_actual_cost(model, response),
                tokens_in=response.usage.prompt_tokens,
                tokens_out=response.usage.completion_tokens,
                fallback_attempt=attempt
            )
            
            return response
            
        except RateLimitError as e:
            telemetry.record(model=model.id, error="rate_limit", attempt=attempt)
            chain.circuit_breaker.record_failure(model.id)
            if attempt < len(chain.fallbacks):
                await sleep(chain.retry_policy.next_delay(attempt))
                continue
            raise
            
        except (TimeoutError, ServerError) as e:
            telemetry.record(model=model.id, error=type(e).__name__, attempt=attempt)
            chain.circuit_breaker.record_failure(model.id)
            if attempt < len(chain.fallbacks):
                await sleep(chain.retry_policy.next_delay(attempt))
                continue
            raise
    
    raise NoModelAvailableError("All models in fallback chain exhausted")
```

## Configuration

### Provider Registry (OpenRouter + Direct + Local)
```yaml
# advanced-model-router config
advanced_model_router:
  # OpenRouter (100+ models, single API)
  openrouter:
    enabled: true
    api_base: "https://openrouter.ai/api/v1"
    api_key_env: "OPENROUTER_API_KEY"
    # Free models (auto-discovered via :free suffix)
    free_models:
      - "meta-llama/llama-3.1-8b-instruct:free"
      - "mistralai/mistral-7b-instruct:free"
      - "google/gemma-2-9b-it:free"
      - "microsoft/phi-3-mini-128k-instruct:free"
    # Cheap paid
    budget_models:
      - "deepseek/deepseek-chat"
      - "deepseek/deepseek-coder"
      - "google/gemini-1.5-flash"
      - "meta-llama/llama-3.1-70b-instruct"
    # Premium
    premium_models:
      - "anthropic/claude-3.5-sonnet"
      - "openai/gpt-4o"
      - "google/gemini-1.5-pro"
    # Model metadata cache TTL
    metadata_cache_ttl_hours: 24
  
  # Direct provider APIs (for when OpenRouter not available)
  direct_providers:
    anthropic:
      enabled: true
      api_base: "https://api.anthropic.com"
      api_key_env: "ANTHROPIC_API_KEY"
    openai:
      enabled: true
      api_base: "https://api.openai.com/v1"
      api_key_env: "OPENAI_API_KEY"
    google:
      enabled: true
      api_base: "https://generativelanguage.googleapis.com/v1beta"
      api_key_env: "GOOGLE_API_KEY"
  
  # Local/Private models (Ollama, vLLM, TGI, etc.)
  local_providers:
    - name: "ollama"
      enabled: true
      api_base: "http://localhost:11434/v1"
      models:
        - id: "llama-3.1-70b-instruct"
          context: 128000
          tags: ["local", "private", "reasoning", "coding"]
        - id: "deepseek-coder-33b"
          context: 16000
          tags: ["local", "private", "coding"]
        - id: "codellama-34b"
          context: 16000
          tags: ["local", "private", "coding"]
        - id: "llama-3.1-8b-instruct"
          context: 128000
          tags: ["local", "private", "fast"]
    - name: "vllm"
      enabled: false
      api_base: "http://localhost:8000/v1"
  
  # Routing Policy
  routing_policy:
    # Privacy gates (HARD - cannot be overridden)
    privacy_gates:
      PUBLIC:      ["cloud", "openrouter", "local"]
      INTERNAL:    ["openrouter", "local"]
      CONFIDENTIAL: ["local", "private"]
      RESTRICTED:  ["local", "airgapped"]
    
    # Task-type preferences (soft - cost/quality tradeoff)
    task_preferences:
      code_generation:
        primary_tags: ["coding", "reasoning"]
        budget_fallback_tags: ["coding", "budget"]
        max_cost_usd: 2.00
      reasoning:
        primary_tags: ["reasoning"]
        budget_fallback_tags: ["reasoning", "budget"]
        max_cost_usd: 2.00
      classification:
        primary_tags: ["fast", "structured"]
        budget_fallback_tags: ["free", "structured"]
        max_cost_usd: 0.10
      long_context:
        primary_tags: ["long_context"]
        budget_fallback_tags: ["long_context", "budget"]
        max_cost_usd: 1.00
    
    # Global constraints
    global_max_cost_usd: 10.00
    global_max_latency_seconds: 120
    require_structured_output_for: ["classification", "extraction", "code_generation"]
    require_tools_for: ["code_generation", "debugging"]
  
  # Cost Optimization
  cost_optimization:
    # Prefer free models when quality threshold met
    free_tier_threshold: 0.85  # Quality score >= 85% of best
    # Batch API for classification/extraction
    batch_api_enabled: true
    batch_api_discount: 0.5
    # Prompt caching for repeated analyses
    prompt_caching_enabled: true
    prompt_cache_ttl_hours: 1
    # Model warm-up for local models
    local_warmup_enabled: true
  
  # Reliability
  reliability:
    max_retries: 3
    base_retry_delay: 1.0
    max_retry_delay: 30.0
    circuit_breaker_threshold: 5
    circuit_breaker_timeout: 60
    health_check_interval: 300
  
  # Telemetry
  telemetry:
    enabled: true
    log_level: "INFO"
    metrics_endpoint: "prometheus"  # or "datadog", "cloudwatch"
    audit_log_path: ".router/audit.log"
    retain_audit_days: 90
```

## Free Model Auto-Discovery

```python
async def discover_free_models() -> List[Model]:
    """Fetch current free models from OpenRouter."""
    async with httpx.AsyncClient() as client:
        resp = await client.get(
            "https://openrouter.ai/api/v1/models",
            headers={"Authorization": f"Bearer {os.getenv('OPENROUTER_API_KEY')}"}
        )
        models = resp.json()["data"]
        
        free_models = []
        for m in models:
            if m["id"].endswith(":free") or m.get("pricing", {}).get("prompt") == "0":
                free_models.append(Model(
                    id=m["id"],
                    name=m["name"],
                    context=m["context_length"],
                    pricing=Pricing(input=0, output=0),
                    tags=["free", "openrouter"],
                    capabilities=estimate_capabilities(m["id"])
                ))
        return free_models
```

## Usage Examples

### Example 1: Code Generation (Privacy: Internal)
```python
request = TaskRequest(
    type="code_generation",
    prompt="Write a GraphQL resolver with auth, pagination, N+1 prevention",
    context_files=["schema.graphql", "resolvers/user.ts"],
    privacy=PrivacyLevel.INTERNAL,
    budget_usd=0.50
)

# Router selects:
# 1. Primary: deepseek/deepseek-coder (OpenRouter, $0.14/$0.28, coding=9)
# 2. Fallback: meta-llama/llama-3.1-70b-instruct (OpenRouter, $0.59/$0.79)
# 3. Fallback: anthropic/claude-3.5-sonnet (OpenRouter, $3/$15)
# Cost estimate: ~$0.03
```

### Example 2: Security Analysis (Privacy: Confidential)
```python
request = TaskRequest(
    type="reasoning",
    prompt="Analyze this auth module for vulnerabilities",
    context_files=["auth/*.ts"],
    privacy=PrivacyLevel.CONFIDENTIAL,  # Hard gate!
    budget_usd=2.00
)

# Router selects (privacy gate blocks cloud):
# 1. Primary: local/llama-3.1-70b-instruct (Ollama, FREE, reasoning=8)
# 2. Fallback: local/deepseek-coder-33b (Ollama, FREE)
# Cost: $0.00
```

### Example 3: Batch Classification (Cost Optimized)
```python
request = TaskRequest(
    type="classification",
    items=500,  # Batch!
    prompt="Classify as spam/ham: {text}",
    privacy=PrivacyLevel.PUBLIC,
    budget_usd=0.10,
    use_batch_api=True
)

# Router selects:
# Primary: google/gemini-1.5-flash (OpenRouter, batch API, $0.075/$0.30)
# Cost estimate: $0.007 (50% batch discount)
```

### Example 4: Long Context Repo Analysis
```python
request = TaskRequest(
    type="reasoning",
    prompt="Analyze architecture of this 50k-line codebase",
    context_files=["**/*.ts"],  # ~200k tokens
    privacy=PrivacyLevel.INTERNAL,
    budget_usd=1.00
)

# Router selects:
# Primary: google/gemini-1.5-pro (OpenRouter, 1M context, $1.25/$5)
# Fallback: google/gemini-1.5-flash (OpenRouter, 1M context, cheaper)
# Cost estimate: ~$0.35 (with prompt caching on repeat: $0.08)
```

## Integration with Skills

```yaml
# In workflow-orchestrator or any skill config
model_routing:
  skill_defaults:
    codebase-intelligence:
      task_type: "long_context"
      privacy: "INTERNAL"
    autonomous-debugging:
      task_type: "reasoning"
      privacy: "INTERNAL"
    multi-agent-review:
      task_type: "reasoning"
      privacy: "CONFIDENTIAL"  # Security review = confidential
    autonomous-testing:
      task_type: "code_generation"
      privacy: "INTERNAL"
```

## Audit Log Format

```json
{
  "timestamp": "2026-11-24T10:30:00.123Z",
  "request_id": "req_abc123",
  "task_type": "code_generation",
  "privacy_level": "INTERNAL",
  "budget_usd": 0.50,
  "routing_decision": {
    "primary": {
      "model": "deepseek/deepseek-coder",
      "provider": "openrouter",
      "est_cost": 0.028,
      "est_latency_ms": 8500,
      "quality_score": 87
    },
    "fallback_chain": [
      {"model": "meta-llama/llama-3.1-70b-instruct", "provider": "openrouter"},
      {"model": "anthropic/claude-3.5-sonnet", "provider": "openrouter"}
    ],
    "rejected": [
      {"model": "anthropic/claude-3.5-sonnet", "reason": "over_budget"},
      {"model": "local/llama-3.1-70b", "reason": "privacy_gate"}
    ]
  },
  "execution": {
    "model_used": "deepseek/deepseek-coder",
    "attempt": 0,
    "latency_ms": 7234,
    "actual_cost": 0.026,
    "tokens_in": 4521,
    "tokens_out": 1834,
    "success": true
  }
}
```

## Completion Criteria
- Routing decision satisfies privacy, capability, budget, latency constraints
- Fallback chain has ≥2 alternatives meeting same constraints
- Execution succeeds or fails with clear error (no silent degradation)
- Audit log captures decision rationale, costs, latency, model used
- Free models preferred when quality ≥85% of best available
- Circuit breakers prevent cascade failures

---

*This skill requires OpenRouter API key for cloud models. Local models require Ollama/vLLM/TGI running. Degrades to direct provider APIs if OpenRouter unavailable.*