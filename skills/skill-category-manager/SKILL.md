---
name: skill-category-manager
description: Central category management for all skills. Manages skill categories, tracks category membership, ensures category consistency, and provides category-based skill discovery and routing.
version: 1.0.0
tags: [category, management, organization, classification, taxonomy, skill-registry]
dependencies: [skill-analyzer, discovery-engine, evolution-engine]
---

# Skill Category Manager

## Objective
Central category management for all skills. Manages skill categories, tracks category membership, ensures category consistency across the skills registry, and provides category-based skill discovery and routing for the entire skills ecosystem.

## Trigger
- "Manage skill categories for repository X"
- "Organize skills by category"
- "Update skill category assignments"
- "Audit category consistency across skills"

Anti-triggers: "Delete categories without reviewing skill impact" / "Assign skills to categories without verification" — those violate category integrity principles.

## Inputs
- Skills registry: skills-index.json with all skills and their categories
- Skill files: individual SKILL.md files with category metadata
- Category definitions: category names, descriptions, scope rules
- Category change requests: add, remove, move skills between categories

## Outputs
- Category map: all skills organized by category
- Category consistency report: skills with missing or incorrect categories
- Category assignments: updated category membership for each skill
- Category statistics: skill count per category, coverage analysis
- Change log: all category modifications with timestamps and rationale

## Procedure
1. **Inventory all skills**
   - Read skills-index.json for complete skill list
   - Read each SKILL.md for category metadata
   - Build complete skill-to-category mapping

2. **Validate category assignments**
   - Check each skill has a valid category
   - Verify category exists in category definitions
   - Flag skills with missing or invalid categories
   - Identify skills with inconsistent category metadata

3. **Organize skills by category**
   - Group skills under their assigned categories
   - Count skills per category
   - Identify under-populated and over-populated categories
   - Document category coverage

4. **Process category changes**
   - Review category change requests
   - Validate proposed category exists or create new one
   - Update skill metadata with new category
   - Update registry files
   - Log all changes with rationale

5. **Ensure consistency**
   - Cross-reference SKILL.md category with registry category
   - Flag mismatches for correction
   - Standardize category naming conventions
   - Update all references to changed categories

6. **Report**
   - Produce category management report: map, statistics, consistency status, changes

## Safety & Approval Gates
- **Approval required** for category changes affecting production skills
- **No category deletion** without reviewing skill impact
- **Category changes logged** with timestamps and rationale
- **Rollback capability**: Revert category changes if they break skill discovery

## Failure Handling
- Skill missing category → Flag for assignment, do not guess category
- Category not in definitions → Flag for creation or reassignment
- Inconsistent metadata → Report mismatch, request resolution
- No skills in category → Report empty category, recommend merge or removal

## Completion Criteria
- Category map produced with all skills organized
- Category consistency verified for all skills
- Category statistics documented
- All category changes logged
- No skills without valid category assignment
