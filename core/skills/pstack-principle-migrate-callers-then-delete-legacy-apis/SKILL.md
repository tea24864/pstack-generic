---
name: pstack-principle-migrate-callers-then-delete-legacy-apis
description: "Migrate internal callers and remove obsolete APIs."
license: MIT
metadata:
  author: "Lauren Tan (poteto), tea24864"
  version: "0.2.0"
  source-revision: "23e4138daa01c42d4969f7a5465f82704e64f798"
---

# Migrate Callers Then Delete Legacy APIs

## When to Use

Use when replacing an internal API without external compatibility obligations.

## Procedure

When we decide a new API is the right design, migrate callers and remove the old API in the same refactor wave instead of preserving compatibility layers.

**Rule:**
- Do not keep legacy API paths only because internal callers still exist
- Inventory callers, migrate them, and delete the old API immediately
- Treat temporary adapters as exceptional and time-boxed, not default architecture
- Update tests to assert the new contract, and delete tests that only protect pre-refactor implementation details

**When this applies:**
- No external users depend on backward compatibility
- The project can absorb coordinated breaking changes
- The new API is part of a simplification or refactor initiative

Keeping both old and new APIs creates dual-path complexity, slows cleanup, and makes the codebase feel append-only.

Honor compatibility promises to external users and shared production uptime. Planned intermediate breakage belongs only in the explicitly approved isolated migration scope.

## Pitfalls

External compatibility and shared production uptime still bind. Temporary breakage needs an explicitly approved isolated scope.

Stay within the user's task scope and available capabilities. This principle does not authorize publication, merges, destructive cleanup, or configuration changes; preserve approval gates and compatibility commitments.

## Verification

Search the full approved scope for old API references; account for callers, tests, docs, and exceptional adapters. Run checks for the new contract and show legacy paths are absent without breaking external compatibility promises. State the decision changed, retain actual evidence, and disclose remaining uncertainty.

## Attribution

Adapted from Lauren Tan's MIT-licensed pstack 0.15.6, source revision `23e4138daa01c42d4969f7a5465f82704e64f798`. Port contributions: tea24864. See [MIT license](references/license.md).
