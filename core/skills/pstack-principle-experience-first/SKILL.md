---
name: pstack-principle-experience-first
description: "Choose scope and design for the consumer experience."
license: MIT
metadata:
  author: "Lauren Tan (poteto), tea24864"
  version: "0.2.0"
  source-revision: "23e4138daa01c42d4969f7a5465f82704e64f798"
---

# Experience First

## When to Use

Use when scope or implementation choices affect consumers and maintainers.

## Procedure

When implementation convenience conflicts with user delight, choose delight.

- Every feature, control, and option must be justified
- Ship less, ship better (polished experience with three features beats rough one with ten)
- Prototype before committing (design decisions are cheaper in throwaway HTML than production code)
- Get the details right (transitions, alignment, spacing, feedback, error states)
- Tighten the core loop (every feature should serve the central workflow or get out of the way)

The user is whoever consumes the work. For a UI that is the end user. For a library or an internal API it is the colleague who imports it. The engineer who maintains the code next is a user too. Weigh their experience the same way, and explain impact from their perspective.

Foundations should serve the experience. Foundational thinking governs the *sequence* of work. This principle governs the *target*.

## Pitfalls

Experience includes the importing colleague and future maintainer, not only the visible UI. Delight does not override required behavior.

Stay within the user's task scope and available capabilities. This principle does not authorize publication, merges, destructive cleanup, or configuration changes; preserve approval gates and compatibility commitments.

## Verification

Exercise the central workflow as its consumer, including feedback and error states. Justify retained controls and scope; show the prototype or implementation evidence behind the choice and note remaining experience gaps. State the decision changed, retain actual evidence, and disclose remaining uncertainty.

## Attribution

Adapted from Lauren Tan's MIT-licensed pstack 0.15.6, source revision `23e4138daa01c42d4969f7a5465f82704e64f798`. Port contributions: tea24864. See [MIT license](references/license.md).
