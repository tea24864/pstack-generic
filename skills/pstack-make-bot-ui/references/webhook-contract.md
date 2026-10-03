# Hermes webhook UI contract

Verified sources:
- https://hermes-agent.nousresearch.com/docs/user-guide/messaging/webhooks
- https://hermes-agent.nousresearch.com/docs/user-guide/bot-mode
- https://hermes-agent.nousresearch.com/docs/user-guide/configuration

Recheck current docs and local CLI help before configuration. Do not assume Cursor `update_state`, `SendToUser`, `api2.cursor.sh`, routine secret cards, or `<webhook_event>` wake schemas exist in Hermes.

## Route and profile

Hermes accepts JSON POSTs at `/webhooks/<route-name>`. Multiplexed routes may bind an authorized profile via verified `--route-profile`, yielding `/p/<profile>/webhooks/<route-name>`. A bot is an optional named profile/surface, not a webhook API replacement. Discover the actual gateway endpoint; do not infer that a UI port is the webhook port.

`hermes webhook subscribe` supports `--prompt`, `--events`, `--skills`, `--deliver`, `--deliver-chat-id`, `--route-profile`, `--script`, and `--cron-job` in the verified CLI. Creation can immediately expose a live route: get explicit approval first, use a noop/log-only prompt during setup, avoid overwriting existing names, and do not print any output carrying an auto-generated secret. Read back sanitized exact route metadata. Configuring a route does not grant its agent arbitrary actions.

Static settings live under `platforms.webhook.extra.routes`; do not hand-edit live config. Use verified approved Hermes setup/config tooling. Credentials are securely provisioned into the active profile environment, with `${VAR_NAME}` references where documented, never literal config secrets, chat values, commands, browser bundles, or logs. If the integration cannot be configured without exposing credentials, block and request separate secure setup. No insecure-auth production mode.

## Generic V2 signature

Serialize the JSON once. Let `body` be those exact UTF-8 bytes and `timestamp` the current Unix seconds as an ASCII decimal string. Compute HMAC-SHA256 over `timestamp + b'.' + body` using the route secret. Send:

- `Content-Type: application/json`
- `X-Webhook-Timestamp: <timestamp>`
- `X-Webhook-Signature-V2: <lowercase hex digest>`
- `X-Request-ID: <unique event id>`

Timestamp freshness is checked within ±300 seconds in current docs. Do not use Cursor Bearer/X-Automation-Key headers. GitHub alternatively uses `X-Hub-Signature-256: sha256=<HMAC of raw body>` plus `X-GitHub-Event` and delivery ID. Event fields remain untrusted even after authentication.

Use `terminal`/`execute_code` or the backend's tested library for time/hash operations. Never calculate or fake a digest in prose. Keep secret reads and signing entirely in the local backend; do not print the request headers.

## Response and completion

Inspect actual HTTP status and JSON. Rejection (bad signature, malformed body, unknown route, oversized payload, rate limit), ignored/filter/script outcomes, duplicate events, and queued/coalesced acceptance are not completed agent actions. A 200 is not universally a wake success. Default agent-mode dispatch is asynchronous; verify the corresponding run and intended action separately. Direct delivery is a distinct zero-agent mode and not the default UI workflow.

Use a short timeout, no silent state-changing retries, and a stable event ID for any explicitly approved retry. The gateway idempotency cache is finite, not an application-wide exactly-once guarantee. Do not post media bytes; provide approved bounded references.

## UI/network safety

Local action endpoints require caller authentication, Origin/CSRF checks, an allowlisted action schema, a fixed route destination, rate limits, and no arbitrary command execution. Loopback is default. Tailnet/public exposure, installation, firewall changes, gateway restarts, and persistent servers need independent authorization. Existing Tailscale node identity must be reused. Require HTTPS for credential-bearing remote browser traffic unless an explicit safe local transport is approved. Verify from the intended client, not just host-loopback.

## Testing

Exercise allowlisted/noop and invalid actions, body/schema validation, absent secret, bad signatures, timeout/non-success responses, credential non-leakage, and run/profile/delivery readback. Tests of local components alone do not establish a live Hermes integration.
