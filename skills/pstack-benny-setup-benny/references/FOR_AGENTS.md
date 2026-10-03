# Benny workflow intent for Hermes

The user wants two bounded workflows that share one immutable report identity.

## Triage

Read the full source report and attachments, classify bug/performance/feature/question/reroute, trace the likely owning layer before routing, dedupe in the configured tracker, enrich a confident duplicate only when allowed, and create only a clearly broken net-new report in a separate tracker with approved compensation. A GitHub source issue already in the target tracker is not a new-ticket candidate. With posting authority, produce one concise source-parent verdict ending in one `[benny:bug]`, `[benny:performance]`, or `[benny:other]` marker; optional `tracker=<URL>`. Otherwise return a local draft.

## Reproduce and optionally fix

After a trusted configured bug/performance verdict, stop for human fix ownership or switch to verify mode for an existing PR/commit. Use the completed user-facing feature map and verified control adapter to reproduce the exact symptom twice through real UI interaction, record screenshot/video and a read-only state cross-check, then review whether evidence shows the discriminating final state. No repro means no authored fix. A separately approved bounded fix needs runtime root-cause evidence and twice-repeated patched proof plus tests/blast-radius smoke. A draft PR needs independent commit/push/publication approval. Never merge or deploy.

## Shared constraints

- Freeze source identity before work and preflight immediately before writes.
- GitHub: exact configured repository, issue number, canonical URL, triage login. Slack: exact configured channel/root timestamp/triage identity; no root/fallback/cross-channel messages.
- Utility bots are evidence, not fix ownership.
- The coordinator owns all approved source/tracker/PR writes. Workers return findings only, get no credentials/posting permission, and cannot redelegate or clarify. If isolation is not proven, use the coordinator rather than prompt-only safety promises.
- Keep user config/feature/routing maps outside installed skill files, preserve local edits, and keep secrets only in secure local environment/secret managers.
- Fail closed for missing source coordinates, tracker operations/compensation, control adapter, map, recorder, or trusted marker.
- Native operational skills are `pstack-benny-triage-issue-reports` and `pstack-benny-reproduce-and-fix-issues`; dependencies are `pstack-how`, `pstack-why`, `pstack-tdd`, `pstack-unslop`, and the cited native principle skills.

## Setup boundary

Ask for missing configuration only in an interactive parent session. A delegated child returns gaps to its parent. Setup is proposal/manual-first; optional jobs/routes require a separate confirmed request and current Hermes CLI/docs. Do not use Cursor `/automate`, `.cursor/settings.json`, direct cloud APIs, or editor deep links. Do not install or schedule this pack automatically. Read back each exact authorized external target before claiming success.

See `templates/configuration.example.yaml` in the setup skill and the operational skills' feature/routing examples. This file is intent, not credentials or blanket action authority.
