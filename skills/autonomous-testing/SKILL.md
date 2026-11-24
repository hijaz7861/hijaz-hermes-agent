---
name: autonomous-testing
description: Design and execute risk-based tests for software changes, then report reproducible evidence. Use before merging, releasing, debugging regressions or validating agent-generated code.
---

# Autonomous Testing

## Objective
Demonstrate that a change meets acceptance criteria and does not introduce unacceptable regressions.

## Procedure
1. Read repository instructions and identify the project's official test commands.
2. Establish baseline status. Preserve user changes and note pre-existing failures.
3. Convert acceptance criteria into observable test cases.
4. Prioritize by risk:
   - Critical paths and security boundaries
   - Regression tests for the reported defect
   - Unit tests for changed logic
   - Integration/API/database tests for affected boundaries
   - End-to-end tests for essential user journeys
   - Lint, type checks, build and packaging
5. Include negative and boundary cases: invalid input, missing permissions, empty data, duplicates, timeouts, retries and partial failures where relevant.
6. Use isolated test data and disposable environments. Never run destructive tests against production.
7. Execute checks in increasing cost order. Capture exact commands, exit codes and concise output.
8. Investigate failures; do not weaken assertions, skip tests or alter production behavior just to make the suite pass.
9. Inspect coverage gaps and the final diff.
10. Report passed, failed, blocked and not-run checks separately.

## Evidence format
For each check record:
- Command or test identifier
- Environment/runtime version when relevant
- Exit status
- Result summary
- Known limitation

## Release gate
Do not recommend release when a critical test fails, security-sensitive behavior is unverified, migrations are unsafe, or the tested artifact differs from the proposed release artifact. Human approval remains required for production deployment unless explicitly and safely delegated.

## Completion criteria
Acceptance criteria have corresponding evidence, relevant regression checks pass, failures and limitations are disclosed, and no production data was endangered.
