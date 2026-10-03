---
name: pstack-benny-reproduce-and-fix-issues
description: "Prove Benny bugs and prepare bounded draft fixes."
license: MIT
metadata:
  author: "Lauren Tan (poteto), tea24864"
  version: "0.2.0"
  source-revision: "23e4138daa01c42d4969f7a5465f82704e64f798"
---

# Reproduce and optionally fix issues

## When to Use

Use after a trusted configured Benny bug/performance verdict, or a manually confirmed triage decision for local proof.

## Prerequisites

{{runtime.skill_loading}}

Use only capabilities and credentials actually available in this session. Invoking this workflow does not authorize publication, merges, destructive cleanup, dependency installation, or configuration changes. Preserve the caller's scope and user-owned state.

## Procedure

{{runtime.files}}

Load explicit Benny config, `references/source-workflow.md`, `references/control-adapter.md`, and the completed feature map. The reference preserves detailed Slack-specific gates; GitHub source identity is the issue repo/number/URL. Missing config, adapter, feature map, or required capability means blocked, no authored fix.

1. Freeze and validate the immutable source parent and source permalink before any analysis or delegation. For GitHub, fresh-read the exact configured repo/issue and comments; for Slack, enforce channel/root thread preflight. No source root/fallback posts, cross-posts, or guessed URLs. Only the coordinator may make explicitly approved external writes.
2. Require exactly one configured triage marker from the configured trusted identity in that same issue/thread. Proceed only for bug/performance and capture optional tracker URL. Missing/untrusted/conflicting/other marker stops silently in unattended source channels. Waiting is a bounded deadline/checkpoint, not an unbounded sleep. A manual local repro may use an explicitly confirmed trusted triage decision without inventing a posted marker.
3. Re-read ownership and artifacts immediately before work. Stop if a person clearly claims implementation or delegates a fix. Utility bot diagnosis is evidence, not ownership. An open PR/merged commit plausibly addressing the report switches to `references/verify-existing-fix.md`; do not edit it or create a competing patch.
4. Optional operations/status output needs explicit approval and separate immutable coordinates; otherwise report locally. Never confuse status IDs with the source parent. Slack status posting requires a verified adapter; no tool means an explicit gap. Screenshots, video, logs, tokens, and test profiles stay out of source control and follow approved retention.
5. Confirm all seven adapter capabilities: start correct revision/environment, mapped navigation, real UI input, read-only inspection, screenshots, recording, and safe cleanup. Load the relevant feature-map section before driving. Stable app/account/workspace/data markers must identify the test target. Ordinary browser tooling does not guarantee recording. Use a verified desktop or browser harness only after checking actual capabilities.

{{runtime.web}}
6. Study full thread/issue/media and use `pstack-how`/`pstack-why` for competing root-cause hypotheses. Workers return narrow findings only, with no credentials or source-posting instructions; every prompt forbids source, tracker and repository external writes. Prompt restrictions are not isolation. Unless tool/credential isolation is proven, the coordinator owns edits and sensitive work. Leaf workers return next-wave proposals instead of waiting for descendants.

{{runtime.delegation}}
7. Reproduce the exact discriminating final state through the real UI twice, resetting between independent attempts. Name correct versus broken final state, reach their divergence, observe it, and cross-check a real state value when possible. Fixtures may arrange safe preconditions but never inject the symptom into storage/DOM. A loading dialog, source reading, unit test, or screenshot alone is not a confirmed repro. Respect configured budget; distinguish Could not reproduce from Blocked.
8. Capture full-path recording, broken-final-state screenshot, and exact steps. Review media locally with verified image inspection or a verified read-only reviewer: does it visibly show the discriminating state? If no/uncertain, improve within budget or mark unconfirmed. No confirmed repro means no authored fix. With authority, post at most one concise source update after fresh preflight, read back it, and use operations/run output for detailed evidence. No source update for blocked/could-not-reproduce. A configured rejection window must finish with gates rechecked before fixing.
9. For an existing fix, baseline and patched builds must each run the same real UI path twice with comparable revision inputs/data and before/after recordings, screenshots, and cross-checks. Baseline that fails to reproduce means inconclusive, not verified. Open no PR in verify mode. Do not reset or overwrite user changes; use an approved isolated worktree.
10. An optional new fix requires separate scope/authorization plus plain confirmed repro, media proof, no fix artifact or human ownership, runtime root-cause evidence, budget fit, and baseline/patched capability. Implement the smallest justified root-cause change. Use `pstack-tdd` when cheap (or the caller's stricter existing TDD policy); preserve original assertions. Skip impractical new tests only with a reason and a closest useful executable check. No unrelated cleanup or symptom guards. Stop if risk/effort expands.
11. Keep original baseline evidence. Patched real UI path must pass twice, show expected final state, remove broken state, and capture after recording/screenshot plus the same read-only cross-check. Run focused tests and blast-radius smoke over nearby states, inputs, permissions, platforms, and failure paths. A plausible diff/compile/test alone is not after proof; remaining regressions mean no PR.
12. Only after before/after proof AND explicit commit/push/draft-PR authority, use the verified repository publication workflow, review the real diff for scope/secrets, run checks and create a draft PR with actual public links. Include repro steps, root cause, tests, evidence, tracker syntax and blast-radius checks; apply `pstack-unslop`. Verify the exact PR is draft on the intended branch/repository/base. Never merge or deploy. Failure means actual branch/commit state and Fix did not land, not success. Without authority, return a local uncommitted patch and draft description.

{{runtime.integrations}}
13. Bound direct follow-ups; apply at most one concrete setup correction and rerun when it invalidates interpretation. Stay out of side chatter and stop on request. Always use safe adapter cleanup only for processes/profiles/data this run created. Preserve user work and approved evidence, report retained artifacts and open failures.

{{runtime.persistent_work}}

## Pitfalls

Keep the user's scope and explicit checkpoints. Missing evidence or unavailable dependencies are gaps, not passes. Do not replace a working existing skill or change another user-owned execution environment.

## Verification

Record two baseline repros, media review, trusted/ownership gates, optional fix qualification, two patched proofs, focused/blast-radius checks, exact approved external readbacks, and safe cleanup. Missing evidence stays blocked/inconclusive, never fabricated.

## Attribution

Adapted from Lauren Tan's MIT-licensed pstack 0.15.6, source revision `23e4138daa01c42d4969f7a5465f82704e64f798`. See `references/license.md`.
