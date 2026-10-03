# Verification and delivery

## Delivered scope

- 52 installed namespaced Hermes skills: 49 core plus 3 optional Benny workflows, including all 24 engineering principles.
- All 23 Poteto Mode playbooks adapted.
- All 160 original files accounted for by `provenance/coverage.json`; unsupported helpers explicitly retained as reference-only.
- Source: `https://github.com/cursor/plugins`, pstack 0.15.6, revision `23e4138daa01c42d4969f7a5465f82704e64f798`. MIT license and Lauren Tan attribution retained.

## Structural and helper verification

The portability follow-up passed 41 automated tests: 22 package/native-loader/installer tests, 9 orchestration-helper tests, and 10 decision-logger tests. Node and Bash syntax checks also passed. New installer regressions cover explicit nondefault homes (including spaces), initializing an empty home, and refusing unscanned additional files. `package-manifest.json` records the reviewed portable artifact hashes; `reports/verification.json` is generated locally and ignored by Git.

Native validation finds all 52 entrypoints and 23 playbooks, with zero errors. All 257 installed package files match the freshly validated staged artifacts. Direct installed-catalog inspection and native skill loading also confirmed all 52 names and exact entrypoint bytes under the default profile.

Preexisting skill contents and `config.yaml` match their pre-install hashes. Normal Hermes skill-usage/curator telemetry changed while loading and patching the newly installed suite; this is recorded separately. No dependencies, provider changes, recurring jobs, hooks, webhook routes, or external integrations were activated.

## Live workflow evidence

Actual isolated Hermes runs used the explicitly selected `openai-codex` / `gpt-6.1-sol`. Raw attempts are retained in `reports/live/`; `reports/live-review.json` distinguishes semantic results from process exit codes.

- Investigation: actual function input/call/output/error trace, including exactly three fetches for three IDs. Source unchanged.
- Adversarial review: two completed independent same-model reviewers identified the half-open interval bug. The lead independently executed seven cases, proving two failures. No fix was applied; source unchanged. Lack of model-family diversity is disclosed.
- TDD: regression failed for underscore loss before implementation changed, then both local tests and an independent direct contract probe passed. Only the two authorized fixture source/test files changed.
- Architecture, independent attempts: initial run timed out. A larger-budget retry produced and read both distinct independent design artifacts, then the independent judge was refused because the one-shot run had used its two-child total budget; final synthesis/checkpoint did not complete before timeout. Neither attempt changed cache.py. These are incomplete results, not passes.
- Architecture, disclosed inline fallback: completed two distinct designs, judged/synthesized them, specified types and get/set semantics, and stopped for approval. Source unchanged; no independent candidate or judge ran in this attempt. This verifies the serial fallback, not the complete independent-panel pipeline.

The architecture/arena skills now distinguish concurrent-child caps from run-wide child budgets, budget for later synthesis, and explicitly fall back inline after verified exhaustion rather than retrying or changing global settings.

## Advisory review

The native scanner returned safe verdicts with informational/structural findings; it was not disabled. Advisories cover optional agent-document references, illustrative loopback URLs, subprocess use in audited helpers/tests, executable Node/reference-only helper files, and Poteto Mode's file count. Linter/identifier notices include the future generated feature-map README, generated-name placeholders, an ownership label, and ordinary prose containing “head.” These are not unresolved executable Cursor dependencies. See exact findings in `reports/validation.json`.

## Limits

- Same-model delegation is not multi-model diversity.
- Eighteen Bun/store helper sources remain reference-only; their runtime integrations were not exercised.
- Live GitHub publishing, shipping, Benny automation, webhooks, MCP/private connectors, scheduled jobs, and external-model runners were not tested or activated.
- Linux was exercised. Platform metadata is not evidence of live macOS integration testing.
- Poteto Mode is opt-in conversation behavior, not runtime-enforced persistent state.
- Full independent architecture candidate/judge/synthesis execution remains unverified end-to-end in one run; individual candidates and the inline completion path have actual evidence.

## Usage and locations

Package: this repository checkout.
Installed skills: `<selected-Hermes-home>/skills/software-development/pstack-*`.

Install with `python3 tools/manage.py install --home /path/to/hermes-home`. The prior default-profile-only restriction is removed from the portable installer; only the explicitly selected target is written. Local reports and transcripts remain available on the original workstation, but are excluded from version control because they contain machine paths and profile snapshots. Fresh clones generate their own reports.

Start a fresh Hermes session to refresh catalog/slash commands, then invoke `/pstack-poteto-mode <task>` or a focused skill such as `/pstack-how`, `/pstack-architect`, `/pstack-interrogate`, or `/pstack-tdd`.

Nothing was pushed or published. Updates require a reviewed diff and backup; the fresh installer refuses existing names rather than overwriting local edits.
