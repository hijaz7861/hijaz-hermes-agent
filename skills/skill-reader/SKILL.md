---
name: skill-reader
description: Reads and parses existing skill files (SKILL.md) to extract structure, frontmatter, sections, procedures, safety gates, and dependencies. Provides structured understanding of any skill for further analysis or creation.
version: 1.0.0
tags: [skill-reading, parsing, extraction, structure, frontmatter, understanding]
dependencies: [codebase-intelligence]
---

# Skill Reader

## Objective
Read and parse existing skill files (SKILL.md) to extract structure, YAML frontmatter, sections, procedures, safety gates, dependencies, and playbooks. Provides a structured, machine-readable understanding of any skill for further analysis, combination, or creation.

## Trigger
- "Read skill X's structure"
- "Parse SKILL.md for skill Y"
- "Extract frontmatter from skill Z"
- "Read and understand skill procedures"

Anti-triggers: "Modify skill content" / "Create new skill from scratch" — those are separate tasks (skill-generator, skill-improvement-planner), not pure reading.

## Inputs
- Skill path: path to SKILL.md file or skill directory
- Read scope: frontmatter only, full content, sections only, or dependencies only
- Parse depth: surface-level or detailed (procedure steps, safety gates, failure modes)

## Outputs
- Frontmatter: name, description, version, tags, dependencies, capabilities
- Structure: all sections with headings and content
- Procedure: numbered steps with decision points and sub-steps
- Safety gates: approval requirements, read-only constraints, rollback procedures
- Dependencies: direct dependencies and reverse dependents
- Playbook references: linked playbook files and scenarios
- Structured output: JSON or YAML representation of skill structure

## Procedure
1. **Locate skill file**
   - Resolve skill path to SKILL.md file
   - Verify file exists and is readable
   - Identify skill directory and related files (playbook, tests)

2. **Parse YAML frontmatter**
   - Extract name, description, version, tags
   - Extract dependencies, capabilities, min_hermes_version, protocol_version
   - Record frontmatter validity and completeness

3. **Parse sections**
   - Identify all section headings (Objective, Trigger, Procedure, Safety, Failure Handling, Completion Criteria)
   - Extract section content with line references
   - Preserve section order and hierarchy

4. **Parse procedure steps**
   - Extract numbered steps with sub-steps
   - Identify decision points and conditional logic
   - Record tool references and commands
   - Note approval gates within procedure

5. **Parse safety and failure sections**
   - Extract safety rules and approval gates
   - Extract failure modes and handling procedures
   - Extract rollback and escalation procedures

6. **Parse dependencies**
   - Extract direct dependencies from frontmatter
   - Read playbook for additional dependency references
   - Record skill relationships

7. **Produce structured output**
   - Generate JSON/YAML representation of skill structure
   - Include all extracted fields with source references
   - Flag missing or incomplete sections

8. **Report**
   - Produce reading report: structure summary, completeness, issues found

## Safety & Approval Gates
- **Read-only operation**: Does not modify any skill files
- **No secret logging**: Redacts secrets if found in skill files
- **Respects file permissions**: Does not read files without access
- **No automated changes**: Reading only, no modifications

## Failure Handling
- File not found → Report "skill file not found," verify path
- Invalid YAML → Report "frontmatter parse error," suggest manual review
- Missing sections → Report "incomplete skill structure," list missing sections
- Unreadable file → Report "file access denied," check permissions

## Completion Criteria
- Frontmatter extracted and validated
- All sections identified and extracted
- Procedure steps parsed with decision points
- Safety gates and dependencies identified
- Structured output produced in JSON/YAML
- No secrets in output
