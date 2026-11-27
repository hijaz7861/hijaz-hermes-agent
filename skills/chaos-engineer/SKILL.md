---
name: chaos-engineer
description: Run chaos engineering experiments by combining performance profiling with incident response. Injects failures (latency, errors, service outages) to verify system resilience, monitoring, and incident response procedures.
version: 1.0.0
tags: [chaos, resilience, testing, failure-injection, reliability]
dependencies: [performance-profiler, incident-responder]
---

# Chaos Engineer

## Objective
Combine performance profiling with incident response to run chaos engineering experiments. Injects controlled failures (latency, errors, timeouts, service outages) to verify system resilience, monitoring effectiveness, and incident response procedures.

## Trigger
- "Run chaos experiment on service X"
- "Test resilience of component Y under failure"
- "Verify monitoring detects injected failures"
- "Chaos test: latency, errors, outages"

Anti-triggers: "Break production without a plan" / "Run chaos without rollback" — those are unsafe, not controlled chaos engineering.

## Inputs
- Target: service, endpoint, or dependency to inject failure into
- Failure type: latency, error rate, timeout, service outage, network partition
- Blast radius: percentage of requests or instances affected
- Safety thresholds: max error rate, max latency, auto-abort conditions
- Rollback plan: how to stop the experiment and recover

## Outputs
- Experiment hypothesis: what failure is injected, what behavior is expected
- Experiment results: system behavior during failure, error rates, latency changes
- Resilience assessment: system degraded gracefully vs. cascaded failure
- Monitoring verification: did alerts fire, did dashboards show the issue
- Incident response verification: was the failure detected and responded to
- Recommendations: improve error handling, add retries, circuit breakers, monitoring

## Procedure
1. **Design the experiment** (performance-profiler + incident-responder)
   - Define hypothesis: "If dependency X fails, service Y should return cached data."
   - Select failure type: latency injection, error injection, timeout, service kill.
   - Define blast radius: % of traffic, % of instances.
   - Set safety thresholds: auto-abort if error rate > X% or latency > Yms.
   - Define rollback plan: how to stop injection and recover.

2. **Establish baseline** (performance-profiler)
   - Measure normal operation: error rate, latency, throughput.
   - Record monitoring state: active alerts, dashboard views.
   - Confirm system is healthy before injecting failure.

3. **Inject failure** (incident-responder)
   - Apply failure injection: add latency, return errors, kill instances.
   - Start with small blast radius, increase gradually.
   - Monitor system behavior in real time.
   - Auto-abort if safety thresholds exceeded.

4. **Observe system behavior**
   - Track: error rates, latency, throughput, queue depths, circuit breaker states.
   - Check: does system degrade gracefully or cascade?
   - Check: do fallbacks, retries, circuit breakers activate correctly?
   - Check: are dependent services affected?

5. **Verify monitoring and response**
   - Check: did alerts fire for the injected failure?
   - Check: did dashboards show the anomaly?
   - Check: would incident response procedures have detected this?
   - Record detection time vs. injection time.

6. **Recover and analyze**
   - Stop failure injection, confirm recovery.
   - Compare before/during/after metrics.
   - Identify: single points of failure, missing fallbacks, monitoring gaps.
   - Document lessons learned.

7. **Report**
   - Produce chaos experiment report: hypothesis, results, resilience assessment, monitoring verification, recommendations.

## Safety & Approval Gates
- **Approval required** before any failure injection.
- **Safety thresholds mandatory:** auto-abort conditions must be defined.
- **Blast radius limits:** start small, never affect 100% of production traffic without explicit approval.
- **Rollback plan required:** must be able to stop injection and recover.
- **No production without approval:** run on staging first.

## Failure Handling
- System cascades → abort immediately, report cascade, recommend circuit breakers.
- Monitoring doesn't detect → report monitoring gap, recommend alerting.
- Safety threshold exceeded → auto-abort, report, do not continue.
- Approval denied → stop, report, no injection.

## Completion Criteria
- Chaos experiment report with hypothesis, results, and resilience assessment.
- Monitoring verification: alerts confirmed or gaps identified.
- Safety thresholds respected, auto-abort if needed.
- System recovered after experiment.
- Recommendations for resilience improvements.
- No secret values in output.
