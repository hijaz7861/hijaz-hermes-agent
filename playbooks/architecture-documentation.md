# Playbook: Architecture Documentation

*Practical examples for the `architecture-documentation` skill*

---

## Scenario 1: Generate architecture docs for a new repo (happy path)

**Trigger:** "Document the architecture of this repository for onboarding."

**Invocation:**
```
Generate architecture documentation for the auth module.
Include: module overview, API reference, data flow, dependencies, entry points.
```

**Execution Log:**
```
## Architecture Documentation: src/auth/

### Codebase Map (codebase-intelligence)
- Entry points: src/auth/routes.ts (/auth/* endpoints)
- Modules: AuthService, SessionManager, TokenValidator, Middleware
- Dependencies: bcrypt, jsonwebtoken, express
- Data flow: request → middleware → validate → authenticate → session → response
- Trust boundaries: external input → validation → business logic → DB
- Risk areas: token handling, password comparison, session fixation

### Public Symbols Extracted (documentation-synthesizer)
| Symbol | Signature | Documented Before? |
|--------|-----------|-------------------|
| authenticate() | authenticate(creds): Promise<AuthResult> | No |
| logout() | logout(sessionId): Promise<void> | No |
| AuthService | class AuthService | Partially |
| SessionManager | class SessionManager | No |

### Generated Documentation
File: docs/auth-architecture.md
- Module overview with data flow diagram
- API reference: 14 symbol entries with signatures, params, returns, errors, examples
- 6 usage examples extracted from tests (real code, not invented)

### Coverage Report
- Documented before: 3 of 14 (21%)
- Documented after: 14 of 14 (100%)
- Stale docs: 0 contradictions found

Exit code: 0.
```

**Expected Output:**
Architecture markdown with module overview, API reference, data flow, coverage report, and list of files created.

---

## Scenario 2: Sync stale docs with code (happy path)

**Trigger:** "The README auth section is outdated. Sync it with current code."

**Invocation:**
```
Sync README.md authentication section with src/auth/ implementation.
Report contradictions found.
```

**Execution Log:**
```
## Documentation Sync: README.md vs src/auth/

### Contradictions Found
| Doc Statement | Code Reality | Severity |
|---------------|--------------|----------|
| "Uses JWT tokens" | Now uses opaque session tokens | HIGH |
| "Login endpoint: /auth/login" | Changed to /auth/session | HIGH |
| "Token expiry: 24 hours" | Now 1 hour (configurable) | MEDIUM |

### Reconciled Documentation
Updated README authentication section:
- Session-based auth (not JWT)
- Endpoint: /auth/session
- Configurable expiry (default 1 hour)

### Verification
- All doc statements cross-checked against code
- No contradictions remaining
- Examples verified against actual API

Exit code: 0 (contradictions found and resolved).
```

**Expected Output:**
Updated documentation section, staleness report listing contradictions resolved, verification that docs match code.

---

## Scenario 3: Dynamic behavior cannot be statically documented (safety case)

**Trigger:** "Document the plugin system — it uses dynamic imports at runtime."

**Invocation:**
```
Document the plugin system in src/plugins/. It dynamically loads modules.
```

**Execution Log:**
```
## Architecture Documentation: src/plugins/ (Dynamic System)

### Static API Documented
- registerPlugin(), getPlugin(), listPlugins() — documented with signatures
- Plugin interface: { name, version, setup, teardown }

### Limitation
Dynamic plugin discovery cannot be statically analyzed:
- Plugin names unknown until runtime
- Plugin behavior varies by installed plugins

### Generated Documentation
- Static API: fully documented (100% of static symbols)
- Dynamic loading: documented with caveats
- Note: "Individual plugin behavior must be documented manually per plugin"

### Status
- Documented: 4 static symbols
- Undocumented: N dynamic plugins (runtime-discovered)
- No invented plugin details

Exit code: 0 (documented static API, marked dynamic behavior as manual).
```

**Expected Output:**
Documentation for static API surface, clear marking of dynamic behavior requiring manual documentation, no invented details.
