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

{{runtime.skill_loading}}
2. Verify `pstack-how`, `pstack-why`, `pstack-tdd`, `pstack-unslop`, the listed principle dependencies, and both native Benny operational skills in the actual execution profile. Fresh jobs must resolve these names; current-session loading alone does not prove that. Missing dependencies block activation.
3. Copy `templates/configuration.example.yaml` into an approved user-owned location outside installed skill files, for example `.benny/configuration.yaml` in the target project. Preserve destination-only files and conflicts with local edits. Never overwrite existing user config. Copy the feature/routing examples into user-owned files. Fill every placeholder, including safe environment, stable account/data markers, screenshot/recording capability, budgets, trusted triage identity, marker strings, source coordinates and retention. Secrets remain environment/secret-manager references; forms use the approved secure-entry channel.

{{runtime.files}}

{{runtime.configuration}}
4. GitHub intake uses an already authenticated verified source/tracker integration. Verify exact repository, issue/comment reads, complete search/dedupe, existing approved labels, narrowly scoped create/update/compensating close and draft PR capability only if separately authorized. No label creation, reassignment, deletion, merge or shipping is implied. Slack requires exact channel/thread read/post actions, attachment access and trusted identity; never treat a generic channel response as a thread API. Missing actions leave the integration blocked.

{{runtime.integrations}}
5. Read `pstack-benny-reproduce-and-fix-issues`'s control-adapter contract and completed feature map. UI interaction is allowed only after all seven capabilities (startup, mapped navigation, real input, read-only inspection, screenshots, recording, safe cleanup) are demonstrated. Screenshots alone do not prove video capture. Missing capability leaves repro disabled.

{{runtime.web}}
6. Prepare, but do not enable, the two prompt templates. Manual invocation is the default. Optional GitHub `issues` webhook routes use a verified filter/script for configured repo, `action: opened`, and report identity; route event filtering alone does not restrict action or repo. `issue_comment` events must exclude Benny's own output and unrelated comments to avoid loops. Default route delivery is `log`; the coordinator performs only explicitly approved comments. Generic webhook acceptance is not a Slack Events API bridge or a durable reproduction queue.
7. Only if separately requested and confirmed, propose a verified authenticated event route or a paused schedule with exact working directory, both operational skill attachments, explicit log-only delivery and bounded prompt. Verify current supported management controls before writing. No jobs are created by loading this workflow. Model/provider/reasoning choices remain user-owned; no per-role selection is assumed. Recurring collection requires a separately implemented/tested checkpoint and dedupe adapter. Long verdict/rejection/follow-up windows are saved deadlines, not long sleeps. Preserve source identity across resumptions and recheck every gate.

{{runtime.persistent_work}}
8. Before activation, obtain explicit authorization for each trigger and external write type. Test with a harmless issue/thread: immutable source identity; one verdict/one marker; trusted author gate; no root/fallback posts or cross-posts; no write on missing/deleted/inaccessible parent; compensation for a newly created tracker issue if handoff fails; no worker writes. Plain prompts do not prove isolation; perform sensitive work in the coordinator when isolation is unverified. Test the full control adapter in disposable state separately. Read back the exact job/route and test artifacts before claiming configured. Keep all activation off if any test fails.

## Pitfalls

Keep the user's scope and explicit checkpoints. Missing evidence or unavailable dependencies are gaps, not passes. Do not replace a working existing skill or change another user-owned execution environment.

## Verification

Enumerate configuration placeholders, capability checks, user-approved writes, and thread/issue safety tests. Confirm no active job, hook, route, or external write exists unless explicitly approved and verified.

## Attribution

Adapted from Lauren Tan's MIT-licensed pstack 0.15.6, source revision `23e4138daa01c42d4969f7a5465f82704e64f798`. See `references/license.md`.
