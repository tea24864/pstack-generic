---
name: pstack-how
description: "Explain runtime flow, ownership, and code architecture."
license: MIT
metadata:
  hermes: {"tags": ["pstack", "engineering", "workflow"], "config": [{"key": "pstack.panel_size", "description": "Default independent panel size; explicit scope wins.", "default": 3, "prompt": "Default independent panel size"}, {"key": "pstack.model_strategy", "description": "Policy only; external runners require separate verification.", "default": "inherit-parent", "prompt": "Model strategy (inherit-parent or verified-external)"}]}
  author: "Lauren Tan (poteto), tea24864"
  version: "0.2.0"
  source-revision: "23e4138daa01c42d4969f7a5465f82704e64f798"
---

# How

## When to Use

Use for “how does X work”, subsystem onboarding, code walkthroughs, ownership, placement, or layering questions. Use `pstack-why` for motivation. Investigation is read-only.

## Prerequisites

Use only capabilities and credentials actually available. This workflow does not authorize publication, merges, destructive cleanup, installation, or configuration changes.

## Procedure

Explore the codebase to answer "how does X work?" questions. Produce architectural explanations at the level of a senior engineer onboarding onto a subsystem, enough to build a working mental model, not so much that it reads like annotated source code.

Use `delegate_task(tasks=[{"goal":"...","context":"..."}, ...])` for independent children. Each brief includes scope, evidence, exclusive output/worktree, verification and no delegation or user questions. Children share filesystems; read-only prompts are not sandboxes. Native children inherit the parent model or global pin: do not pass model/provider/readonly/background arguments or claim model diversity. Budget candidates, judges and synthesis together; obey confirmed concurrency and one-shot total-child limits. On exhaustion finish permitted lenses inline and label reduced independence, never retry or change global settings. For async delivery, finish independent work and end the turn; do not poll transcripts. Parent verifies returned artifacts and coordinates later waves. If an independent panel is explicitly required and unavailable, mark it blocked rather than substituting silently.

## Step 1. Assess Complexity

If the scope is ambiguous, state your interpretation and explore. The user can redirect.

- **Simple** (a single module, a small utility, a narrow question such as "how does function X work"): no explorers. One explainer explores and explains in a single pass. Go to Step 2b.
- **Complex** (a subsystem spanning multiple files or services, a cross-cutting feature, a full architectural overview): run distinct exploration slices, in parallel when supported, then hand off to the explainer. Go to Step 2a.

When in doubt, take the simple path.

## Step 2a. Explore (complex questions only)

Decompose the question into 2 to 4 exploration angles, each a distinct slice of the subsystem. Assign one evidence task per angle with the question, code roots, complete reference prompt, and read-only scope. Coordinate supported parallel exploration, or run the same slices inline when independent delegation is unavailable.

Each explorer gets the prompt in `references/explorer-prompt.md` with its angle filled in. Then go to Step 3.

## Step 2b. Direct Explain (simple questions)

Use one explainer task, delegated when supported or inline, to explore and explain in one pass. Supply the complete prompt and read-only scope.

Build its prompt from `references/explainer-prompt.md` without the explorer-findings section. Go to Step 4.

## Step 3. Synthesize (complex questions only)

Once every explorer result is available, delegate synthesis when supported or synthesize inline. Supply the question, all findings, complete explainer prompt, and no-writes scope.

Build its prompt from `references/explainer-prompt.md` with every explorer's findings filled in.

## Step 4. Present

Present the explainer's output to the user. Light edits for clarity or context from the conversation are fine. Do not substantially rewrite it.

## Output Format

The explanation uses the sections defined in `references/explainer-prompt.md`, dropping any that do not apply: Overview, Key Concepts, How It Works, Where Things Live, Gotchas.


## Pitfalls

Names are not behavior. Resolve contradictions in actual code. Read-only delegation is not filesystem isolation. Do not invent ownership, historical intent, tools, or model diversity.

## Verification

Use `read_file`, `search_files`, `write_file` and `patch` for file work; use `terminal(command="...", timeout=...)` for real Git, helpers and tests. Read existing files before full replacement. Bundle mechanical loops through `execute_code` when appropriate. Use actual tool output as evidence.

Spot-check entry points, flow boundaries, and cited file/line claims against source. Return the mental model plus open questions, not agent activity narration. Confirm all requested angles are accounted for.

## Attribution

Adapted from Lauren Tan's MIT-licensed pstack 0.15.6, source revision `23e4138daa01c42d4969f7a5465f82704e64f798`. See `references/license.md`.
