---
name: model-router
description: Choose and route tasks to available AI models/providers based on capability, reliability, latency, context window, privacy and cost. Use in multi-provider agent systems or when a preferred model is unavailable or rate-limited.
---

# Model Router

## Objective
Select the least costly available model that meets the task's quality, safety and privacy requirements.

## Routing procedure
1. Classify the task: code generation, code review, reasoning, extraction, translation, vision, tool use or summarization.
2. Determine constraints: data sensitivity, required context length, latency target, output format, tool support, budget and provider availability.
3. Consult live provider/model metadata when available. Verify exact model IDs, supported modalities, context limits, pricing and rate limits; do not rely on stale model names.
4. Apply policy gates:
   - Do not send secrets, personal data or confidential source code to an unapproved provider.
   - Use approved local/self-hosted models for data that must not leave the environment.
   - Require structured output validation before downstream execution.
5. Rank eligible models using task fit first, then reliability, latency and cost.
6. Use bounded retries with exponential backoff and jitter for transient failures. Respect provider retry-after signals and rate limits.
7. Fail over only to a model that satisfies the same privacy and capability constraints.
8. Record provider, exact model ID, latency, token/cost estimate and fallback reason when telemetry is permitted.
9. Return a clear failure when no eligible model is available; do not silently exceed budget.

## Routing policy
- High-risk code/security decisions: strong reasoning model plus independent review.
- Routine extraction/classification: efficient model with schema validation.
- Long-context repository analysis: model with sufficient context, using targeted retrieval rather than blindly sending the entire repository.
- Tool execution: require explicit tool authorization and validate arguments independently of model output.

## Reliability
- Set per-task timeouts and retry budgets.
- Prevent retry storms and circular provider fallback.
- Use circuit breakers for repeated provider failures.
- Never treat a model response as executable authorization.

## Completion criteria
The selected route satisfies declared privacy, capability and budget constraints; fallback behavior is bounded; and routing decisions are auditable without logging sensitive prompts or credentials.
