---
name: pstack-principle-redesign-from-first-principles
description: "Integrate new requirements into a coherent design."
license: MIT
metadata:
  author: "Lauren Tan (poteto), tea24864"
  version: "0.2.0"
  source-revision: "23e4138daa01c42d4969f7a5465f82704e64f798"
---

# Redesign From First Principles

## When to Use

Use when a new requirement changes an existing design.

## Procedure

When integrating a change, don't bolt it onto the existing design. Redesign as if the requirement had been there from the start.

- Read all affected files and understand the current design
- Ask: "if we were writing this from scratch with this new requirement, what would we build?"
- Propagate the change through every reference: types, docs, examples, rationale sections
- Think about the whole redesign, then deliver it incrementally

This is the method for preserving option value when integrating changes into an existing design.

**Example:** Adding multi-account support should reshape account ownership and callers coherently, not bolt a second account flag onto every layer.

## Pitfalls

A coherent target design is not permission for an unbounded rewrite; deliver within the granted scope.

Stay within the user's task scope and available capabilities. This principle does not authorize publication, merges, destructive cleanup, or configuration changes; preserve approval gates and compatibility commitments.

## Verification

Compare the integrated design with the stated new requirement. Account for every affected type, caller, document, example, and rationale; verify each delivered increment and disclose remaining inconsistencies. State the decision changed, retain actual evidence, and disclose remaining uncertainty.

## Attribution

Adapted from Lauren Tan's MIT-licensed pstack 0.15.6, source revision `23e4138daa01c42d4969f7a5465f82704e64f798`. Port contributions: tea24864. See [MIT license](references/license.md).
