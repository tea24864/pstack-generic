# Bundled helper status and requirements

Resolve `<skill-dir>` from the loaded skill's actual directory, never a hardcoded home or profile. Run supported commands in the native shell. Helpers grant no installation, cleanup, external-write or long-lived-monitoring authority.

## Supported local helpers

- `node "<skill-dir>/scripts/check-plan.mjs" "<plan.md>"`. Requires pre-existing Node. Read-only strict lint for the multi-phase template, ordered headings/sub-blocks, verification rule, ten concrete live coverage lanes, evidence/pass predicates, performance and operator review gates. It is a heavyweight plan checker, not a general Markdown linter. Exit 0 proves structure only. The parser checks explicit execution-playbook loading, bounded audit checkpoints and status-message evidence without requiring a particular runtime API.
- `bash "<skill-dir>/scripts/worktree-audit.sh" "<repo>"`. Requires existing Bash, Python 3 and git on Linux/macOS. The shim invokes adjacent stdlib Python. Offline inventory only: no fetch, transcript scan, forge calls or deletion. Handles spaces and porcelain rename records. Reports ignored/untracked/tracked work, size errors, stale tracking-ref divergence and unknown activity/PR state. Every row is held/review-required, with deletion authorization false. Inventory plus fresh activity/PR/retention checks are required before proposing an explicitly approved deletion set.

## Unsupported upstream watcher and store

Unexercised Bun watcher/store sources are not shipped in this skill or available as supported integrations. The repository's immutable `upstream/pstack/` snapshot is provenance only. There is no local helper directory to load or execute for these sources. Do not copy or run archived machinery as production infrastructure.

Future promotion is separately scoped: verify an already installed Bun runtime, required pinned Commander 14.0.0 dependency, git and authenticated forge client; run the original watcher tests and pre-existing TypeScript compiler without dependency-fetching runners; test wrapper help/status/timeouts in isolated fixtures; then perform an authorized real forge read. Orchestration-store tests require their own path and Graphite-adapter review. No live result is claimed by these documents.

Static source assessment records JSON/NDJSON output, single/stack/queued status, bounded timeouts, tier-major blocker ordering, retry/backoff, strict type/enum parsing, readiness-versus-merge distinctions and queue snapshots. Retrieval success is not PASS. The archived watcher's zero default timeout is unbounded; any future promoted invocation needs a positive bound. Its discovery cap is 300 open PRs and review threads cover only the first GraphQL page of 100. Use complete independent paginated reads before coverage or merge claims. Pretty Markdown tables need adaptation for text-only delivery surfaces.

The archived store discovers frontier through Graphite metadata and has its own bootstrap and Bun/Commander requirements. The authored Orchestrate playbook instead owns plain files and exact forge/git reads. It does not provide a scheduler, worker lifecycle or automatic merge machinery.

## Local regression tests

Run `python3 "<skill-dir>/scripts/test-helpers.py"` with existing Python 3, Node, Bash and git. The ten stdlib tests build disposable git fixtures under the configured temporary workspace, exercise the actual audit wrapper with whitespace paths and tracked/untracked/ignored work plus rename records, prove no audit mutation, and run the actual Node checker against accepted/rejected neutral plan fixtures and usage errors. No network or dependency installation is used. The neutral-loading regression proves plans need no foreign API marker. These tests do not prove upstream Bun helpers or live forge state.
