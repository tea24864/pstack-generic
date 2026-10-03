---
name: pstack-principle-build-the-lever
description: "Build rerunnable tools for nontrivial work and checks."
license: MIT
metadata:
  author: "Lauren Tan (poteto), tea24864"
  version: "0.2.0"
  source-revision: "23e4138daa01c42d4969f7a5465f82704e64f798"
---

# Build the Lever

## When to Use

Use when nontrivial edits, analysis, or verification need a repeatable recipe.

## Procedure

When the work isn't trivial, build the tool that does it instead of doing it by hand.

**Why:** Two payoffs. Throughput: a codemod, generator, or script does the work the same way every time and reruns for free. Confidence: the tool is one artifact a reviewer can read and rerun to check the work. Hand-done changes can only be re-verified by redoing them. A deterministic script turns "trust me" into "run this".

**Pattern:** Default to building the lever. Skip it only when the task is trivial, a couple of obvious edits you can see at a glance.

- Do the first unit by hand to learn the recipe, then build the tool. Prove it by rerunning it on that unit and diffing against your hand-done version. Make the lever safe to rerun.
- Codemod or script for edits, generator for repetitive files, a dump-to-sqlite query for analysis, a rerunnable check for verification.
- A deterministic lever beats fan-out. If the tool can process every unit in one pass, run it yourself. Don't fan out delegates to hand-apply what a script can do.
- When you fan work out to subagents, write the lever as a skill they all read: the recipe, the verification contract, and the do-not-touch fences in one artifact. Keep it outside the delegates' write scope so they can't quietly edit the contract.
- Applying this principle produces a file. If you cited it and there is no codemod, script, generator, or delegate skill in the diff, you didn't apply it.
- Preserve the lever when the work outlives the session; commit it only when that delivery is authorized.

**Balance:** The bar is triviality, not repetition. A one-off still earns a lever when the lever is what makes the work checkable. Per the [Laziness Protocol](../pstack-principle-laziness-protocol/SKILL.md), build the smallest script that does or proves the job, never a framework.

Distinct from [Encode Lessons in Structure](../pstack-principle-encode-lessons-in-structure/SKILL.md), which makes a recurring instruction a durable guardrail. This is throughput and reviewability on the work in front of you. For scripting the verification itself, see [Prove It Works](../pstack-principle-prove-it-works/SKILL.md).

## Pitfalls

Build the smallest tool, not a framework. Preserve or commit reusable artifacts only within the approved delivery scope.

Stay within the user's task scope and available capabilities. This principle does not authorize publication, merges, destructive cleanup, or configuration changes; preserve approval gates and compatibility commitments.

## Verification

Run the lever on the hand-checked unit and compare outputs. Rerun it to prove safety, then check every processed unit. Retain the tool and actual output so another reviewer can reproduce the result. State the decision changed, retain actual evidence, and disclose remaining uncertainty.

## Attribution

Adapted from Lauren Tan's MIT-licensed pstack 0.15.6, source revision `23e4138daa01c42d4969f7a5465f82704e64f798`. Port contributions: tea24864. See [MIT license](references/license.md).
