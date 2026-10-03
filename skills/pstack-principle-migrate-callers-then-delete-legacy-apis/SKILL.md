---
name: pstack-principle-migrate-callers-then-delete-legacy-apis
description: "Migrate internal callers and remove obsolete APIs."
version: 0.1.0
author: "Lauren Tan (poteto), tea24864, Hermes Agent"
license: MIT
platforms: ["linux", "macos"]
metadata:
  hermes:
    tags: [pstack, engineering, workflow]
    related_skills: []
---
# Migrate Callers Then Delete Legacy APIs

## When to Use

Use when migrate internal callers and remove obsolete APIs. Do not treat a design principle as a mandate to expand the task.

## Prerequisites

Read `references/hermes-runtime.md` with `skill_view` before executing this workflow. Use only tools and credentials actually available in this session. Invoking this skill does not authorize publication, merges, destructive cleanup, or configuration changes.

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

Apply the rule to observed constraints, not as an absolute ban. Preserve approval gates, compatibility contracts, and higher-priority user instructions. The runtime contract defines tool and profile boundaries.

## Verification

Name the concrete decision this principle changed and the artifact or evidence that supports it. For execution claims, use real tool output; for a design judgment, state its constraints and remaining uncertainty.

## Attribution

Adapted from Lauren Tan's MIT-licensed pstack 0.15.6, source revision `23e4138daa01c42d4969f7a5465f82704e64f798`. See `references/license.md`.
