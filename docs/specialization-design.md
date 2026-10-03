# Setup-time runtime specialization

Status: approved design; implement in the repository only. Existing installed skills are not migration targets.

## Alternatives and choice

1. A universal runtime manual loaded on every skill invocation: rejected because every agent pays for irrelevant branches and pure principles inherit orchestration clutter.
2. Setup writes a remembered tool mapping or global rule: rejected because future sessions and isolated workers do not reliably inherit it, and global instructions broaden scope.
3. Shared source plus deterministic setup-time specialization: selected. Each installed workflow contains its own relevant native instructions. Setup does not create absent capabilities.

## Owned data

- `core/skills/<name>/`: the only authored workflow/reference/script source. Standard Agent Skills frontmatter. Natural-language workflow plus explicit `{{runtime.KEY}}` insertion points where host behavior actually matters. Pure principles use no insertion points.
- `adapters/<runtime>.json`: supported adapter facts, limitations and short instructions for named insertion points. No executable templates, provider credentials or per-role scheduler.
- `skills/`: reproducible Hermes distribution retained for backwards-compatible installation; generated, never hand-edited.
- `build/<runtime>/`: other generated distributions, ignored by Git. `distribution.json` records adapter/core hashes, selected runtime and capability limitations; no secrets.
- `tools/specialize.py`: stdlib renderer, validator and setup/install CLI. Strict placeholders, deterministic generation, no overwrite, full artifact verification and rollback of owned copies only.
- `core/skills/pstack-setup-pstack/`: neutral setup entrypoint. It identifies runtime from actually observed tool evidence, selects a reviewed adapter, confirms the exact destination, generates native files and verifies them. Runtime identity is not inferred merely from a directory or installed CLI.

## Insertion-point contract

Allowed keys: `files`, `delegation`, `task_tracking`, `history`, `skill_loading`, `skill_maintenance`, `configuration`, `integrations`, `persistent_work`, `web`, `setup`. Each insertion point expands only at the local workflow boundary that needs it. No broad runtime contract appended to every file. Core instructions never name Hermes/Cursor tool APIs or paths; original attribution and immutable source snapshot remain separate provenance.

## Initial runtime scope

- `hermes`: concrete native delegation, loading, editing, policy and lifecycle instructions; verified through the installed native loader and disposable live fixtures.
- `generic`: explicitly limited native-file/shell baseline for another Agent-Skills-capable agent. No independent delegation, model selection, durable execution or runtime settings claimed. User must acknowledge limits and choose a skills destination explicitly. This is not a tested adapter for every named agent product.
- Unknown or ambiguous runtime evidence does not select an adapter silently. Setup proposes a reviewed new adapter or the explicitly acknowledged generic fallback. No LLM rewriting of all workflows, global prompt changes, settings changes or auto-installed integrations.

## Verification contract

Preserve all 52 source workflows, 23 playbooks, MIT attribution and all 160 upstream source dispositions. Validate pure principles need no runtime map; no host-tool leakage in authored core; generated output contains no placeholders or other runtime branches. Test deterministic output, missing slots, ambiguous detection, explicit fallback acknowledgement, collisions, partial-copy rollback, tampering and paths with spaces. Exercise generated Hermes loading and generic workflow fallback in fresh fixtures. Re-read installation targets. Confirm preexisting live skill/config hashes unchanged, keep local reports ignored, and commit only tested repository artifacts.
