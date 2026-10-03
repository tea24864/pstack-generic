---
name: pstack-principle-exhaust-the-design-space
description: "Compare distinct designs before choosing a new shape."
license: MIT
metadata:
  author: "Lauren Tan (poteto), tea24864"
  version: "0.2.0"
  source-revision: "23e4138daa01c42d4969f7a5465f82704e64f798"
---

# Exhaust the Design Space

## When to Use

Use when a novel interaction or architectural choice has several viable shapes.

## Procedure

When a novel interaction or architectural decision has no established precedent, explore several concrete alternatives before implementation. Building the wrong thing costs more than exploring three options.

**The rule.** When the right answer is not obvious, build 2-3 competing prototypes or sketches. Compare them side by side. Only then commit. Design it twice is this rule by another name. A second flavor of the first shape does not count.

**When it applies:**
- Novel UI interactions (no prior art in the codebase)
- Architectural choices with multiple viable approaches
- Product design decisions where user experience depends on feel, not logic

**When it doesn't:**
- Mechanical implementation where the pattern is established
- Bug fixes or refactors with a clear target state
- Changes where constraints dictate a single viable approach

**Example:** Compare an inline editor, a modal editor, and a dedicated editing view for the same workflow; three color schemes for one modal do not count.

## Pitfalls

Variants of the same shape are not alternatives; mechanical changes with a clear target do not require prototypes.

Stay within the user's task scope and available capabilities. This principle does not authorize publication, merges, destructive cleanup, or configuration changes; preserve approval gates and compatibility commitments.

## Verification

Retain 2-3 genuinely different sketches or prototypes, compare them against the same constraints, and explain the selected shape and rejected tradeoffs. If there is only one viable option, document why exploration was unnecessary. State the decision changed, retain actual evidence, and disclose remaining uncertainty.

## Attribution

Adapted from Lauren Tan's MIT-licensed pstack 0.15.6, source revision `23e4138daa01c42d4969f7a5465f82704e64f798`. Port contributions: tea24864. See [MIT license](references/license.md).
