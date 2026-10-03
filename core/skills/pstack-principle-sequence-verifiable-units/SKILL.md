---
name: pstack-principle-sequence-verifiable-units
description: "Deliver work as small independently verifiable units."
license: MIT
metadata:
  author: "Lauren Tan (poteto), tea24864"
  version: "0.2.0"
  source-revision: "23e4138daa01c42d4969f7a5465f82704e64f798"
---

# Sequence work into verifiable units

## When to Use

Use when a sweep, migration, or delivery contains several dependent changes.

## Procedure

Order work as a sequence of small units, each ending in a state you can check, and don't advance until the current one is green.

**Why:** A break caught at the unit that caused it is cheap to localize. A break caught after a batch is buried, and you have already built further on a broken base. Sequencing those same units into a delivery a reviewer can replay turns "trust me" into "watch it go red, then green."

**Execution.** In a sweep, migration, or any run of similar edits, verify each change before starting the next. Each unit is a before/after bracket: known-good state, one change, run the check, then proceed. Establish a clean, current baseline first; rebase only when that operation is authorized, so each check measures the real baseline. When a lever does the edits, the per-unit check is nearly free. Run it anyway.

**Delivery.** Stack commits and PRs in the order that proves the work. The canonical shape is the failing test first, then the fix on top. Other story orders are a subtraction before the reshape, a baseline capture before the treatment, the scaffold before the feature. Each commit lands on its own and the sequence reads as an argument.

The sequencing complement to [Prove It Works](../pstack-principle-prove-it-works/SKILL.md), which keeps each check real, and [Build the Lever](../pstack-principle-build-the-lever/SKILL.md), which makes the per-unit check cheap.

Do not rebase, commit, push, or intentionally break a shared branch without the corresponding scope. Use isolated worktrees for staged failing tests and migration boundaries.

## Pitfalls

Do not rebase, commit, push, or intentionally break a shared branch without authorization. Stage failing tests and migration gates in isolation.

Stay within the user's task scope and available capabilities. This principle does not authorize publication, merges, destructive cleanup, or configuration changes; preserve approval gates and compatibility commitments.

## Verification

Record each unit's baseline, change, check, and result. Verify the current unit before advancing; if delivering a failing-test/fix sequence, demonstrate the intended red/green bracket in isolation and run final integration checks. State the decision changed, retain actual evidence, and disclose remaining uncertainty.

## Attribution

Adapted from Lauren Tan's MIT-licensed pstack 0.15.6, source revision `23e4138daa01c42d4969f7a5465f82704e64f798`. Port contributions: tea24864. See [MIT license](references/license.md).
