---
name: pstack-principle-guard-the-context-window
description: "Keep bulk payloads out of the main reasoning context."
license: MIT
metadata:
  author: "Lauren Tan (poteto), tea24864"
  version: "0.2.0"
  source-revision: "23e4138daa01c42d4969f7a5465f82704e64f798"
---

# Guard the Context Window

## When to Use

Use when large outputs, documents, or long phases threaten reasoning continuity.

## Procedure

The context window is finite; compression can lose detail within a session. Every token should be worth its cost.

**Why:** Context overflow degrades reasoning quality, creates compression artifacts, and halts progress.

**Pattern:**
- **Isolate large payloads.** Extract or summarize verbose outputs, screenshots, and large documents outside the main reasoning context. Use independent workers when available and appropriate; return summaries and evidence locations, not raw bulk.
- **Keep frequently used content inline.** Templates and references used on every invocation belong in the skill file, not in separate files that cost a read each time.
- **Size phases and cap scope.** Limit files per phase, set turn budgets, account for mechanism costs.

Prefer deterministic extraction scripts for mechanical bulk. Reopen source instructions lost to compression before relying on them, and save resumable evidence in the task workspace rather than assuming child contexts persist.

## Pitfalls

Summaries are indexes, not replacements for evidence. Do not assume delegated contexts persist or that lost instructions remain known.

Stay within the user's task scope and available capabilities. This principle does not authorize publication, merges, destructive cleanup, or configuration changes; preserve approval gates and compatibility commitments.

## Verification

Keep bulk artifacts outside the main reasoning context and return bounded summaries with exact evidence locations. Demonstrate the next phase can resume from saved decisions/results; reopen any pruned source before relying on it. State the decision changed, retain actual evidence, and disclose remaining uncertainty.

## Attribution

Adapted from Lauren Tan's MIT-licensed pstack 0.15.6, source revision `23e4138daa01c42d4969f7a5465f82704e64f798`. Port contributions: tea24864. See [MIT license](references/license.md).
