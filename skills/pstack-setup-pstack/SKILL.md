---
name: pstack-setup-pstack
description: "Configure confirmed pstack panel policy for Hermes."
version: 0.1.0
author: "Lauren Tan (poteto), tea24864, Hermes Agent"
license: MIT
platforms: ["linux", "macos"]
metadata:
  hermes:
    tags: [pstack, engineering, workflow]
    related_skills: []
    config:
      - key: pstack.panel_size
        description: Default independent panel size; explicit scope wins.
        default: 3
        prompt: Default independent panel size
      - key: pstack.model_strategy
        description: Policy only; external runners require separate verification.
        default: inherit-parent
        prompt: Model strategy (inherit-parent or verified-external)
---
# Set up pstack

## When to Use

Use for an explicit setup-pstack request, pstack panel size, or delegation-policy configuration. Do not run implicitly during another workflow.

## Prerequisites

Read `references/hermes-runtime.md` with `skill_view` before executing this workflow. Use only tools and credentials actually available in this session. Invoking this skill does not authorize publication, merges, destructive cleanup, or configuration changes.

## Procedure

This workflow configures pstack-owned settings, not Hermes providers or per-role models. Run it only when explicitly invoked; show proposed changes and obtain confirmation before any settings write.

1. Load `hermes-agent` and its configuration reference. Check the live CLI with `terminal(command="hermes config --help")` and `terminal(command="hermes config set --help")`. Resolve the active profile; do not inspect other profiles, auth files, or dump broad configuration.
2. Read only `skills.config.pstack.panel_size` and `skills.config.pstack.model_strategy` with targeted `terminal(command="hermes config get skills.config.pstack.panel_size")` and the equivalent strategy command. An unset key means defaults, not permission to modify anything.
3. Propose `panel_size: 3` and `model_strategy: inherit-parent` unless the caller requests a different positive panel size. The parent may batch panels within actual runtime concurrency. Same-model delegation is the default unless the user already configured a GLOBAL delegation model pin. Do not change that pin here.
4. Explain that reasoning effort is inherited and stays unchanged. There is no implemented per-role model map or role-specific reasoning knob. Do not translate budget labels into invented model slugs, use a Cursor model picker, write `.mdc` rules, or promise different-family panels. `auto` is not a pstack strategy value in this port.
5. `verified-external` is optional only when an already available external CLI workflow has been verified using its help, actual model availability, role/task prompts, scope/isolation, and real output. Otherwise keep `inherit-parent` and state that cross-model execution is unavailable. The strategy is a policy marker, not a built-in per-role router. No unsupported path or role config keys are supplied here.
6. Present both proposed settings, active profile, cost/fan-out impact, and unchanged reasoning/provider/delegation settings. Wait for explicit confirmation. If the session cannot clarify, return the proposal without writing.
7. After confirmation only, use `terminal(command="hermes config set skills.config.pstack.panel_size 3")` and `terminal(command="hermes config set skills.config.pstack.model_strategy inherit-parent")`, substituting only confirmed valid values. Read back these exact two keys. Check unrelated settings were not touched without dumping secrets. If a write fails, do not claim completion or automatically overwrite broader config.
8. Offer `pstack-create-verification-skill` once if the project has no real-app verification harness; only invoke it on approval. Do not install skills or change settings merely because this file was loaded.

## Pitfalls

Keep the user's scope and explicit checkpoints. Missing evidence or unavailable dependencies are gaps, not passes. Do not replace a working existing skill or change another profile.

## Verification

Show exact readback of the two approved keys and identify unchanged reasoning/provider/global delegation policy. If proposing only, report no settings changed.

## Attribution

Adapted from Lauren Tan's MIT-licensed pstack 0.15.6, source revision `23e4138daa01c42d4969f7a5465f82704e64f798`. See `references/license.md`.
