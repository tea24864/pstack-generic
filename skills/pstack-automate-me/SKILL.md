---
name: pstack-automate-me
description: "Capture working preferences in an approved mode skill."
version: 0.1.0
author: "Lauren Tan (poteto), tea24864, Hermes Agent"
license: MIT
platforms: ["linux", "macos"]
metadata:
  hermes:
    tags: [pstack, engineering, workflow]
    related_skills: ["pstack-recall", "pstack-poteto-mode", "pstack-unslop"]
---

# Automate me

## When to Use

Use for “automate me”, capture working conventions, or create/update a personal mode skill. Not for one narrow task workflow or automatic permanent behavior changes.

## Prerequisites

Read `references/hermes-runtime.md` with `skill_view` before executing this workflow. Use only tools and credentials actually available in this session. Invoking this skill does not authorize publication, merges, destructive cleanup, or configuration changes.

## Procedure

A guided flow for turning the user's working conventions into a skill agents will follow. The output is one `-mode` skill tailored to them (e.g. `jay-mode`, `priya-mode`).

This skill orchestrates three others: an inline mining pass (see step 1), the native authoring contract in `references/skill-authoring.md` and `skill_manage` (authoring), and the **pstack-unslop** skill (prose discipline). It sequences them. It doesn't replace them.

## Flow

### 0. Check for an existing skill

Use `skills_list`/`skill_view` for visible profile/project skills and `search_files` only inside the active repo's `.hermes/skills/` or `.agents/skills/` if needed. Confirm the current profile and matching handle; never scan another profile. If a matching skill exists and update intent is not explicit, ask in ordinary chat whether to update (default) or start fresh. Namespaced installed `pstack-*` skills remain intact.

- Update the existing skill (default for repeat runs)
- Start fresh (rare, ask why before doing it)

Update mode changes the rest of the flow:
- Step 1 mines only history since the skill was last edited (`terminal` running `git log -1 --format=%cI -- <path>` in a git-tracked skill repo; otherwise use verified file modification time and say which).
- Step 2 asks what's changed or missing, not what to capture from zero.
- Step 4 edits the existing file in place. Preserve sections the user hasn't contradicted. Revise ones with new evidence. Add new sections only for genuinely new rules.

### 1. Mine their history

Discover `session_search` via `tool_describe`, then use `tool_call` to find sessions only in the active workspace and chosen time window. Check provenance before reading, paginate supported search/read results, and report inaccessible history. Do not enumerate unrelated transcript directories or profiles.

Survey recent agent conversations within that scope for recurring patterns. When delegation is available, use parent-launched `delegate_task` tasks across non-overlapping session/time slices of history (e.g. last 2-4 weeks, split into 3 slices so each has enough material). Each slice mining child gets scoped session IDs and the full parent-supplied context, reads only those sessions with actual available tools, never writes/delegates/asks the user, looks for the signals below, and returns a short structured list of patterns it saw with evidence pointers. Default signals worth hunting:

- Response preferences (length, tone, format, "dumb it down" corrections)
- Delegation habits (subagents, models, specialized workflows, parallelism)
- Verification posture (what "done" means, unit tests vs live repro, reviewers)
- Code and prose discipline (style, principles cited, lint/format tools)
- Process conventions (worktrees, commits, PRs, review/merge tooling)
- Meta preferences (fixing skills mid-task, proposing new ones)

Cross-check across slices before elevating a signal. Patterns seen in 2+ slices are high-confidence. Lone signals are weak and usually get dropped.

### 2. Ask the user directly

Mining misses intent that hasn't come up yet. Offer compact multiple-choice questions in ordinary chat. Use a clarification tool only if its actual schema is available; never invent `AskQuestion`. Only the parent asks the user.

Shape: one or two questions with 4-6 options each, allow multiple selections for category questions. Start broad ("Which areas matter most?"), then follow up on selected areas with specific options. After the structured rounds, one free-form chat question catches anything the options missed.

Don't dump 20 questions.

### 3. Cluster findings

Group the combined signals into sections. Common ones (use only what applies):

- **Response style**: length, tone, format.
- **Autonomy**: how much to do without asking, MCP tool use.
- **Understand first**: which skills to reach for when scoping or investigating a change.
- **Subagents**: default, parallelism, model-to-task, specialized workflows.
- **Prose / code discipline**: principles, lint tools, style guides.
- **Review and verify**: repro posture, verification skills, live-testing tools.
- **Process**: git worktrees, commits, PRs, review/merge tooling.
- **Skills**: skill-authoring habits, fix-the-skill-first, proposing new skills.

The **pstack-poteto-mode** skill shows the shape. Read it for granularity. Don't copy its content. The user's rules are not the same as poteto-mode's.

### 4. Draft the skill

Read `references/skill-authoring.md`. Confirm the handle, name, intended scope, and overwrite/update intent. Preserve the category of an existing mode.

- Profile-local: `skill_manage` create/patch and supporting-file operations target the active profile (or configured create directory). Confirm that destination before writing. Do not change creation config merely for this task.
- Project-local: For a new mode, default to `.hermes/skills/pstack-<handle>-mode/` inside the approved repo, or an established `.agents/skills/` convention. A trusted existing project skill can be patched with `skill_manage`; for a new repo artifact, use `write_file` because `skill_manage` create otherwise targets the profile/configured creation directory. Disclose trust requirements and do not run `hermes skills trust` without explicit approval.
- Description: one quoted YAML scalar, at most 57 characters, ending with a period; trigger on their handle and working-style intent rather than generic coding terms.
- Include explicit scope and invocation triggers in the body. Do not transplant Cursor frontmatter or enable permanent skill autoload, edit system prompts, or write durable memory by implication. A mode skill is on-demand unless the user separately requests and approves persistent application.
- Reference existing skills by their actual names (including `pstack-*`); do not inline their bodies or overwrite their guidance.

### 5. Iterate on prose

Apply the **pstack-unslop** skill and the native authoring guidelines to every line.

Show the draft to the user and take feedback. Expect multiple iterations. Cut ruthlessly. A mode skill is not a manual.

### 6. Land it

For a project skill, use a worktree off the confirmed base when authorized. Commit/open a PR only when separately authorized; never push directly to main. For a profile-local skill, report the saved skill and approval outcome, not a fabricated PR.

## Guardrails

- **Don't overfit to one conversation.** A preference stated once and contradicted another time is noise. Require multiple instances before codifying it.
- **Don't be clever.** Restating other skills' contents, inventing metaphors, or writing "poetic" prose for an agent reader is cost without benefit. Keep it operational.
- **Reference, don't inline.** Other skills the user relies on should appear as path references, not pasted excerpts. Same for any principle docs they maintain elsewhere.
- **Keep sections minimal.** Only add a section if the user has a specific, non-default rule there. "Communicate clearly" is not a section. "Short paragraphs. Tables when comparing options. Bullets only when items are genuinely parallel." is.
- **Name conventions generic.** Use "the user" or "the human" in imperatives, not the author's first name.
- **Don't force symmetry.** If a user has no process rules worth writing down, skip the Process section entirely.

## Evaluation

A `-mode` skill is subjective output. A generic benchmark loop isn't useful here. Vibe-check with the user: does it read like them? Did it miss anything? Then save the approved scope; publication is a separate action.

Run a description-optimization loop only if the skill's trigger accuracy turns out to be a problem in practice.

## When not to use

- User wants a task-specific skill (not working conventions): native skill authoring alone, no mining required.
- User wants to capture one narrow workflow (e.g. "how I write commit messages"). That's a regular skill, not a mode skill.



## Pitfalls

Do not overfit a single chat, copy another person’s mode, silently replace a name collision, enable permanent autoload, or alter global memory. Project trust and profile-local creation are separate scopes.

## Verification

Validate scalar description, required sections, intended profile/project destination, references, and user approval. Cross-check durable preferences across evidence slices. The user’s confirmation of fit is the acceptance test; report staged writes accurately and never claim a PR without read-back.

## Attribution

Adapted from Lauren Tan's MIT-licensed pstack 0.15.6, source revision `23e4138daa01c42d4969f7a5465f82704e64f798`. See `references/license.md`.
