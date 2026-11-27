---
name: skill-pattern-recognizer
description: Identifies patterns across multiple skills including common structures, procedures, safety patterns, and combination opportunities. Discovers reusable patterns and anti-patterns to inform skill creation and improvement.
version: 1.0.0
tags: [pattern-recognition, skill-patterns, common-structures, anti-patterns, combination-opportunities, analysis]
dependencies: [skill-reader, skill-comprehension-analyzer, discovery-engine]
---

# Skill Pattern Recognizer

## Objective
Identify patterns across multiple skills including common structures, procedures, safety patterns, and combination opportunities. Discovers reusable patterns and anti-patterns to inform skill creation, improvement, and combination decisions.

## Trigger
- "Find patterns across skills in category X"
- "Identify common procedures in skills Y and Z"
- "Discover combination opportunities between skills"
- "Find anti-patterns in skill ecosystem"

Anti-triggers: "Force skills into patterns without evidence" / "Create patterns from single skill" — those require multiple skills for pattern detection.

## Inputs
- Skills inventory: multiple SKILL.md files to analyze
- Pattern types: structure, procedure, safety, combination, anti-pattern
- Similarity threshold: minimum similarity to consider a pattern
- Scope: all skills, specific category, or specific skill set

## Outputs
- Pattern report: identified patterns with frequency and examples
- Common structures: recurring section layouts and section ordering
- Common procedures: repeated step types and decision patterns
- Safety patterns: common gate types, approval requirements, failure modes
- Combination opportunities: skills that combine well together
- Anti-patterns: recurring issues, unclear language, missing sections
- Pattern frequency: how often each pattern appears
- Pattern examples: specific skill instances for each pattern

## Procedure
1. **Read all target skills** (skill-reader)
   - Parse frontmatter, sections, procedures, safety gates for each skill
   - Extract structured representation of each skill
   - Normalize content for comparison

2. **Identify structural patterns**
   - Section ordering patterns (which sections appear in what order)
   - Section presence patterns (which sections are always/rarely present)
   - Frontmatter field patterns (which tags are commonly used together)
   - Section heading patterns (common heading text and formatting)

3. **Identify procedure patterns**
   - Step type patterns (read, write, run, verify, approve, report)
   - Decision point patterns (conditional branches, gates, escalations)
   - Tool reference patterns (commonly referenced commands and tools)
   - Error handling patterns (retry, rollback, escalate, skip)

4. **Identify safety patterns**
   - Gate type patterns (approval, quality, security, budget)
   - Approval requirement patterns (which changes need approval)
   - Failure mode patterns (common failure types and handling)
   - Rollback patterns (when and how rollback is performed)

5. **Identify combination opportunities**
   - Skills with complementary procedures (one reads, one writes)
   - Skills with related domains (same category, related tags)
   - Skills that share dependencies (common dependency chains)
   - Skills that could be combined into composite skills

6. **Identify anti-patterns**
   - Vague language patterns ("handle appropriately," "do everything")
   - Missing section patterns (skills without safety gates or completion criteria)
   - Unclear trigger patterns (triggers too broad or too narrow)
   - Dependency pattern issues (missing or circular dependencies)

7. **Calculate pattern frequency**
   - Count occurrences of each pattern across skills
   - Calculate pattern strength (frequency / total skills)
   - Rank patterns by frequency and impact

8. **Report**
   - Produce pattern report with patterns, frequency, examples, and anti-patterns

## Safety & Approval Gates
- **Read-only analysis**: Does not modify any skill files
- **Evidence-based**: Patterns based on actual skill content, not assumptions
- **No secret logging**: Redacts secrets found in skill content
- **No forced patterns**: Does not force skills into patterns without evidence

## Failure Handling
- No skills to analyze → Report "no skills found," provide inventory path
- All skills too different → Report "no common patterns found," suggest narrower scope
- Unreadable skills → Skip, mark as unanalyzable, continue with others
- Insufficient similarity → Report "no significant patterns," suggest different threshold

## Completion Criteria
- Pattern report with identified patterns and frequency
- Common structures, procedures, safety patterns documented
- Combination opportunities identified
- Anti-patterns documented with examples
- Pattern frequency calculated and ranked
