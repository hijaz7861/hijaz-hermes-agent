# Per-User GitHub Identity, Authorization, and Attribution

## Product requirement

HIJAZ Hermes is a multi-user product. Every person who installs or downloads it must connect their own GitHub account before Hermes can perform write operations in that person's name.

For every user-initiated GitHub mutation, GitHub must record the actual connected user as the actor. Hermes must not silently use the publisher's, maintainer's, developer's, or another tenant's credentials.

This is an identity and authorization requirement, not merely a commit-message or display-name setting.

## Required authentication model

Use a GitHub App with **user-to-server access tokens** for actions that must be attributed to the connected person.

GitHub documents that requests made with a GitHub App user access token are attributed to the user who authorized the app. GitHub's UI can show the user's avatar/name with an app identicon badge. Requests made with an installation access token are attributed to the app instead.

Official documentation:
- https://docs.github.com/en/apps/creating-github-apps/authenticating-with-a-github-app/authenticating-with-a-github-app-on-behalf-of-a-user
- https://docs.github.com/en/apps/creating-github-apps/authenticating-with-a-github-app/generating-a-user-access-token-for-a-github-app
- https://docs.github.com/en/apps/creating-github-apps/authenticating-with-a-github-app/authenticating-as-a-github-app-installation

### Device and browser authorization

Support both:
- GitHub App web authorization for users using the web interface.
- GitHub App device flow for CLI/headless/mobile onboarding, after the app owner enables Device Flow in the GitHub App registration.

Device flow is appropriate for Termux and headless CLI onboarding: Hermes displays GitHub's verification URL and one-time user code; the person completes authorization in their own browser. Hermes polls only according to GitHub's returned interval and stops on denial, expiry, or success.

Official documentation:
- https://docs.github.com/en/apps/maintaining-github-apps/modifying-a-github-app-registration
- https://docs.github.com/en/apps/creating-github-apps/writing-code-for-a-github-app/building-a-cli-with-a-github-app

## Onboarding and profile confirmation

After authorization, call GitHub's authenticated-user endpoint with that user's access token and show a confirmation screen before enabling write operations.

Show only fields returned and actually needed, for example:
- GitHub login/username
- Display name (when set)
- Avatar
- GitHub account ID (stable internal identifier)
- Profile URL
- Public bio, company, and location (optional display)
- Public email only when GitHub returns it and the user wants it displayed
- Selected account/repository installation and granted permissions

The person must see which GitHub account is connected and which repositories/permissions Hermes can use. Provide a clear account switch, disconnect/revoke, and reauthorization flow.

Do not interpret "show my account data" as permission to harvest or retain every available private profile field. Collect the minimum data needed for identity, permissions, and the requested operations. Do not request private email, organization membership details, private repository metadata, or other unrelated information unless a specific feature requires it and the user separately consents.

Never display, log, export, or commit access tokens, refresh tokens, private keys, or other credentials. Profile information and credentials must be stored separately.

## Per-user credential isolation

- Use a separate authorization record and credential vault entry for each GitHub user/account.
- Bind each task to the user who submitted it and the authorization that user selected.
- Resolve the user's token at the moment of each GitHub write operation.
- Never fall back to a global publisher/maintainer token if the user's token is missing, expired, revoked, or under-permissioned.
- If the user has not connected GitHub, allow public read-only research where appropriate, but block writes and offer account connection.
- If a token is revoked or authorization is removed, stop making requests for that user and require reconnection.
- For a shared server, encrypt credentials at rest, restrict service access, redact logs, and enforce tenant isolation. For a local/mobile installation, use the OS secure storage facility where available; do not store tokens in repository files, project logs, plaintext config committed to Git, or shell history.

## Required GitHub actor attribution

Use the connected user's user-to-server token for:
- Creating issues and comments
- Creating, editing, and submitting pull requests/reviews
- Creating branches and repository contents
- Pushing user-requested commits
- Merging pull requests when the user has permission and branch protections allow it
- Other write actions initiated on the user's behalf

A GitHub App installation token or a GitHub Actions bot token may be used only for explicitly identified app-owned/background automation where bot attribution is expected. It must not be used as a hidden fallback for user-requested actions.

For Git commits, set author and committer metadata consistently with the connected user's chosen Git identity. Use an email address verified and associated with that GitHub account, or the user's GitHub-provided noreply address when email privacy is enabled. Do not invent or copy another person's author identity. Git commit author/committer metadata is distinct from the authenticated API actor; verify both.

GitHub documentation:
- https://docs.github.com/en/account-and-profile/concepts/email-addresses
- https://docs.github.com/en/authentication/troubleshooting-commit-signature-verification/using-a-verified-email-address-in-your-gpg-key

## Permissions: least privilege

Configure the GitHub App with only the permissions required for enabled features. A typical optional permission map is:

| Feature | GitHub permission |
|---|---|
| Confirm connected identity | Authenticated user/profile access needed by the app |
| Read repository metadata | Metadata: read |
| Inspect source and create commits/branches | Contents: read/write |
| Read/create issues and comments | Issues: read/write |
| Create/update/review/merge pull requests | Pull requests: read/write |
| Modify workflow files or Actions | Not enabled by default; request only when explicitly needed |

The effective access is limited by both the app's granted permissions and the user's own access. A user token cannot grant rights the person does not have. Organization-owned repositories may also require the app to be installed/approved for that organization and the user to authorize the app.

## Token lifecycle

Prefer expiring user-to-server access tokens and refresh tokens. GitHub's current documentation states that expiring user access tokens last 8 hours by default and refresh tokens last 6 months. Refresh tokens rotate when used. Handle expiry/revocation explicitly and request reauthorization after refresh-token expiry.

Do not configure non-expiring tokens merely to make unattended work appear continuous. A task that loses authorization must pause safely and ask the same user to reconnect.

Official documentation:
- https://docs.github.com/en/apps/creating-github-apps/authenticating-with-a-github-app/refreshing-user-access-tokens
- https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/token-expiration-and-revocation

## Acceptance tests

1. User A connects GitHub account A; the connected profile screen shows A's GitHub login and stable account ID.
2. User B connects GitHub account B on the same server; user A cannot read or use B's credential or profile record.
3. User A asks Hermes to create an issue comment; GitHub records A as the actor (with the app badge where GitHub displays it).
4. User A asks Hermes to create a PR; GitHub records A as the author/creator actor.
5. User A asks Hermes to merge a PR; if authorized and branch protections pass, GitHub records A as the merger.
6. A commit pushed for A uses A's configured author/committer identity and an associated verified/noreply email; no unrelated publisher identity appears.
7. When A's token is expired, revoked, or under-permissioned, the operation pauses; it never switches to the product publisher's credentials.
8. If A disconnects GitHub, future write requests are blocked until A reconnects.
9. Logs and reports contain account identifiers and action outcomes as needed, but never tokens or private keys.
10. An operation explicitly run as the Hermes bot is clearly labelled as bot-owned and is never represented as the user's own action.

## Implementation order

1. Define the GitHub App registration and request only the minimum user/repository permissions.
2. Implement web and device-flow authorization, callback/state validation, and secure token storage.
3. Implement authenticated profile confirmation and per-user account selection.
4. Add a tenant-safe GitHub client that resolves only the task owner's user token.
5. Route GitHub writes through user-to-server authentication; separate bot-owned automation.
6. Set Git author/committer identity for local Git operations and verify commit attribution.
7. Add integration tests against a dedicated test repository and at least two test GitHub accounts.
8. Add disconnect, revocation webhook, expiry, refresh, and reauthorization tests.

## Non-negotiable rule

**Never fake attribution.** If GitHub cannot perform the requested operation as the connected user, Hermes must stop and explain that the action would appear under a bot or another identity. It must not proceed under a different account without the user's explicit choice.
