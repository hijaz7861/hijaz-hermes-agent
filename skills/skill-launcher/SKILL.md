---
name: skill-launcher
description: Launches skills with proper context, parameters, and execution tracking. Manages skill invocation, input validation, output collection, and result reporting for the skills ecosystem.
version: 1.0.0
tags: [launcher, execution, invocation, skill-orchestration, context-management]
dependencies: [skill-reader, skill-benchmarker, workflow-orchestrator]
---

# Skill Launcher

## Objective
Launch skills with proper context, parameters, and execution tracking. Manages skill invocation, input validation, output collection, and result reporting for the skills ecosystem. Ensures skills are executed correctly with proper governance and audit trails.

## Trigger
- "Launch skill X with parameters"
- "Execute skill Y on repository Z"
- "Run skill A with input B"
- "Start skill execution with context"

Anti-triggers: "Create new skill" / "Modify skill content" — those are skill creation tasks, not skill launching.

## Inputs
- Skill name: name of the skill to launch
- Skill inputs: parameters and context for the skill execution
- Execution context: repository path, branch, user permissions, time budget
- Output requirements: output format, detail level, destination
- Safety constraints: approval requirements, resource limits, privacy gates

## Outputs
- Execution result: skill output, exit code, execution time
- Evidence log: tool calls made, outputs captured, decisions made
- Performance metrics: execution time, resource usage, cost estimate
- Validation results: input validation, output validation, quality checks
- Audit trail: complete execution record for compliance

## Procedure
1. **Validate skill exists**
   - Look up skill in skills-index.json
   - Verify SKILL.md file exists and is readable
   - Check skill version and compatibility
   - Record skill metadata for audit trail

2. **Validate inputs**
   - Check required inputs against skill's input specification
   - Validate input types and formats
   - Check for missing or invalid inputs
   - Apply defaults for optional inputs

3. **Establish execution context**
   - Set repository path and branch
   - Record user permissions and approval status
   - Set time budget and resource limits
   - Configure output destination and format

4. **Check safety gates**
   - Verify approval status for protected operations
   - Check privacy gates for confidential data
   - Validate resource limits won't be exceeded
   - Confirm no destructive operations without authorization

5. **Execute skill**
   - Invoke skill procedure with validated inputs
   - Monitor execution for errors and timeouts
   - Collect tool calls and outputs as evidence
   - Track execution time and resource usage

6. **Collect and validate output**
   - Collect skill output in structured format
   - Validate output against expected format
   - Check for secrets or sensitive data in output
   - Record output quality and completeness

7. **Record audit trail**
   - Log skill name, inputs, outputs, execution time
   - Record evidence of all tool calls and decisions
   - Store audit record for compliance
   - Update skill execution history

8. **Report**
   - Produce execution report: result, metrics, evidence, audit trail
   - Report success/failure with details
   - Provide recommendations for next steps

## Safety & Approval Gates
- **Approval required** for skills that modify code, deploy, or access production
- **Privacy gates**: Confidential data must be routed to approved models/environments
- **Resource limits**: Execution time and resource usage must be within declared limits
- **No destructive operations** without explicit user authorization
- **Audit trail required**: All executions must be logged

## Failure Handling
- Skill not found → Report error, suggest similar skills, do not proceed
- Input validation fails → Report specific validation errors, request corrected inputs
- Safety gate violation → Block execution, report gate that blocked, suggest alternatives
- Execution error → Capture error details, rollback if changes made, report with stack trace
- Output validation fails → Report validation errors, mark output as unverified
- Timeout → Terminate execution, report partial results if available, suggest increasing time budget

## Completion Criteria
- Skill executed successfully or failure clearly reported
- All inputs validated before execution
- All outputs collected and validated
- Audit trail complete with evidence
- Performance metrics recorded
- No secrets in output
