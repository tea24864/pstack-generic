# pstack: shared source, runtime-native skills

MIT-licensed engineering workflows adapted from Lauren Tan's pstack 0.15.6 (`cursor/plugins`, revision `23e4138daa01c42d4969f7a5465f82704e64f798`).

## Ownership and scope

- **Author `core/skills/` only:** 52 standard-format skills, including 24 principles, 23 Poteto Mode playbooks and three optional Benny workflows. Supporting references and executable helpers live beside their authored entrypoints.
- **Maintain `adapters/`:** short, reviewed runtime facts and localized insertion instructions. No executable templates, credentials, hidden role scheduler or automatic integrations.
- **Generate `skills/`:** checked-in Hermes output for backwards-compatible installation. Never hand-edit it. Pure principles require no runtime mapping or mandatory orchestration manual.
- **Keep provenance:** all 160 original files remain byte-identical in `upstream/pstack/`; `provenance/coverage.json` maps every source disposition to canonical core or immutable provenance. Archived watcher/store sources are not installed instructions or supported integrations.

Setup specializes relevant operations once. Installed workflows contain their own native instructions for fresh sessions and isolated workers; they do not depend on a remembered global mapping. Standard packaging does not standardize execution APIs.

## Initial adapters

- **`hermes`:** concrete native file, delegation, skill, history and policy mappings. Native catalog/loading/config injection and helper checks are exercised on Linux. No per-task provider/model selector; same-model independence is not model diversity. Concurrency and run-wide child budgets differ.
- **`generic`:** an explicitly limited file/shell baseline for another Agent-Skills-capable host. No independent delegates/cross-judge, private history API, per-role model routing, durable work or runtime settings are supplied. This is **not a verified adapter for every named agent product**. Required unavailable capabilities remain blockers.
- **Unknown runtime:** review a new adapter or explicitly acknowledge the generic baseline. Detection uses actually observed tools, proposes candidates and refuses ambiguous/unknown automatic selection. It is not a capability probe or authorization.

See [docs/specialization-design.md](docs/specialization-design.md) for boundaries and [VERIFICATION.md](VERIFICATION.md) for proofs and gaps.

## Agent-driven setup

Read `core/skills/pstack-setup-pstack/SKILL.md` directly from a trusted checkout. This bootstrap needs no prior skill loader or remembered mapping. It checks live schemas, confirms runtime and destination, generates native skills and verifies installation. A source checkout and Python 3.10+ are explicit prerequisites; an installed bootstrap does not pretend to contain the whole compiler/source repository.

For detection, create a local JSON file containing `{"tool_names": ["actually-observed-tool", "..."]}`; do not use the illustrative names literally. Run:

```bash
python3 tools/setup.py detect --evidence observed-tools.json
```

Inspect the proposed adapter against the current host's schemas. Then select explicitly:

```bash
python3 tools/setup.py build --runtime hermes --output build/hermes-new
python3 tools/setup.py verify --distribution build/hermes-new
python3 tools/setup.py install --distribution build/hermes-new --home /confirmed/hermes-home
```

Add `--runtime-version <observed-version>` to build when known; otherwise the installation profile records an unreported version. `--home` is Hermes-only and writes skills beneath that explicitly selected home. There is no implicit destination.

For an acknowledged generic baseline:

```bash
python3 tools/setup.py build --runtime generic --output build/generic-new
python3 tools/setup.py verify --distribution build/generic-new
python3 tools/setup.py install --distribution build/generic-new \
  --skills-dir /confirmed/host-skill-directory --acknowledge-limits
```

Build refuses an existing output directory. Installation checks the exact generated artifact set/hashes, refuses existing skill names across categories, rolls back owned copies on failure and reads back all targets. `.pstack-runtime.json` records selected runtime/version, source/adapter hashes, supported capabilities and limits. Recheck actual capabilities during execution. The manifest is an integrity record, not a cryptographic signature; trust/review the checkout you install.

**Loading, generation and installation never authorize settings changes, credential/provider changes, external writes, dependency installation, hooks or recurring jobs.** Benny and bot-UI integrations remain manual/conditional. Panel-policy changes require separately confirmed documented keys and exact readback; preferences cannot create missing routing or execution capabilities.

### Existing Hermes installer

The old entrypoint still installs the reviewed, generated Hermes distribution using stdlib only:

```bash
python3 tools/manage.py install --home /confirmed/hermes-home
```

It retains the `skills/software-development/pstack-*` layout and collision refusal. Its legacy implicit default follows `HERMES_HOME`, then `~/.hermes`; use an explicit home. It does not migrate existing installations or create configuration. Prefer the new setup path for a recorded runtime profile.

## Use

Refresh the host's catalog/session after installation. Hermes examples:

```text
/pstack-poteto-mode reproduce this defect, fix it and verify
/pstack-how explain this subsystem with traced evidence
/pstack-architect design this change; stop before implementation
/pstack-interrogate review without applying changes
/pstack-tdd demonstrate the regression before fixing it
```

Poteto Mode remains opt-in conversational behavior, not an always-applied rule or runtime-enforced state. User scope, checkpoints and permission gates win.

## Maintain and verify

Edit the neutral core or selected adapter, then run these tested commands from the checkout:

```bash
python3 -B tools/regenerate.py
python3 -B tools/coverage.py
hermes --run-module unittest discover -s tests -p test_port.py -k test_full_native_validation -v
python3 -B tools/manage.py manifest
python3 -B tools/verify.py
git diff
```

Regeneration refuses edited/extra generated files and replaces only the owned distribution; it never touches installed skills. Broad runtime-manual synchronization and the old separate authoring/generation scripts are retired. The manifest consumes an actual native scan and refuses stale artifacts. Full verification includes source coverage, runtime leakage, reproducibility, generic generation, native loaders/config injection, tampering, collision/isolation/rollback and real helper execution. Verification needs an existing Hermes launcher, Git, Node and Bash; installation/rendering use stdlib only.

`tools/live_specialized.py` runs explicitly selected provider/model probes against generated content in disposable fixtures. It skips user rules/config injection and supplies selected files directly, with only file/shell tools. Native catalog loading is a separate proof; these probes do not verify independent delegation or another agent product. Distinct attempt labels preserve failures and retries. See its `--help`; local traces stay ignored.

Commit core, adapters, generated skills, manifests and coverage together. Reports, local transcripts/profile snapshots, environments, credentials, bytecode and `build/` stay ignored. Pin and account for upstream changes; do not copy Cursor instructions over native output. Existing installations require an explicitly reviewed migration and backup, not forced overwrite.

## Attribution

Original copyright/MIT text remains in `LICENSE` and every skill's `references/license.md`. Source author: Lauren Tan (poteto). Adaptation: tea24864 with Hermes Agent. This project is not affiliated with or endorsed by Cursor. No remote publishing is implied by local repository maintenance.
