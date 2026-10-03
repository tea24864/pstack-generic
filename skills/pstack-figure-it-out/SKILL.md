---
name: pstack-figure-it-out
description: "Design and execute an auditable hypothesis-driven plan."
license: MIT
metadata:
  author: "Lauren Tan (poteto), tea24864"
  version: "0.2.0"
  source-revision: "23e4138daa01c42d4969f7a5465f82704e64f798"
---

# Figure it out

## When to Use

Use for an ambitious multi-part change or migration when no narrower playbook fits. First deliver the designed workflow; execution follows authorized scope.

## Prerequisites

Use only capabilities and credentials actually available. This workflow does not authorize publication, merges, destructive cleanup, installation, or configuration changes.

## Procedure

When the task matches no playbook, design one. The deliverable before any code is the workflow itself: a sequence of phases that scales rigor to the task, runs the scientific method, and leaves a decision trail a human can audit after stepping away.

## Start

Track phases using the deferred `todo_list` tool. Discover its current schema first with `tool_describe` and invoke through `tool_call`; mark only verified outcomes complete and keep at most one task in progress. A local checklist suffices when that capability is absent.

Load named skills with `skill_view(name="pstack-...")`; load supporting material with the same skill name and `file_path="references/..."`. Resolve all paths to the actual loaded skill directory. Do not invent missing skills or assume another profile shares the same catalog.

Open a task list whose first item is to read the Principles section of `pstack-poteto-mode`. Then add the phases below as concrete items.

## Phase A: Frame

Ground first, then commit. Don't start the run until you can state:

- The definition of done as a falsifiable predicate (the **pstack-principle-prove-it-works** principle skill).
- Scope, quantified: rough units and effort, plus the blockers grounding surfaced.
- The rigor level, biased high. One-way doors and high blast radius get more. Reversible low-stakes steps get less. Rigor is gates and artifacts, not "try harder".

Present the framing and tradeoffs before committing to a long run. Reversible work proceeds (the **pstack-principle-never-block-on-the-human** principle skill), but a multi-hour run earns one checkpoint.

## Phase B: Design the workflow

Decompose into atomic, independently-landable units. Sequence riskiest-unknown-first. Scaffold and verification come before features (the **pstack-principle-foundational-thinking** principle skill).

- Build the verification harness before the work, with the baseline captured from the pre-change state, so the check reads as "old value vs new value".
- For one-way-door design decisions, run the **pstack-architect** skill (it runs **pstack-arena**). Skip it for mechanical work whose shape is already concrete. A second arena over a settled design is over-engineering (the **pstack-principle-laziness-protocol** principle skill).
Use `delegate_task(tasks=[{"goal":"...","context":"..."}, ...])` for independent children. Each brief includes scope, evidence, exclusive output/worktree, verification and no delegation or user questions. Children share filesystems; read-only prompts are not sandboxes. Native children inherit the parent model or global pin: do not pass model/provider/readonly/background arguments or claim model diversity. Budget candidates, judges and synthesis together; obey confirmed concurrency and one-shot total-child limits. On exhaustion finish permitted lenses inline and label reduced independence, never retry or change global settings. For async delivery, finish independent work and end the turn; do not poll transcripts. Parent verifies returned artifacts and coordinates later waves. If an independent panel is explicitly required and unavailable, mark it blocked rather than substituting silently.

- Decide what fans out. Parallelize only across seams and give concurrent writers separate working trees or disjoint ownership (the **pstack-principle-separate-before-serializing-shared-state** principle skill). Don't over-fan. A branch alone does not isolate concurrent edits. The coordinator schedules later waves and verifies every artifact. Without independent delegation, execute the same units inline.
- Write the designed phase list down. That list is what the human reviews.

Native children stop with the parent/session. For separately authorized durable work use supported scheduling or `terminal(background=true, notify=true, persist_on_release=true)` for a real bounded job; never detached child claims or background sleep/poll loops. Discover cron/process tools before use, preserve explicit scope and leave actionable handoff evidence.

Then execute the design only within the authorized edit scope. A playbook or skill invocation grants no permission to ship, merge, delete unrelated work, or alter configuration. Add its steps to the todolist as concrete items, after the Phase C entry and before Phase D. Run each under the Phase C loop discipline, and weave the Phase D log through them, a row as each step lands, rather than saving the whole trail for the end.

## Phase C: Run the loop

Use `read_file`, `search_files`, `write_file` and `patch` for file work; use `terminal(command="...", timeout=...)` for real Git, helpers and tests. Read existing files before full replacement. Bundle mechanical loops through `execute_code` when appropriate. Use actual tool output as evidence.

Each unit is an experiment. State the hypothesis, make the smallest change, measure against the predicate on the real artifact, keep it if it advanced, revert only that unit's own changes if it didn't; preserve user and sibling work.
Apply the **pstack-principle-sequence-verifiable-units** principle skill, verifying each unit before starting the next instead of batching checks at the end.

- Verify by inspecting the artifact, never a self-report. When something passes too easily, suspect the observation method before the system.
- Pair delegated work with a judge. If a worker games the gate, reset and harden the contract. If the gate itself is wrong, fix the gate in its own change rather than routing around it.
- A verdict is VERIFIED, NOT VERIFIED, or INCONCLUSIVE. Inconclusive is not a pass. Don't hide a negative.

## Phase D: Keep the audit trail

Log the run via the **pstack-show-me-your-work** skill. figure-it-out's work is usually ambitious enough to retain the trail with the approved artifacts so the reviewer can read it; commit or publish it only within explicitly authorized shipping scope. The trail plus the diff is what lets the human come back and trust the work.

## Phase E: Verify and hand back

Check the whole against the Phase A predicate on the real product, not just the harness. Encode any recurring correction as a gate, a lint rule, a check, or a script (the **pstack-principle-encode-lessons-in-structure** principle skill).

**Reply:** the playbook you designed, the rigor level and why, the decision-trail path, what's verified against the predicate, and what's still open.


## Pitfalls

Branch names do not isolate shared working trees. Gates can be wrong; fix the gate separately rather than routing around it. Reverts must preserve unrelated work. A long run and publication need explicit checkpoints, not blanket autonomy.

## Verification

Test every unit and the whole product against the falsifiable done predicate, inspect real artifacts independently, and return VERIFIED / NOT VERIFIED / INCONCLUSIVE with the phase plan, rigor rationale, audit path, and open gaps.

## Attribution

Adapted from Lauren Tan's MIT-licensed pstack 0.15.6, source revision `23e4138daa01c42d4969f7a5465f82704e64f798`. See `references/license.md`.
