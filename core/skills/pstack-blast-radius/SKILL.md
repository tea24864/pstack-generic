---
name: pstack-blast-radius
description: "Find downstream breakage and execute a safety proof."
license: MIT
metadata:
  author: "Lauren Tan (poteto), tea24864"
  version: "0.2.0"
  source-revision: "23e4138daa01c42d4969f7a5465f82704e64f798"
---

# Blast radius

## When to Use

Use for “what could this break”, blast-radius reviews, or suspiciously small diffs. Do not merge or alter the product by implication.

## Prerequisites

Use only capabilities and credentials actually available. This workflow does not authorize publication, merges, destructive cleanup, installation, or configuration changes.

## Procedure

Find what a change breaks somewhere else, before it ships. Use for "blast radius of X", "what could this break", or reviewing a small diff you don't trust yet.

Companion to `pstack-how` and `pstack-why`. `pstack-how` tells you what the code does. `pstack-why` tells you why it's shaped that way. Blast radius tells you what it breaks somewhere else.

Listing the callers is not the job. A repository symbol search can find those quickly. The job is the breakage a symbol search won't show you.

## Don't trust your own writeup

A blast-radius writeup that sounds right is worthless. It reads as convincing whether or not it's true. So don't hand back the writeup. Find the one or two facts the whole thing depends on and prove them by running code.

### How sure are you

For each fact the change's safety depends on, get it as far down this list as is cheap, and say where it stopped.

1. You said so. Worthless on its own.
2. You pointed at the line. A real `file:line`, or the library's own source.
3. You showed the bad case can't happen. You walked the failure step by step and it doesn't reach.
4. You ran it. A script or test that calls the real code and fails loud if you're wrong.
5. You reproduced it in the running app.

Step 4 is usually one small script that imports the same library the app ships and calls the exact function you're worried about.

## Steps

{{runtime.skill_loading}}

{{runtime.files}}

1. Read the change. The diff, the symbols it adds, changes, and deletes, and what it now does differently, including the part the diff doesn't spell out. Use `pstack-why` step 2 to pull the PR and commits.
2. Find the one fact it's safe because of. Most changes that look risky are safe because of a single fact, like "this call only drops already-dead cache entries and does nothing else". Find that fact. If it holds, most risky cases are cleared at once. Spend your time here, not on a long list of maybes.
3. Look where symbol search stops. Read the source of the library you call, and check its pinned version and any local patch. Work out when things run: microtasks, unmount and teardown, Solid versus React. Follow what a symbol search misses: the JSON an API returns, a DB column, a wire format, another language reading the same bytes, a feature flag, code three hops downstream.
4. Be honest about each risk. Give it a real chance of happening and a real cost if it does. Keep the risks you confirmed. List the ones you checked and cleared separately. Same rules as `pstack-why`. Cite a real `file:line`, a search that finds nothing is still an answer, and never make up a caller or an API.
5. Prove the one fact. Run a minimal probe/test importing the real pinned code, not a mock or reimplementation. In read-only scope, keep the probe in memory or request permission for an isolated scratch artifact; do not alter tracked files incidentally. Record command, version, exit code, stdout/stderr, and failure cases. Live-app proof requires an authorized isolated instance and side-effect scope. Never call an unexecuted script proof.
{{runtime.delegation}}

6. For a big or wide change, use `pstack-arena`. Compare independent role lenses when supported and merge their evidence; otherwise run the lenses inline and disclose the lost independence. Model diversity requires actual verified capability and authorization, never role labels or invented settings.

## What to hand back

- **What it does.** What changed, including the part that isn't obvious.
- **The one fact it's safe because of.** State it, say which step you got it to, and show the proof. If you couldn't prove it, write unproven.
- **Risks.** Each names how it breaks, the `file:line`, how likely and how bad, and how to check. Paste the proof for the ones that matter.
- **Cleared.** What you checked and why it's fine.
- **Before you merge.** The cheapest test or repro that catches the real bug, including the script you wrote.

Write it through `pstack-unslop`, cite real code, and strip anything private before it goes anywhere public.

**Reply:** the writeup above, with the one safety fact either proven or marked unproven.


## Pitfalls

A persuasive writeup, mock test, source citation, or unexecuted helper is not runtime proof. Check pinned versions/local patches. Do not claim a same-model role panel is multi-model. Isolation and authorization still apply to repro side effects.

## Verification

The safety fact has command/output evidence from real code or is marked unproven. Record confirmed risks separately from cleared cases, proof tier reached, and the cheapest pre-merge regression test. Never call an inconclusive result safe.

## Attribution

Adapted from Lauren Tan's MIT-licensed pstack 0.15.6, source revision `23e4138daa01c42d4969f7a5465f82704e64f798`. See `references/license.md`.
