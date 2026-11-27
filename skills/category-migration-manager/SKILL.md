---
name: category-migration-manager
description: Manages category migrations for skills when categories are renamed, merged, split, or deprecated. Ensures smooth transitions with skill reassignment, registry updates, and backward compatibility.
version: 1.0.0
tags: [category, migration, transition, reassignment, deprecation, backward-compatibility]
dependencies: [skill-category-manager, category-analyzer, evolution-engine, quality-control]
---

# Category Migration Manager

## Objective
Manages category migrations for skills when categories are renamed, merged, split, or deprecated. Ensures smooth transitions with skill reassignment, registry updates, and backward compatibility for skill discovery.

## Trigger
- "Migrate skills from category X to category Y"
- "Deprecate category Z and reassign skills"
- "Split category A into categories B and C"
- "Rename category M to category N"

Anti-triggers: "Migrate skills without impact analysis" / "Delete categories without skill reassignment" — those violate migration safety principles.

## Inputs
- Source category: category being changed (renamed, merged, split, deprecated)
- Target category(s): destination category(s) for skills
- Skills affected: all skills currently in source category
- Migration type: rename, merge, split, deprecate
- Migration timeline: when migration should occur
- Rollback plan: how to revert if migration causes issues

## Outputs
- Migration plan: skills to move, target categories, timeline, rollback plan
- Migration log: all skill reassignments with timestamps
- Updated registry: skills-index.json with new category assignments
- Updated SKILL.md files: category metadata updated
- Backward compatibility: old category references preserved where needed
- Migration report: skills migrated, issues encountered, verification results

## Procedure
1. **Analyze migration scope**
   - Identify all skills in source category
   - Identify all references to source category (registry, SKILL.md files, playbooks)
   - Assess impact of migration on skill discovery
   - Document all affected files and references

2. **Design migration plan**
   - For rename: update category name, keep skills in same logical group
   - For merge: move skills from source to target, deprecate source
   - For split: create new categories, distribute skills based on criteria
   - For deprecate: move skills to replacement categories, mark source as deprecated
   - Document timeline and rollback plan

3. **Execute migration**
   - Update skills-index.json with new category assignments
   - Update each affected SKILL.md file with new category
   - Update playbooks if they reference categories
   - Update category definitions
   - Maintain backward compatibility (old category references point to new)

4. **Verify migration**
   - Confirm all skills have valid category assignments
   - Confirm no skills left in deprecated category
   - Confirm registry consistency (SKILL.md matches skills-index.json)
   - Test skill discovery through new categories
   - Verify backward compatibility (old references still work)

5. **Log migration**
   - Record each skill reassignment with timestamp
   - Record category changes with rationale
   - Record rollback information
   - Document any issues encountered

6. **Report**
   - Produce migration report: skills migrated, issues, verification, rollback status

## Safety & Approval Gates
- **Approval required** for all category migrations
- **Impact analysis required** before migration
- **Rollback plan required** for all migrations
- **No skill left without category** during or after migration
- **Backward compatibility maintained** for old category references

## Failure Handling
- Skill reassignment fails → Rollback that skill, report, continue with others
- Registry inconsistency → Report, fix inconsistency, re-verify
- Discovery broken → Rollback migration, report, investigate
- Rollback fails → Alert, document manual recovery steps
- Approval denied → Stop, report, no changes made

## Completion Criteria
- Migration plan executed with all skills reassigned
- Registry updated with new category assignments
- All SKILL.md files updated with new categories
- Backward compatibility maintained
- Migration log complete with all changes
- Verification passed (skill discovery works through new categories)
