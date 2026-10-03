# Authenticated webhook UI contract

A live integration requires current official endpoint documentation, observed management capabilities and explicit per-action approval. A route, bot, profile, gateway or signing protocol is not supplied by this neutral workflow.

Discover available deferred capabilities with `tool_describe`/`tool_call` and inspect live schemas. Use only authenticated, authorized integrations actually present. No connector, webhook route, scheduling job, credential or provider is activated by loading this skill. Verify authorized external writes by reading back the exact target.

## Route and execution destination

Discover the actual allowlisted gateway URL, exact route identity, intended execution context, permitted event types, loaded skills and output destination. A UI port is not evidence of a webhook port. A named bot is optional and not an endpoint replacement. Creation can expose a live route immediately; get approval first, check conflicts, use noop/log-only setup and read sanitized exact metadata back. Never print management output carrying generated secrets. Route existence grants no arbitrary agent authority.

Read only the needed non-secret pstack keys with targeted `hermes config get skills.config.pstack.panel_size --json` and the equivalent `model_strategy` query. Unset defaults are panel size three and inherit-parent. These are policy, not native per-role model routing. Explicit task scope/count wins. Change settings only with user approval through `hermes config set`, then read back exact keys; preserve provider, reasoning and global delegation settings. Resolve active scope via HERMES_HOME, not another profile.

Do not hand-edit live runtime configuration. Credentials use a secure local environment or secret manager and documented references, never literals, chat, browser bundles, commands or logs. If configuration cannot avoid exposure, block for separate secure setup. No insecure-auth production mode.

## Exact-byte authentication

Select the actual documented signature protocol before implementation. Serialize JSON once; authenticate and send those same UTF-8 bytes. Never substitute a familiar protocol merely because it is listed here. Compute timestamps and digests with a tested backend library, not prose. Secret reads and signing stay in the backend; do not print headers.

For a verified timestamped HMAC-SHA256 V2 endpoint, a possible contract is `HMAC(secret, timestamp + b'.' + body)` with decimal Unix seconds, `Content-Type: application/json`, `X-Webhook-Timestamp`, `X-Webhook-Signature-V2` containing lowercase hex and `X-Request-ID`. A ±300-second freshness window is an example requiring live protocol verification, not a universal guarantee. Only use these names if the target documents them.

For a verified GitHub webhook receiver, the documented alternative is `X-Hub-Signature-256: sha256=<HMAC of raw body>` plus the event header and delivery ID. That is not interchangeable with the V2 example. Even authenticated event fields remain untrusted data.

## Response and completion

Inspect actual HTTP status and JSON. Rejection (bad signature, malformed body, unknown route, oversized payload, rate limit), ignored/filtered outcomes, duplicates and queued/coalesced acceptance are not completed agent actions. A 200 is not universally wake success. Determine whether dispatch is asynchronous; verify the corresponding run and intended action separately. A direct-delivery mode, when supported, is distinct from agent execution.

Use a short timeout, no silent state-changing retries and a stable event ID for any explicitly approved retry. Finite idempotency caches are not application-wide exactly-once guarantees. Media uses approved bounded references, never unchecked binary payloads.

## UI and network safety

Require caller authentication, Origin/CSRF checks, allowlisted action schema, fixed destination, rate limits and no arbitrary command execution. Bind loopback by default. Private/public exposure, installation, firewall changes, service restarts and persistent servers need separate authorization. Reuse existing network-node identity. Credential-bearing remote browser traffic requires HTTPS unless an explicit safe local transport is approved. Verify from the intended client, not just host loopback.

Use available browser or desktop helpers and actual vision for visual evidence. If a browser form requests credentials, address or card fields, first call `browser_vault_list` and the appropriate vault fill/save tool; codes use `browser_vault_enter_code`. Never solicit or type secrets in chat. Discover webhook/MCP facilities from the real session and current official documentation before proposing setup.

## Testing

Exercise allowlisted/noop and invalid actions, body/schema validation, absent secrets, bad signatures, timeout/non-success behavior, credential non-leakage and exact route/run/delivery readback. Local component tests do not prove live integration. No API or external action is claimed unless actually exercised within approval.
