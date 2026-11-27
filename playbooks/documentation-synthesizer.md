# Playbook: Documentation Synthesizer

*Practical examples for the `documentation-synthesizer` skill*

---

## Scenario 1: Generate API reference from code (happy path)

**Trigger:** "Generate API reference docs for the auth module in src/auth/."

**Invocation:**
```
Generate API reference documentation for src/auth/.
Output: markdown API reference with signatures, parameters, return types, examples.
Include coverage report of documented vs. undocumented symbols.
```

**Execution Log:**
```
## Documentation Synthesis: src/auth/

### Inventory
Public symbols found: 14
- Functions: authenticate(), logout(), refreshToken(), validateSession()
- Classes: AuthService, SessionManager, TokenValidator
- Types: User, Credentials, Token, AuthResult
- Constants: TOKEN_EXPIRY, MAX_LOGIN_ATTEMPTS

Existing docs: README.md (basic), no inline docstrings

### Extracted Contracts
| Symbol | Signature | Params | Returns | Errors | Documented Before? |
|--------|-----------|--------|---------|--------|--------------------|
| authenticate | authenticate(creds: Credentials): Promise<AuthResult> | creds | AuthResult | InvalidCredentials, RateLimited | No |
| logout | logout(sessionId: string): Promise<void> | sessionId | void | SessionNotFound | No |
| refreshToken | refreshToken(token: string): Promise<Token> | token | Token | InvalidToken, ExpiredToken | No |
| AuthService | class AuthService { ... } | — | — | — | Partially |

### Generated Documentation
File: docs/auth-api-reference.md
- 14 symbol entries with signatures, descriptions, parameters, return types, errors
- 6 usage examples extracted from tests/callers (real code, not invented)
- Module overview with data flow diagram

### Coverage Report
- Documented before: 3 of 14 (21%)
- Documented after: 14 of 14 (100%)
- Undocumented: 0
- Stale docs: 0 contradictions found

### Verification
- Example code checked against signatures — all match
- No invented behavior or parameters
- No secret values in output

Exit code: 0.
```

**Expected Output:**
Generated API reference markdown, coverage report, and list of files created/modified.

---

## Scenario 2: Sync stale docs with code (happy path)

**Trigger:** "The README's auth section is outdated — sync it with current code."

**Invocation:**
```
Sync README.md authentication section with src/auth/ implementation.
Report any contradictions found.
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
| "Supports OAuth2" | OAuth2 not yet implemented | MEDIUM |

### Reconciled README Section
Updated authentication section to match current code:
- Session-based auth (not JWT)
- Endpoint: /auth/session
- Configurable expiry (default 1 hour)
- OAuth2 removed from docs (not implemented)

### Verification
- All doc statements cross-checked against code
- No contradictions remaining
- Examples verified against actual API

Exit code: 0 (contradictions found and resolved).
```

**Expected Output:**
Updated README section, staleness report listing contradictions resolved, verification that docs match code.

---

## Scenario 3: Dynamic behavior cannot be documented (safety case)

**Trigger:** "Document the plugin system in src/plugins/ — it uses dynamic imports."

**Invocation:**
```
Document the plugin system in src/plugins/. It dynamically loads modules at runtime.
```

**Execution Log:**
```
## Documentation Synthesis: src/plugins/ (Dynamic System)

### Inventory
- Static exports: registerPlugin(), getPlugin(), listPlugins()
- Dynamic behavior: Plugins loaded via `import()` at runtime from plugins/ directory
- Plugin interface: { name, version, setup, teardown }

### Limitation
Dynamic plugin discovery cannot be fully statically analyzed:
- Plugin names unknown until runtime
- Plugin behavior varies by installed plugins
- No compile-time contract for individual plugins

### Generated Documentation
- Static API: registerPlugin, getPlugin, listPlugins documented
- Plugin interface contract documented
- Dynamic loading behavior documented (with caveats)
- Example: how to create and register a plugin

### Status
- Documented: 4 static symbols (100% of static API)
- Undocumented: N dynamic plugins (runtime-discovered)
- Note: "Dynamic plugin behavior must be documented manually per plugin"

Exit code: 0 (documented static API, marked dynamic behavior as manual).
```

**Expected Output:**
Documentation for static API surface, clear marking of dynamic behavior that requires manual documentation, no invented plugin details.
