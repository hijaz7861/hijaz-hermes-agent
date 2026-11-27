---
name: category-organizer
description: Organizes skills into logical category groups based on functionality, dependencies, and usage patterns. Creates category hierarchies and ensures skills are placed in the most appropriate categories.
version: 1.0.0
tags: [category, organization, grouping, hierarchy, classification, skill-grouping]
dependencies: [skill-category-manager, skill-analyzer, codebase-intelligence]
---

# Category Organizer

## Objective
Organizes skills into logical category groups based on functionality, dependencies, and usage patterns. Creates category hierarchies and ensures skills are placed in the most appropriate categories for discoverability and routing.

## Trigger
- "Reorganize skills into better categories"
- "Create category hierarchy for skill ecosystem"
- "Group skills by functionality and dependencies"
- "Reorganize skill categories based on usage patterns"

Anti-triggers: "Force skills into categories without analysis" / "Create categories without skill coverage" — those violate organization principles.

## Inputs
- Skills inventory: all skills with capabilities, dependencies, versions
- Skill procedures: SKILL.md files with objective, trigger, dependencies
- Usage patterns: how skills are invoked and combined
- Category definitions: existing category names and descriptions

## Outputs
- Category hierarchy: parent-child category relationships
- Skill-to-category mapping: each skill assigned to optimal category
- Category groupings: skills grouped by functionality and dependencies
- Reorganization plan: proposed category changes with rationale
- Verification: skills correctly categorized, no skill left uncategorized

## Procedure
1. **Analyze skill functionality**
   - Read each skill's objective, trigger, and procedure
   - Identify primary function and secondary capabilities
   - Map skill dependencies and related skills
   - Document usage patterns from playbooks

2. **Analyze existing categories**
   - Review current category definitions and assignments
   - Identify over-populated and under-populated categories
   - Identify skills that span multiple categories
   - Document category gaps (capabilities with no category)

3. **Design category hierarchy**
   - Create parent categories for broad functional areas
   - Create child categories for specific specializations
   - Ensure hierarchy is logical and discoverable
   - Balance category sizes (not too many, not too few per category)

4. **Assign skills to categories**
   - Assign each skill to its primary category
   - Assign secondary categories for multi-capability skills
   - Ensure every skill has at least one category
   - Balance workload across categories

5. **Verify categorization**
   - Cross-reference skill capabilities with category scope
   - Verify no skill is uncategorized
   - Verify no category is empty (unless intentionally reserved)
   - Validate category assignments with skill-analyzer

6. **Report**
   - Produce organization report: hierarchy, mappings, groupings, changes

## Safety & Approval Gates
- **Approval required** for major category reorganizations
- **No skill left uncategorized**: Every skill must have a category
- **Category changes documented** with rationale
- **Rollback capability**: Revert reorganizations that break discovery

## Failure Handling
- Skill spans multiple categories → Assign primary + secondary categories
- No appropriate category exists → Create new category or mark for creation
- Skill capabilities unclear → Mark for manual review, assign temporary category
- Category too large → Recommend sub-categories
- Category too small → Recommend merge with related category

## Completion Criteria
- Category hierarchy documented with parent-child relationships
- Every skill assigned to at least one category
- No empty categories (unless intentionally reserved)
- Category groupings documented by functionality
- Reorganization plan with rationale for all changes
