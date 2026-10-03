---
name: pstack-principle-attack-the-premise
description: "Challenge shared assumptions after repeated failed fixes."
license: MIT
metadata:
  author: "Lauren Tan (poteto), tea24864"
  version: "0.2.0"
  source-revision: "23e4138daa01c42d4969f7a5465f82704e64f798"
---

# Attack the Premise

## When to Use

Use when two or more fixes sharing an assumption fail the same gate.

## Procedure

When two or more fixes that share one premise have failed the same gate, suspect the premise, not the fixes.

**Why:** Each failure under a shared premise is evidence about the premise.

**Pattern:**
- **Write the premise down.** The premise is the one sentence that every failed fix assumed.
- **Take a census before the next fix.** Count the imbalance per actor. The census shows which actors hold the imbalance, not how large it is. Write the census as a rerunnable script per [Build the Lever](../pstack-principle-build-the-lever/SKILL.md).
- **Read the skew.** If the same few actors hold most of the imbalance on every run, something assigns them that role. Find what assigns the role. That assignment is the next "why" per [Fix Root Causes](../pstack-principle-fix-root-causes/SKILL.md).
- **Remove the asymmetry instead of compensating for it**, per the [Laziness Protocol](../pstack-principle-laziness-protocol/SKILL.md). Rotate the role between actors, randomize the assignment, or move the role, so that no actor holds it on every run. A return path, a shared pool, a batched hand-off, or a periodic rebalance leaves the assignment in place and adds work on every run.

**Stop:**
- Do not start the next fix before the premise is written down and the census exists.
- If the census is even across actors, the premise is not the cause. Look for the cause elsewhere and keep the census as evidence.

This principle is distinct from [Redesign from First Principles](../pstack-principle-redesign-from-first-principles/SKILL.md), which rebuilds a design around a new requirement. It questions a fact the current design assumes.

## Pitfalls

Do not replace an untested premise with another guess; an even census is evidence to look elsewhere.

Stay within the user's task scope and available capabilities. This principle does not authorize publication, merges, destructive cleanup, or configuration changes; preserve approval gates and compatibility commitments.

## Verification

Keep the written premise, rerunnable census, and gate results. Show the per-actor distribution before and after changing the assignment; if it is even, reject this hypothesis rather than compensating for it. State the decision changed, retain actual evidence, and disclose remaining uncertainty.

## Attribution

Adapted from Lauren Tan's MIT-licensed pstack 0.15.6, source revision `23e4138daa01c42d4969f7a5465f82704e64f798`. Port contributions: tea24864. See [MIT license](references/license.md).
