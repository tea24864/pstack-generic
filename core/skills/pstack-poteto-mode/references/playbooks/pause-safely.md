### Pause safely

**You own a clean stop. Leave a checkpoint a cold-start agent can resume from.** This is explicit only. On "keep going", "going to bed, keep going", or "don't stop", do not pause.

{{runtime.persistent_work}}

1. Stop at a safe boundary. Finish the current atomic step or back out of it. Start nothing new, and launch no new workers, use actual supported stop/cancel controls if available, and reconcile bounded children as stopped on session end.
2. Take no irreversible action to pause. No PR and no push unless you already had one out.
3. Make the work durable. Preserve only authorized task edits without disturbing unrelated work; when a local commit is appropriate, commit them as one clear `wip:` commit on the current branch so nothing is lost. If the tree is broken, say so in the commit body in one line.
4. Write the resume note off-context. Capture intent, what you were doing, progress and what's verified, current state, next steps, key files, and gotchas. For the compaction trigger write it to a file like `$TMPDIR/<slug>-resume.md` or a user-approved durable project-state path. If a show-me-your-work trail exists, point at it instead of duplicating it.

**Reply:** where you are in the loop, what's on disk versus still in your head (paths, no diff dumps), the commits you made and whether the tree is clean, and the first action on resume. This is a pause, not a final report.


**Permission boundary.** Publication, merges, configuration changes, installs, destructive cleanup and durable scheduling require explicit relevant scope. Missing evidence or capability is a gap, not a pass. Concurrent writers need exclusive ownership; the coordinator relays dependencies. Use bullets instead of Markdown tables where the delivery surface does not support tables.
