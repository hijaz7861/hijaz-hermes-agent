# Playbook: Multi-Agent Review

*Practical examples for the `multi-agent-review` skill*

---

## Scenario 1: Security-Critical PR Review

**Trigger:** "Review PR #445 — new OAuth2 provider with token exchange."

**Invocation:**
```
Coordinate independent review of PR #445 (OAuth2 provider):
- Coordinator: define scope, delegate, integrate
- Implementer: already did the work (PR author)
- Reviewer: security-focused code review
- Test Analyst: design security test cases
```

**Execution Log:**
```
## Multi-Agent Review: PR #445 - OAuth2 Provider

### Scope Definition (Coordinator)
```
Files in scope:
- src/modules/auth/oauth2/ (new directory)
  - provider.ts — provider abstraction
  - google.ts — Google implementation
  - github.ts — GitHub implementation
  - token-exchange.ts — RFC 8693 implementation
  - routes.ts — /auth/oauth2/* endpoints
- tests/unit/auth/oauth2/ (new)
- tests/integration/auth/oauth2/ (new)

Acceptance criteria:
1. Implements RFC 6749 + RFC 8693 correctly
2. No token leakage in logs/errors
3. PKCE enforced for public clients
4. State parameter validated (CSRF)
5. Token exchange: subject token validation
6. Rate limiting on token endpoints
```

### Role Execution

#### Reviewer (Security Focus)
**Findings:**
| ID | File | Line | Severity | Finding |
|----|------|------|----------|---------|
| SEC-001 | token-exchange.ts | 67 | **CRITICAL** | Subject token not validated for audience — allows token replay across services |
| SEC-002 | provider.ts | 45 | HIGH | `client_secret` logged in error stack trace |
| SEC-003 | google.ts | 23 | MEDIUM | No `nonce` validation for OIDC ID tokens |
| SEC-004 | routes.ts | 89 | LOW | Missing `Cache-Control: no-store` on token endpoint |

**Evidence for SEC-001:**
```typescript
// token-exchange.ts:67 — CURRENT (vulnerable)
async function exchangeToken(req: TokenExchangeRequest) {
  const subjectToken = await validateToken(req.subject_token); // Only validates signature
  // MISSING: Check subjectToken.aud === THIS_SERVICE
  return issueActorToken(subjectToken.sub, req.requested_token_type);
}
```

#### Test Analyst
**Test Cases Designed:**
| ID | Scenario | Type | Priority |
|----|----------|------|----------|
| TEST-001 | Token exchange with wrong audience rejected | Integration | CRITICAL |
| TEST-002 | PKCE challenge required for public client | Unit | HIGH |
| TEST-003 | State parameter mismatch returns 400 | Integration | HIGH |
| TEST-004 | Client secret never appears in logs | Unit | HIGH |
| TEST-005 | Rate limit: 10 req/min per IP on /token | Integration | MEDIUM |
| TEST-006 | Refresh token rotation enforced | Integration | MEDIUM |
| TEST-007 | ID token nonce validated when present | Unit | MEDIUM |

#### Implementer Response
**Fixes Applied:**
```diff
--- src/modules/auth/oauth2/token-exchange.ts
+++ src/modules/auth/oauth2/token-exchange.ts
@@ -64,7 +64,12 @@ export async function exchangeToken(req: TokenExchangeRequest) {
   const subjectToken = await validateToken(req.subject_token);
+  // SEC-001: Validate audience
+  if (subjectToken.aud !== config.serviceAudience) {
+    throw new OAuthError('invalid_token', 'Token audience mismatch');
+  }
   return issueActorToken(subjectToken.sub, req.requested_token_type);
 }
```

```diff
--- src/modules/auth/oauth2/provider.ts
+++ src/modules/auth/oauth2/provider.ts
@@ -42,7 +42,7 @@ export async function exchangeCodeForTokens(code: string, client: Client) {
   try {
     return await provider.tokenEndpoint(code, client);
   } catch (err) {
-    logger.error({ err, clientSecret: client.secret }, 'Token exchange failed');
+    logger.error({ err, clientId: client.id }, 'Token exchange failed');
     throw err;
   }
 }
```

### Re-Review (Reviewer)
**Verification:**
- SEC-001: ✅ Fixed — audience validated
- SEC-002: ✅ Fixed — secret removed from logs
- SEC-003: ✅ Fixed — nonce validation added in google.ts:31
- SEC-004: ✅ Fixed — headers added in routes.ts:92

### Test Execution (Test Analyst)
```
$ pnpm test tests/integration/auth/oauth2/token-exchange.test.ts
✓ TEST-001: Wrong audience rejected (400)
✓ TEST-002: PKCE required for public client
✓ TEST-003: State mismatch returns 400
✓ TEST-005: Rate limit enforced

$ pnpm test tests/unit/auth/oauth2/
✓ TEST-004: No secrets in logs (log output asserted)
✓ TEST-006: Refresh rotation verified
✓ TEST-007: Nonce validation works

All 7 security tests: ✅ PASS
```

### Coordinator Integration
**Final Report:**
- **Critical findings:** 1 (SEC-001) — **RESOLVED**
- **High findings:** 1 (SEC-002) — **RESOLVED**
- **Medium findings:** 2 (SEC-003, SEC-004) — **RESOLVED**
- **Tests added:** 7 security-focused tests
- **Code changes:** 4 files, 23 lines added/changed
- **Verdict:** ✅ APPROVED FOR MERGE

### Audit Trail
```
2026-11-24T10:15:00Z Coordinator: Scope defined, roles assigned
2026-11-24T10:18:00Z Reviewer: SEC-001..004 reported
2026-11-24T10:22:00Z Test Analyst: TEST-001..007 designed
2026-11-24T10:35:00Z Implementer: Fixes pushed to PR branch
2026-11-24T10:40:00Z Reviewer: Re-review, all findings resolved
2026-11-24T10:42:00Z Test Analyst: All 7 tests pass
2026-11-24T10:45:00Z Coordinator: Final report, merge approved
```
```

---

## Scenario 2: Cross-Module Refactoring Review

**Trigger:** "Review the shared config refactor — touches 12 modules."

**Invocation:**
```
Review PR #567 (config: centralized Zod schema, removes 47 duplicate validations):
- Coordinator: manage scope across modules
- Reviewer: correctness, backward compatibility
- Test Analyst: migration tests, config validation
```

**Execution Log:**
```
## Multi-Agent Review: PR #567 - Shared Config Refactor

### Scope (Coordinator)
```
Affected modules (12): auth, users, billing, teams, notifications, 
  webhooks, admin, audit, search, storage, email, scheduler

Changes:
- NEW: src/shared/config/schema.ts (Zod schema, 180 lines)
- NEW: src/shared/config/loader.ts (typed config access)
- REMOVED: 47 inline Zod schemas across modules
- CHANGED: All modules import from @shared/config
- MIGRATION: Config keys renamed (e.g., DB_URL → DATABASE_URL)
```

### Reviewer Findings
| ID | Module | Severity | Finding |
|----|--------|----------|---------|
| REF-001 | billing | **HIGH** | `STRIPE_WEBHOOK_SECRET` marked optional but required at runtime |
| REF-002 | auth | MEDIUM | `JWT_SECRET` min length 32 not enforced (was 64) |
| REF-003 | scheduler | MEDIUM | `CRON_TZ` default 'UTC' — breaks existing 'America/New_York' deployments |
| REF-004 | All | LOW | No deprecation warnings for renamed keys |

### Test Analyst: Migration Tests
```typescript
// tests/integration/config/migration.test.ts
test('old key names still work with deprecation warning', () => {
  process.env.DB_URL = 'postgres://...';
  delete process.env.DATABASE_URL;
  
  const config = loadConfig();
  expect(config.database.url).toBe('postgres://...');
  expect(warnings).toContain('DB_URL deprecated, use DATABASE_URL');
});

test('required keys enforced per module', () => {
  // billing requires STRIPE_WEBHOOK_SECRET
  delete process.env.STRIPE_WEBHOOK_SECRET;
  expect(() => loadConfig({ module: 'billing' }))
    .toThrow('STRIPE_WEBHOOK_SECRET required for billing');
});
```

### Resolution
- REF-001: ✅ Made required in schema, added module-specific validation
- REF-002: ✅ Min 64 enforced, added migration guide
- REF-003: ✅ Default removed, now required with docs
- REF-004: ✅ Deprecation warnings added for 6 renamed keys

### Verdict: ✅ APPROVED WITH CONDITIONS
- Condition: Deploy with feature flag, monitor for 48h
- Condition: Run migration script in staging first
```

---

## Scenario 3: AI-Generated Code Review

**Trigger:** "Review the AI-written GraphQL resolver for user search."

**Invocation:**
```
Review AI-generated GraphQL resolver (model: gpt-4o):
- File: src/modules/users/resolvers/search.ts
- Review for: N+1, authorization, injection, performance
- Test Analyst: load test, edge cases
```

**Execution Log:**
```
## Multi-Agent Review: AI-Generated GraphQL Resolver

### Reviewer Findings (Static Analysis)
| ID | Line | Severity | Finding |
|----|------|----------|---------|
| AI-001 | 34 | **CRITICAL** | Direct string interpolation in SQL — `WHERE name LIKE '%${query}%'` |
| AI-002 | 41 | HIGH | No pagination — `limit` defaults to 1000 |
| AI-003 | 28 | HIGH | No authorization check — returns all users |
| AI-004 | 47 | MEDIUM | No rate limiting on search endpoint |
| AI-005 | 52 | LOW | `console.log` left in production code |

### Test Analyst: Attack Tests
```typescript
test('SQL injection via search query', async () => {
  const malicious = "'; DROP TABLE users; --";
  const result = await executeSearch(malicious);
  expect(result.errors).toBeDefined(); // Should reject, not execute
  expect(await userCount()).toBeGreaterThan(0); // Table intact
});

test('authorization: user sees only own org', async () => {
  const orgA = await createOrg();
  const orgB = await createOrg();
  const userA = await createUser({ org: orgA });
  const userB = await createUser({ org: orgB });
  
  const results = await searchAs(userA, '*');
  expect(results.every(u => u.orgId === orgA.id)).toBe(true);
});

test('pagination enforced', async () => {
  await createUsers(5000);
  const results = await searchAs(admin, '*', { limit: 100 });
  expect(results.length).toBeLessThanOrEqual(100);
});
```

### Resolution
- AI-001: ✅ Rewritten with parameterized query (Prisma `contains`)
- AI-002: ✅ Max limit 50, default 20, cursor pagination
- AI-003: ✅ Added `requirePermission('users:read')` guard
- AI-004: ✅ Rate limited: 30 req/min per user
- AI-005: ✅ Removed debug log

### Verdict: ⚠️ REQUIRED SIGNIFICANT REWORK
AI code had critical vulnerabilities. After fixes: ✅ APPROVED
```

---

## Tips for Effective Use

1. **Define scope upfront** — File list, acceptance criteria
2. **Separate roles clearly** — No implementer reviews own code
3. **Require evidence** — Line numbers, reproduction, test cases
4. **Track all findings** — Severity, status, resolution
5. **Coordinator owns the verdict** — Not consensus