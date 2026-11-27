---
name: screen-content-reader
description: Read and interpret content from computer screens, UI screenshots, and application interfaces. Identifies UI elements, text, buttons, menus, and application state from visual screen captures.
version: 1.0.0
tags: [screen-reading, UI-analysis, interface-inspection, screenshot-reading, application-state]
dependencies: [ocr-text-extractor, image-content-analyzer]
---

# Screen Content Reader

## Objective
Read and interpret content from computer screens, UI screenshots, and application interfaces. Identifies UI elements, text, buttons, menus, and application state from visual screen captures without requiring code access.

## Trigger
- "Read content from this screenshot"
- "Identify UI elements in interface X"
- "Read error message from screen Y"
- "Analyze application state from screen capture"

Anti-triggers: "Control application" / "Interact with UI" — those are automation tasks, not screen reading.

## Inputs
- Screen capture: PNG, JPG, or screenshot of application interface
- UI element types: buttons, text fields, menus, dialogs, notifications
- Text regions: specific areas to read text from
- Application context: expected application type (web, desktop, mobile)

## Outputs
- UI elements: buttons, text fields, dropdowns, checkboxes, radio buttons
- Text content: all readable text from the screen
- Application state: active window, open dialogs, error messages, notifications
- Menu structure: menu items, navigation options
- Error and warning messages: displayed errors, warnings, confirmations
- Screen description: natural language summary of screen contents

## Procedure
1. **Assess screen quality** (visual-quality-assessor)
   - Check screenshot resolution, clarity, readability
   - Identify blurred or unreadable regions
   - Document quality limitations

2. **Extract all text** (OCR text extractor)
   - Read all visible text from the screen
   - Preserve text hierarchy (headings, body, labels, values)
   - Record text regions with bounding boxes
   - Capture error messages, notifications, and dialog text

3. **Identify UI elements** (image content analyzer)
   - Detect buttons, text fields, dropdowns, checkboxes
   - Identify menu items and navigation elements
   - Classify element types and states (enabled, disabled, selected)
   - Record element locations and bounding boxes

4. **Determine application state**
   - Identify active application and window
   - Detect open dialogs, modals, or popups
   - Identify error messages, warnings, confirmations
   - Determine current screen/context within application

5. **Analyze screen structure**
   - Map UI element relationships (labels to fields, buttons to actions)
   - Identify form groups, tab panels, modal dialogs
   - Document navigation structure

6. **Generate screen description**
   - Produce natural language description of screen contents
   - Summarize UI elements, text, application state
   - Note any anomalies or issues visible

7. **Report**
   - Produce screen reading report: elements, text, state, description

## Safety & Approval Gates
- **No sensitive data logging**: Redact passwords, credit cards, personal data from screenshots
- **No UI interaction**: Reader only observes, does not click or input
- **No credential capture**: Exclude login credentials from output
- **Privacy compliance**: Respect screen content privacy

## Failure Handling
- Screen too blurry → Report "insufficient quality," recommend clearer screenshot
- No text detected → Report "no readable text," verify screenshot content
- UI elements unrecognized → Report "unknown elements," describe visually
- Application unknown → Report "application unidentified," describe visible elements

## Completion Criteria
- UI elements identified with types and locations
- All readable text extracted
- Application state determined
- Screen description produced
- No sensitive data in output
