# Verification: setup-time specialization

## Repository deliverable

- One runtime-neutral authored core: 52 skills, including 24 principles and all 23 playbooks. Standard frontmatter has scalar-string metadata. Pure principles use no runtime insertion points.
- Reviewed `hermes` adapter and explicitly limited `generic` baseline; deterministic setup/build/install tooling and ownership-safe regeneration.
- Reproducible generated Hermes distribution: 52 skills, 186 installable files. The former duplicated runtime manuals and unsupported helper copies are no longer installed.
- All 160 upstream files remain byte-identical and fully accounted for at canonical targets. MIT copyright and Lauren Tan attribution retained; pinned revision `23e4138daa01c42d4969f7a5465f82704e64f798`, pstack 0.15.6.

## Automated checks

The current full verification command passed **83 tests**: 63 source/package/specialization/native-loader/installer/uninstaller checks, 10 orchestration-helper tests and 10 decision-logger tests. Node/Bash syntax checks also passed. Native frontmatter/lint/security validation reported zero errors; advisory findings remain visible in local `reports/validation.json` rather than disabling scanning.

Coverage includes:

- Exact core/skill/playbook/license/upstream coverage and scalar metadata.
- No host API names or machine-local paths in authored core; allowed insertion points only; principles need no runtime map.
- Rebuilding from core/adaptor facts reproduces every committed Hermes artifact and its distribution manifest byte-for-byte.
- Generic generation contains no foreign host APIs or unresolved placeholders and discloses its absent capabilities.
- Native Hermes discovery/loading of all 52 entrypoints, nested playbooks/rubrics, slash invocation and retained panel-policy default/override injection.
- Observed-tool detection, ambiguity/unknown refusal, explicit generic acknowledgement, unknown/missing insertion points and symlink/template refusal.
- Exact artifact integrity, additions/changes, collisions across categories, preserved local edits, partial-copy failure and post-copy injected-file rollback.
- Runtime/version profile recording, valid native metadata placement and isolated-Python CLI imports.
- Receipt-owned uninstall: preview by default, confirmed removal, edits/additions/missing files/extra directories/symlinks/malformed or legacy receipt refusal; staging failure restores the installation and cleanup failure reports remaining staging.
- Two complete install → uninstall cycles for each adapter (52 skills/186 files per install), via isolated CLI calls in disposable paths with spaces; all unrelated fixture skills/configuration preserved.
- Actual helper/logger behavior: neutral plan checker, live-lane/evidence rejection, read-only Git/index preservation, append/concurrent-write and safety regressions.

Maintainer commands and prerequisites are in [README.md](README.md). The generator refuses local edits/additions to owned generated output. The native-scanned package manifest is an integrity record, not a signature or universal runtime certification.

## Disposable installation and preserved live state

Both full distributions were generated and installed into separate disposable homes with spaces using **isolated stdlib Python (`-I`)**. Each copied all 52 skills/186 files, read back every hash and runtime profile, and preserved preexisting fixture configuration/unrelated skills. These tests required no dependency installation or runtime configuration changes.

The previously installed default-profile package's **257 files** still match the pre-refactor snapshot, and the live `config.yaml` hash is unchanged. Repository generation is not a migration of that installation. No other profiles were modified; no providers, credentials, integrations, jobs, hooks or routes were activated.

## Live behavioral probes

`tools/live_specialized.py` supplies generated instruction content and direct reference paths to fresh Hermes CLI sessions using explicitly selected `openai-codex` / `gpt-6.1-sol`, with rules/config injection disabled and only file/shell tools. This deliberately separates instruction behavior from native catalog loading and does not claim independent delegation or another agent product was exercised.

Semantically reviewed tool traces show:

- **Investigation:** actual source reads and executable probes traced input/calls/output/errors, including exactly three fetches for three IDs. Fixture code unchanged; no independent reviewers claimed.
- **TDD:** the underscore-preservation test was added first, failed with `hello-world` versus `hello_world`, then passed after the regex fix. Both local tests and a separate direct contract probe passed. Only the authorized source/test fixture files changed.
- **Generic architecture fallback:** the first attempt timed out after producing design artifacts; it remains incomplete. A separately labelled compact retry completed grounding, two structurally distinct designs, rubric comparison, chosen base/grafts/rejections, public types/usage and proposed acceptance cases, stopping at the design checkpoint. Source unchanged; no independent children or cross-judge were claimed or available.

Raw attempts, receipts, hashes and semantic review evidence stay in ignored `reports/specialized-live/`. A later fallback pass does not rewrite the failed attempt as a pass. Prior pre-refactor independent architecture attempts also remained incomplete; the complete independent candidate/judge/synthesis pipeline is **not verified end-to-end** by these probes.

## Limits

- `generic` is an acknowledged restricted baseline, not a tested adapter for Cursor, Claude Code, Codex or every Agent-Skills-capable product.
- Same-model independence is not model diversity. Missing facilities and task-required independence remain explicit blockers, not fabricated tool calls or silently equivalent serial review.
- Eighteen original Bun/store helper sources remain reference-only. Live GitHub publishing/shipping, Benny automation, webhooks/MCP/private connectors, scheduling and external-model runners were neither tested nor activated.
- Linux was exercised. Packaging/compatibility metadata does not prove live behavior on other operating systems.
- Bootstrap requires a trusted source checkout/Python. Setup does not freely rewrite skills, memorize a global map or create absent capabilities.
- Existing skill collisions require a separate reviewed migration/backup. No live migration, push or publication is part of this repository refactor.
