---
name: config-adjuster
description: Adjust environment configuration parameters based on usage patterns, error rates, and operational feedback. Fine-tunes timeouts, retries, limits, and feature flags for optimal operation.
version: 1.0.0
tags: [adjustment, configuration, tuning, parameters, feature-flags, limits]
dependencies: [environment-config-manager, configuration-validator, observability-instrumenter]
---

# Config Adjuster

## Objective
Adjust environment configuration parameters based on usage patterns, error rates, and operational feedback. Fine-tunes timeouts, retries, limits, and feature flags for optimal operation without service disruption.

## Trigger
- "Adjust timeout for service X"
- "Tune retry policy for API Y"
- "Adjust rate limiting thresholds"
- "Optimize feature flag configuration"

Anti-triggers: "Change configuration without measurement" / "Adjust production config without approval" — those violate safety principles.

## Inputs
- Configuration parameter: timeout, retry count, rate limit, feature flag, limit
- Current value and acceptable range
- Usage patterns: call frequency, error rates, latency distribution
- Operational feedback: incidents, alerts, on-call feedback
- Adjustment limits: min/max values, step size

## Outputs
- Adjustment plan: parameter, current → target value, rationale
- Adjustment log: changes made, timestamps, impact metrics
- Verification: service stability maintained, error rates improved
- Rollback plan: previous values documented

## Procedure
1. **Collect operational data** (observability-instrumenter)
   - Query error rates, latency distributions, retry rates, timeout occurrences
   - Identify patterns: timeouts under load, excessive retries, rate limit hits
   - Correlate configuration values with operational issues

2. **Analyze configuration impact**
   - Determine if current values cause issues (too low → failures, too high → resource waste)
   - Identify parameters that need adjustment
   - Assess risk: changing timeouts affects user experience, changing retries affects load

3. **Design adjustments**
   - Calculate target values based on observed patterns
   - Set adjustment step size for gradual changes
   - Document rollback values

4. **Apply adjustments** (requires approval for production)
   - Apply one parameter change at a time
   - Monitor service stability during and after
   - Use feature flags for gradual rollout if applicable

5. **Verify**
   - Confirm service stability (error rates, latency)
   - Verify improvement in targeted metric
   - Confirm no new issues introduced
   - Roll back if stability degrades

6. **Report**
   - Produce adjustment report: parameters, before/after values, impact, verification

## Safety & Approval Gates
- **Approval required** for production configuration changes
- **One parameter at a time**: no batching unrelated changes
- **Rollback values documented**: can revert to previous configuration
- **Feature flags used** for gradual rollout when possible
- **No drastic changes without testing**

## Failure Handling
- Metrics unavailable → Mark as "insufficient data," recommend monitoring
- Adjustment causes instability → Revert immediately, report
- Cannot determine target → Mark as "manual review," do not guess
- Configuration load failure → Revert, report, do not proceed

## Completion Criteria
- Adjustment plan with current → target values
- Each adjustment verified with service stability maintained
- Target metrics improved
- No new issues introduced
- Rollback values documented
