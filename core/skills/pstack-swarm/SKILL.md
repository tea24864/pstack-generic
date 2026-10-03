---
name: pstack-swarm
description: "Coordinate parallel coverage and evidence reports."
license: MIT
metadata:
  author: "Lauren Tan (poteto), tea24864"
  version: "0.2.0"
  source-revision: "23e4138daa01c42d4969f7a5465f82704e64f798"
---

# Swarm

## When to Use

Use for coverage matrices, partitioned investigations, races, or verification gauntlets. Do not call coverage complete while a required slice is missing.

## Prerequisites

{{runtime.skill_loading}}

Use only capabilities and credentials actually available in this session. Invoking this workflow does not authorize publication, merges, destructive cleanup, dependency installation, or configuration changes. Preserve the caller's scope and user-owned state.

## Procedure

Fan out N parallel bounded workers. They may cover separate slices, race the same brief, or mix both. The parent waits, aggregates, and returns one report.

## Start

{{runtime.task_tracking}}

Use the available task tracker to open a phase checklist, or write a local checklist with one entry per phase before launching anything.

1. Frame
2. Fan out
3. Aggregate
4. Report

## Phase A: Frame

1. State the done predicate and the artifact or report the swarm must return.
2. Choose the shape. Partition into slices, race N workers on identical briefs, or mix both. For a race or mixed shape, declare `first pass`, `rank all`, or `best-of` before spawning.
3. Set N from the user or derive it from the shape. N is total workers, not the runtime concurrency limit.
4. Declare the actual worker capabilities and observed model policy under the worker execution boundary below. A model race requires verified, authorized runners with real provider/model options. If independent workers are unavailable, execute bounded slices directly and report that no independent race ran.
5. Give each worker its own writable output when it writes. When workers verify or measure commits, each brief names the exact SHAs. A measurement brief also names the method (sample count, what one sample is, order). The worker records both in its result.

## Phase B: Fan out

Launch bounded workers in one independent wave where supported, extending to N. Each brief includes goal, exact slice or race arm, exact SHAs and sampling method, inputs, exclusive worktree/output, verification, timebox, write restrictions and report format. Use only supported controls. If N exceeds actual concurrency, queue or coordinate bounded waves; N still counts total workers. If unavailable, execute the slices serially and disclose the loss of independent coverage.

When a worker needs a non-default branch, the parent prepares an exclusive worktree at the exact commit and passes its absolute path. Do not invent a cloud branch parameter.

Every brief stands alone. Include the goal, scope, exact slice or race arm, how to verify, and what to report. Reports use `PASS`, `ISSUES`, or `BLOCKED` with evidence. A worker that can prove a defect reports `ISSUES` and lists every issue it can prove, not only the first.

If a worker drops out, proceed with N-1 and note it.

## Phase C: Aggregate

Read the terminal results. Drop a result that does not record the SHAs and method its brief names, and respawn that worker once. After a second miss, record a gap. A gap does not count as a pass. For coverage, every required slice needs a result. For a race, apply the selection rule declared up front. Use first pass, rank all, or best-of. Do not paste raw worker dumps.

Keep a compact result table, or equivalent bullets on Discord, one-line evidenced issues, and explicit gaps or dropouts.

## Phase D: Report

Return one consolidated in-chat report with the table (bullets on Discord), issue one-liners, gaps or dropouts, and the race rule when used.

## Worker execution boundary

{{runtime.delegation}}

Every brief stands alone: scope, exact paths and revisions, inputs, acceptance criteria, verification commands, budget, forbidden actions and report format. A read-only instruction is not a sandbox. Concurrent writers own exclusive worktrees/branches; artifact-only candidates use separate output directories. The coordinator relays dependencies and integrates only completed, checked artifacts.

Do not call repeated same-model attempts model diversity. Genuine diversity needs verified available runners and actual provider/model choices within explicit scope. Record what ran and its correlated-model limitation; never invent models or silently change providers. Budget candidates, judging, synthesis and verification together. When independent execution is absent or exhausted, do assigned work directly, preserve distinct alternatives where required, and disclose lost independence rather than retrying a known exhausted budget.


## Pitfalls

Keep the user's scope and explicit checkpoints. Missing evidence or unavailable dependencies are gaps, not passes. Do not replace a working existing skill or change another user-owned execution environment.

## Verification

Check each promised artifact and claim against a real tool result. Report evidence, skipped checks, and limitations. A child's self-report is not independent verification.

## Attribution

Adapted from Lauren Tan's MIT-licensed pstack 0.15.6, source revision `23e4138daa01c42d4969f7a5465f82704e64f798`. See `references/license.md`.
