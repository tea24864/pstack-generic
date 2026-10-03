# Skill format and authoring scope

## Decide the target before writing

{{runtime.skill_loading}}

- Load the existing target and confirm its exact name, source path, category, active user/project scope, and intended changes. Prefer an approved edit over a duplicate skill. Preserve `pstack-*` names and references; do not overwrite another installed skill or user scope.
- Confirm whether the approved destination is user-local or project-local. A default creation destination is not proof of project scope. Inspect the resolved path before writing. Never change creation configuration merely to make a task easier.
- Use the established project skills convention or an explicitly confirmed destination. Read existing files before replacement. Project scope is not global permanent behavior.
- Confirm discovery and trust requirements from actual runtime evidence. Do not grant trust implicitly or promise immediate current-session registration.
- Choose a collision-safe new name such as `pstack-verify-<app>` or `pstack-<handle>-mode`, unless the user intentionally chooses otherwise. Preserve existing user-owned names when updating.
- An on-demand mode is not an always-on system prompt. Do not edit persistent memory, prompts, autoload, or configuration as a side effect. Publication, pushes, PRs, merges, and tracker writes need separate authorization.

{{runtime.skill_maintenance}}

## Draft, exercise, iterate

1. Use standard Agent Skills YAML frontmatter starting at byte zero: required `name` and one quoted `description` scalar. For this workflow, keep description at most 57 characters ending with a period. Include `license` where appropriate and optional scalar `compatibility` for audited execution constraints. Put credited author, version, and provenance in `metadata` with scalar string values. Do not copy unsupported runtime-specific configuration or nested platform/related-skill objects. Reference actual related skills in the body.
2. Include When to Use, Prerequisites, Procedure, Pitfalls, and Verification. Keep the main document under roughly 200 lines; move bulky branch-specific detail to references, scripts, templates, or assets and link it explicitly.
3. Write lessons, not session logs. Each rule changes future behavior and briefly explains the pitfall's mechanism. Reference other skills by exact name instead of inlining their contents. Do not invent connectors, CLI flags, credentials, or model settings.
4. Validate YAML structure, scalar metadata, description length, required sections, local links, and referenced-skill existence. Use an available validator or real structural check and report which checks ran. Availability is not permission to claim an unexecuted check passed.
5. Exercise workflow commands against the real authorized artifact. For an app-verification skill, run launch, doctor, an actual mapped user feature, evidence capture, and cleanup; verify saved evidence survives teardown. A helper needs a documented invocation and executable mode where applicable. An untested procedure remains a draft.
6. For subjective mode preferences, show the draft and take feedback rather than inventing an objective benchmark. For trigger tuning, inspect positive/counter-trigger examples; avoid broad unrelated activation.
7. Apply only approved edits in the confirmed directory. A staged write is not a saved write; preserve any approval mechanism's status. Report the exact destination, what was exercised, and remaining limitations; never install or trust implicitly.

Check actual runtime scope and documentation when behavior differs. Missing capabilities or trust are explicit blockers, not reasons to write into a different user scope.
