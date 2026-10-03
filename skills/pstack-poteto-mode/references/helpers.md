# Bundled helper status and requirements

Resolve `<skill-dir>` from the loaded skill path, never a hardcoded user home. Invoke through `terminal`. These helpers do not authorize side effects, installs or long-lived monitoring.

## Supported local helpers

- `terminal(command="node <skill-dir>/scripts/check-plan.mjs <plan.md>")`. Requires pre-existing Node only. Read-only strict lint for the multi-phase template, required headings/verification rule, ten concrete live coverage lanes, evidence/pass predicates, perf and review gates. This is deliberately a heavyweight plan checker, not a generic Markdown linter. Hermes markers are skill_view/audit/status message rather than Cursor ticks. Exit 0 is structural acceptance, not runtime correctness.
- `terminal(command="bash <skill-dir>/scripts/worktree-audit.sh <repo>")`. Requires bash, Python 3 and git on Linux/macOS. Shim invokes the adjacent stdlib Python audit. Offline/no fetch/no transcript scanning/no deletion. Handles spaces and porcelain rename records. Reports ignored/untracked/tracked state, size errors, stale tracking-ref divergence and unknown activity/PR state. Every row is held/review-required and deletion_authorized is false. Run inventory plus explicit activity/PR/retention checks before proposing cleanup.

## Reference-only Bun GitHub watcher

UNAVAILABLE as an exercised integration in this port. Bun is absent and no dependencies were installed. Every original watcher source, test, fixture, type assertion, config and pinned lock is retained under `references/upstream-helpers/scripts/`, not the supported scripts directory. The adapted bootstrap fails closed on missing/wrong pre-existing Commander 14.0.0; it never installs, writes markers, or restarts itself. Do not execute archived helpers as production machinery.

A separately approved future promotion must verify Bun, existing Commander 14.0.0, git and authenticated gh; run `bun test watch-pr` and the pre-existing TypeScript compiler against `watch-pr/tsconfig.json` without dependency-fetching runners; exercise wrapper help/status/timeout against isolated fixtures; and then perform an authorized real GitHub read. Archived orch tests require their own path and Graphite-adapter review, not just a watcher test pass. No runtime result is claimed here.

Static behavior assessment: watcher supports JSON/NDJSON, single/stack/queued status, bounded timeouts, tier-major blocker ordering, retry/backoff, strict type/enum parsing, readiness versus actual merge distinctions, and explicit queue snapshots. Status-only exit 0 is retrieval success, not PASS. Its default timeout zero is unbounded; any future invocation needs a positive bound. Pretty output contains Markdown tables, unsuitable for direct Discord replies. Auto discovery caps open PRs at 300, and review threads fetch only the first GraphQL page of 100. Use complete independent paginated reads before any coverage/merge claim. Cursor mentions in source identify remote bots, not a local Hermes requirement.

The native Babysit/Shipping playbooks use direct verified gh reads with full pagination instead. Missing tools/auth/results are BLOCKED, never a fabricated green state.

## Runnable local regression checks

Run `terminal(command="python3 <skill-dir>/scripts/test-helpers.py")` with pre-existing Python 3, Node, bash and git. The nine stdlib tests build disposable git fixtures under `$TMPDIR`, exercise the actual POSIX audit wrapper with whitespace paths, tracked/untracked/ignored work and rename records, prove no audit mutation, and run the actual Node checker against accepted/rejected plan fixtures and usage errors. No network or dependency installation is used. This does not test Bun helpers or live GitHub state.

## Reference-only orchestration store

Read `references/upstream-helpers/README.md`. Original orch CLI/store/tests are archived for study, not runnable integration. They discover frontier through Graphite metadata, import their former bootstrap, and have Bun/Commander requirements. The Hermes Orchestrate playbook instead owns plain files via tools and exact gh/git reads. No scheduler, child lifecycle or automatic merge is supplied by these files.
