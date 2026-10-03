---
name: pstack-how
description: "Explain runtime flow, ownership, and code architecture."
version: 0.1.0
author: "Lauren Tan (poteto), tea24864, Hermes Agent"
license: MIT
platforms: ["linux", "macos"]
metadata:
  hermes:
    tags: [pstack, engineering, workflow]
    related_skills: ["pstack-why", "pstack-teach"]
    config:
      - key: pstack.panel_size
        description: Default independent panel size; explicit scope wins.
        default: 3
        prompt: Default independent panel size
      - key: pstack.model_strategy
        description: Policy only; external runners require separate verification.
        default: inherit-parent
        prompt: Model strategy (inherit-parent or verified-external)
---

# How

## When to Use

Use for “how does X work”, subsystem onboarding, code walkthroughs, ownership, placement, or layering questions. Use `pstack-why` for motivation. Investigation is read-only.

## Prerequisites

Read `references/hermes-runtime.md` with `skill_view` before executing this workflow. Use only tools and credentials actually available in this session. Invoking this skill does not authorize publication, merges, destructive cleanup, or configuration changes.

## Procedure

Explore the codebase to answer "how does X work?" questions. Produce architectural explanations at the level of a senior engineer onboarding onto a subsystem, enough to build a working mental model, not so much that it reads like annotated source code.

Delegation uses `delegate_task(tasks=[{"goal": "...", "context": "..."}])` only after discovering its actual schema. Roles are prompt lenses, not per-task models. Optional `skills.config.pstack.*` values are descriptive runtime preferences (default inherit-parent); do not change configuration or pass unsupported `model`, `readonly`, `subagent_type`, `environment`, or `run_in_background` fields. Children share the filesystem and must be explicitly told not to write or ask the user. Flatten later waves through the parent. If delegation is unavailable, execute the same evidence slices inline.

## Step 1. Assess Complexity

If the scope is ambiguous, state your interpretation and explore. The user can redirect.

- **Simple** (a single module, a small utility, a narrow question such as "how does function X work"): no explorers. One explainer explores and explains in a single pass. Go to Step 2b.
- **Complex** (a subsystem spanning multiple files or services, a cross-cutting feature, a full architectural overview): spawn parallel explorers first, then hand off to the explainer. Go to Step 2a.

When in doubt, take the simple path.

## Step 2a. Explore (complex questions only)

Decompose the question into 2 to 4 exploration angles, each a distinct slice of the subsystem. Launch the explorer wave in one `delegate_task` tasks batch, subject to the discovered concurrency limit. Each goal names an angle; context includes the question, code roots, and full reference prompt. No incidental writes.

Each explorer gets the prompt in `references/explorer-prompt.md` with its angle filled in. Then go to Step 3.

## Step 2b. Direct Explain (simple questions)

Use one `delegate_task` child (or work inline) to explore and explain in one pass. Pass the complete explainer prompt and read-only behavioral scope.

Build its prompt from `references/explainer-prompt.md` without the explorer-findings section. Go to Step 4.

## Step 3. Synthesize (complex questions only)

Once the parent has every explorer result, launch one synthesis child, or synthesize inline. Give it the question, all findings, the complete explainer prompt, and a no-writes scope. Children never delegate.

Build its prompt from `references/explainer-prompt.md` with every explorer's findings filled in.

## Step 4. Present

Present the explainer's output to the user. Light edits for clarity or context from the conversation are fine. Do not substantially rewrite it.

## Output Format

The explanation uses the sections defined in `references/explainer-prompt.md`, dropping any that do not apply: Overview, Key Concepts, How It Works, Where Things Live, Gotchas.


## Pitfalls

Names are not behavior. Resolve contradictions in actual code. Read-only delegation is not filesystem isolation. Do not invent ownership, historical intent, tools, or model diversity.

## Verification

Spot-check entry points, flow boundaries, and cited file/line claims using `read_file` and `search_files`. Return the mental model plus open questions, not agent activity narration. Confirm all requested angles are accounted for.

## Attribution

Adapted from Lauren Tan's MIT-licensed pstack 0.15.6, source revision `23e4138daa01c42d4969f7a5465f82704e64f798`. See `references/license.md`.
