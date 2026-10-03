# Native skill authoring and scope

## Decide the target before writing

- Load the existing target with `skill_view` and confirm its exact name, source path, category, active profile, and intended changes. Prefer an approved edit over a new duplicate skill. Preserve `pstack-*` names and references; do not overwrite another installed skill or another profile.
- For profile-local skills, use `skill_manage` create/patch/supporting-file actions. New creation goes to the active profile or configured `skills.create_dir`, not automatically to the current repo. Inspect the resolved destination before applying. Never change creation config merely to make a task easier.
- For approved repo artifacts, use `.hermes/skills/<name>/` or the existing `.agents/skills/<name>/` convention. Trusted existing project skills can be edited through `skill_manage` where supported. New repo skills use `write_file`/`patch` because `skill_manage` create otherwise writes to the profile/configured creation directory. Read an existing file before replacing it. Project scope is explicit and not global permanent behavior.
- Hermes discovers project skills only inside the relevant git project and after user-approved project trust. Explain `hermes skills trust`; do not run it or alter `skills.trusted_project_dirs` without explicit approval. Non-interactive sessions inherit trust and cannot grant it. Do not promise immediate current-session registration.
- Project names override same-named profile skills when active, so choose a collision-safe project name, such as `pstack-verify-<app>` or `pstack-<handle>-mode` for new pstack-generated skills, unless the user intentionally chooses another name. Preserve existing user-owned names when updating.
- An on-demand mode is not an always-on system prompt. Do not edit persistent memory, profile prompts, autoload, or configuration as a side effect of authoring. Publication, pushes, PRs, merges, and tracker writes require separate authorization.

## Draft, exercise, iterate

1. Write YAML frontmatter starting at byte zero: name, one quoted description scalar of at most 57 characters ending with a period, version, credited author, MIT license where appropriate, audited platforms, and actual resolvable related skills. Do not copy unsupported Cursor frontmatter.
2. Include When to Use, Prerequisites, Procedure, Pitfalls, and Verification. Keep the main document under roughly 200 lines; move bulky branch-specific detail to references, scripts, templates, or assets and link it explicitly.
3. Write lessons, not session logs. Each rule changes future behavior and explains the pitfall's mechanism briefly. Reference other skills by their exact names instead of inlining their contents. Do not invent connectors, CLI flags, credentials, or model settings.
4. Validate YAML structure, description length, required sections, local links, and related-skill existence. Use an available validator or a real Python structural check via `terminal`; report which checks ran. Validator availability is not permission to claim an unexecuted check passed.
5. Exercise workflow commands against the real authorized artifact. For an app-verification skill, run launch, doctor, an actual mapped user feature, evidence capture, and cleanup; verify saved evidence survives teardown. A helper needs a documented invocation and executable mode where applicable. An untested procedure remains a draft.
6. For subjective mode preferences, show the draft to the user and take feedback rather than inventing an objective benchmark. For trigger tuning, inspect positive/counter-trigger examples; avoid broad unrelated activation.
7. Apply only approved edits using `skill_manage` for registered skills. A staged write is not a saved write; preserve the approval tool's status. For a repo artifact, use file tools in the confirmed directory. Report the exact destination, what was exercised, and remaining limitations; never install or trust implicitly.

## Official references

- Skills and project trust: https://hermes-agent.nousresearch.com/docs/user-guide/features/skills
- Authoring: https://hermes-agent.nousresearch.com/docs/developer-guide/creating-skills

Check the live tool schema/documentation if runtime scope behavior differs. Missing tools or trust are explicit blockers, not reasons to write into a different profile.
