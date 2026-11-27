---
name: test-environment-orchestrator
description: Orchestrate ephemeral test environments for CI/CD and pull request validation. Creates isolated, disposable environments with test data, runs tests, and tears down after completion.
version: 1.0.0
tags: [test, environment, ephemeral, ci-cd, pull-request, isolation]
dependencies: [environment-provisioner, autonomous-testing, database-environment-setter]
---

# Test Environment Orchestrator

## Objective
Orchestrate ephemeral test environments for CI/CD and pull request validation. Creates isolated, disposable environments with test data, runs tests, and tears down after completion to prevent resource waste and ensure test isolation.

## Trigger
- "Create test environment for PR #X"
- "Orchestrate test environment for CI pipeline"
- "Set up ephemeral environment for integration tests"
- "Tear down test environment after tests complete"

Anti-triggers: "Leave test environments running indefinitely" / "Use production data in test environments" — those violate isolation and safety principles.

## Inputs
- Test scope: pull request, branch, commit, or tag
- Test types: unit, integration, end-to-end, performance
- Test data: fixtures, anonymized production data, synthetic data
- Environment requirements: services, databases, external dependencies
- Resource limits: compute, memory, storage, time

## Outputs
- Ephemeral environment: created, configured, accessible
- Test data: loaded, consistent, isolated
- Test results: pass/fail matrix, coverage, performance metrics
- Teardown confirmation: environment destroyed, resources released
- Test report: results, failures, recommendations

## Procedure
1. **Plan test environment** (environment-provisioner)
   - Determine required services and dependencies
   - Calculate resource requirements based on test scope
   - Set environment lifetime (ephemeral: tear-down after tests)

2. **Provision ephemeral environment**
   - Create isolated environment with unique identifier
   - Configure network isolation from other environments
   - Set resource limits to prevent runaway consumption
   - Configure automatic tear-down schedule

3. **Load test data** (database-environment-setter)
   - Load test fixtures or synthetic data
   - Anonymize any production-derived data
   - Ensure data consistency across services
   - Seed required state for test scenarios

4. **Run tests** (autonomous-testing)
   - Execute unit tests (fast, isolated)
   - Execute integration tests (service interactions)
   - Execute end-to-end tests (full user journeys)
   - Execute performance tests (if in scope)

5. **Collect results**
   - Capture pass/fail matrix for each test
   - Record coverage metrics
   - Record performance metrics (latency, throughput)
   - Capture logs and traces for failures

6. **Tear down environment**
   - Destroy all resources (compute, storage, network)
   - Release IP addresses and DNS records
   - Delete test data
   - Confirm teardown completion

7. **Report**
   - Produce test report: results, failures, coverage, performance, teardown confirmation

## Safety & Approval Gates
- **No production data in test environments** (must be anonymized)
- **Automatic tear-down required** (no lingering resources)
- **Resource limits required** (prevent runaway consumption)
- **Test environments isolated** from production and each other

## Failure Handling
- Provisioning failure → Report, do not run tests
- Test failure → Report failing tests, continue with remaining tests, tear down
- Data loading failure → Report, use synthetic fallback data
- Teardown failure → Alert, attempt manual cleanup, report resource leak

## Completion Criteria
- Test environment created and destroyed
- Tests executed with results captured
- Environment tear-down confirmed
- No resources left running
- No production data in test environment
