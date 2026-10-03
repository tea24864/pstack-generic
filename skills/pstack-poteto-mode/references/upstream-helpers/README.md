# Reference-only upstream Bun helpers

UNAVAILABLE as exercised Hermes runtime integrations. Do not invoke these archives as production machinery. No Bun runtime or dependencies were installed or tested in this port session.

`scripts/orch/` retains the original CLI/store/tests. Its frontier is Graphite-metadata dependent, not gh-native; the CLI is bookkeeping only and never spawns, waits, schedules or wakes agents. Units, lock, standing-order, ledger, gate, inbox and derived-status designs are useful source references. A future port needs explicit scope, a verified frontier adapter, lifecycle/lock/init/frontier/status tests and dependency approval.

`scripts/watch-pr/` retains the upstream gh/git/Bun watcher, tests, fakes, compile assertions and types. The adjacent bootstrap is adapted to fail closed without installation. The package and lock retain the upstream dependency identity. Study these files under the requirements and limitations in `references/helpers.md` from the skill root. Full pagination gaps and unbounded default timeout prevent treating copied code as a complete verified readiness gate.

The supported scripts are only the Node plan checker, POSIX worktree shim, portable Python audit and their stdlib self-tests. See the active native Orchestrate, Babysit and Shipping playbooks for runtime behavior.
