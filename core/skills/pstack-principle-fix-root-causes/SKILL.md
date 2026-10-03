---
name: pstack-principle-fix-root-causes
description: "Reproduce defects and fix their demonstrated cause."
license: MIT
metadata:
  author: "Lauren Tan (poteto), tea24864"
  version: "0.2.0"
  source-revision: "23e4138daa01c42d4969f7a5465f82704e64f798"
---

# Fix Root Causes

## When to Use

Use when debugging a reproducible defect or a failure after restart.

## Procedure

When debugging, do not fix symptoms. Trace every problem to its root cause and fix it there.

**Why:** Symptom fixes accumulate. Each workaround makes the system harder to reason about, and the real bug remains. Root-cause fixes are slower upfront but reduce total debugging time.

**Pattern:**
- Reproduce first
- Ask "why" until you hit the root cause
- Do not add guards (adding a nil check to silence a crash is a symptom fix)
- If a workaround needs a paragraph-long comment to justify it, the code is wrong (fix the code, not the comment)
- Check for the pattern, not just the instance (search the repository for the same pattern and fix the in-scope instances)
- When stuck, instrument. Don't guess (add logging, read the actual error)

**Restart bugs: suspect state before code**

When something "fails after restart," suspect stale persistent state first: config files, caches, lock files, serialized state. If clearing a state file restores behavior, prioritize state validation as the fix.

State-reset experiments need an isolated copy and explicit cleanup scope. Do not delete production caches or persistent state merely to test a hypothesis.

## Pitfalls

Guards may be valid boundary handling, but must not merely hide the defect. Never reset production state to test a hypothesis.

Stay within the user's task scope and available capabilities. This principle does not authorize publication, merges, destructive cleanup, or configuration changes; preserve approval gates and compatibility commitments.

## Verification

Demonstrate the original failure, the causal evidence, and the same check passing after the fix. Search for the pattern and account for all in-scope instances. For restart bugs, rerun with persisted state; keep reset experiments isolated. State the decision changed, retain actual evidence, and disclose remaining uncertainty.

## Attribution

Adapted from Lauren Tan's MIT-licensed pstack 0.15.6, source revision `23e4138daa01c42d4969f7a5465f82704e64f798`. Port contributions: tea24864. See [MIT license](references/license.md).
