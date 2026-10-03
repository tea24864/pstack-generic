---
name: pstack-recall
description: "Rebuild scoped work context from history and live state."
license: MIT
metadata:
  author: "Lauren Tan (poteto), tea24864"
  version: "0.2.0"
  source-revision: "23e4138daa01c42d4969f7a5465f82704e64f798"
---

# Recall

## When to Use

Use before resuming work: “catch me up”, “where did I leave off”, or “recall my work on X”. Use the supplied state capsule when complete; do not mine unrelated history.

## Prerequisites

Use only capabilities and credentials actually available. This workflow does not authorize publication, merges, destructive cleanup, installation, or configuration changes.

## Procedure

**Before you start or resume work, you rebuild the user's recent working context and hand back a tight capsule of where things stand now and what to do next.**

Keep it tight and on-topic. Read only what the in-scope threads need, then stop.

Your context lives in two records. Your own chat history holds what you did and decided. The shared record holds everything that happened around the same code under other names: the symptoms users keep reporting, the fixes that shipped and got reverted, the errors still firing in prod. That second record is what the **pstack-why** skill searches, across source control, the issue tracker, chat and issue channels, long-form docs, and error tracking. A feature with a long bug tail keeps most of its story there, so don't reconstruct it from your transcripts alone.

{{runtime.history}}

Restrict history to the active workspace and agreed time window. Verify provenance before opening a candidate; post-filter metadata if source filters are unavailable. Never scan unrelated projects or user scopes. Missing provenance or needed messages is a limit to report, not permission to mine arbitrary transcript directories.

{{runtime.skill_loading}}

{{runtime.delegation}}

1. Classify, then route. One specific prior chat to resume is the session-pickup playbook of `pstack-poteto-mode`, not this. Turning habits into a durable skill is `pstack-automate-me`. A human-readable summary of your work is a different task. Recall loads working context across recent chats before you act. If the user already gave you a full state capsule (paths, branch, the change), use it and skip the mining.
2. Lock the scope before searching. Pin the window ("recent" is a real range, default the last 7 days), the topic if named, and the workspace (default the active one. Never read another project's transcripts without being asked). State the scope back. Never quietly turn "all" into "recent N".
3. Fan out across chat history only after scoped discovery establishes candidate IDs. For one or two chats, search and read directly. Otherwise assign non-overlapping ID/time slices with complete context and no-write/no-nested-delegation/no-user-question scope. Order by real timestamps, not ID text. Search the topic before reading relevant regions. Exclude the active chat and obvious child/eval/test noise. Each slice returns topic, user goal, decisions, open threads, struggles/corrections, and artifacts (PRs, tickets, branches), each citing its session ID. Results, not raw transcript dumps, return to the coordinator. Without independent delegation, do the same slices inline.
4. Sweep the shared record whenever the topic names a feature, file, subsystem, area, or bug. This is the default, not a judgment call, and "my work on X" does not exempt it. Hand it to the **pstack-why** skill's source investigators, but steer their question from "why was this built this way" to "what's the current state, what's been tried and didn't hold, and what are users still reporting". Reuse its per-source playbooks, run the investigators in parallel with the chat-history mining, and inherit its posture: one investigator per source, null results are findings, skip an unavailable MCP and say so. Fold what comes back into the brief. Skip this step only for pure activity recall with no named target ("what did I do this week"), where your own history and live state are the entire answer.
5. Verify against live state. Take the PRs, branches, and tickets that the mining and the sweep surfaced and check them with `git` and `gh`. When the answer hinges on what an agent actually did (the tools it ran, files it read, errors it hit), retrieve the full relevant conversation through the session read operation, paginate until complete, and explicitly mark gaps if unavailable.
6. Write the brief to the contract below. Group by thread. Stay on the named topic.

## Output contract

Lead with the capsule, then the thread status, then the problems, then the next move. Deeper detail goes below or gets cut.

- **Capsule.** At most 5 bullets. What this work is and where it stands overall.
- **Threads.** One line each, prefixed with exactly one status tag: `[merged #N]`, `[open PR #N]`, `[in flight <branch>]`, `[verified, uncommitted]`, `[reverted #N]`, or `[planned, not started]`. A thread with no tag is not done yet, so tag it.
- **Problems.** At most 5, the recurring ones. Include the symptoms users keep reporting and any fix that shipped and was reverted, so the next attempt starts where the last one failed.
- **Next move.** The single most useful next action, concrete.

An adjacent feature or ticket stays out unless it blocks this one. When the capsule and thread lines outgrow a screen, cut detail before you cut threads. Write the brief through the **pstack-unslop** skill, cite chat findings by UUID and shared-record findings by their source (PR #, ticket ID, chat permalink, error-tracker issue), and sanitize private context before any public output.

**Reply:** the brief, to the contract above.


## Pitfalls

A session ID is not a timestamp; never sort UUIDs as recency. Do not cross workspace/profile boundaries or silently reduce an “all” request. Missing provenance/transcript pages and unavailable shared-record tools must remain visible gaps.

## Verification

Read back current PR/branch/ticket state using available git/gh/connectors. Cite session IDs and source links. Deliver capsule (at most five bullets), tagged threads, problems (at most five), and one next move; unresolved live status is explicitly unknown, not guessed.

## Attribution

Adapted from Lauren Tan's MIT-licensed pstack 0.15.6, source revision `23e4138daa01c42d4969f7a5465f82704e64f798`. See `references/license.md`.
