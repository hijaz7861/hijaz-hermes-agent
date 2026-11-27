---
name: container-orchestrator
description: Orchestrate containerized applications using Docker and Kubernetes. Creates container images, deployment manifests, service definitions, and orchestration rules for multi-environment deployment.
version: 1.0.0
tags: [container, docker, kubernetes, orchestration, deployment, microservices]
dependencies: [observability-instrumenter, security-audit]
---

# Container Orchestrator

## Objective
Orchestrate containerized applications using Docker and Kubernetes. Creates container images, deployment manifests, service definitions, and orchestration rules for reliable multi-environment deployment.

## Trigger
- "Containerize application X"
- "Create Kubernetes deployment for service Y"
- "Set up container orchestration for microservices"
- "Create container deployment pipeline"

Anti-triggers: "Run containers without security scanning" / "Deploy to production without resource limits" — those violate safety principles.

## Inputs
- Application: source code, dependencies, entry point
- Container base image: language runtime, version
- Resource requirements: CPU, memory, storage limits
- Network configuration: ports, services, ingress
- Environment variables: configuration, secrets (redacted)

## Outputs
- Dockerfile: optimized, multi-stage build
- Container image: built, tagged, security-scanned
- Kubernetes manifests: Deployment, Service, Ingress, ConfigMap, Secret
- Orchestration rules: resource limits, health checks, scaling policies
- Deployment verification: pod status, service endpoints, health checks

## Procedure
1. **Analyze application** (codebase-intelligence)
   - Identify entry point, dependencies, runtime requirements
   - Identify configuration needs and environment variables
   - Identify security requirements and compliance needs

2. **Create Dockerfile**
   - Multi-stage build: build stage + runtime stage
   - Non-root user for security
   - Minimal base image for reduced attack surface
   - Health check instruction

3. **Build and scan container image**
   - Build image with proper tagging
   - Security scan: vulnerabilities in base image and dependencies
   - Secret scan: no credentials in image layers
   - Size optimization: remove unnecessary files

4. **Create Kubernetes manifests**
   - Deployment: replicas, resource limits, health checks
   - Service: cluster-internal or load-balanced
   - Ingress: external access, TLS termination
   - ConfigMap: non-sensitive configuration
   - Secret: sensitive data (referenced, not inlined)

5. **Configure orchestration rules**
   - Resource limits: CPU and memory requests/limits
   - Health checks: liveness and readiness probes
   - Scaling: horizontal pod autoscaler rules
   - Update strategy: rolling update with max surge/unavailable

6. **Verify deployment**
   - Deploy to test cluster
   - Verify pod status and service endpoints
   - Confirm health checks pass
   - Verify observability is reporting

7. **Report**
   - Produce orchestration report: image details, manifests, resource usage, verification results

## Safety & Approval Gates
- **No root user in containers**
- **No secrets in image layers**: Use Kubernetes Secrets or external secret store
- **Resource limits required**: Prevent resource exhaustion
- **Security scan must pass** before production deployment

## Failure Handling
- Dockerfile syntax error → Report, fix, rebuild
- Image build failure → Report error, do not proceed
- Security scan failure → Report vulnerabilities, do not deploy
- Kubernetes manifest error → Report, fix, redeploy
- Health check failure → Report, mark deployment as unhealthy

## Completion Criteria
- Container image built and security-scanned
- Kubernetes manifests created and verified
- Resource limits and health checks configured
- Deployment verified on test cluster
- No secret values in image or manifests
