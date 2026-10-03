---
name: pstack-arena
description: "Compare candidates, select a base, and graft ideas."
license: MIT
metadata:
  author: "Lauren Tan (poteto), tea24864"
  version: "0.2.0"
  source-revision: "23e4138daa01c42d4969f7a5465f82704e64f798"
---

# Arena

## When to Use

Use for competing designs, code or prose bakeoffs, and best-of artifact synthesis. For coverage partitions use pstack-swarm.

## Prerequisites

{{runtime.skill_loading}}

Use only capabilities and credentials actually available in this session. Invoking this workflow does not authorize publication, merges, destructive cleanup, dependency installation, or configuration changes. Preserve the caller's scope and user-owned state.

## Procedure

Fan out N parallel attempts at the same task. Read every candidate end to end. Pick the strongest as the base. Graft the best ideas from the others into it. Verify the synthesized result.

## Start

{{runtime.task_tracking}}

Use the available task tracker to open a checklist, or write a local phase checklist with one entry per phase before launching anything.

1. Frame
2. Fan out
3. Cross-judge
4. Pick
5. Graft
6. Verify

## Phase A: Frame

The N candidates will receive the same prompt, so the prompt is the contract.

1. State the artifact each candidate is producing.
2. Derive the rubric. State what success looks like for *this* task, then turn it into 3-6 concrete gradeable criteria. The rubric is the picker's tool in Phase D. Candidates only see the task.
3. Pick N independent runners under the worker execution boundary below. Default to three same-model candidates. Increase N only for distinct design directions and within the authorized budget. Keep the rubric private to judges. A same-model panel is not model diversity.
4. Assign each repository-writing candidate an exclusive git worktree and branch; use separate workspace or `$TMPDIR` output directories for artifact-only work. Never let concurrent candidates write a shared checkout, index, or branch.

## Phase B: Fan out

Launch the candidates in one independent wave where supported. Each gets an identical task brief, shared grounding, exclusive output/worktree path, acceptance criteria, rationale requirement and no-publication restriction. Bind real paths before starting; pass no judge rubric to candidates. If unavailable, produce distinct serial candidates and state the loss of parallel separation.

Each rationale names the alternatives the candidate considered and what it rejected.

If a candidate fails to produce output, proceed with N-1 and note the dropout in the synthesis record.

## Phase C: Cross-judge

Budget the entire workflow, not just the first wave: concurrent-child limits and a one-shot total-child budget are different. Reserve a judge slot when the verified remaining budget permits. A confirmed exhausted budget is not fixed by retrying or splitting batches; judge and synthesize inline, explicitly stating that no independent cross-judge ran. Never change global delegation settings to finish this workflow. Bound artifact length and leave time for reading, synthesis, verification, and the user checkpoint.

After every candidate has finished writing, assign an independent no-write judge the rubric and completed candidate paths by neutral label. Require per-criterion scores and a recommended base with rationale. It may run while the coordinator reads, never while candidates write. Record the actual model policy; externally different-model judging requires verified capability and explicit scope. If no independent judge can run, judge inline and record that gap.

## Phase D: Pick a base

Read every candidate end to end before picking.

Score each candidate against the rubric criterion by criterion, not on holistic feel. Compare against the cross-judge. Agreement on the base confirms the pick. Disagreement means one of you is biased or the rubric was ambiguous. Read both rationales before deciding.

Pick the base on which candidate a future maintainer can extend most easily without breaking invariants. Prefer the cleaner boundary or smaller API when two feel tied, per the Laziness Protocol.

Record the pick and the reason in a short synthesis note alongside the base artifact, including the cross-judge's verdict.

## Phase E: Graft

Walk each losing candidate once more and identify what is worth porting into the base. The signal is usually one or two things per candidate, not most of it.

Fold each graft in by hand, per the **pstack-principle-redesign-from-first-principles** principle skill. Don't paste mechanically. The result has to remain coherent under one mental model.

Record what was grafted, from which candidate, and what was rejected and why.

When N candidates converge on the same shape, that is a strong agreement signal. Note the convergence in the record and ship the consensus shape. No graft is needed. When N candidates wildly diverge, Phase A was under-specified. Reframe and re-run rather than averaging the divergence.

## Phase F: Verify

The synthesized artifact has to hold up under the same scrutiny as any other output, per the **pstack-principle-prove-it-works** principle skill.

If verification surfaces a problem the arena did not catch, either Phase A was wrong (re-frame and re-run) or one candidate caught it and you missed the graft (go back to Phase E). Don't paper over.

## Outputs

One synthesized artifact. One short synthesis note alongside, naming the base, the grafts (with source candidate), the rejections, the dropouts if any, and the verification result.

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
