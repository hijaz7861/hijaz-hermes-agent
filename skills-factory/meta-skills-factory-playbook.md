# Playbook: Meta-Skills Factory

*Practical examples for the `meta-skills-factory` skill*

---

## Scenario 1: Improve factory skill creation success rate (happy path)

**Trigger:** "Improve the factory's skill creation success rate — analyze pipeline bottlenecks and optimize."

**Invocation:**
```
Execute meta-skills-factory improvement:
- Measure current factory performance on skill creation tasks
- Identify bottlenecks in factory components
- Propose and test factory improvements
- Report before/after metrics
```

**Execution Log:**
```
## Meta-Skills Factory Improvement Cycle

### Phase 1: Measure Factory Performance
- Skill creation success rate: 85% (baseline)
- Test pass rate: 92%
- Regression rate: 3%
- Average skill creation time: 12 minutes

### Phase 2: Analyze Factory Weaknesses
Bottlenecks identified:
- skill-generator: slow at creating playbooks (40% of total time)
- quality-control: inconsistent application of checklist
- benchmark-engine: insufficient repetitions for statistical significance

### Phase 3: Design Factory Improvements
Proposed improvements:
1. skill-generator: template-based playbook generation (reduce time by 30%)
2. quality-control: automated checklist validation (reduce inconsistency)
3. benchmark-engine: increase repetitions from 3 to 5

### Phase 4: Implement and Test
Improvements applied:
- skill-generator template system implemented
- quality-control checklist validator added
- benchmark-engine repetitions increased to 5

Re-test results:
- Skill creation success rate: 85% → 91% (+6%)
- Test pass rate: 92% → 94% (+2%)
- Regression rate: 3% → 2% (-1%)
- Average skill creation time: 12 min → 9 min (-25%)

### Phase 5: Promote and Document
- All improvements pass quality control
- Factory component files updated
- Evolution log: v1.0.0 → v1.1.0 (MINOR: new capability)

### Report
Meta-improvement: SUCCESS
Factory performance improved across all metrics
No regression in skill quality
Factory governance rules still enforced
Exit code: 0.
```

**Expected Output:**
Factory improvement report with before/after metrics, component improvements documented, evolution log updated.

---

## Scenario 2: Factory improvement reduces skill quality (failure case)

**Trigger:** "Optimize the skill-generator to create skills faster."

**Invocation:**
```
Optimize the skill-generator component for speed.
Measure impact on skill quality.
```

**Execution Log:**
```
## Meta-Skills Factory: Generator Optimization

### Baseline Measurement
- Skill creation time: 12 minutes
- Skill quality score: 8.5/10
- Quality control pass rate: 88%

### Optimization Applied
- Removed research-engine verification step from skill-generator
- Streamlined playbook template (fewer scenarios)
- Parallelized file writing

### Post-Optimization Measurement
- Skill creation time: 8 minutes (-33%)
- Skill quality score: 6.2/10 (-27%)
- Quality control pass rate: 61% (-27%)

### Quality Regression Detected
- Quality score dropped below acceptable threshold (7.0/10)
- Pass rate dropped significantly
- Missing playbook scenarios in generated skills

### Rollback Triggered
- Reverted skill-generator to previous version
- Re-measured: quality score 8.5/10, pass rate 88%
- No factory changes remain

### Report
Meta-improvement: REJECTED
Reason: quality regression (27% drop in quality score)
Rollback completed successfully
Next: Propose optimization that maintains quality while improving speed
Exit code: 1 (quality regression, rollback completed).
```

**Expected Output:**
Factory improvement report showing regression, rollback decision, and evidence of quality preservation.

---

## Scenario 3: Authorization denied for factory change (safety case)

**Trigger:** "Update factory-core to allow automatic production deployment of skills."

**Invocation:**
```
Modify factory-core governance to enable automatic deployment of skills to production without quality control review.
```

**Execution Log:**
```
## Meta-Skills Factory: Governance Change Request

### Request Analysis
Requested change: Allow automatic production deployment without QC review
Governance rules affected: GOV-005 (test evidence required), GOV-010 (documentation and tests required), GOV-009 (authorization for external publication)

### Safety Check
This change violates multiple factory governance rules:
- GOV-005: Never claim a skill is tested without actual test evidence
- GOV-010: Ensure every production skill has documentation and reproducible tests
- GOV-009: Require authorization for external publication

### Decision
REQUEST DENIED
- Change would violate factory governance rules
- Would compromise skill quality and security
- Cannot proceed without explicit authorization to modify governance rules

### Report
Meta-improvement: BLOCKED
Reason: violates factory governance rules
No factory changes made
Next: Submit governance rule change request with explicit authorization if needed
Exit code: 0 (blocked by governance, no changes).
```

**Expected Output:**
Factory report showing governance block, rationale, and no changes made.
