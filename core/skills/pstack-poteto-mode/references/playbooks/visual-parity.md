### Visual parity

**You own pixel-exact equivalence. The baseline is the spec. You do not touch it.** Equivalence is verified by image diff, not by eye.

{{runtime.web}}

1. Establish the baseline first, before any migration: a visual regression harness that screenshots the current component across its states, plus the target when matching two implementations. No baseline, no parity claim. A blocking prerequisite, not a follow-up.
2. Anti-shortcut clauses, stated and held: no harness modifications, no baseline tampering, no component restructuring to make a diff pass. If the baseline looks wrong, stop and ask, don't edit it.
3. Migrate one component at a time. Parallelize across worktrees, one owner per component (the **pstack-principle-separate-before-serializing-shared-state** principle skill). Shared primitives migrate first as a blocking phase.
4. Verify each component against its baseline via image diff on the matching surface via the verified browser, desktop, or shell surface driver. A nonzero diff is a fail. Investigate the pixel delta. Use bounded iterations per component until the diff is zero, or report the session budget/access gap without claiming parity.
5. Run **Opening a PR** per component or safe batch only when publication is authorized.

**Reply:** components migrated, the diff result for each, the baseline harness location, what's left.


**Permission boundary.** Publication, merges, configuration changes, installs, destructive cleanup and durable scheduling require explicit relevant scope. Missing evidence or capability is a gap, not a pass. Concurrent writers need exclusive ownership; the coordinator relays dependencies. Use bullets instead of Markdown tables where the delivery surface does not support tables.
