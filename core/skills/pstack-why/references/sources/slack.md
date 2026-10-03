# Slack Conversations

## What this source contains

- Real-time discussions of problems and decisions
- Incident channels where fire-drill decisions were made
- Design discussion threads where tradeoffs were debated
- Questions answered by senior engineers that didn't make it into docs
- Post-merge discussions that explain why something was revisited
- DMs (usually not searchable, scope accordingly)

Slack is frequently where the *real* decisions got made, especially for smaller changes that didn't warrant a doc. It's also the most ephemeral source. Threads get deleted, channels get archived, and search quality degrades over time.

## How to search it

{{runtime.integrations}}

Use an actually discovered authenticated team-chat read connector (Slack is an example). Inspect the available search/thread schema and supported authentication flow. If auth fails, stop and report the gap; do not invent an auth tool.

1. Bound by the PR author and merge-date window.
2. Search feature names and symbols, including informal names and misspellings.
3. Search PR URLs or `/pull/<number>` and exact relevant error strings.
4. Restrict to authorized owning-team, engineering, project, incident/severity, and design channels as appropriate.
5. Fetch whole threads and paginate replies; the initial message alone can invert the meaning. Confirm declared reply totals against collected results.
6. Record channel, permalink/thread ID, participants, dates, quotes, queries, inaccessible DMs, and retention gaps.

## What good evidence looks like here

- A thread where tradeoffs were explicitly debated ("I was going to use A but B is better because...")
- An incident channel message describing the bug the code prevents
- A question from a reviewer and an authoritative answer from the author or lead
- A reference to a meeting where a decision was made
- A message from a product manager or customer-facing engineer explaining a customer ask

## Common pitfalls

- **Channel archaeology limits.** Very old messages may be gone due to retention policies. If you can't find anything before a certain date, note the retention cliff.
- **Unsearched DMs.** Many decisions happen in DMs that aren't searchable. You'll miss them. That's a known limitation.
- **Speculative jokes as "decisions."** Slack is casual. "Lol just do the thing" isn't a decision, even if it preceded the commit. Look for considered discussion.
- **Context collapse in single messages.** Without the thread, a single message often reads differently than in context. Always fetch threads.
- **Auth failures.** If the MCP isn't authenticated, stop. Don't make up findings. Report that Slack wasn't searchable.

## What to return

For each relevant thread:
- Channel name
- Permalink or thread ID
- Participants
- Date range of the discussion
- The key quotes (verbatim) with attribution
- Context: what thread/incident/discussion this was part of
