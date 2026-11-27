---
name: security-debugger
description: Debug security-related defects by combining autonomous debugging with security auditing. Reproduce security issues (injection, auth bypass, data exposure), find root cause, apply verified security fixes, and add regression tests.
version: 1.0.0
tags: [security, debugging, vulnerabilities, root-cause, remediation]
dependencies: [autonomous-debugging, security-audit]
---

# Security Debugger

## Objective
Combine autonomous debugging with security auditing to diagnose and fix security defects. Reproduce the security issue, find the root cause (injection point, auth bypass, data exposure), apply a minimal security fix, and verify with security-focused regression tests.

## Trigger
- "Debug the SQL injection in endpoint X"
- "Find the auth bypass vulnerability in module Y"
- "Debug the data exposure in component Z"
- "Security issue: reproduce, diagnose, fix, verify"

Anti-triggers: "Scan for all vulnerabilities" / "Patch everything automatically" — those are security-audit or dependency-management, not defect debugging.

## Inputs
- Security issue: vulnerability report, CVE, pen-test finding, or observed insecure behavior
- Reproduction steps or exploit pattern
- Environment details
- Acceptable security target (what "fixed" means)

## Outputs
- Reproduction evidence: exact input, exploit pattern, observed insecure behavior
- Root cause: file:line, vulnerability type, explanation, evidence
- Fix: minimal security patch, before/after security verification
- Regression test: security test that fails before fix, passes after
- Verification: security scan results, test suite, build results

## Procedure
1. **Capture the security failure** (autonomous-debugging)
   - Obtain exact vulnerability details: CVE ID, exploit input, expected vs. actual behavior.
   - Identify deterministic reproduction path. If impossible, state hypotheses.

2. **Scan for related issues** (security-audit)
   - Scan the affected module and related files for similar patterns.
   - Check for committed secrets, weak crypto, insecure config in the same area.
   - Flag any additional candidates by location only (never print secret values).

3. **Establish security baseline**
   - Record current security posture: auth mechanism, input validation, output encoding, crypto usage.
   - Document what "secure" looks like for this code path.

4. **Form hypotheses** (autonomous-debugging)
   - Rank likely root causes: missing input validation, missing output encoding, broken auth, broken crypto, insecure defaults.
   - Trace the exploit input through validation, business logic, and output.

5. **Test one cause at a time** (autonomous-debugging)
   - Prefer focused experiment: add input validation, test with exploit input.
   - Avoid unrelated refactors.

6. **Implement the fix** (autonomous-debugging + security-audit principles)
   - Add regression test that fails before fix (exploit succeeds), passes after (exploit blocked).
   - Smallest safe patch; preserve public interfaces unless behavior change is authorized.
   - Never log secrets or credentials in fix or tests.

7. **Verify** (security-audit + autonomous-debugging)
   - Re-run reproduction: exploit no longer succeeds.
   - Re-run security audit on affected files: no new findings.
   - Run full test suite, lint, typecheck, build.

8. **Report**
   - State root cause, vulnerability type, fix, before/after security verification, remaining risks.

## Safety & Approval Gates
- **Approval required** before any code change.
- **Rollback:** Record pre-fix state; revert if security verification degrades or tests fail.
- **No secret logging:** Never print secret values, tokens, or credentials in output, tests, or fixes.
- **No production mutation:** Debug on staging or synthetic inputs only.

## Failure Handling
- Cannot reproduce → State why, continue with labeled hypotheses only.
- Exploit still works after fix → Report failure, do not claim fix; continue investigation.
- Security audit tool unavailable → Manual code review, mark as "unverified."
- Cannot determine vulnerability type → Mark as "unclassified," recommend expert review.

## Completion Criteria
- Original security failure no longer reproducible (exploit blocked).
- Regression test protects the behavior (fails before, passes after).
- Security scan of affected files shows no new findings.
- Diff contains only justified security changes.
- No secret values in output.
