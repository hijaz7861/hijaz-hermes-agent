# Skills Making Factory — Reports

## Purpose
The reports directory contains all factory-generated reports: discovery reports, gap analyses, skill analysis reports, improvement recommendations, regression reports, optimization results, and factory status reports.

## Subdirectory Structure (by report type)

### discovery-report.json
Results from the discovery engine: skill inventory, capability mapping, gap analysis.

### gap-analysis.json
Identified capability gaps in the existing skills ecosystem.

### skill-analysis-report.json
Quality assessment of all existing skills with improvement recommendations.

### improvement-recommendations.json
Prioritized list of skill improvements and new skill proposals.

### regression-report-<skill-name>.json
Regression detection results when comparing new vs original skills.

### optimization-results-<skill-name>.json
Before/after benchmark results for skill optimizations.

### factory-status-report.json
Overall factory health: skills created, improved, tested, rejected, promoted.

## Governance
- **Reports are immutable once written**: Historical reports not modified
- **Evidence-based**: All reports backed by test data and measurements
- **No secrets**: Reports exclude credentials and secret values
