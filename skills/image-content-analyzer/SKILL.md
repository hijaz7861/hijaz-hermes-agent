---
name: image-content-analyzer
description: Analyze visual content in images including objects, scenes, colors, composition, and visual elements. Provides detailed description and categorization of image contents.
version: 1.0.0
tags: [image-analysis, computer-vision, object-detection, scene-recognition, visual-content]
dependencies: [visual-quality-assessor, ocr-text-extractor]
---

# Image Content Analyzer

## Objective
Analyze visual content in images including objects, scenes, colors, composition, and visual elements. Provides detailed description and categorization of image contents with confidence scores.

## Trigger
- "Analyze this image content"
- "What objects are in image X?"
- "Describe the scene in this photo"
- "Categorize visual elements in screenshot Y"

Anti-triggers: "Identify specific people" / "Facial recognition" — those require explicit authorization and privacy considerations, not general content analysis.

## Inputs
- Image file: PNG, JPG, TIFF, WebP
- Analysis scope: objects, scenes, colors, text, composition
- Confidence threshold: minimum score for detections
- Categories of interest: specific object types to detect

## Outputs
- Object detections: objects found, bounding boxes, confidence scores
- Scene classification: scene type (indoor, outdoor, office, etc.)
- Color analysis: dominant colors, color palette
- Composition analysis: layout, balance, focal points
- Text detection: presence and location of text (delegates to OCR if detailed reading needed)
- Visual description: natural language summary of image contents

## Procedure
1. **Assess image quality** (visual-quality-assessor)
   - Check resolution, lighting, focus, composition quality
   - Document quality limitations for analysis accuracy

2. **Detect objects**
   - Identify objects in image with bounding boxes
   - Classify object types (person, vehicle, furniture, etc.)
   - Record confidence scores per detection
   - Exclude faces unless explicitly authorized

3. **Classify scene**
   - Determine scene category (indoor/outdoor, specific type)
   - Identify setting characteristics (lighting, time of day, weather)
   - Record scene confidence

4. **Analyze colors and composition**
   - Extract dominant colors and color palette
   - Analyze visual composition (rule of thirds, balance, focal points)
   - Identify visual hierarchy

5. **Detect text presence**
   - Identify regions containing text
   - Delegate to OCR text extractor if detailed reading required
   - Record text region locations

6. **Generate description**
   - Produce natural language description of image contents
   - Summarize objects, scene, colors, composition
   - Note confidence levels and limitations

7. **Report**
   - Produce analysis report: objects, scene, colors, description, confidence

## Safety & Approval Gates
- **No facial recognition**: Do not identify specific people without explicit authorization
- **No sensitive content logging**: Redact or flag sensitive visual content
- **Confidence threshold**: Flag low-confidence detections for review
- **Privacy compliance**: Respect image content privacy

## Failure Handling
- Image too blurry → Report "insufficient quality," recommend clearer image
- No objects detected → Report "no objects found," verify image content
- Scene unclassifiable → Report "scene unknown," describe visible elements
- Low confidence detections → Flag for manual review

## Completion Criteria
- Object detections with bounding boxes and confidence
- Scene classification with confidence
- Color and composition analysis
- Natural language description
- No specific person identification without authorization
