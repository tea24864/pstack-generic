---
name: pstack-principle-outcome-oriented-execution
description: "Verify end states at explicit migration boundaries."
license: MIT
metadata:
  author: "Lauren Tan (poteto), tea24864"
  version: "0.2.0"
  source-revision: "23e4138daa01c42d4969f7a5465f82704e64f798"
---

# Outcome-Oriented Execution

## When to Use

Use for planned rewrites or migrations with explicit verification boundaries.

## Procedure

Optimize for the intended, verifiable end state rather than preserving smooth intermediate states.

**Why:** Keeping every intermediate step fully stable often creates temporary compatibility code that becomes long-lived debt. Converge on the target architecture and prove correctness at explicit verification boundaries.

**Core rule:**
- Prioritize end-state integrity over transitional stability
- Intermediate breakage is acceptable when it is planned, scoped, and reversible

**Guardrails:**
- Use this for planned rewrites and migrations with explicit phase boundaries
- Declare where temporary breakage is acceptable
- Keep high-signal checks for actively touched areas while migrating
- Require full static and runtime verification at plan completion

Honor compatibility promises to external users and shared production uptime. Planned intermediate breakage belongs only in the explicitly approved isolated migration scope.

**Example:** In an approved isolated migration, replace the data model first, migrate callers at the next gate, then run the complete contract suite before delivery.

## Pitfalls

Temporary breakage is not permission to disrupt shared production or violate external compatibility; keep it isolated, planned, and reversible.

Stay within the user's task scope and available capabilities. This principle does not authorize publication, merges, destructive cleanup, or configuration changes; preserve approval gates and compatibility commitments.

## Verification

Record approved temporary-breakage scope and phase gates. Run touched-area checks during migration and the complete static and execution checks at completion; do not declare success while a target invariant or compatibility promise is unverified. State the decision changed, retain actual evidence, and disclose remaining uncertainty.

## Attribution

Adapted from Lauren Tan's MIT-licensed pstack 0.15.6, source revision `23e4138daa01c42d4969f7a5465f82704e64f798`. Port contributions: tea24864. See [MIT license](references/license.md).
