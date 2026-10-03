### Orchestrate

**Own a standing program through briefs, evidence, queue discipline and a computed frontier.** One task within the session budget uses Autonomous run instead. A bespoke one-off uses pstack-figure-it-out. Multi-day continuity is durable state plus separately authorized scheduling/processes, never a long-lived delegated child.

#### Roles and placement

- Coordinator frames, authors briefs, drains results, owns reports and judgment. Keep code ownership in workers. Clean integration of independently verified commits is bookkeeping only within the grant; conflicted merges and code edits become fresh units.
- Track roles are organizational, not assumed nested worker trees. The coordinator owns dependent worker/verifier waves. Leaves perform assigned work and return questions/proposed next waves. A separate coordinator process needs explicit authorization, verified capability, isolation and budget; it is not implied child recursion.
- Workers and verifiers have isolated conversations but shared filesystem. One writer per exclusive git worktree and branch. Read-only is a brief constraint, not a sandbox. Pass exact paths/SHAs. Report each reviewer's actual model policy and any diversity limitation. Never claim a cloud VM, per-task model, or durable child.

#### Store layout

Use an approved project state directory, for example `.pstack/orchestrate/<project-slug>/`. Keep it outside committed source unless audit publication is explicitly requested. Do not touch another user's runtime state. One coordinator writer owns each shared table. The original orchestration store exists only in the immutable `upstream/pstack/` provenance snapshot, not as shipped machinery.

Use `read_file`, `search_files`, `write_file` and `patch` for file work; use `terminal(command="...", timeout=...)` for real Git, helpers and tests. Read existing files before full replacement. Bundle mechanical loops through `execute_code` when appropriate. Use actual tool output as evidence.

- `preferences.md`: numbered standing orders, one constraint each. Relay them verbatim in every fresh brief with all later directives. Encode recurring corrections before the next wave.
- `overview.md`: append-only durable PR/issue facts, not rewrites per event.
- `units.tsv`: id, track, state, branch, PR, head SHA, brief path. Reconcile every launched child to one terminal outcome.
- `frontier.json`: generation, ordered PR rows (number, branch, head/base SHAs, state), and lowest unmerged PR. Derive it from exact paginated `gh` reads and actual git refs at drain points, never narrative or Graphite metadata assumptions.
- `ledger.tsv`: PR plus exact head SHA, verdict, evidence path, verifier, timestamp. Include base SHA and patch-id in receipts. Verdicts are `live-ui-verified`, `unit-test-verified`, `type-check-only`, `verifier-blocked`, `verifier-failed`. Behavioral work needs more than type-check-only.
- `inbox/`: completed report pointers; archive consumed pointers instead of losing receipts. `gates.md`: operator gates and default proposals, never permission to bypass.
- `decisions.tsv`: pstack-show-me-your-work trail. `status.md`: derived counts/frontier/gates from the tables. Generate and count with Python through the native shell, not mental arithmetic.

#### Brief contract

Every leaf brief is self-contained. A dependency requires context relay, not only ordering. Include GOAL, writable/forbidden SCOPE, exclusive WORKTREE/branch, CONTEXT paths and prior result facts, checkable ACCEPTANCE, exact VERIFY commands/surface, TIMEBOX, FORBIDDEN actions, REPORT status/branch/head/PR/verdict/actual runs/deviations/follow-ups, and verbatim STANDING orders. Never spawn with missing acceptance or write ownership. Collapse a one-command brief to a paragraph while preserving these fields. Audit a sampled brief per track per wave; a failing brief pauses the next refill and repairs the template.

#### Steps

1. Frame a countable predicate, unit count, effort, tracks, expected stacks and wall-clock budget. If one agent fits, collapse to ordinary session execution without store ceremony. Schedule integration from the first verified unit. Before budget exhaustion stop new work and preserve verified output; around 70% reassess whether the remaining time is enough to verify and integrate. Contested decomposition goes through pstack-arena before the pilot. Present framing once and respect named gates.
2. Initialize the plain-file state and decision trail. Write standing orders before any child. Seed frontier from exact current PRs, never a copied stale list. No dependencies or profile changes are installed by this step.
3. Pilot one unit through brief, worker, actual verification, integration/PR state, ledger row and authorized merge if landing is granted. Use evidence to falsify the brief, recipe and unit size before fan-out. For cheap identical units the first normal verified unit is the pilot; expensive/novel work gets independent verification. Merge withheld means the pilot ends at verified review-ready, not an automatic merge.
4. Scale only ready independent units. Batch full self-contained briefs with exact exclusive worktrees, acceptance, verification, budgets, forbidden actions and evidence format. Honor actual concurrency and total budget; bounded waves are acceptable when asynchronous refill is absent. Relay upstream receipts to downstream units and sibling communication through the coordinator. Never make a leaf wait on descendants. If independent workers are unavailable, collapse to a bounded serial program and disclose the lost coverage.

Use `delegate_task(tasks=[{"goal":"...","context":"..."}, ...])` for independent children. Each brief includes scope, evidence, exclusive output/worktree, verification and no delegation or user questions. Children share filesystems; read-only prompts are not sandboxes. Native children inherit the parent model or global pin: do not pass model/provider/readonly/background arguments or claim model diversity. Budget candidates, judges and synthesis together; obey confirmed concurrency and one-shot total-child limits. On exhaustion finish permitted lenses inline and label reduced independence, never retry or change global settings. For async delivery, finish independent work and end the turn; do not poll transcripts. Parent verifies returned artifacts and coordinates later waves. If an independent panel is explicitly required and unavailable, mark it blocked rather than substituting silently.
5. Drain actual completion events at critical-section ends, wave boundaries, frontier events and before reports. Finish atomic brief/stack/gate/ledger updates first. Use the runtime's supported delivery/lifecycle controls, not transcript polling or guessed worker state. Snapshot arrivals, classify landed/needs-verify/failed/cancelled/noise, preserve receipts, update tables, derive status and launch only ready work. Deep review is a separate verification unit, never hidden in the drain. Count every worker, including dropped or absorbed scopes.
6. Integrate continuously. Exactly one topology owner per stack; workers never restack or force-push shared branches. Babysitters report conflicts and work the immutable frontier generation. PR closes/retargets are gated topology operations. Merges require Shipping's independent current-patch verdict, explicit grant, bottom-up contiguous safety and exact readback. A retro pass checks merged PRs for reverts, post-merge CI failures and orphan follow-ups only within the monitoring grant.
7. Close by reconciling every launched child to done/abandoned/cancelled/reconciled, independently confirming the predicate on the real artifact, and checking every landed PR's exact-patch receipt. Audit the trail, preserving the actual same-model limitation. Encode recurring corrections into project standing orders, not another profile. Leave durable state intact as the postmortem.

#### Verification, liveness and failure

Scale verification to the unit. A cheap command gets worker output plus parent rerun/receipt inspection; an expensive, judgment-heavy or high-blast-radius unit gets a separate verifier. CI is an input, never the verdict. A new head voids a ledger row unless Shipping's precise patch-id/build-noise rule preserves a lane; CI/mergeability still refresh. BLOCKED never counts as PASS.

Read actual artifacts, ledger, PRs and branches rather than transcripts or mtime as liveness. Use supported lifecycle evidence; a missing update alone does not prove death. On failure preserve last evidence, scope and options. Scope/cap/OOM gets a smaller fresh task; transient network gets a bounded retry; tool failure first gets capability/inputs diagnosed, not an invented model fallback. Unknown gets one retry. Two retries maximum, then record a gap and replan. A late external-process result reconciles against current head/frontier before accepting anything. Do not replace an active writer until it is confirmed stopped; otherwise use a new isolated worktree and reject stale integration.

Stop new workers on bad upstream output, broken acceptance or dead infrastructure. Preserve in-flight state, repair the cause and resume only within budget. Bound coordinator infrastructure retries too. After restart, inspect supported worker/process state and artifacts; do not assume survival. Re-read orders/tables, reconstruct frontier, reconcile unknown units and use fresh briefs. No fabricated resurrection or persistent-cloud claim.

Native children stop with the parent/session. For separately authorized durable work use supported scheduling or `terminal(background=true, notify=true, persist_on_release=true)` for a real bounded job; never detached child claims or background sleep/poll loops. Discover cron/process tools before use, preserve explicit scope and leave actionable handoff evidence.

#### Escalation

Batch real operator gates: irreversible/destructive actions, external actions outside grant, genuine preference calls, contradictory standing orders, unresolved program dead ends. Park them and route other work around them. In-scope retries, CI triage and evidence-backed local fixes do not need repeated permission. Only frontier-blocking discoveries enter the current program; unrelated work stays in follow-ups.

**Reply:** predicate and counts computed from units/ledger, track outcomes, actual PR frontier plus SHAs, verdict classes/evidence, abandoned units/reasons, operator gates, state/trail paths and real PR links. Use bullets on Discord.
