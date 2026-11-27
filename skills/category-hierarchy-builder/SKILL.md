---
name: category-hierarchy-builder
description: Builds and maintains category hierarchies for the skills ecosystem. Creates parent-child category relationships, manages category levels, and ensures hierarchical consistency for skill discovery and navigation.
version: 1.0.0
tags: [category, hierarchy, parent-child, levels, navigation, taxonomy]
dependencies: [category-organizer, category-analyzer, skill-category-manager]
---

# Category Hierarchy Builder

## Objective
Builds and maintains category hierarchies for the skills ecosystem. Creates parent-child category relationships, manages category levels, and ensures hierarchical consistency for skill discovery and navigation.

## Trigger
- "Build category hierarchy for skill ecosystem"
- "Create parent-child category relationships"
- "Organize categories into levels"
- "Manage category hierarchy for navigation"

Anti-triggers: "Create circular category dependencies" / "Build hierarchy without skill coverage" — those violate hierarchy integrity principles.

## Inputs
- Categories: all existing category names and descriptions
- Skills: all skills with their category assignments
- Category relationships: existing parent-child relationships (if any)
- Usage patterns: how users navigate categories
- Navigation requirements: depth, breadth, discoverability goals

## Outputs
- Category hierarchy: tree structure with parent-child relationships
- Category levels: level assignments for each category
- Navigation paths: paths from root to leaf categories
- Hierarchy validation: consistency check results
- Hierarchy report: structure, levels, paths, validation results

## Procedure
1. **Analyze existing categories**
   - List all categories with descriptions and scope
   - Identify existing parent-child relationships
   - Identify orphan categories (no parent, no children)
   - Identify root categories (no parent, has children)

2. **Determine category levels**
   - Assign level 0 to root categories (broadest scope)
   - Assign increasing levels to child categories (more specific)
   - Ensure hierarchy depth is manageable (recommend max 4 levels)
   - Document level assignments with rationale

3. **Build parent-child relationships**
   - For each category, determine parent based on scope inclusion
   - Ensure no category has multiple parents (single inheritance)
   - Ensure no circular dependencies
   - Document each relationship with rationale

4. **Validate hierarchy**
   - Check for circular dependencies
   - Check for orphan categories (no path to root)
   - Check for duplicate relationships
   - Validate all skills can be reached through hierarchy
   - Validate hierarchy depth doesn't exceed maximum

5. **Generate navigation paths**
   - For each leaf category, generate path from root
   - Document path for skill discovery
   - Identify shortest and longest paths
   - Document navigation recommendations

6. **Report**
   - Produce hierarchy report: tree structure, levels, paths, validation results

## Safety & Approval Gates
- **Approval required** for hierarchy restructuring
- **No circular dependencies allowed**
- **Every category must have a path to root**
- **Skill coverage maintained**: Every skill reachable through hierarchy

## Failure Handling
- Circular dependency detected → Report, break cycle, recommend manual review
- Orphan category detected → Report, assign parent or mark as root
- Multiple parents detected → Report, choose primary parent, mark others as cross-references
- Skill unreachable → Report, fix category assignment or hierarchy
- Hierarchy too deep → Recommend flattening, suggest max depth

## Completion Criteria
- Category hierarchy tree documented with parent-child relationships
- Level assignments for all categories
- Navigation paths for all leaf categories
- Hierarchy validation passed (no cycles, no orphans, no duplicates)
- All skills reachable through hierarchy
