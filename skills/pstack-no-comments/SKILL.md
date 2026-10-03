---
name: pstack-no-comments
description: "Review comments and fix accepted scoped workarounds."
version: 0.1.0
author: "Lauren Tan (poteto), tea24864, Hermes Agent"
license: MIT
platforms: ["linux", "macos"]
metadata:
  hermes:
    tags: [pstack, engineering, workflow]
    related_skills: []
---
# No comments

## When to Use

Use for explicit no-comments review or a scoped comment/workaround cleanup request.

## Prerequisites

Read `references/hermes-runtime.md` with `skill_view` before executing this workflow. Use only tools and credentials actually available in this session. Invoking this skill does not authorize publication, merges, destructive cleanup, or configuration changes.

## Procedure

Keep the caller's fence. Use its files or diff; otherwise inspect the current diff and working tree against the discovered base branch (default `main` only when present). Do not sweep unrelated code.

1. Read `references/comment-reviewer.md`. A parent with `delegate_task` may spawn a fresh reviewer using `delegate_task(tasks=[{"goal":"Review comments in the bounded scope; return findings only.","context":"<exact scope, base, reviewer reference contents, read-only/no-write instruction>"}])`. Pass the reviewer rules, not a fictional `subagent_type`. No `model`, `readonly`, `environment`, or `background` arguments. A child cannot delegate or clarify; if unavailable, perform a separate evidence-based pass locally and disclose the missing independent reviewer. Prompt-only read-only instructions are not tool isolation.
2. The reviewer proposes comment-only deletions and exact `MUST KILL` refactor targets. The coordinator applies accepted edits. Inspect every finding: reject application-code edits, scope escapes, exception-protected deletions, false reasons, and flags blaming intentional code that stays. Our-code surprises remain actionable reshape flags, not excuses to restore prose. Audit missed scoped lint/TypeScript suppressions. Correctness/safety suppressions require a root-cause fix, not blind suppression deletion that breaks the build. Restore only with a precise exception and scoped proof.
3. Before accepting thin `IMPORTANT` or `do not remove` kills or keeps, use `pstack-how` or `pstack-why` on the symbol. Ambiguous keeps without exception proof do not qualify. Rerun a rejected report once with its failure named. A second rejection fails this review; report it open. Do not revert unrelated changes.
4. Fix trivial accepted flags by removing a proven dead path, dropping a parameter, or using the real API. If a fix needs a new shape, use `pstack-architect` once for the accepted set and nearby code, stop at the sketch, then implement separately. The principles on root causes and redesign do not authorize widening scope. Never bolt on symptom guards.
5. Constraint comments (`do not remove`, `do not change wording`, `talk to X`) qualify for a keep only when they cover something outside our control. Offer the cheapest in-scope type, runtime check, test, or CI lint. Wait for approval before encoding; unattended runs need prior approval. Without approval, delete an unprotected comment only if doing so leaves required behavior intact, report the unenforced constraint, and sketch out-of-scope work. Keep legal headers, public API contracts, justified external constraints, required tool directives, and necessary issue/RFC links.
6. Run the repository's existing focused checks after changes. Never delete tests or weaken assertions to make the diff pass. Report counts of deletions and restorations, reruns, architecture sketch, fixes, encoding offers/accepted encodings, and all open constraints.

## Pitfalls

Keep the user's scope and explicit checkpoints. Missing evidence or unavailable dependencies are gaps, not passes. Do not replace a working existing skill or change another profile.

## Verification

Inspect the actual scoped diff, reconcile every deletion with an accepted finding, and run real checks. An unimplemented safety fix or rejected second review stays open.

## Attribution

Adapted from Lauren Tan's MIT-licensed pstack 0.15.6, source revision `23e4138daa01c42d4969f7a5465f82704e64f798`. See `references/license.md`.
