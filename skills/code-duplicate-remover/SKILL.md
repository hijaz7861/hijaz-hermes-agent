---
name: code-duplicate-remover
description: Detect and remove duplicate code blocks, functions, and logic across the codebase. Extracts shared functionality into reusable modules to improve maintainability and reduce bugs from inconsistent duplicates.
version: 1.0.0
tags: [duplicate, removal, code, deduplication, refactoring, maintainability]
dependencies: [codebase-intelligence, code-refactorer, autonomous-testing]
---

# Code Duplicate Remover

## Objective
Detect and remove duplicate code blocks, functions, and logic across the codebase. Extracts shared functionality into reusable modules to improve maintainability and reduce bugs caused by inconsistent duplicates.

## Trigger
- "Remove duplicate code in module X"
- "Find and deduplicate similar functions across the codebase"
- "Extract shared logic from duplicated code blocks"
- "Deduplicate repeated patterns in file Y"

Anti-triggers: "Remove all repetition without analysis" / "Deduplicate without tests" — those violate safety and verification principles.

## Inputs
- Target: file, module, directory, or repository to analyze
- Similarity threshold: minimum similarity to consider code as duplicate (default: 85%)
- Extraction scope: which duplicates to extract into shared modules

## Outputs
- Duplicate report: duplicate blocks, locations, similarity percentage
- Extraction plan: shared modules to create, files to update
- Before/after metrics: lines of code, duplicate count, complexity
- Verification: tests pass before and after deduplication

## Procedure
1. **Scan for duplicates** (codebase-intelligence)
   - Read all source files in target
   - Use AST-based or token-based similarity detection
   - Identify duplicated code blocks, functions, classes, logic patterns
   - Record locations, similarity scores, and block sizes

2. **Classify duplicates**
   - Exact duplicates: identical code, safe to extract
   - Near-duplicates: similar with minor variations, parameterize
   - False positives: common patterns (imports, boilerplate), exclude

3. **Plan extraction**
   - For each duplicate group: determine shared module location
   - Design parameterized interface for near-duplicates
   - Map all call sites to update

4. **Extract shared modules** (code-refactorer)
   - Create shared module with extracted functionality
   - Update all call sites to use shared module
   - Preserve function signatures and behavior
   - One extraction at a time

5. **Verify** (autonomous-testing)
   - Run tests before and after each extraction
   - Confirm behavior unchanged (same inputs → same outputs)
   - Run lint, typecheck, build
   - Roll back any extraction that breaks tests

6. **Report**
   - Produce deduplication report: duplicates found, extracted, lines saved, verification results

## Safety & Approval Gates
- **Approval required** before modifying code
- **Test gate**: every extraction verified with tests passing before and after
- **One extraction at a time**: no batching unrelated changes
- **Rollback**: revert if tests fail or behavior changes

## Failure Handling
- Cannot parse file → Skip, mark as unanalyzable, continue
- Extraction breaks tests → Revert immediately, report, do not proceed
- False positive rate too high → Adjust similarity threshold, rescan
- No duplicates found → Report "no duplicates detected," no changes made

## Completion Criteria
- Duplicate report with locations and similarity scores
- Each extraction verified with tests passing before and after
- Lines of code reduced, duplicate count decreased
- No behavior changes introduced
