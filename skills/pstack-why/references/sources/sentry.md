# Sentry Error History

## Hermes execution contract

Read the owning skill's `references/hermes-runtime.md` first. This reference is a procedure/prompt, not authority to change state. Use `read_file`, `search_files`, and `terminal` for local read-only evidence. Discover deferred tools with `hermes_tool_search`/`tool_describe` before `tool_call`; use only authenticated read operations actually present. Service names identify conditional evidence categories, not guaranteed tools. Missing access, unsupported searches, retention limits, and incomplete pagination are explicit gaps.

For delegation, the parent supplies this full prompt, repository/session scope, and all evidence needed in `delegate_task` goal/context tasks. Children cannot delegate or ask the user and must not write files or external state. They share the filesystem; read-only is a behavior contract, not enforced sandboxing. Return findings in the tool response. The parent owns subsequent waves; async results arrive after the parent yields, never through transcript polling. Role lenses inherit the parent model, so never claim model diversity from role labels.

## What this source contains

Sentry is the archive of things that went wrong. For defensive, corrective, or error-handling code, it often holds the direct motivation: the specific exceptions, stack traces, and frequencies that pushed someone to add a check, catch, retry, or fallback.

- **Issues.** Grouped errors with counts, first/last seen timestamps, affected releases, and comments
- **Events.** Individual error instances within an issue (stack traces, tags, user context)
- **Releases.** Deployment records with associated issues (useful for "which version fixed this?")
- **Replays.** Session recordings of user-facing errors (if enabled)
- **Profiles.** Performance profiling data (less useful for "why", more for "how slow")
- **Issue comments & assignments.** Sometimes contain engineer notes on root cause

The most valuable thing Sentry provides is **temporal correlation**: "issue X was created 2024-01-02, peaked at 500 events/day, stopped appearing after release v2.14.0 on 2024-01-15, the release that shipped the defensive check."

## How to search it

Use an actually discovered authenticated error-tracker read connector (Sentry is an example). Inspect available schemas; absent access is an error-history coverage gap.

1. Resolve the approved organization and project from metadata, not guesses.
2. Search issues using exception classes, symbols, file paths, and exact handled error strings.
3. Filter issue/event reads by release, environment, trace ID, and time window. Inspect first/last seen, frequency trajectory, affected versions, and sampling.
4. Fetch representative full events with stack traces, tags, and breadcrumbs through the target. Read issue comments for author-stated rationale.
5. Read releases near the target commit date and compare their contents to the exact PR, not only the merge date.
6. AI root-cause summaries, if already available via an authorized read operation, are hypothesis generators, not primary evidence. Do not start expensive analysis jobs or call state-changing analysis tools during read-only investigation. Cite real events/timestamps instead.

## What good evidence looks like here

- An issue whose **first seen** is shortly before the target's PR and **last seen** shortly after, suggesting the target addressed this error
- Stack traces that pass through or land on the target function, showing the exact failure mode being defended against
- A comment on the issue from the PR author describing the fix
- The target's PR description or commit message referencing a Sentry issue URL or ID
- An issue with high event counts that stops after the release containing the target

## Common pitfalls

- **Grouping drift.** Sentry groups errors by fingerprint. Refactors or renames can track the "same" error under a new issue ID. If an issue ends abruptly, the error may have just been regrouped. Check for new issues immediately after.
- **Release correlation is noisy.** A release contains many commits. An issue stopping at v2.14.0 doesn't prove the target fixed it. Another change in the same release might have. Cross-reference with the target's exact commit.
- **Silent fixes.** Sometimes the error stops because upstream changed, not because of the defensive code. The correlation suggests the fix. It doesn't prove authorship.
- **Resolved != fixed.** Issues can be marked "resolved" manually without any code change. Treat `resolved` as a human marker, not evidence that code fixed it.
- **Seer hallucinations.** Seer can generate confident-sounding explanations that aren't right. Fall back to the actual events, stack traces, and timestamps when making claims.
- **Sampling.** Some projects sample events aggressively. A low event count may just mean high sampling, not a rare error. If in doubt, note the gap.

## What to return

For each relevant issue:
- Issue ID and title
- Project and organization
- First seen / last seen timestamps
- Event count (and sampling rate if known)
- Affected releases
- A representative stack trace snippet showing relevance to the target (verbatim excerpt, not summary)
- First/last-seen correlation with the target's ship date
- Link to the issue
- Any author comments or resolution notes
