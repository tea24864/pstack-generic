---
name: pstack-interrogate
description: "Challenge changes with independent adversarial reviews."
version: 0.1.0
author: "Lauren Tan (poteto), tea24864, Hermes Agent"
license: MIT
platforms: ["linux", "macos"]
metadata:
  hermes:
    tags: [pstack, engineering, workflow]
    related_skills: ["pstack-architect", "pstack-arena", "pstack-poteto-mode"]
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
# Interrogate

## When to Use

Use for adversarial review, stress testing a diff, or blind-spot checks. The deliverable is a verdict, never automatically applied fixes.

## Prerequisites

Read `references/hermes-runtime.md` with `skill_view` before executing this workflow. Use only tools and credentials actually available in this session. Invoking this skill does not authorize publication, merges, destructive cleanup, or configuration changes.

## Procedure

Spawn independent reviewers to challenge code changes. Every reviewer gets the same intent, prompt, rubric, and code-quality lens. Native reviewers are same-model by default; independence is useful but cannot reproduce genuine model-diversity signal. Disclose that limitation.

The deliverable is a synthesized verdict. Do NOT auto-apply changes.

## Step 1, Determine Scope

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

Use three independent reviewers by default, or the user's bounded count. Follow the Hermes execution contract below. Prepare completed immutable review inputs and issue an explicit no-write instruction in each context; that instruction is not a sandbox. Launch `delegate_task(tasks=[{"goal": "Adversarially review the stated changes", "context": "Filled reviewer template, immutable diff/context paths, exact base and head SHAs, no writes, no delegation; return every proven finding with severity, location, evidence."}, {"goal": "Independently review the same changes", "context": "The same filled template, exact input paths/SHAs, and restrictions."}])`, extending to the reviewer count. Do not provide reviewer findings to peers before they finish. If the tool is unavailable, perform the rubric review directly and state that panel coverage was unavailable.

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

## Hermes execution contract

Use `delegate_task(tasks=[{"goal": "Produce the assigned artifact", "context": "Standalone brief with scope, exact paths, inputs, acceptance criteria, verification commands, write restrictions, and report format."}])` only when that tool is available to the parent. Discover its current schema first. Do not add Cursor-only arguments. Child conversations are isolated but the filesystem is shared. A read-only instruction is not a sandbox. Give concurrent repository writers separate git worktrees and branches; artifact-only candidates may use separate output directories under the agreed workspace or `$TMPDIR`.

Children cannot call `delegate_task` or clarify. The parent coordinates flattened waves and relays dependency results. A child executing this workflow does its assigned leaf work directly, returns evidence and proposed next-wave briefs, and never waits for grandchildren. For asynchronous delegation, results arrive after the parent ends its turn; do not poll child transcripts. Children are bounded and die on stop or session end. Durable work requires separately authorized cron or independent processes, not a claim that a child is persistent.

Delegates use the current parent model or the global delegation pin. Optional `skills.config.pstack.*` runtime policy defaults to `inherit-parent`; it does not create a per-task model argument. Call the default panel independent same-model attempts and disclose its correlated-model limitation. Genuine model diversity requires verified external agent CLI support, explicit user scope, and provider/model selections from currently available options. Do not invent model names or silently substitute providers. See `references/hermes-runtime.md` for the shared policy.


## Pitfalls

Keep the user's scope and explicit checkpoints. Missing evidence or unavailable dependencies are gaps, not passes. Do not replace a working existing skill or change another profile.

## Verification

Check each promised artifact and claim against a real tool result. Report evidence, skipped checks, and limitations. A child's self-report is not independent verification.

## Attribution

Adapted from Lauren Tan's MIT-licensed pstack 0.15.6, source revision `23e4138daa01c42d4969f7a5465f82704e64f798`. See `references/license.md`.
