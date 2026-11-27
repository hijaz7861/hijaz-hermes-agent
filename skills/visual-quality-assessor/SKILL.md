---
name: visual-quality-assessor
description: Assess visual quality of images, documents, and screens. Evaluates resolution, blur, contrast, lighting, focus, and composition quality with quantitative scores and recommendations.
version: 1.0.0
tags: [visual-quality, image-assessment, quality-scoring, image-analysis, quality-metrics]
dependencies: []
---

# Visual Quality Assessor

## Objective
Assess visual quality of images, documents, and screens. Evaluates resolution, blur, contrast, lighting, focus, and composition quality with quantitative scores and recommendations for improvement.

## Trigger
- "Assess image quality for file X"
- "Check document scan quality"
- "Evaluate screenshot readability"
- "Score visual quality of image Y"

Anti-triggers: "Enhance image quality" / "Edit image" — those are image editing tasks, not quality assessment.

## Inputs
- Image file: PNG, JPG, TIFF, PDF, or screenshot
- Quality dimensions: resolution, blur, contrast, lighting, focus, composition
- Quality thresholds: minimum acceptable scores per dimension
- Use case: document scanning, screen capture, photograph, etc.

## Outputs
- Quality scores: per-dimension scores (0-100) and overall quality score
- Quality issues: blur, low contrast, poor lighting, out of focus, skew, noise
- Resolution analysis: dimensions, DPI, suitability for intended use
- Lighting analysis: exposure, shadows, highlights, evenness
- Focus analysis: sharp regions, blur regions, focus quality
- Composition analysis: framing, balance, rule of thirds
- Recommendations: specific improvements for quality issues
- Use case suitability: whether image meets requirements for intended purpose

## Procedure
1. **Analyze resolution**
   - Measure image dimensions and DPI
   - Assess suitability for intended use (document scanning, screen reading, etc.)
   - Identify upscaling or downscaling needs

2. **Detect blur**
   - Measure sharpness and focus quality
   - Identify motion blur, out-of-focus regions, lens blur
   - Score blur severity per region

3. **Analyze contrast and lighting**
   - Measure contrast ratio and dynamic range
   - Identify underexposed, overexposed, or uneven lighting
   - Detect shadows and highlights issues

4. **Assess composition**
   - Evaluate framing, subject placement, balance
   - Check rule of thirds alignment
   - Identify cropping or framing issues

5. **Detect artifacts**
   - Identify compression artifacts, noise, pixelation
   - Check for scan artifacts (lines, bands, shadows)
   - Detect color issues (cast, banding)

6. **Calculate overall quality score**
   - Weight dimensions based on use case
   - Combine into overall score (0-100)
   - Classify quality: excellent, good, fair, poor, unusable

7. **Generate recommendations**
   - Specific improvements for each quality issue
   - Rescanning or recapturing recommendations
   - Preprocessing suggestions for OCR or analysis

8. **Report**
   - Produce quality report: scores, issues, recommendations, suitability

## Safety & Approval Gates
- **Read-only assessment**: Does not modify images
- **No content logging**: Does not describe image content in detail
- **Quality thresholds configurable**: Based on use case requirements
- **No sensitive data**: Does not extract or log sensitive visual content

## Failure Handling
- Image unreadable → Report "cannot assess," verify file integrity
- Unsupported format → Report "format unsupported," suggest conversion
- Corrupted image → Report "image corrupted," recommend restoration
- No quality issues → Report "image passes quality assessment," confirm suitability

## Completion Criteria
- Quality scores for all dimensions
- Overall quality score and classification
- Identified issues with severity
- Specific recommendations for improvement
- Use case suitability determination
