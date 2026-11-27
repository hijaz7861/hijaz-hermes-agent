---
name: human-feedback-collector
description: Collect, organize, and analyze human feedback from users, stakeholders, and team members. Identifies patterns, sentiment, and actionable insights to inform skill and system improvements.
version: 1.0.0
tags: [human, feedback, collection, sentiment, insights, understanding]
dependencies: [documentation-synthesizer, skill-benchmarker]
---

# Human Feedback Collector

## Objective
Collect, organize, and analyze human feedback from users, stakeholders, and team members. Identifies patterns, sentiment, and actionable insights to inform skill and system improvements.

## Trigger
- "Collect user feedback on feature X"
- "Gather stakeholder input on system Y"
- "Analyze team feedback about process Z"
- "Collect feedback on skill performance"

Anti-triggers: "Make decisions based on feedback without analysis" / "Collect feedback without acting on it" — those violate the evidence-based improvement principle.

## Inputs
- Feedback sources: surveys, interviews, support tickets, code reviews, comments, ratings
- Feedback format: text, ratings, structured forms, verbal (transcribed)
- Target: specific feature, system, process, or skill
- Time period: feedback collection window

## Outputs
- Feedback report: collected feedback, categorized by theme and sentiment
- Pattern analysis: recurring issues, suggestions, praise
- Actionable insights: specific recommendations for improvement
- Sentiment analysis: positive, neutral, negative distribution
- Priority ranking: insights ranked by impact and frequency

## Procedure
1. **Identify feedback sources**
   - List all channels where human feedback is collected
   - Identify owners and access methods for each source
   - Document feedback collection frequency and coverage

2. **Collect feedback** (documentation-synthesizer)
   - Gather feedback from all identified sources
   - Normalize format: text, ratings, categories
   - Preserve context: who, when, where, what they were doing
   - Redact personal information: names, emails, identifiers

3. **Analyze patterns**
   - Categorize feedback by theme: usability, performance, reliability, features, documentation
   - Identify recurring issues and suggestions
   - Detect sentiment: positive, neutral, negative
   - Flag urgent issues: security concerns, data loss, blocking bugs

4. **Generate insights**
   - Translate feedback into actionable recommendations
   - Rank insights by: frequency, impact, urgency, feasibility
   - Connect related feedback items
   - Identify root causes behind repeated complaints

5. **Verify**
   - Cross-reference feedback with system data (error logs, usage metrics)
   - Validate that feedback patterns match observed behavior
   - Confirm no bias in sample (representative users)

6. **Report**
   - Produce feedback report: themes, sentiment, insights, priorities, recommendations

## Safety & Approval Gates
- **No personal data in output**: Redact names, emails, identifiers
- **Feedback used for improvement only**: Not for individual performance evaluation
- **Anonymous feedback protected**: Never attribute anonymous feedback
- **Approval required** before acting on sensitive feedback

## Failure Handling
- No feedback sources → Report "no feedback available," recommend collection setup
- Feedback unreadable → Mark as "unparseable," continue with readable items
- Contradictory feedback → Report conflict, recommend user research
- No actionable insights → Report "feedback collected but no clear patterns," recommend deeper research

## Completion Criteria
- Feedback report with themes, sentiment, and insights
- Patterns identified and categorized
- Actionable recommendations with priority ranking
- No personal data in output
- Sentiment distribution reported
