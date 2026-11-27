---
name: dependency-duplicate-remover
description: Detect and remove duplicate dependency declarations, conflicting versions, and transitive dependency duplicates across manifest files. Consolidates to single versions to reduce bundle size and security risk.
version: 1.0.0
tags: [duplicate, removal, dependencies, deduplication, package-management, security]
dependencies: [dependency-management, codebase-intelligence]
---

# Dependency Duplicate Remover

## Objective
Detect and remove duplicate dependency declarations, conflicting versions, and transitive dependency duplicates across manifest files. Consolidates to single versions to reduce bundle size, attack surface, and maintenance overhead.

## Trigger
- "Remove duplicate dependencies across manifests"
- "Consolidate conflicting package versions"
- "Deduplicate transitive dependencies in lockfile"
- "Clean up duplicate package declarations"

Anti-triggers: "Upgrade all dependencies to latest" / "Remove dependencies without analysis" — those violate safety and stability principles.

## Inputs
- Dependency manifests: package.json, requirements.txt, go.mod, Cargo.toml, pom.xml, etc.
- Lockfiles: package-lock.json, Pipfile.lock, go.sum, Cargo.lock, etc.
- Version consolidation policy: which version to keep when conflicts exist

## Outputs
- Duplicate report: duplicate declarations, conflicting versions, locations
- Consolidation plan: which version to keep, which to remove
- Updated manifests and lockfiles
- Verification: build and tests pass after consolidation

## Procedure
1. **Inventory dependencies** (dependency-management)
   - Read all dependency manifests and lockfiles
   - List all dependencies with versions and sources
   - Identify direct vs. transitive dependencies

2. **Detect duplicates and conflicts**
   - Same package declared in multiple manifests
   - Same package with different versions across manifests
   - Transitive dependencies with conflicting version requirements
   - Duplicate packages with different sources (npm vs. yarn, etc.)

3. **Plan consolidation**
   - For conflicts: determine which version to keep (usually latest compatible)
   - Assess breaking change risk of version consolidation
   - Map all files that import the affected packages

4. **Apply consolidation** (requires approval)
   - Update manifests to single version per package
   - Update lockfiles to match
   - Remove duplicate declarations
   - One package at a time

5. **Verify**
   - Run install/build to confirm dependencies resolve
   - Run test suite to confirm no breaking changes
   - Verify no duplicate declarations remain
   - Roll back any consolidation that breaks the build

6. **Report**
   - Produce deduplication report: duplicates found, versions consolidated, files updated, verification results

## Safety & Approval Gates
- **Approval required** before modifying manifests or lockfiles
- **Build and test gate**: consolidation verified with passing build and tests
- **One package at a time**: no batching unrelated changes
- **Rollback**: revert if build or tests fail

## Failure Handling
- Manifest parse error → Skip, mark as unanalyzable, continue
- Consolidation breaks build → Revert immediately, report, do not proceed
- No compatible version found → Mark as "manual review required," do not force
- No duplicates found → Report "no duplicate dependencies detected"

## Completion Criteria
- Duplicate report with declarations and versions
- Each consolidation verified with passing build and tests
- No duplicate declarations remain
- Lockfiles consistent with manifests
