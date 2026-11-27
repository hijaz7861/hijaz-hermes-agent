---
name: ci-cd-pipeline-builder
description: Build CI/CD pipelines for building, testing, and deploying code across environments. Creates pipeline definitions with quality gates, security scans, and environment promotion rules.
version: 1.0.0
tags: [ci-cd, pipeline, build, test, deploy, automation]
dependencies: [code-refactorer, autonomous-testing, security-audit]
---

# CI/CD Pipeline Builder

## Objective
Build CI/CD pipelines that automate building, testing, and deploying code across environments. Every pipeline includes quality gates, security scans, and environment promotion rules to ensure only verified code reaches production.

## Trigger
- "Create CI/CD pipeline for repository X"
- "Build deployment pipeline for service Y"
- "Add quality gates to existing pipeline"
- "Create multi-environment deployment pipeline"

Anti-triggers: "Deploy directly to production without pipeline" / "Skip tests in pipeline" — those violate the quality gate principle.

## Inputs
- Repository: source code location and branch strategy
- Build system: language, build tool, test framework
- Environments: development, staging, production (with promotion rules)
- Quality gates: test coverage, lint, typecheck, security scan thresholds
- Security requirements: dependency scan, secret scan, compliance check

## Outputs
- Pipeline definition file (.github/workflows, .gitlab-ci.yml, Jenkinsfile, etc.)
- Pipeline stages: build, test, security-scan, quality-gate, deploy
- Environment promotion rules: staging → production with approval
- Pipeline configuration: secrets, environment variables, caching

## Procedure
1. **Analyze repository** (code-refactorer)
   - Identify build system and dependencies
   - Identify test frameworks and configuration
   - Identify security requirements and compliance needs

2. **Design pipeline stages**
   - Build: compile, package, create artifacts
   - Test: unit, integration, end-to-end tests
   - Security scan: dependency vulnerabilities, secrets, SAST
   - Quality gate: coverage threshold, lint, typecheck
   - Deploy: staging → production with approval gates

3. **Configure environment promotion**
   - Development: auto-deploy on merge to feature branches
   - Staging: auto-deploy on merge to main/develop
   - Production: manual approval required, quality gate must pass

4. **Create pipeline definition**
   - Write pipeline file in appropriate format
   - Configure secrets and environment variables
   - Set up caching for dependencies and build artifacts
   - Configure notifications and alerts

5. **Verify pipeline**
   - Run pipeline on test repository
   - Confirm all stages pass/fail correctly
   - Verify quality gates block deployment on failure
   - Confirm production deployment requires approval

6. **Report**
   - Produce pipeline report: stages, gates, environments, configuration

## Safety & Approval Gates
- **Production deployment requires manual approval**
- **Quality gates cannot be bypassed** without explicit authorization
- **No secrets in pipeline files**: Use environment variables or secret stores
- **Pipeline changes require review** before merging

## Failure Handling
- Build failure → Pipeline stops, report error, do not deploy
- Test failure → Pipeline stops, report failing tests, do not deploy
- Security scan failure → Pipeline stops, report vulnerabilities, do not deploy
- Quality gate failure → Pipeline stops, report gate status, do not deploy

## Completion Criteria
- Pipeline definition created and verified
- All stages configured with appropriate gates
- Environment promotion rules defined
- Pipeline tested on sample repository
- No secret values in pipeline files
