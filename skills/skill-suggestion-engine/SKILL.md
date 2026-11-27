---
name: skill-suggestion-engine
description: Suggests relevant skills based on user intent, context, task type, and historical usage. Analyzes user requests to match them with appropriate skills from the skills ecosystem, providing ranked recommendations with rationale.
version: 1.0.0
tags: [suggestion, recommendation, intent-matching, skill-discovery, context-aware]
dependencies: [skill-reader, skill-pattern-recognizer, skill-category-manager, discovery-engine]
---

# Skill Suggestion Engine

## Objective
Suggest relevant skills based on user intent, context, task type, and historical usage. Analyzes user requests to match them with appropriate skills from the skills ecosystem, providing ranked recommendations with rationale and confidence scores.

## Trigger
- "Suggest skills for task X"
- "Which skill should I use for Y?"
- "Recommend skills for this goal"
- "Find skills that can help with Z"

Anti-triggers: "Execute skill without suggestion" / "Force a specific skill without analysis" — those are skill-launcher tasks, not suggestion tasks.

## Inputs
- User request: natural language description of task or goal
- Context: repository type, programming language, existing files, previous skills used
- Task type: debugging, testing, documentation, refactoring, security, etc.
- User preferences: preferred skills, skill categories, past usage patterns
- Constraints: time budget, privacy requirements, approval availability

## Outputs
- Skill suggestions: ranked list of skills with confidence scores
- Rationale: explanation of why each skill is relevant
- Confidence scores: 0-100% confidence for each suggestion
- Alternative suggestions: backup skills if primary choices unavailable
- Skill combinations: suggestions for combining multiple skills
- Execution guidance: how to invoke each suggested skill

## Procedure
1. **Analyze user request**
   - Parse natural language request for intent, entities, and task type
   - Identify key concepts: programming languages, file types, operations, domains
   - Extract context: repository type, existing files, previous interactions
   - Classify request type: debugging, testing, documentation, refactoring, security, etc.

2. **Match skills to request**
   - Compare request against skill triggers and descriptions
   - Match keywords and concepts to skill capabilities
   - Score each skill based on relevance to request
   - Consider skill category and domain alignment

3. **Apply context filters**
   - Filter by repository type (matches skill's supported languages/tools)
   - Filter by available dependencies (skills whose dependencies are met)
   - Filter by user permissions (skills requiring approval the user has)
   - Filter by time budget (skills that can complete within budget)

4. **Rank suggestions**
   - Rank by confidence score (relevance to request)
   - Consider success rate from historical usage
   - Consider skill effectiveness score from comprehension analysis
   - Consider recency of skill usage
   - Produce ranked list with top suggestions first

5. **Identify skill combinations**
   - Find skills that complement each other for complex tasks
   - Suggest skill sequences (e.g., codebase-intelligence → autonomous-debugging → autonomous-testing)
   - Document combination rationale
   - Identify parallel execution opportunities

6. **Generate execution guidance**
   - For each suggested skill: provide invocation command, required inputs, expected outputs
   - Provide safety gate information (approval needed, privacy considerations)
   - Provide estimated execution time and resource requirements
   - Provide examples of similar successful executions

7. **Report**
   - Produce suggestion report: ranked skills with rationale, confidence scores, combinations, execution guidance

## Safety & Approval Gates
- **Read-only suggestion**: Does not execute skills, only recommends
- **No secret logging**: User requests and context are not logged with sensitive data
- **Transparency**: All ranking factors and confidence scores are explainable
- **No bias toward specific skills**: Suggestions based on relevance, not preference

## Failure Handling
- No skills match → Report "no matching skills found," suggest broader search terms
- Request too vague → Report "request too vague," ask for more specifics
- No context available → Report "limited context," suggestions based on request only
- All skills require approval → Report "all suggestions require approval," list approval requirements

## Completion Criteria
- Ranked skill suggestions with confidence scores
- Rationale provided for each suggestion
- Skill combinations identified for complex tasks
- Execution guidance provided for each suggestion
- No secrets in output
