---
name: communication-improver
description: Improve communication clarity, effectiveness, and understanding between humans and systems. Analyzes messages, documentation, and interactions to reduce ambiguity and improve outcomes.
version: 1.0.0
tags: [human, communication, clarity, understanding, documentation, messaging]
dependencies: [documentation-synthesizer, human-feedback-collector]
---

# Communication Improver

## Objective
Improve communication clarity, effectiveness, and understanding between humans and systems. Analyzes messages, documentation, and interactions to reduce ambiguity and improve outcomes.

## Trigger
- "Improve documentation clarity for feature X"
- "Make error messages more understandable"
- "Clarify API documentation for developers"
- "Improve team communication about system Y"

Anti-triggers: "Write marketing copy" / "Create persuasive content without clarity focus" — those are different objectives.

## Inputs
- Communication content: documentation, error messages, UI text, emails, chat messages
- Audience: developers, users, stakeholders, operations team
- Context: technical, user-facing, operational, external
- Clarity goals: reduce ambiguity, improve comprehension, speed up understanding

## Outputs
- Communication report: identified issues, ambiguity, confusion points
- Improved content: rewritten messages with clarity improvements
- Clarity metrics: readability score, ambiguity count, comprehension time
- Recommendations: templates, style guidelines, templates
- Before/after comparison: original vs. improved communication

## Procedure
1. **Analyze communication** (documentation-synthesizer)
   - Read communication content: docs, messages, UI text, emails
   - Identify audience and context
   - Document current clarity issues: jargon, ambiguity, missing context

2. **Identify clarity issues**
   - Ambiguity: words or phrases with multiple meanings
   - Jargon: technical terms unfamiliar to audience
   - Missing context: assumptions about reader knowledge
   - Complexity: long sentences, nested concepts, unclear structure
   - Inconsistency: different terms for same concept

3. **Design improvements**
   - Rewrite for target audience: appropriate technical level
   - Simplify language: shorter sentences, common words
   - Add context: explain assumptions, define terms
   - Structure: headings, lists, examples, clear flow
   - Standardize: consistent terminology and formatting

4. **Apply improvements**
   - Rewrite communication content
   - Preserve meaning and accuracy
   - One document/message at a time

5. **Verify**
   - Check readability: Flesch-Kincaid or similar metric
   - Test comprehension: ask target audience to summarize
   - Compare before/after: clarity metrics improved
   - Confirm accuracy: no meaning lost in simplification

6. **Report**
   - Produce improvement report: issues found, improvements made, metrics, recommendations

## Safety & Approval Gates
- **Meaning preserved**: Simplification must not change technical accuracy
- **Audience-appropriate**: Different audiences need different detail levels
- **Approval required** before changing user-facing or external communication
- **No content removal without justification**: Only remove if truly unnecessary

## Failure Handling
- Content unreadable → Mark as "unparseable," recommend manual review
- Audience unknown → Mark as "audience undefined," recommend audience research
- Meaning ambiguous → Mark as "ambiguous," clarify with author before changing
- No improvement possible → Report "content already clear," no changes made

## Completion Criteria
- Communication report with issues and improvements
- Readability metrics improved
- Comprehension verified with target audience
- Accuracy preserved (no meaning lost)
- Recommendations for templates and style guidelines
