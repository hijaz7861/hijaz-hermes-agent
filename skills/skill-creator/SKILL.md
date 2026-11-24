---
name: skill-creator
description: Create, improve, test and document reusable agent skills. Use when a recurring workflow should become a maintainable SKILL.md or when an existing skill is unclear, unsafe or incomplete.
---

# Skill Creator

## Objective
Turn a repeatable task into a concise, discoverable and testable procedure that an agent can follow reliably.

## Design process
1. **Identify the trigger**
   - Describe the user intent and situations that should activate the skill.
   - Keep the description specific; avoid broad triggers that cause irrelevant activation.
2. **Define the outcome**
   - State the task objective, required inputs, expected outputs and boundaries.
   - Separate mandatory requirements from optional techniques.
3. **Inspect the runtime**
   - Confirm the agent's actual skill discovery path, supported frontmatter and tool capabilities.
   - Do not invent commands, connectors, environment variables or APIs.
4. **Write the skill**
   - Use a short imperative workflow with numbered steps.
   - Include decision points, failure handling, safety/approval gates and completion criteria.
   - Prefer concrete examples and exact commands only when verified for the target environment.
   - Keep reusable knowledge in the skill; keep task-specific values out of it.
5. **Validate**
   - Check YAML frontmatter and required fields.
   - Check that every referenced path, command and tool is either verified or clearly marked as an example.
   - Walk through at least one normal case, one failure case and one safety-sensitive case.
   - Remove contradictions, duplicated instructions and vague phrases such as "do everything".
6. **Maintain**
   - Add an owner or maintenance note when appropriate.
   - Record version/change notes if the skill is used across teams.
   - Revalidate when the runtime, APIs or policies change.

## Required structure
- YAML frontmatter: `name`, `description`
- Objective
- Trigger/use cases
- Procedure
- Safety and approval gates
- Failure handling
- Completion criteria

## Quality rubric
A skill is ready only if it is discoverable, actionable, bounded, safe, testable and portable. Do not claim a skill was tested in a live agent unless an actual runtime test was performed.

## Safety
A skill is guidance, not authorization. It cannot grant permissions, bypass approvals, reveal secrets or override higher-priority system and user instructions.
