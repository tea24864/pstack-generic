### Autonomous run

**Define a countable exit predicate, then work toward it within explicit scope and runtime limits.** One sustained task belongs here; a standing project belongs to Orchestrate.

1. State done as a checkable predicate such as original repro fixed, all named gates passed, all N authorized PRs merged, or pixel diff zero. Record scope, spend/runtime budget, forbidden paths, publication permissions and named pause gates. "Keep going" does not waive them.
2. Choose a real wake mechanism. Use bounded iterations in the current session by default. Events use supported bounded forge/check reads or process notifications when available. Archived watchers are provenance only. Scheduled checks or independent processes need separate approval and verified capability. Specify duration, stop predicate, delivery and shutdown. No fictitious loop command, heartbeat worker or persistent child.

Native children stop with the parent/session. For separately authorized durable work use supported scheduling or `terminal(background=true, notify=true, persist_on_release=true)` for a real bounded job; never detached child claims or background sleep/poll loops. Discover cron/process tools before use, preserve explicit scope and leave actionable handoff evidence.
3. Each iteration makes the smallest evidence-backed change, verifies the predicate, records a scoped local commit if appropriate, and discards changes that did not help. Apply pstack-principle-sequence-verifiable-units instead of checking only at the end.
4. Address reversible in-scope blockers. Separate out-of-scope discoveries as proposed follow-ups rather than silently expanding work, publishing a fix, or changing an installed skill. Escalate irreversible writes, genuine product calls, permission gaps, or a dead end. Return to the main predicate after each permitted side fix.
5. Checkpoint every iteration via pstack-show-me-your-work: what changed, evidence, whether the predicate moved, rejected hypotheses and next action. Children are leaf tasks coordinated in parent waves; no nested orchestration or transcript polling.
6. Stop only with real predicate evidence, an explicit stop, exhausted authorized budget, permission gate or genuine dead end. A plateau triggers a different hypothesis, not relaxation of done. A runtime interruption requires a safe resumable checkpoint and an explicit incomplete status.

**Reply:** predicate and actual final state, iterations from the log, accepted versus discarded work, evidence paths and any remaining boundary or blocker.
