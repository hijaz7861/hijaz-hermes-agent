---
name: ocr-text-extractor
description: Extract text from images, scanned documents, and screenshots using Optical Character Recognition. Supports multiple languages, handwritten text, and low-quality images with confidence scoring.
version: 1.0.0
tags: [ocr, text-extraction, computer-vision, image-reading, document-processing]
dependencies: [image-content-analyzer, visual-quality-assessor]
---

# OCR Text Extractor

## Objective
Extract text from images, scanned documents, and screenshots using Optical Character Recognition (OCR). Supports multiple languages, handwritten text, and low-quality images with confidence scoring for each extracted text region.

## Trigger
- "Extract text from image X"
- "OCR this scanned document"
- "Read text from screenshot Y"
- "Extract handwritten notes from image"

Anti-triggers: "Translate text" / "Summarize document content" — those are separate tasks (translation, summarization), not pure OCR text extraction.

## Inputs
- Image file: PNG, JPG, TIFF, PDF, or screenshot
- Language hints: expected languages (default: English)
- Text type: printed, handwritten, mixed
- Quality expectations: minimum confidence threshold
- Region of interest: specific area to extract (optional)

## Outputs
- Extracted text: full text content with confidence scores
- Text regions: bounding boxes for each text block, line, word
- Language detection: identified languages per region
- Confidence scores: per-region and overall confidence
- Quality assessment: image quality impact on extraction

## Procedure
1. **Assess image quality** (visual-quality-assessor)
   - Check image resolution, contrast, blur, noise
   - Identify text orientation and skew
   - Document quality issues that may affect OCR accuracy
   - Recommend preprocessing if quality is low

2. **Preprocess image**
   - Deskew and rotate text to horizontal
   - Enhance contrast and remove noise
   - Binarize if needed (black and white for better OCR)
   - Crop to region of interest if specified

3. **Extract text** (OCR engine)
   - Run OCR with language-specific models
   - Handle mixed printed and handwritten text
   - Detect multiple languages if present
   - Record confidence scores for each text region

4. **Post-process results**
   - Correct common OCR errors (confusable characters: 0/O, 1/l, 5/S)
   - Merge text regions into logical blocks (paragraphs, lines)
   - Preserve reading order and layout structure
   - Flag low-confidence regions for review

5. **Verify**
   - Compare extracted text against expected patterns (if known)
   - Flag regions below confidence threshold
   - Document extraction limitations
   - Produce confidence report

6. **Report**
   - Produce OCR report: extracted text, regions, confidence, quality notes

## Safety & Approval Gates
- **No sensitive data logging**: Redact PII, credit cards, SSNs from output
- **Confidence threshold**: Flag low-confidence text for human review
- **No automated decisions**: OCR output requires human verification for critical data
- **Privacy compliance**: Respect data protection regulations for extracted personal data

## Failure Handling
- Image unreadable → Report "image too low quality," recommend better scan
- No text detected → Report "no text found," verify image contains text
- Language not supported → Report "language unsupported," suggest alternative
- Low confidence overall → Mark as "unverified," recommend manual transcription

## Completion Criteria
- Extracted text with confidence scores for all regions
- Text regions with bounding boxes
- Language detection results
- Quality assessment documented
- No sensitive values in output
