# Playbook: Codebase Intelligence

*Practical examples for the `codebase-intelligence` skill*

---

## Scenario 1: New Repository Onboarding

**Trigger:** "I just cloned this repo. Help me understand it."

**Invocation:**
```
Map this repository. Identify:
- Primary language, framework, build system
- Entry points (CLI, HTTP server, tests)
- Architecture pattern (layered, modular, microkernel)
- Key dependencies and their versions
- Test strategy and how to run them
```

**Expected Output:**
```
## Repository Map: acme-api (v2.3.1)

### Basics
- Language: TypeScript 5.2 (Node 20 LTS)
- Package Manager: pnpm 9.1 (lockfile v6)
- Build: tsc + esbuild (scripts: build, dev, test)
- Lint: eslint + prettier (husky pre-commit)

### Structure
src/
├── main.ts              # HTTP server entry (Fastify)
├── modules/
│   ├── auth/            # JWT + OAuth2 (self-contained)
│   ├── users/           # CRUD + profile
│   └── billing/         # Stripe integration
├── shared/
│   ├── db/              # Prisma client + migrations
│   ├── config/          # Zod-validated env schema
│   └── errors/          # AppError hierarchy
└── tests/
    ├── unit/            # Vitest (fast, isolated)
    ├── integration/     # Testcontainers (Postgres, Redis)
    └── e2e/             # Playwright (critical paths only)

### Entry Points
- `pnpm dev` → tsx watch src/main.ts (port 3000)
- `pnpm test` → vitest run (unit + integration)
- `pnpm test:e2e` → playwright (requires running dev server)

### Risk Areas
1. `billing/` — external Stripe calls, webhook verification, idempotency keys
2. `auth/tokens.ts` — JWT signing key rotation not implemented
3. `shared/db/migrations/` — 47 migrations, no down scripts
4. `modules/users/avatar.ts` — S3 upload, no size validation

### Test Baseline
```
$ pnpm test
✓ 234 passed (unit: 187, integration: 47)
✗ 0 failed
Duration: 12.3s
```

### Unknowns
- No documented deployment process (Dockerfile exists but untested)
- Rate limiting middleware present but config unclear
- Observability: logs only, no metrics/tracing
```

---

## Scenario 2: Feature Trace

**Trigger:** "Where is the password reset flow implemented?"

**Invocation:**
```
Trace the password reset feature end-to-end:
- HTTP route and handler
- Token generation, storage, validation
- Email sending integration
- Frontend touchpoints (if in repo)
- Database schema changes
- Tests covering this flow
```

**Expected Output:**
```
## Feature Trace: Password Reset

### Request Flow
```
POST /api/auth/password/reset-request
  → modules/auth/routes.ts:42 (resetRequestHandler)
  → modules/auth/service.ts:118 (initiateReset)
  → shared/db/prisma.ts (user lookup by email)
  → modules/auth/tokens.ts:67 (generateResetToken)
  → modules/auth/email.ts:23 (sendResetEmail)
  → modules/auth/tokens.ts:89 (storeTokenHash)
```

### Key Files
| File | Role | Lines |
|------|------|-------|
| `src/modules/auth/routes.ts` | Route definitions | 40-55 |
| `src/modules/auth/service.ts` | Business logic | 110-145 |
| `src/modules/auth/tokens.ts` | Token crypto + storage | 60-110 |
| `src/modules/auth/email.ts` | Email template + send | 20-45 |
| `prisma/schema.prisma` | User model + ResetToken | 78-95 |

### Token Lifecycle
1. `generateResetToken()` → 32-byte random, SHA-256 stored
2. Expires in 1 hour (config: `RESET_TOKEN_TTL_HOURS`)
3. Single-use: deleted on successful reset
4. Rate limited: 3 requests/hour per email (Redis)

### Tests
- `tests/unit/auth/tokens.test.ts` — crypto, expiry, hashing
- `tests/integration/auth/password-reset.test.ts` — full flow with test DB
- `tests/e2e/auth/password-reset.spec.ts` — browser flow (happy path only)

### Gaps
- No test for expired token rejection
- No test for already-used token rejection
- Email template not tested (snapshot missing)
- Frontend reset page not in this repo (separate `acme-web`)
```

---

## Scenario 3: Risk Assessment Before Refactor

**Trigger:** "We want to replace Prisma with Drizzle. What breaks?"

**Invocation:**
```
Assess impact of replacing Prisma ORM with Drizzle:
- All files importing Prisma client
- Raw SQL usage
- Migration strategy
- Test dependencies on Prisma
- Type safety implications
```

**Expected Output:**
```
## Impact Assessment: Prisma → Drizzle

### Direct Imports (47 files)
```
grep -r "from '@prisma/client'" --include="*.ts"
```
| Category | Count | Examples |
|----------|-------|----------|
| Service modules | 23 | `auth/service.ts`, `billing/service.ts` |
| Repository/DAO | 12 | `users/repo.ts`, `teams/repo.ts` |
| Scripts/CLI | 5 | `scripts/seed.ts`, `scripts/backfill.ts` |
| Tests | 7 | `tests/integration/**/*.ts` |

### Prisma-Specific Patterns
| Pattern | Occurrences | Migration Effort |
|---------|-------------|------------------|
| `prisma.$transaction` | 18 | Medium (Drizzle has tx) |
| `prisma.user.findUnique` | 67 | Low (direct mapping) |
| `include: { posts: true }` | 34 | Medium (Drizzle relations) |
| Raw `$queryRaw` | 3 | High (verify SQL) |
| Middleware/extensions | 2 | High (reimplement) |

### Schema & Migrations
- 47 migration files → need replay or baseline migration
- Enum types: 4 (Role, SubscriptionStatus, ...) → Drizzle enums
- Composite indexes: 12 → verify in Drizzle schema
- Row-level security: 3 policies → raw SQL in Drizzle

### Type Safety
- Prisma generates types from schema → Drizzle infers from schema
- `Prisma.UserGetPayload<{ include: ... }>` → manual or `infer`
- Nullable fields: Prisma hides in select, Drizzle exposes

### Test Impact
- 7 integration test files use `prisma` fixture
- `tests/helpers/prisma.ts` — test DB setup/teardown
- Seed script used by E2E tests

### Recommendation
1. **Phase 1:** Add Drizzle alongside Prisma, dual-write in new code
2. **Phase 2:** Migrate read-heavy modules first (users, teams)
3. **Phase 3:** Migrate transaction-heavy modules (billing, auth)
4. **Phase 4:** Remove Prisma, drop migrations, update CI
5. **Estimated effort:** 3-5 engineer-weeks

### Blockers
- No Drizzle expertise on team
- Billing module has complex transactions — high risk
- CI/CD runs Prisma migrate in staging — needs coordination
```

---

## Scenario 4: Security Audit Prep

**Trigger:** "Security team needs a map of all auth boundaries."

**Invocation:**
```
Identify all authentication and authorization boundaries:
- Public vs protected routes
- Token validation points
- Permission checks
- Service-to-service auth
- External API auth
```

**Expected Output:**
```
## Auth Boundaries Map

### HTTP Routes (Fastify)
| Route Pattern | Auth Required | Auth Method | Permissions |
|---------------|---------------|-------------|-------------|
| GET /health | ❌ | — | — |
| POST /api/auth/login | ❌ | — | — |
| POST /api/auth/register | ❌ | — | — |
| POST /api/auth/refresh | ❌ | Refresh token | — |
| * /api/auth/* | ✅ | JWT Bearer | — |
| * /api/users/me/* | ✅ | JWT Bearer | owner |
| * /api/users/:id/* | ✅ | JWT Bearer | admin OR owner |
| * /api/billing/* | ✅ | JWT Bearer | subscription:active |
| * /api/admin/* | ✅ | JWT Bearer | role:admin |

### Token Validation
- `src/shared/auth/validate.ts:15` — single entry point
- Verifies: signature, expiry, issuer, audience
- Revocation: Redis blocklist (logout, password change)
- JWKS rotation: not implemented (static HS256)

### Permission Checks
- `src/shared/auth/guard.ts` — Fastify preHandler hook
- Role-based: `requireRole('admin')`
- Resource-based: `requireOwnership('user', params.id)`
- Subscription-gated: `requireSubscription('pro')`

### Service-to-Service
- Internal API: `X-Internal-Token` header (static, rotate quarterly)
- Webhook callbacks: Stripe signature verification
- No mTLS, no SPIFFE

### External APIs
| Service | Auth Type | Credential Location |
|---------|-----------|---------------------|
| Stripe | Secret key | `STRIPE_SECRET_KEY` env |
| SendGrid | API key | `SENDGRID_API_KEY` env |
| S3 | IAM role | EC2 instance profile |
| Redis | Password | `REDIS_PASSWORD` env |

### Gaps for Security Review
1. No audit logging for auth decisions
2. JWT uses HS256 (symmetric) — prefer RS256
3. Internal token is static, long-lived
4. No device fingerprinting / anomaly detection
5. Password reset token stored as SHA-256 (no pepper)
```

---

## Tips for Effective Use

1. **Be specific** — "Map the billing module" > "Map the repo"
2. **Provide context** — Share error messages, issue links, goals
3. **Ask for evidence** — "Cite file paths and line numbers"
4. **Define scope** — Limit to module, feature, or layer
5. **Request baselines** — Always ask for test/lint/build status