---
name: pstack-architect
description: "Design types and boundaries before implementation."
license: MIT
metadata:
  author: "Lauren Tan (poteto), tea24864"
  version: "0.2.0"
  source-revision: "23e4138daa01c42d4969f7a5465f82704e64f798"
---

# Architect

## When to Use

Use for architecture sketches, nontrivial boundary changes, or "design this". Do not implement a design-only request.

## Prerequisites

{{runtime.skill_loading}}

Use only capabilities and credentials actually available in this session. Invoking this workflow does not authorize publication, merges, destructive cleanup, dependency installation, or configuration changes. Preserve the caller's scope and user-owned state.

## Procedure

Design before implementing. Sketch types, function signatures, class shapes, and module boundaries with `not implemented` bodies and pseudocode. Synthesize across independent candidate perspectives, then fill in code against the chosen sketch. If implementation proves the sketch wrong, throw it out and redesign.

## Start

{{runtime.task_tracking}}

1. Ground
2. Sketch
3. Agree
4. Implement
5. Scrap

## Phase A: Ground the problem

Build a real mental model of every system the new code touches. Run the **pstack-how** skill over the relevant subsystems.

Naming a file isn't grounding. Produce the traced model `pstack-how` prescribes. If the design redefines ownership or layering, also run the **pstack-why** skill on the existing shape so the rationale becomes a constraint, not a guess.

Skip Phase A only when the work is genuinely greenfield with no surrounding system to integrate.

## Phase B: Sketch

Run the **pstack-arena** skill with the design-sketch task and the Phase A grounding artifacts. Pass `references/runner-prompt.md` as each runner's prompt. Each candidate produces a design package shaped per `references/rationale-template.md`.

Use at least two independent candidates. Read the worker execution boundary below. The default is same-model exploration, not multi-model diversity; external diverse-model runners are opt-in and must be verified and authorized.

Budget grounding, candidates, synthesis and checkpoint together. For a small fixture use compact designs, not exhaustive supporting reports. If independent children or the cross-judge are unavailable or a verified one-shot child budget is exhausted, apply the arena fallback inline and disclose the loss of independent review; never retry an exhausted budget or leave synthesis unfinished merely because a third child cannot run. Preserve at least two structurally distinct designs.

Design it twice. Require at least two structurally distinct candidates before synthesis, even when the first looks sufficient. This is the **pstack-principle-exhaust-the-design-space** principle skill made concrete. Whole-shape alternatives, not point fixes inside one shape.

Screen every candidate against [`references/design-red-flags.md`](references/design-red-flags.md) before synthesis. Reject or revise shallow modules, information leakage, temporal decomposition, and pass-through methods.

Compare viable candidates on interface depth. Prefer the design that hides more complexity behind a smaller, simpler public surface. A rich interface can keep call chains short by concentrating capability instead of scattering it across layers.

Arena returns one synthesized design package. The synthesis decision populates the rationale's "Synthesis decision" section.

## Phase C: Agree (opt-in)

Default: proceed directly only when implementation is already in the user's scope. Design-only requests end with the sketch. User-requested checkpoints, scope expansions, and permission gates always stop implementation.

Opt in to a checkpoint when the invoker explicitly asks: "/pstack-architect with checkpoint," "stop and show me before implementing," or similar. Then surface the synthesized design and pause for sign-off.

Within authorized local repository scope, the synthesis can be recorded as its own scaffold commit, as the "scaffold first" mode of the **pstack-principle-foundational-thinking** principle skill. Planned and scoped breakage during fill-in is fine, per the **pstack-principle-outcome-oriented-execution** principle skill. For adversarial pressure on the design before implementing, run the **pstack-interrogate** skill on the synthesized sketch.

If the human pushes back on the shape (in a checkpoint or after the fact), treat that as Phase A evidence. Re-ground and re-run Phase B before writing more code.

## Phase D: Implement against the sketch

Replace `not implemented` bodies with code, pseudocode with logic. The synthesized sketch is the contract.

Deviations from the sketch are signal worth surfacing, not friction to absorb silently. If a function needs a parameter the sketch didn't anticipate, ask whether the sketch was wrong, the requirement was missed, or the implementation is overreaching.

## Phase E: Scrap when the architecture is wrong

If implementation keeps producing friction the sketch can't absorb, throw the sketch out. Don't bolt fixes onto a wrong design, per the **pstack-principle-redesign-from-first-principles** and **pstack-principle-fix-root-causes** principle skills.

The signal is a *pattern*, not single instances. Tells:

- The same shape of workaround appearing repeatedly across unrelated code.
- Multiple unrelated edge cases that all need special-case branches.
- Types that need escape hatches (`any`, casts, optional fields always set in practice) to compile.
- The "we need a lock" reflex when the sketch said the state wasn't shared.
- Callers having to know the abstraction's internal rules to use it.
- Two or more independent Phase D deviations of the same shape across the implementation.

Use judgment. A few edge cases don't condemn an architecture. Some problems are legitimately complex. Complexity in the data is not complexity in the design.

When you scrap:

1. Re-run the **pstack-how** skill over what's been built.
2. Redesign as if the new constraints had been day-one assumptions, per redesign-from-first-principles.
3. Subtract before adding, per the **pstack-principle-subtract-before-you-add** principle skill. The new sketch should be smaller than the old one before it grows.
4. Return to Phase B and re-run arena.

## Outputs

The caller's usage is written first and the type sketch derived from it. One file with new types and signatures for small changes. Module map plus type definitions for larger work. The rationale ships alongside, shaped per `references/rationale-template.md`, including the usage sketch and the synthesis decision.

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
