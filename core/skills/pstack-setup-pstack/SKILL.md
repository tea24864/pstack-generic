---
name: pstack-setup-pstack
description: "Specialize and install skills for a confirmed runtime."
license: MIT
metadata:
  author: "Lauren Tan (poteto), tea24864"
  version: "0.2.0"
  source-revision: "23e4138daa01c42d4969f7a5465f82704e64f798"
---

# Set up pstack

## When to Use

Use for explicitly requested installation, runtime specialization or panel-policy setup. Do not run implicitly during another workflow. This bootstrap is readable directly from source: it depends on neither a remembered mapping nor another skill loader.

## Prerequisites

- A trusted checkout of this pstack source repository, Python 3 and actual access to the intended destination. Confirm the checkout; do not assume it was shipped inside an installed skill directory.
- The runtime's observed tool names and live schemas, its version when available, and the user's installation scope. Tool names propose identity; they do not prove every capability is enabled or authorized.
- Permission to write only the requested destination. Loading this skill is not permission to install, replace existing skills, change configuration, publish or activate integrations.

Repository paths below are relative to the trusted checkout, not to this installed skill directory.

## Procedure

1. **Inspect rather than infer.** Record the tools actually exposed in the active session in a local evidence JSON object with a `tool_names` array. A runtime name in a path, installed executable or chat label is insufficient. Use the host's real native facilities to read/write these files and run the setup commands; do not invent APIs.
2. **Propose a reviewed adapter.** Run `python3 tools/setup.py detect --evidence <observed-tools.json>`. Read the proposed adapter's identity, capability facts, short insertion instructions and limits in `adapters/<runtime>.json`; compare them with live schemas. Record runtime/version and observed restrictions in the task-local setup report, without dumping configuration or credentials. Detection proposes a candidate, not authorization or a capability probe.
3. **Resolve uncertainty explicitly.** Unknown or ambiguous evidence stops automatic selection. Propose a reviewed new adapter or the explicitly limited generic baseline. Do not freely rewrite all workflows, guess missing tool schemas or silently claim another product is supported. The generic baseline has no independent delegates, per-worker model selection, private session-history API or durable scheduling. Sequential lenses are not independent review. If acceptance requires a missing capability, report blocked.
4. **Confirm one target.** Present runtime, actual versus unverified capabilities, limitations, output directory and exact skill destination. Obtain the user's selection unless that exact installation scope is already authorized. Ask for the host's documented skill directory when no reviewed adapter defines it; never guess another profile or user installation.
5. **Generate, don't teach a global map.** Run `python3 tools/setup.py build --runtime <selected-adapter> --output <new-output-directory>`. Add `--runtime-version <actually-observed-version>` when known; an omitted version is recorded as unreported rather than inferred. The command expands only each workflow's relevant insertion points. It does not alter installed skills or runtime settings. Fresh sessions and child workers read native instructions in their own generated skill; pure principles need no runtime mapping.
6. **Verify the distribution.** Run `python3 tools/setup.py verify --distribution <new-output-directory>`. Check all source workflows/playbooks are present, source/adaptor hashes and recorded limitations are correct, and output contains no unresolved insertion syntax. Use the repository's verification suite for maintenance changes; runtime-native loading and live behavior are separate proofs from generation.
7. **Install only the confirmed output.** Run `python3 tools/setup.py install --distribution <new-output-directory> --skills-dir <confirmed-directory>`. A reviewed adapter may document an equivalent explicit home option. Generic installation additionally requires `--acknowledge-limits`. The installer verifies file hashes, refuses name collisions across categories and records the selected runtime/capability profile in `.pstack-runtime.json` within the chosen skills directory. Never force replacement of user edits; stage and review a migration separately.
8. **Read back.** Confirm every installed artifact matches the generated distribution and that the host discovers/loads representative entrypoints and supporting references. Exercise one relevant workflow in a disposable fixture; loading is not behavior verification. Record unrun capabilities honestly. Recheck live limits during execution because configuration can change after setup.

## Separately requested panel policy

Ordinary setup changes no runtime configuration. If the user separately requests panel preferences, propose a positive panel size (default three) and inherited-model strategy unless a verified external runner is already authorized. Inspect only the selected adapter's configuration mapping and the host's current non-secret documented keys. Present exact proposed keys, destination, fan-out/cost impact and unchanged provider/reasoning/global routing; wait for confirmation before writes and read back the exact changed keys afterward.

A policy marker cannot create per-role models, model diversity or scheduling. Verify any external runner's actual help, supported provider/models, isolation, task prompts and real output before proposing it. Never add permanent prompt rules, credentials, integrations or recurring jobs as a hidden setup dependency.

If the project lacks a real-app verification harness, offer pstack-create-verification-skill once; invoke only within approved scope.

## Pitfalls

- Standard skill packaging does not standardize runtime tool APIs or permission enforcement.
- Generic fallback is an acknowledged limitation, not verified support for every agent product.
- A read-only instruction is not a sandbox; shared writers require distinct ownership/worktrees.
- Generation does not grant publication, configuration or migration authority. Existing collisions are deliberate refusal, not a reason to bypass safeguards.
- If Python, checkout access or secure authentication is unavailable, leave a precise handoff instead of simulating installation.

## Verification

Report selected runtime/version, evidence source, observed versus assumed capabilities, generated/installed counts, exact destination and readback results. Distinguish proposed, generated, installed, loaded and behavior-tested states. Confirm unrelated files/settings were preserved. Report gaps and failed attempts without relabeling serial fallback as independent execution.

## Attribution

Adapted from Lauren Tan's MIT-licensed pstack 0.15.6, source revision `23e4138daa01c42d4969f7a5465f82704e64f798`. See `references/license.md`.
