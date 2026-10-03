---
name: pstack-benny-setup-benny
description: "Prepare optional safe Benny issue workflows."
version: 0.1.0
author: "Lauren Tan (poteto), tea24864, Hermes Agent"
license: MIT
platforms: ["linux", "macos"]
metadata:
  hermes:
    tags: [pstack, engineering, workflow]
    related_skills: []
---
# Set up Benny for Hermes

## When to Use

Use only for an explicit request to prepare or change Benny configuration. Manual GitHub issue intake is the safe initial workflow.

## Prerequisites

Read `references/hermes-runtime.md` with `skill_view` before executing this workflow. Use only tools and credentials actually available in this session. Invoking this skill does not authorize publication, merges, destructive cleanup, or configuration changes.

## Procedure

Benny is optional and dormant until explicitly configured. These are native skills, not Cursor cloud automations. Setup does not grant tracker writes, source posts, draft PRs, jobs, hooks, deployment, or deletion authority.

1. Read `references/README.md`, `references/FOR_AGENTS.md`, and `references/integration-contract.md`. Load `hermes-agent` and the live cron/webhook docs. Confirm the repository, active Hermes profile, existing skill availability, intended source (GitHub issue by default; Slack only with a verified adapter), and explicitly authorized write policy. Do not install anything now or copy a pack into `.cursor`.
2. Verify `pstack-how`, `pstack-why`, `pstack-tdd`, `pstack-unslop`, the listed principle dependencies, and both native Benny operational skills in the actual execution profile. Fresh jobs must resolve these names; current-session loading alone does not prove that. Missing dependencies block activation.
3. Copy `templates/configuration.example.yaml` into a caller-approved user-owned location outside installed skill files, such as `.hermes/benny/configuration.yaml` in the target repository. Preserve destination-only files and merge conflicts with local edits. Do not overwrite an existing user config. Copy the operational feature/routing examples from the named skills into user-owned files. Fill all placeholders, including safe environment, stable account/data markers, screenshot/recording capability, runtime budgets, trusted triage identity, marker strings, source repository/number or Slack coordinates, and artifact retention. Secrets are environment/secret-manager references only; browser forms use the vault.
4. GitHub intake uses existing authenticated `gh` and `github-issues`/`github-pr-workflow` skills. Verify repo identity, issue/comment reads, search/dedupe, exact approved labels, narrowly scoped create/update/compensating close, and draft PR capability only if separately authorized. No label creation, reassignment, issue deletion, merging, or shipping is implied. For Slack, verify exact channel/thread read/post APIs, attachment access, and identity, never map a gateway channel response onto a guessed thread API. Missing Slack or tracker actions are a blocked integration, not a synthetic endpoint.
5. Read `pstack-benny-reproduce-and-fix-issues`'s control-adapter contract and completed feature map. Browser tools or `computer-use` can provide real UI interaction only if all seven capabilities (startup, mapped navigation, real input, read-only inspection, screenshots, recording, safe cleanup) are demonstrated. Ordinary browser screenshots do not prove video capture. A missing capability leaves repro disabled.
6. Prepare, but do not enable, the two prompt templates. Manual invocation is the default. Optional GitHub `issues` webhook routes use a verified filter/script for configured repo, `action: opened`, and report identity; route event filtering alone does not restrict action or repo. `issue_comment` events must exclude Benny's own output and unrelated comments to avoid loops. Default route delivery is `log`; the coordinator performs only explicitly approved comments. Generic webhook acceptance is not a Slack Events API bridge or a durable reproduction queue.
7. If explicitly requested and confirmed, choose either an authenticated webhook route or a paused cron job with `--workdir`, both native `--skill` attachments, explicit delivery, and a bounded run prompt after live CLI/schema verification. CLI `hermes cron create ... --paused` is supported; no jobs are created by loading this skill. Cron inference pins are user-owned, reasoning stays inherited, and delegation has no per-role models. A recurring collector requires a separately implemented/tested checkpoint and dedupe adapter. Long verdict/rejection/follow-up windows are deadlines in saved state, not instructions to sleep past runtime limits. Preserve source identity across resumptions and recheck gates each time.
8. Before activation, obtain explicit authorization for each trigger and external write type. Test with a harmless issue/thread: immutable source identity; one verdict/one marker; trusted author gate; no root/fallback posts or cross-posts; no write on missing/deleted/inaccessible parent; compensation for a newly created tracker issue if handoff fails; no worker writes. Plain prompts do not prove isolation; perform sensitive work in the coordinator when isolation is unverified. Test the full control adapter in disposable state separately. Read back the exact job/route and test artifacts before claiming configured. Keep all activation off if any test fails.

## Pitfalls

Keep the user's scope and explicit checkpoints. Missing evidence or unavailable dependencies are gaps, not passes. Do not replace a working existing skill or change another profile.

## Verification

Enumerate configuration placeholders, capability checks, user-approved writes, and thread/issue safety tests. Confirm no active job, hook, route, or external write exists unless explicitly approved and verified.

## Attribution

Adapted from Lauren Tan's MIT-licensed pstack 0.15.6, source revision `23e4138daa01c42d4969f7a5465f82704e64f798`. See `references/license.md`.
