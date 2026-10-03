---
name: pstack-why
description: "Trace design rationale through cited historical evidence."
version: 0.1.0
author: "Lauren Tan (poteto), tea24864, Hermes Agent"
license: MIT
platforms: ["linux", "macos"]
metadata:
  hermes:
    tags: [pstack, engineering, workflow]
    related_skills: ["pstack-how", "pstack-recall", "pstack-teach"]
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

# Why

## When to Use

Use for “why this design”, historical tradeoffs, regressions, postmortems, or data-backed thresholds. Use `pstack-how` for mechanics. Investigation is read-only.

## Prerequisites

Read `references/hermes-runtime.md` with `skill_view` before executing this workflow. Use only tools and credentials actually available in this session. Invoking this skill does not authorize publication, merges, destructive cleanup, or configuration changes.

## Procedure

Investigate the motivation and intent behind code.

Companion to the `pstack-how` skill. `pstack-how` answers what the code does and how it works. `pstack-why` answers what forces led to its shape.

Delegation uses `delegate_task(tasks=[{"goal": "...", "context": "..."}])` only after discovering its actual schema. Roles are prompt lenses, not per-task models. Optional `skills.config.pstack.*` values are descriptive runtime preferences (default inherit-parent); do not change configuration or pass unsupported `model`, `readonly`, `subagent_type`, `environment`, or `run_in_background` fields. Children share the filesystem and must be explicitly told not to write or ask the user. Flatten later waves through the parent. If delegation is unavailable, execute the same evidence slices inline.

## Operating Posture

Operate as a **careful, cautious, and precise investigator**. Be honest about what you know vs what you're inferring. Read `references/epistemics.md` for the full confidence framework and phrasing guide. The synthesizer must follow it.

## Step 1. Understand the Target and the Question

Parse what the user is asking. The **target** is usually a chunk of code, a pattern, a feature, or a named design decision. The **question** is usually a design rationale, a tradeoff, a motivating edge case, an external constraint, dead code, or a broad history sweep.

If the target is vague ("why do we do it this way?" with no clear referent), make your best guess from conversation context (files already in context, recent edits, what was just discussed). State your interpretation briefly so the user can redirect if you're off, then proceed.

## Step 2. Establish the Code Anchor

Before spawning investigators, anchor the investigation in concrete code. You need:

- The relevant file path(s) and line range(s)
- The key symbols (function names, class names, constants)
- An initial commit list. The last few commits touching the target.
- PR numbers from merge commits (pattern `(#1234)` in the subject line)

Build this inline.

Run these read-only command templates via `terminal(command=..., workdir=<repo>)` after substituting observed values. Do not run angle-bracket placeholders.

```bash
# Blame target lines for last-touch commits
git blame -L <start>,<end> <file>

# Full file history, with patches, through renames
git log --follow -p -- <file>

# Last N commits touching the file, PR numbers visible
git log --oneline -20 -- <file>

# Extract PR numbers from a commit message
git log -1 --format=%B <commit>
```

Pull PR bodies and discussion via `terminal` running `gh` for any substantive commits:

```bash
gh pr view <number> --json title,body,author,createdAt,mergedAt,labels,closingIssuesReferences,comments,reviews
```

Capture this as seed context (file paths, symbols, commits, PR numbers, linked ticket IDs). Pass it to the investigators.

## Step 3. Spawn Parallel Investigators (default posture)

**Default to the full parallel investigation.**

### Discovery

Before investigators, discover available tools in this session with `hermes_tool_search`; load matching schemas with `tool_describe` and invoke with `tool_call`. Classify actual MCP connectors from their schemas, not a presumed server directory. An installed service skill is not proof of a connected or authenticated service. Use `terminal` for git/gh, `search_files` and `read_file` for local evidence.

Map each available MCP to one evidence category:

1. Source control history
2. Issue / ticket tracker
3. Long-form documents
4. Real-time team chat
5. Infrastructure observability
6. Error / exception tracking
7. Product analytics warehouse

Source control is the baseline: check git checkout/history and `gh` availability/authentication first. A shallow clone, missing CLI, or failed authentication is an explicit coverage gap, not guaranteed access. For the other six, classify using the MCP name, server instructions, tool names, and resource descriptors. If an MCP could fit more than one category, choose the one matching its primary evidence. Record ambiguous cases in the coverage map.

Aim for a complete **coverage map**, not a minimal one. Document the null, don't skip the search.

Launch all matching investigators in a single message so they run concurrently. Don't ask one agent to cover multiple MCPs.

Use a `delegate_task` tasks batch with one goal per source and self-contained context. Instruct each investigator to use read operations only, return evidence in its response, not delegate, and not ask the user. Behavioral read-only scope is not sandbox enforcement; shared filesystem and connector side effects still require care.

Each investigator gets:
1. The base prompt from `references/investigator-prompt.md`
2. The category playbook `references/sources/<source>.md` for the selected MCP, adapted from the examples in `references/source-playbook.md`
3. The cross-cutting `references/sources/incident-postmortem.md` **if the target code looks defensive** (null checks, retry logic, timeout handling, rate limiting, feature flags, egress guards, OOM handlers)
4. The code anchor from Step 2 (file paths, symbols, commit hashes, PR numbers, ticket IDs)
5. The user's original question

### Investigator roster. One per available source within a category

Launch one investigator per available source, grouped by category; never mix connectors inside a worker. Git and gh are the source-control bundle. Combine findings by category in final coverage.

Each entry names the category and the kind of "why" it uniquely surfaces. Use it to know what to expect back, how to name a gap when a category returns empty, and (only in the rare provably-irrelevant case) to justify a skip.

1. **Source control investigator**. Git history, `gh` for PRs, code comments, tests. Always attempt. Availability still requires a usable checkout and authenticated PR access. Best at surfacing *implementation-time rationale captured during review*.

2. **Issue / ticket tracker investigator** (e.g. Linear, Jira, GitHub Issues, Plane, Shortcut MCP). Best at surfacing *the product or business forcing function*. Strongest when the why is external to engineering.

3. **Long-form documents investigator** (e.g. Notion, Confluence, Google Docs, Coda MCP). Best at surfacing *long-form design rationale*. Where the why is written out before it becomes code.

4. **Real-time team chat investigator** (e.g. Slack, Discord, Microsoft Teams, Mattermost MCP). Best at surfacing *real-time deliberation that never reached a doc*. Especially important when the source control, ticket, and doc paper trail is thin.

5. **Infrastructure observability investigator** (e.g. Datadog, New Relic, Honeycomb, Grafana, Splunk MCP). Infra/runtime view. Best at surfacing *infrastructure and runtime reality that motivated the code*. Strongest when the target reacts to an infra signal (timeouts, retries, rate limits, circuit breakers).

6. **Error / exception tracking investigator** (e.g. Sentry, Rollbar, Bugsnag, Airbrake MCP). Best at surfacing *the specific exceptions and error trajectories that motivated defensive or corrective code*. Strongest for catch blocks, null guards, type checks, retries, and other defenses.

7. **Product analytics warehouse investigator** (e.g. Databricks, Snowflake, BigQuery, ClickHouse, dbt, Redshift MCP). Product/data view. Best at surfacing *product and data reality that shaped the code*. Strongest for flag-gated code, experiment-driven ships, data migrations, and "where did this number come from" questions.

### When to skip an investigator

Only skip with an **explicit, written justification** that goes in the final "Sources Consulted" section. Two valid reasons:

- **No MCP is available for that category** in this environment. Flag this as a gap, not a choice. Example: "Real-time team chat skipped. No matching MCP available, so the conversational record was not searchable."
- **The source is provably irrelevant**, not just "probably irrelevant." A high bar. Example: "Error / exception tracking skipped. Target is a build-time script with no runtime code path."

If your scope assessment suggests a single-commit trivial target where the PR description already contains the complete answer, you may answer inline **only after** confirming every available source search across all seven categories would be redundant. Say so explicitly. This should be rare.

## Step 4. Synthesize

After all source results return to the parent, launch one synthesis child with `delegate_task`, or synthesize inline. It may spot-check using available read tools/connectors, but must not write or delegate.

The synthesizer gets:
1. The investigator findings, including any null results and any categories skipped with justification
2. The code anchor from Step 2 (file paths, symbols, commit hashes, PR numbers, ticket IDs)
3. The user's original question
4. The epistemics framework from `references/epistemics.md`
5. The synthesizer prompt template from `references/synthesizer-prompt.md`

## Step 5. Present

Take the synthesizer's output and present it to the user. You may lightly edit for clarity or add context from the conversation, but **do not rewrite the confidence language**.

## Output Format

The output structure is the one in `references/synthesizer-prompt.md`: The Question, The Code in Question, What We Found, What We Can Reasonably Infer, Competing Hypotheses, What We Don't Know, Sources Consulted, Confidence Summary. Adapt as needed, but keep the confidence separation intact, and keep Sources Consulted as one line per investigator, including the ones that returned nothing or were skipped, with the reason.

After the Sources Consulted block, if the user's `pstack-why` question is a precursor to actually changing this code, convert the lineage findings into a Preserve / Change / Avoid / Risk constraint set suitable for planning the change.

## Common Failure Modes to Avoid

- **Recency bias**. Assuming the most recent commit is authoritative. The current shape is often the accretion of many earlier decisions. Trace back.

## Reference Files

- `references/epistemics.md`. Confidence tiers and phrasing guide. The synthesizer must follow it.
- `references/investigator-prompt.md`. Base prompt template for investigator subagents.
- `references/source-playbook.md`. Index pointing at the category playbooks below.
- `references/sources/*.md`. One self-contained example playbook per category, plus cross-cutting `incident-postmortem.md`. Give an investigator the single file that matches its category and adapt it to the available MCP.
- `references/synthesizer-prompt.md`. Prompt template for the synthesizer subagent, including the output format.


## Pitfalls

Recency bias and tidy rationalization erase history. A missing connector, failed auth, retention cliff, shallow checkout, or null search is a coverage fact, not a pass. Do not infer intent from mechanics or change state during investigation.

## Verification

Spot-check every Direct/Supported claim and preserve confidence separation. Account for all seven evidence categories with exact queries, sources/null results, skip reasons, and access limitations. Include Preserve / Change / Avoid / Risk constraints when planning follows.

## Attribution

Adapted from Lauren Tan's MIT-licensed pstack 0.15.6, source revision `23e4138daa01c42d4969f7a5465f82704e64f798`. See `references/license.md`.
