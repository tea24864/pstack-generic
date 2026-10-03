---
name: pstack-arena
description: "Compare candidates, select a base, and graft ideas."
version: 0.1.0
author: "Lauren Tan (poteto), tea24864, Hermes Agent"
license: MIT
platforms: ["linux", "macos"]
metadata:
  hermes:
    tags: [pstack, engineering, workflow]
    related_skills: ["pstack-architect", "pstack-swarm", "pstack-interrogate"]
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
# Arena

## When to Use

Use for competing designs, code or prose bakeoffs, and best-of artifact synthesis. For coverage partitions use pstack-swarm.

## Prerequisites

Read `references/hermes-runtime.md` with `skill_view` before executing this workflow. Use only tools and credentials actually available in this session. Invoking this skill does not authorize publication, merges, destructive cleanup, or configuration changes.

## Procedure

Fan out N parallel attempts at the same task. Read every candidate end to end. Pick the strongest as the base. Graft the best ideas from the others into it. Verify the synthesized result.

## Start

Use `todo_list` to open a checklist, or write a local phase checklist with one entry per phase before launching anything.

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
3. Pick N independent runners under the Hermes execution contract below. Default to three same-model candidates. Increase N only for distinct design directions and within the authorized budget. Keep the rubric private to judges. A same-model panel is not model diversity.
4. Assign each repository-writing candidate an exclusive git worktree and branch; use separate workspace or `$TMPDIR` output directories for artifact-only work. Never let concurrent candidates write a shared checkout, index, or branch.

## Phase B: Fan out

Launch the candidates in one `delegate_task(tasks=[{"goal": "Build candidate A", "context": "Identical task brief, shared grounding paths, exclusive output/worktree path, acceptance criteria, rationale requirement, no delegation and no publication."}, {"goal": "Build candidate B", "context": "The same task brief with B's exclusive output/worktree path."}])` call, extending the array to N. Bind real paths before spawning. If unavailable, produce independent serial candidates and state the loss of parallel separation.

Each rationale names the alternatives the candidate considered and what it rejected.

If a candidate fails to produce output, proceed with N-1 and note the dropout in the synthesis record.

## Phase C: Cross-judge

Budget the entire workflow, not just the first wave: concurrent-child limits and a one-shot total-child budget are different. Reserve a judge slot when the verified remaining budget permits. A confirmed exhausted budget is not fixed by retrying or splitting batches; judge and synthesize inline, explicitly stating that no independent cross-judge ran. Never change global delegation settings to finish this workflow. Bound artifact length and leave time for reading, synthesis, verification, and the user checkpoint.

After every candidate has finished writing, launch one independent judge with `delegate_task(tasks=[{"goal": "Score completed candidates against the rubric and recommend a base", "context": "Rubric, completed candidate paths by neutral label, no writes, no delegation; return per-criterion scores and rationale."}])`. This is a same-model judge by default. It may run while the parent reads, never while candidates write. If genuine external-model judging is authorized and verified, record its actual provider/model.

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
