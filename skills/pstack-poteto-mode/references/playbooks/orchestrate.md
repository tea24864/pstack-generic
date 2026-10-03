### Orchestrate

**Own a standing program through briefs, evidence, queue discipline and a computed frontier.** One task within the session budget uses Autonomous run instead. A bespoke one-off uses pstack-figure-it-out. Multi-day continuity is durable state plus separately authorized scheduling/processes, never a long-lived delegated child.

#### Roles and placement

- Coordinator frames, authors briefs, drains results, owns reports and judgment. Keep code ownership in workers. Clean integration of independently verified commits is bookkeeping only within the grant; conflicted merges and code edits become fresh units.
- Track roles are organizational, not nested delegate trees. The parent coordinates flattened worker/verifier waves. A leaf cannot delegate or clarify. A separate full Hermes process may coordinate a track only if explicitly authorized, CLI-verified, isolated and budgeted; it is not native child recursion.
- Workers and verifiers have isolated conversations but shared filesystem. One writer per exclusive git worktree and branch. Read-only is a brief constraint, not a sandbox. Pass exact paths/SHAs. Native reviewers are same-model by default; report the diversity limitation. Never claim a cloud VM, per-task model, or durable child.

#### Store layout

Use a user-approved project state directory, for example `.hermes/pstack/orchestrate/<project-slug>/` in the workspace. Keep it outside committed source unless audit publication is explicitly requested. Resolve profile state from the active `$HERMES_HOME` if used, never another profile. Create state with `write_file` and edit with `patch`; one parent writer owns each shared table. The original Graphite store under `references/upstream-helpers/` is reference-only and not the runtime used here.

- `preferences.md`: numbered standing orders, one constraint each. Relay them verbatim in every fresh brief with all later directives. Encode recurring corrections before the next wave.
- `overview.md`: append-only durable PR/issue facts, not rewrites per event.
- `units.tsv`: id, track, state, branch, PR, head SHA, brief path. Reconcile every launched child to one terminal outcome.
- `frontier.json`: generation, ordered PR rows (number, branch, head/base SHAs, state), and lowest unmerged PR. Derive it from exact paginated `gh` reads and actual git refs at drain points, never narrative or Graphite metadata assumptions.
- `ledger.tsv`: PR plus exact head SHA, verdict, evidence path, verifier, timestamp. Include base SHA and patch-id in receipts. Verdicts are `live-ui-verified`, `unit-test-verified`, `type-check-only`, `verifier-blocked`, `verifier-failed`. Behavioral work needs more than type-check-only.
- `inbox/`: completed report pointers; archive consumed pointers instead of losing receipts. `gates.md`: operator gates and default proposals, never permission to bypass.
- `decisions.tsv`: pstack-show-me-your-work trail. `status.md`: derived counts/frontier/gates from the tables. Generate and count with Python through `execute_code` or `terminal`, not mental arithmetic.

#### Brief contract

Every leaf brief is self-contained. A dependency requires context relay, not only ordering. Include GOAL, writable/forbidden SCOPE, exclusive WORKTREE/branch, CONTEXT paths and prior result facts, checkable ACCEPTANCE, exact VERIFY commands/surface, TIMEBOX, FORBIDDEN actions, REPORT status/branch/head/PR/verdict/actual runs/deviations/follow-ups, and verbatim STANDING orders. Never spawn with missing acceptance or write ownership. Collapse a one-command brief to a paragraph while preserving these fields. Audit a sampled brief per track per wave; a failing brief pauses the next refill and repairs the template.

#### Steps

1. Frame a countable predicate, unit count, effort, tracks, expected stacks and wall-clock budget. If one agent fits, collapse to ordinary session execution without store ceremony. Schedule integration from the first verified unit. Before budget exhaustion stop new work and preserve verified output; around 70% reassess whether the remaining time is enough to verify and integrate. Contested decomposition goes through pstack-arena before the pilot. Present framing once and respect named gates.
2. Initialize the plain-file state and decision trail. Write standing orders before any child. Seed frontier from exact current PRs, never a copied stale list. No dependencies or profile changes are installed by this step.
3. Pilot one unit through brief, worker, actual verification, integration/PR state, ledger row and authorized merge if landing is granted. Use evidence to falsify the brief, recipe and unit size before fan-out. For cheap identical units the first normal verified unit is the pilot; expensive/novel work gets independent verification. Merge withheld means the pilot ends at verified review-ready, not an automatic merge.
4. Scale only ready independent units. Batch with `delegate_task(tasks=[{"goal": "Complete the scoped unit", "context": "The full brief contract, exact isolated worktree, no delegation or clarification; return artifacts and evidence."}])`, extending the array. Honor actual concurrency and budget; bounded waves are acceptable where asynchronous refill is unavailable. Parent relays upstream receipts to downstream units. Keep sibling communication through the parent. Never make a child coordinator wait on grandchildren.
5. Drain completion events at the end of a critical section, wave boundary, frontier event, and before a human report. Finish atomic brief/stack/gate/ledger updates first. For async results end the parent turn and await delivered results, not transcript polling. Snapshot arrivals, classify landed/needs-verify/failed/cancelled/noise, preserve receipts, update tables, derive status and launch the next ready wave. Deep review is a separate verification unit, not hidden inside the drain. Count every child including dropped or absorbed scopes.
6. Integrate continuously. Exactly one topology owner per stack; workers never restack or force-push shared branches. Babysitters report conflicts and work the immutable frontier generation. PR closes/retargets are gated topology operations. Merges require Shipping's independent current-patch verdict, explicit grant, bottom-up contiguous safety and exact readback. A retro pass checks merged PRs for reverts, post-merge CI failures and orphan follow-ups only within the monitoring grant.
7. Close by reconciling every launched child to done/abandoned/cancelled/reconciled, independently confirming the predicate on the real artifact, and checking every landed PR's exact-patch receipt. Audit the trail, preserving the actual same-model limitation. Encode recurring corrections into project standing orders, not another profile. Leave durable state intact as the postmortem.

#### Verification, liveness and failure

Scale verification to the unit. A cheap command gets worker output plus parent rerun/receipt inspection; an expensive, judgment-heavy or high-blast-radius unit gets a separate verifier. CI is an input, never the verdict. A new head voids a ledger row unless Shipping's precise patch-id/build-noise rule preserves a lane; CI/mergeability still refresh. BLOCKED never counts as PASS.

Read actual artifacts, ledger, PRs and branches rather than transcripts or mtime as liveness. Native child results arrive at completion; a missing update alone does not prove death. On failure preserve last evidence, scope and options. Scope/cap/OOM gets a smaller fresh task; transient network gets a bounded retry; tool failure first gets capability/inputs diagnosed, not an invented model fallback. Unknown gets one retry. Two retries maximum, then record a gap and replan. A late external-process result reconciles against current head/frontier before accepting anything. Do not replace an active writer until it is confirmed stopped; otherwise use a new isolated worktree and reject stale integration.

Stop new spawns on bad upstream output, broken acceptance or dead infrastructure; preserve in-flight state, repair the cause and resume only within budget. Bound coordinator infrastructure retries too. After process restart native children are gone; authorized independent processes may or may not remain and require real process/artifact checks. Re-read orders and tables, reconstruct actual frontier, reconcile unknown units and continue with fresh briefs. No fabricated resurrection or persistent cloud claim.

#### Escalation

Batch real operator gates: irreversible/destructive actions, external actions outside grant, genuine preference calls, contradictory standing orders, unresolved program dead ends. Park them and route other work around them. In-scope retries, CI triage and evidence-backed local fixes do not need repeated permission. Only frontier-blocking discoveries enter the current program; unrelated work stays in follow-ups.

**Reply:** predicate and counts computed from units/ledger, track outcomes, actual PR frontier plus SHAs, verdict classes/evidence, abandoned units/reasons, operator gates, state/trail paths and real PR links. Use bullets on Discord.
