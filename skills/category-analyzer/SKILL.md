---
name: category-analyzer
description: Analyzes category coverage, identifies gaps and overlaps in the skill category system, and provides recommendations for category optimization and skill categorization improvements.
version: 1.0.0
tags: [category, analysis, coverage, gaps, optimization, recommendations]
dependencies: [skill-category-manager, category-organizer, skill-benchmarker]
---

# Category Analyzer

## Objective
Analyzes category coverage across the skills ecosystem, identifies gaps and overlaps in category coverage, and provides recommendations for category optimization and skill categorization improvements.

## Trigger
- "Analyze category coverage for skill ecosystem"
- "Identify category gaps and overlaps"
- "Evaluate category effectiveness for skill discovery"
- "Recommend category optimizations"

Anti-triggers: "Delete categories without impact analysis" / "Create categories without skill coverage" — those violate category integrity principles.

## Inputs
- Skills inventory: all skills with categories and capabilities
- Category definitions: existing categories with descriptions
- Skill usage data: how skills are discovered and invoked
- Capability matrix: what capabilities each skill provides
- User feedback: reports of difficulty finding skills

## Outputs
- Coverage analysis: capabilities covered vs. not covered by categories
- Gap analysis: capability areas without category coverage
- Overlap analysis: skills in multiple categories, categories with overlapping scope
- Category effectiveness: how well categories support skill discovery
- Recommendations: category additions, merges, splits, reassignments
- Category health score: overall category system health

## Procedure
1. **Map capabilities to categories**
   - List all capabilities from skill inventory
   - Map each capability to its category
   - Identify capabilities with no category coverage
   - Identify capabilities covered by multiple categories

2. **Analyze category coverage**
   - Calculate coverage percentage per category
   - Identify under-covered capability areas
   - Identify over-covered capability areas
   - Document capability-to-category mapping

3. **Analyze category overlaps**
   - Identify skills assigned to multiple categories
   - Identify categories with similar scope descriptions
   - Identify skills that could be in multiple categories
   - Document overlap areas

4. **Evaluate category effectiveness**
   - Assess how easily skills can be found by category
   - Identify categories where skills are hard to discover
   - Identify categories with unclear scope
   - Document discovery issues reported by users

5. **Generate recommendations**
   - Recommend new categories for uncovered capabilities
   - Recommend category merges for overlapping scope
   - Recommend category splits for over-populated categories
   - Recommend skill reassignments for better categorization
   - Prioritize recommendations by impact

6. **Calculate category health score**
   - Score based on coverage, overlap, effectiveness, balance
   - Track score over time for improvement measurement
   - Report score with breakdown by dimension

7. **Report**
   - Produce analysis report: coverage, gaps, overlaps, recommendations, health score

## Safety & Approval Gates
- **Approval required** for category deletions or merges
- **Impact analysis required** before any category change
- **No category removal without skill reassignment**
- **Category changes must improve discovery, not just reorganize**

## Failure Handling
- No usage data available → Mark analysis as "limited," recommend usage tracking
- Unclear category scope → Mark for manual review, recommend category clarification
- No gaps found → Report "category coverage complete," recommend monitoring
- High overlap detected → Report overlap areas, recommend consolidation

## Completion Criteria
- Coverage analysis with capability-to-category mapping
- Gap analysis with uncovered capability areas
- Overlap analysis with multi-category skills
- Category effectiveness evaluation
- Prioritized recommendations with impact ratings
- Category health score calculated
