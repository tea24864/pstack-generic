# pstack for Hermes

A namespaced, MIT-licensed adaptation of Lauren Tan's pstack engineering workflows for Hermes Agent. Upstream snapshot: `cursor/plugins`, revision `23e4138daa01c42d4969f7a5465f82704e64f798`, pstack `0.15.6`.

## Package scope

- 49 core skills and all 23 Poteto Mode playbooks.
- Three optional Benny issue-triage/reproduction/setup skills. Installing the documents does not activate an automation, schedule a job, or connect a service.
- Native `pstack-*` names preserve your existing skills. Benny names use `pstack-benny-*`.
- The original 160-file source snapshot remains under `upstream/pstack/` for comparison and attribution. It is not installed as executable agent instructions.
- No Hermes source changes, plugin, provider changes, or automatic recurring jobs are required for the core workflows.

## Use

Start a new Hermes session after installation so the skill catalog and slash-command index refresh. Examples:

```text
/pstack-poteto-mode investigate this defect, reproduce it, then fix and verify
/pstack-how explain this subsystem with traced evidence
/pstack-architect design this change with a checkpoint before implementation
/pstack-interrogate review this diff without applying changes
/pstack-swarm check every package; one result per package
/pstack-tdd add a focused failing regression test, then fix this bug
/pstack-benchmark-checklist assess this measured speedup
```

Poteto Mode is opt-in conversational behavior, not an always-applied prompt change. Explicit checkpoints, plan-only requests, opt-out, and user permission boundaries remain authoritative. A skill invocation is not authorization to merge, publish, delete data, deploy, or alter configuration.

The three Benny workflows and `pstack-make-bot-ui` describe optional integrations. They must first verify the necessary Hermes/GitHub/webhook/MCP facilities. Their setup steps require a separate configuration request and do not run during installation.

## Compatibility

Read `docs/hermes-runtime.md` for the complete execution contract.

- Cursor `Task` calls become native Hermes delegation. Children share the filesystem, so separate write ownership or worktrees are required.
- The live delegation schema has no per-task model selection. Independent same-model attempts are supported and labelled as such. Genuine multi-model work requires a separately verified external CLI or independent Hermes process and available model/provider credentials; there is no fictional role scheduler.
- Model defaults inherit the current session/profile delegation policy. No hardcoded upstream model slugs are silently substituted.
- Cursor rules, cloud environments, `/loop`, and external Cursor plugins are not requirements. A persistent run or scheduled job needs separate user authorization and supported Hermes machinery.
- Missing MCP/integration evidence is reported as a gap. Credentials are never requested in chat or embedded in skills.
- Source helpers that cannot run on the supported runtime are marked reference-only, not presented as working integrations.
- Target platform support is specified in each skill; the port is exercised on Linux. Linux/macOS gating does not claim that every macOS-specific integration was live-tested.

## Verification and installation

### Install on another machine or profile

Copy or clone this repository to the destination machine. Installation requires Python 3.10+ (stdlib only) and an existing Hermes installation for using the skills. Run from the repository root:

```bash
python3 tools/manage.py install --home "$HOME/.hermes"
```

Select a different agent/profile explicitly with `--home /path/to/that/hermes-home`. Without `--home`, the installer uses `HERMES_HOME` if set, otherwise `~/.hermes`. It writes only `skills/software-development/pstack-*` inside the selected home, never sibling profiles, configuration, credentials, or jobs. An empty selected home can receive the skills without creating configuration. Restart the destination session to refresh its catalog.

`package-manifest.json` contains hashes produced after the maintainer's native Hermes validator/linter/security scan. The installer verifies the exact current file set and every hash before copying, reads back installed bytes, and refuses collisions rather than overwriting local edits. The manifest is an integrity check, not a cryptographic signature: review and trust the repository/revision you install. Local install reports stay untracked. Installation of documents is portable; workflow/platform/tool availability still follows the compatibility limits above.

### Validate and maintain

`tools/manage.py validate` performs a stdlib structural check; `--native` also invokes installed Hermes internals when run in its Python environment. The following tested launcher command runs the native scans and complete package tests without assuming a venv path:

Native tests can run through the verified Hermes Python module launcher:

```text
terminal(command="hermes --run-module unittest discover -s tests -p test_port.py -v", timeout=120)
```

Run that command from the package root. The tests use stdlib unittest plus Hermes's own installed modules and dependencies. They cover source/skill/playbook completeness, the native catalog/skill/slash loaders, attribution, installer collision refusal, post-scan changes, profile isolation, and failed-copy rollback.

`tools/live_smoke.py` runs bounded, isolated live Hermes sessions for investigation, design with a checkpoint, adversarial review, and a regression bug fix. It requires explicit provider/model arguments and writes actual JSONL transcripts plus independently checked fixture results. These live tests do not publish or modify production repositories.

See [VERIFICATION.md](VERIFICATION.md) for the delivery summary and `reports/` for coverage, compatibility, static validation, installation, and actual live execution results. `reports/live-review.json` preserves failed architecture attempts separately from the completed inline fallback; a serial pass is not a claim that a full independent panel completed. A successful loader test is not a claim that every external integration or autonomous shipping workflow has been exercised.

Run `python3 -B tools/verify.py` from this directory for package/helper tests (requires the current Hermes launcher, Git, Node.js and Bash). Add `--installed` only to audit the installation recorded in this checkout's local report. Fresh clones do not require any previous machine's reports.

After approved edits, regenerate portable provenance and the manifest:

```bash
python3 tools/coverage.py
hermes --run-module unittest discover -s tests -p test_port.py -k test_full_native_validation -v
python3 tools/manage.py manifest
python3 -B tools/verify.py
git diff
```

The manifest command consumes the native scan just produced by the focused validation test and refuses files changed since that scan. The full suite then verifies the refreshed manifest. Commit the reviewed skills, updated ledger and manifest together. Never hand-edit hashes to bypass review.

Versioned: skills, scripts/templates/references, tests, tooling, MIT attribution, pinned upstream snapshot, source inventory, `provenance/coverage.json`, and `package-manifest.json`. Ignored: local `reports/`, transcripts, profile snapshots, Python bytecode, environments and credentials. The repository has no remote until one is explicitly configured.

## Updating

Preserve local edits. Pin a new upstream revision, compare it against `inventory.json` and `provenance/coverage.json`, account for every changed source file, and adapt behavior before installing updates. Do not run a blind replacement or install the upstream Cursor instructions directly over the port. The safe installer intentionally refuses existing names; updates need an explicit reviewed diff and a backup.

## License and attribution

Original pstack copyright is retained in `LICENSE` and every skill's `references/license.md`. Source author: Lauren Tan (poteto). Hermes adaptation: tea24864 with Hermes Agent. This port is MIT-licensed and is not affiliated with or endorsed by Cursor.
