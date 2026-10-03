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

{{runtime.task_tracking}}

{{runtime.skill_loading}}

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
{{runtime.delegation}}

- Decide what fans out. Parallelize only across seams and give concurrent writers separate working trees or disjoint ownership (the **pstack-principle-separate-before-serializing-shared-state** principle skill). Don't over-fan. A branch alone does not isolate concurrent edits. The coordinator schedules later waves and verifies every artifact. Without independent delegation, execute the same units inline.
- Write the designed phase list down. That list is what the human reviews.

{{runtime.persistent_work}}

Then execute the design only within the authorized edit scope. A playbook or skill invocation grants no permission to ship, merge, delete unrelated work, or alter configuration. Add its steps to the todolist as concrete items, after the Phase C entry and before Phase D. Run each under the Phase C loop discipline, and weave the Phase D log through them, a row as each step lands, rather than saving the whole trail for the end.

## Phase C: Run the loop

{{runtime.files}}

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
