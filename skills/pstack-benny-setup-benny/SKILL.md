---
name: pstack-benny-setup-benny
description: "Prepare optional safe Benny issue workflows."
license: MIT
metadata:
  author: "Lauren Tan (poteto), tea24864"
  version: "0.2.0"
  source-revision: "23e4138daa01c42d4969f7a5465f82704e64f798"
---

# Set up Benny

## When to Use

Use only for an explicit request to prepare or change Benny configuration. Manual GitHub issue intake is the safe initial workflow.

## Prerequisites

Use only capabilities and credentials actually available in this session. Invoking this workflow does not authorize publication, merges, destructive cleanup, dependency installation, or configuration changes. Preserve the caller's scope and user-owned state.

## Procedure

Benny is optional, manual-first and dormant until explicitly configured. These are authored workflows, not active automations. Setup grants no tracker writes, source posts, draft PRs, jobs, hooks, deployment or deletion authority.

1. Read `references/README.md`, `references/FOR_AGENTS.md` and `references/integration-contract.md`. Confirm repository, intended execution context, available skill versions, intended source (GitHub issue by default; Slack only through a verified adapter) and exact authorized write policy. Do not install or activate anything.

Load named skills with `skill_view(name="pstack-...")`; load supporting material with the same skill name and `file_path="references/..."`. Resolve all paths to the actual loaded skill directory. Do not invent missing skills or assume another profile shares the same catalog.
2. Verify `pstack-how`, `pstack-why`, `pstack-tdd`, `pstack-unslop`, the listed principle dependencies, and both native Benny operational skills in the actual execution profile. Fresh jobs must resolve these names; current-session loading alone does not prove that. Missing dependencies block activation.
3. Copy `templates/configuration.example.yaml` into an approved user-owned location outside installed skill files, for example `.benny/configuration.yaml` in the target project. Preserve destination-only files and conflicts with local edits. Never overwrite existing user config. Copy the feature/routing examples into user-owned files. Fill every placeholder, including safe environment, stable account/data markers, screenshot/recording capability, budgets, trusted triage identity, marker strings, source coordinates and retention. Secrets remain environment/secret-manager references; forms use the approved secure-entry channel.

Use `read_file`, `search_files`, `write_file` and `patch` for file work; use `terminal(command="...", timeout=...)` for real Git, helpers and tests. Read existing files before full replacement. Bundle mechanical loops through `execute_code` when appropriate. Use actual tool output as evidence.

Read only the needed non-secret pstack keys with targeted `hermes config get skills.config.pstack.panel_size --json` and the equivalent `model_strategy` query. Unset defaults are panel size three and inherit-parent. These are policy, not native per-role model routing. Explicit task scope/count wins. Change settings only with user approval through `hermes config set`, then read back exact keys; preserve provider, reasoning and global delegation settings. Resolve active scope via HERMES_HOME, not another profile.
4. GitHub intake uses an already authenticated verified source/tracker integration. Verify exact repository, issue/comment reads, complete search/dedupe, existing approved labels, narrowly scoped create/update/compensating close and draft PR capability only if separately authorized. No label creation, reassignment, deletion, merge or shipping is implied. Slack requires exact channel/thread read/post actions, attachment access and trusted identity; never treat a generic channel response as a thread API. Missing actions leave the integration blocked.

Discover available deferred capabilities with `tool_describe`/`tool_call` and inspect live schemas. Use only authenticated, authorized integrations actually present. No connector, webhook route, scheduling job, credential or provider is activated by loading this skill. Verify authorized external writes by reading back the exact target.
5. Read `pstack-benny-reproduce-and-fix-issues`'s control-adapter contract and completed feature map. UI interaction is allowed only after all seven capabilities (startup, mapped navigation, real input, read-only inspection, screenshots, recording, safe cleanup) are demonstrated. Screenshots alone do not prove video capture. Missing capability leaves repro disabled.

Use available browser or desktop helpers and actual vision for visual evidence. If a browser form requests credentials, address or card fields, first call `browser_vault_list` and the appropriate vault fill/save tool; codes use `browser_vault_enter_code`. Never solicit or type secrets in chat. Discover webhook/MCP facilities from the real session and current official documentation before proposing setup.
6. Prepare, but do not enable, the two prompt templates. Manual invocation is the default. Optional GitHub `issues` webhook routes use a verified filter/script for configured repo, `action: opened`, and report identity; route event filtering alone does not restrict action or repo. `issue_comment` events must exclude Benny's own output and unrelated comments to avoid loops. Default route delivery is `log`; the coordinator performs only explicitly approved comments. Generic webhook acceptance is not a Slack Events API bridge or a durable reproduction queue.
7. Only if separately requested and confirmed, propose a verified authenticated event route or a paused schedule with exact working directory, both operational skill attachments, explicit log-only delivery and bounded prompt. Verify current supported management controls before writing. No jobs are created by loading this workflow. Model/provider/reasoning choices remain user-owned; no per-role selection is assumed. Recurring collection requires a separately implemented/tested checkpoint and dedupe adapter. Long verdict/rejection/follow-up windows are saved deadlines, not long sleeps. Preserve source identity across resumptions and recheck every gate.

Native children stop with the parent/session. For separately authorized durable work use supported scheduling or `terminal(background=true, notify=true, persist_on_release=true)` for a real bounded job; never detached child claims or background sleep/poll loops. Discover cron/process tools before use, preserve explicit scope and leave actionable handoff evidence.
8. Before activation, obtain explicit authorization for each trigger and external write type. Test with a harmless issue/thread: immutable source identity; one verdict/one marker; trusted author gate; no root/fallback posts or cross-posts; no write on missing/deleted/inaccessible parent; compensation for a newly created tracker issue if handoff fails; no worker writes. Plain prompts do not prove isolation; perform sensitive work in the coordinator when isolation is unverified. Test the full control adapter in disposable state separately. Read back the exact job/route and test artifacts before claiming configured. Keep all activation off if any test fails.

## Pitfalls

Keep the user's scope and explicit checkpoints. Missing evidence or unavailable dependencies are gaps, not passes. Do not replace a working existing skill or change another user-owned execution environment.

## Verification

Enumerate configuration placeholders, capability checks, user-approved writes, and thread/issue safety tests. Confirm no active job, hook, route, or external write exists unless explicitly approved and verified.

## Attribution

Adapted from Lauren Tan's MIT-licensed pstack 0.15.6, source revision `23e4138daa01c42d4969f7a5465f82704e64f798`. See `references/license.md`.
