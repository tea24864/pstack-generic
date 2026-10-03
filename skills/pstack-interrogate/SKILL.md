---
name: pstack-interrogate
description: "Challenge changes with independent adversarial reviews."
license: MIT
metadata:
  hermes: {"tags": ["pstack", "engineering", "workflow"], "config": [{"key": "pstack.panel_size", "description": "Default independent panel size; explicit scope wins.", "default": 3, "prompt": "Default independent panel size"}, {"key": "pstack.model_strategy", "description": "Policy only; external runners require separate verification.", "default": "inherit-parent", "prompt": "Model strategy (inherit-parent or verified-external)"}]}
  author: "Lauren Tan (poteto), tea24864"
  version: "0.2.0"
  source-revision: "23e4138daa01c42d4969f7a5465f82704e64f798"
---

# Interrogate

## When to Use

Use for adversarial review, stress testing a diff, or blind-spot checks. The deliverable is a verdict, never automatically applied fixes.

## Prerequisites

Load named skills with `skill_view(name="pstack-...")`; load supporting material with the same skill name and `file_path="references/..."`. Resolve all paths to the actual loaded skill directory. Do not invent missing skills or assume another profile shares the same catalog.

Use only capabilities and credentials actually available in this session. Invoking this workflow does not authorize publication, merges, destructive cleanup, dependency installation, or configuration changes. Preserve the caller's scope and user-owned state.

## Procedure

Spawn independent reviewers to challenge code changes. Every reviewer gets the same intent, prompt, rubric, and code-quality lens. Record actual reviewer model policy. Same-model independence is useful but is not model-diversity signal; disclose that limitation when it applies.

The deliverable is a synthesized verdict. Do NOT auto-apply changes.

## Step 1, Determine Scope

Use `read_file`, `search_files`, `write_file` and `patch` for file work; use `terminal(command="...", timeout=...)` for real Git, helpers and tests. Read existing files before full replacement. Bundle mechanical loops through `execute_code` when appropriate. Use actual tool output as evidence.

Identify what to review from context:

- If the user points at specific files or a diff, use that
- If on a feature branch, run `git diff main...HEAD` (or the appropriate base branch) for the full changeset
- If the user's message references recent work, gather the relevant files

Package the diff (or file contents) plus any surrounding context files the reviewers need to understand the code.

## Step 2, State the Intent

Before spawning reviewers, state the intent explicitly. Derive this from:

- The user's message
- Commit messages
- PR description if one exists
- The code itself

Write one clear paragraph. If you're unsure about the intent, ask the user before proceeding.

## Step 3, Spawn Reviewers

Use three independent reviewers by default, or the user's bounded count. Follow the worker execution boundary below. Prepare completed immutable review inputs and give each the filled reviewer template, exact diff/context paths, base/head SHAs, no-write restriction and a request for every proven finding with severity, location and evidence. Do not share peer findings before completion. No-write prose is not a sandbox. If independent execution is unavailable, perform the rubric review directly and state that panel coverage was unavailable.

For genuine multi-model review, verify external agent CLI capability and actual available provider/model options, obtain explicit user scope, and record what really ran. A configuration entry alone does not prove runtime support. Never invent model slugs or fallbacks.

Read `references/reviewer-prompt.md` and fill in the template with:
1. The stated intent
2. The diff or file contents
3. The review rubric from `references/rubric.md`
4. The code-quality lens from `references/code-quality-review.md`

The same filled template goes to all reviewers, so every model applies the code-quality lens.

## Step 4, Synthesize

As results come back, build a unified picture:

1. **Parse all findings** from the reviewers
2. **Identify consensus**. Findings raised by 2+ reviewers independently are highest signal.
3. **Identify lone-reviewer findings**. Still worth reading, but weight accordingly.
4. **Deduplicate**. Different reviewers may describe the same issue differently. Merge these and note which reviewers raised it.
5. **Note disagreements**. If one reviewer flags something and another reviewer explicitly says the opposite, that's useful context for the verdict.

## Step 5, Lead Judgment

You are the lead reviewer, a pragmatic senior engineer, not a neutral aggregator.

Read `references/lead-judgment.md` for the full framework.

Categorize every finding using these buckets:

- **Act on**. Real issues affecting correctness, security, or maintainability given the actual goals. These would block a real PR.
- **Consider**. Legitimate points, but you're not sure they outweigh the cost of addressing them right now. Worth the user's attention.
- **Noted**. Technically valid but not actionable. Context-dependent, premature optimization, or low-impact given the current stage.
- **Dismissed**. Wrong, nitpicky, or missing context. Brief explanation why.

For each finding, include:
- Which reviewer(s) raised it
- The category (act on / consider / noted / dismissed)
- A one-line rationale for the categorization

## Output Format

Present the verdict in this structure:

### Intent
> [The stated intent paragraph from Step 2]

### Reviewers
- Reviewer [label]: [actual model/provider or inherited-model label], [N findings, status and evidence gaps] (one bullet per reviewer)

### Act On
[Findings that should be addressed. For each: description, which reviewers raised it, why it matters.]

### Consider
[Findings worth thinking about. For each: description, which reviewers raised it, tradeoff involved.]

### Noted
[Valid but low-priority. Brief list.]

### Dismissed
[Rejected findings with brief rationale.]

### Agreement Map
[Where did reviewers agree, where did they diverge, and what does the pattern of agreement/disagreement tell us?]

## Worker execution boundary

Use `delegate_task(tasks=[{"goal":"...","context":"..."}, ...])` for independent children. Each brief includes scope, evidence, exclusive output/worktree, verification and no delegation or user questions. Children share filesystems; read-only prompts are not sandboxes. Native children inherit the parent model or global pin: do not pass model/provider/readonly/background arguments or claim model diversity. Budget candidates, judges and synthesis together; obey confirmed concurrency and one-shot total-child limits. On exhaustion finish permitted lenses inline and label reduced independence, never retry or change global settings. For async delivery, finish independent work and end the turn; do not poll transcripts. Parent verifies returned artifacts and coordinates later waves. If an independent panel is explicitly required and unavailable, mark it blocked rather than substituting silently.

Every brief stands alone: scope, exact paths and revisions, inputs, acceptance criteria, verification commands, budget, forbidden actions and report format. A read-only instruction is not a sandbox. Concurrent writers own exclusive worktrees/branches; artifact-only candidates use separate output directories. The coordinator relays dependencies and integrates only completed, checked artifacts.

Do not call repeated same-model attempts model diversity. Genuine diversity needs verified available runners and actual provider/model choices within explicit scope. Record what ran and its correlated-model limitation; never invent models or silently change providers. Budget candidates, judging, synthesis and verification together. When independent execution is absent or exhausted, do assigned work directly, preserve distinct alternatives where required, and disclose lost independence rather than retrying a known exhausted budget.


## Pitfalls

Keep the user's scope and explicit checkpoints. Missing evidence or unavailable dependencies are gaps, not passes. Do not replace a working existing skill or change another user-owned execution environment.

## Verification

Check each promised artifact and claim against a real tool result. Report evidence, skipped checks, and limitations. A child's self-report is not independent verification.

## Attribution

Adapted from Lauren Tan's MIT-licensed pstack 0.15.6, source revision `23e4138daa01c42d4969f7a5465f82704e64f798`. See `references/license.md`.
