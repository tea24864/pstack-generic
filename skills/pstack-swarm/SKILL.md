---
name: pstack-swarm
description: "Coordinate parallel coverage and evidence reports."
version: 0.1.0
author: "Lauren Tan (poteto), tea24864, Hermes Agent"
license: MIT
platforms: ["linux", "macos"]
metadata:
  hermes:
    tags: [pstack, engineering, workflow]
    related_skills: ["pstack-arena", "pstack-poteto-mode"]
    config:
      - key: pstack.panel_size
        description: Default independent panel size; explicit scope wins.
        default: 3
        prompt: Default independent panel size
      - key: pstack.model_strategy
        description: Policy only; external runners require separate verification.
        default: inherit-parent
        prompt: Model strategy (inherit-parent or verified-external)
---
# Swarm

## When to Use

Use for coverage matrices, partitioned investigations, races, or verification gauntlets. Do not call coverage complete while a required slice is missing.

## Prerequisites

Read `references/hermes-runtime.md` with `skill_view` before executing this workflow. Use only tools and credentials actually available in this session. Invoking this skill does not authorize publication, merges, destructive cleanup, or configuration changes.

## Procedure

Fan out N parallel bounded workers. They may cover separate slices, race the same brief, or mix both. The parent waits, aggregates, and returns one report.

## Start

Use `todo_list` to open a phase checklist, or write a local checklist with one entry per phase before launching anything.

1. Frame
2. Fan out
3. Aggregate
4. Report

## Phase A: Frame

1. State the done predicate and the artifact or report the swarm must return.
2. Choose the shape. Partition into slices, race N workers on identical briefs, or mix both. For a race or mixed shape, declare `first pass`, `rank all`, or `best-of` before spawning.
3. Set N from the user or derive it from the shape. N is total workers, not the runtime concurrency limit.
4. Declare the actual worker runtime and same-model limitation under the execution contract below. Native delegation inherits the current model or global pin. A model race is available only through verified, authorized external CLIs with real provider/model options, never task parameters.
5. Give each worker its own writable output when it writes. When workers verify or measure commits, each brief names the exact SHAs. A measurement brief also names the method (sample count, what one sample is, order). The worker records both in its result.

## Phase B: Fan out

Launch bounded workers with `delegate_task(tasks=[{"goal": "Verify slice A", "context": "Goal, scope, exact slice or race arm, exact SHAs and method if measuring, inputs, exclusive worktree/output paths, verification, timebox, write restrictions, no delegation, report PASS/ISSUES/BLOCKED with receipts."}, {"goal": "Verify slice B", "context": "Standalone B brief with the same required fields."}])`, extending to N. Use the live schema, without Cursor environment or model arguments. If N exceeds configured concurrency, allow the runtime to queue or coordinate bounded waves; N still counts total workers.

When a worker needs a non-default branch, the parent prepares an exclusive worktree at the exact commit and passes its absolute path. Do not invent a cloud branch parameter.

Every brief stands alone. Include the goal, scope, exact slice or race arm, how to verify, and what to report. Reports use `PASS`, `ISSUES`, or `BLOCKED` with evidence. A worker that can prove a defect reports `ISSUES` and lists every issue it can prove, not only the first.

If a worker drops out, proceed with N-1 and note it.

## Phase C: Aggregate

Read the terminal results. Drop a result that does not record the SHAs and method its brief names, and respawn that worker once. After a second miss, record a gap. A gap does not count as a pass. For coverage, every required slice needs a result. For a race, apply the selection rule declared up front. Use first pass, rank all, or best-of. Do not paste raw worker dumps.

Keep a compact result table, or equivalent bullets on Discord, one-line evidenced issues, and explicit gaps or dropouts.

## Phase D: Report

Return one consolidated in-chat report with the table (bullets on Discord), issue one-liners, gaps or dropouts, and the race rule when used.

## Hermes execution contract

Use `delegate_task(tasks=[{"goal": "Produce the assigned artifact", "context": "Standalone brief with scope, exact paths, inputs, acceptance criteria, verification commands, write restrictions, and report format."}])` only when that tool is available to the parent. Discover its current schema first. Do not add Cursor-only arguments. Child conversations are isolated but the filesystem is shared. A read-only instruction is not a sandbox. Give concurrent repository writers separate git worktrees and branches; artifact-only candidates may use separate output directories under the agreed workspace or `$TMPDIR`.

Children cannot call `delegate_task` or clarify. The parent coordinates flattened waves and relays dependency results. A child executing this workflow does its assigned leaf work directly, returns evidence and proposed next-wave briefs, and never waits for grandchildren. For asynchronous delegation, results arrive after the parent ends its turn; do not poll child transcripts. Children are bounded and die on stop or session end. Durable work requires separately authorized cron or independent processes, not a claim that a child is persistent.

Delegates use the current parent model or the global delegation pin. Optional `skills.config.pstack.*` runtime policy defaults to `inherit-parent`; it does not create a per-task model argument. Call the default panel independent same-model attempts and disclose its correlated-model limitation. Genuine model diversity requires verified external agent CLI support, explicit user scope, and provider/model selections from currently available options. Do not invent model names or silently substitute providers. See `references/hermes-runtime.md` for the shared policy.


## Pitfalls

Keep the user's scope and explicit checkpoints. Missing evidence or unavailable dependencies are gaps, not passes. Do not replace a working existing skill or change another profile.

## Verification

Check each promised artifact and claim against a real tool result. Report evidence, skipped checks, and limitations. A child's self-report is not independent verification.

## Attribution

Adapted from Lauren Tan's MIT-licensed pstack 0.15.6, source revision `23e4138daa01c42d4969f7a5465f82704e64f798`. See `references/license.md`.
