---
name: document-visual-inspector
description: Inspect documents visually for quality, formatting, layout issues, and document integrity. Identifies missing pages, formatting inconsistencies, visual defects, and document structure problems.
version: 1.0.0
tags: [document-inspection, visual-quality, document-analysis, layout, formatting]
dependencies: [visual-quality-assessor, ocr-text-extractor, image-content-analyzer]
---

# Document Visual Inspector

## Objective
Inspect documents visually for quality, formatting, layout issues, and document integrity. Identifies missing pages, formatting inconsistencies, visual defects, and document structure problems through visual analysis.

## Trigger
- "Inspect document X for visual issues"
- "Check document formatting consistency"
- "Find missing pages in scanned document"
- "Inspect document layout for problems"

Anti-triggers: "Edit document content" / "Proofread text for grammar" — those are editing tasks, not visual inspection.

## Inputs
- Document file: PDF, scanned images, or multi-page image set
- Inspection scope: formatting, layout, page integrity, visual quality
- Quality standards: expected formatting rules, brand guidelines
- Page range: specific pages to inspect (optional)

## Outputs
- Visual defects: blurry pages, low contrast, skewed pages, cut-off content
- Formatting inconsistencies: font variations, spacing issues, alignment problems
- Missing pages: gaps in page sequence, blank pages
- Layout issues: overlapping elements, misaligned content, broken structure
- Document integrity: page count, file integrity, readability
- Inspection report: issues found, severity, page locations, recommendations

## Procedure
1. **Assess document quality** (visual-quality-assessor)
   - Check overall document quality across all pages
   - Identify pages with low resolution, blur, or poor contrast
   - Document quality variations across pages

2. **Inspect page integrity**
   - Verify page sequence (no missing pages)
   - Detect blank pages
   - Identify cut-off or truncated content
   - Check page orientation and skew

3. **Inspect formatting consistency**
   - Check font consistency across pages
   - Verify spacing and alignment
   - Identify header/footer inconsistencies
   - Check margin and padding uniformity

4. **Inspect layout structure**
   - Check for overlapping elements
   - Identify misaligned tables, images, or text blocks
   - Verify reading order and document structure
   - Check table of contents accuracy (if present)

5. **Read text for verification** (OCR text extractor)
   - Extract text from pages to verify content presence
   - Check for missing or garbled text
   - Compare against expected content (if provided)

6. **Analyze visual elements** (image content analyzer)
   - Check images, charts, and diagrams for quality
   - Identify missing or broken visual elements
   - Verify visual element placement

7. **Report**
   - Produce inspection report: defects, inconsistencies, missing pages, recommendations

## Safety & Approval Gates
- **No content modification**: Inspector only identifies issues, does not edit
- **No sensitive content logging**: Redact document content in reports
- **Read-only inspection**: Does not modify original documents
- **Privacy compliance**: Respect document confidentiality

## Failure Handling
- Document unreadable → Report "document cannot be processed," verify file integrity
- Password protected → Report "password protected," request access
- Corrupted file → Report "file corrupted," recommend restoration
- No issues found → Report "document passes inspection," confirm quality

## Completion Criteria
- Visual defects identified with page locations
- Formatting inconsistencies documented
- Missing pages identified
- Layout issues reported
- Document integrity confirmed
- No document content in output
