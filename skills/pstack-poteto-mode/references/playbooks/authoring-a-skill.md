### Authoring or modifying a skill

**You own the skill's voice.**

1. Use the available `hermes-agent-skill-authoring` workflow for repository files; use `skill_manage` only for authorized active-profile personal skills.
2. Validate the skill: frontmatter has `name` and `description`, referenced files exist, cross-skill links resolve.
3. Test cases if structural. Skip if subjective.
4. Run **Opening a PR** only if publication is explicitly in scope; otherwise deliver the verified local artifact.

When in doubt, delete. Keep only prose that changes a decision. Tell it to do the thing and skip the reason. Explain only when the rule is confusing without one. Match tone to scope. Point at structural sources (types, READMEs, config) per the **pstack-principle-encode-lessons-in-structure** principle skill. Delegate to other skills by path. Don't restate. A workflow you keep hitting but isn't captured → propose a new skill.

**Reply:** summary of the skill, key design decisions, validation notes.


**Hermes boundaries.** Read this skill's `references/hermes-runtime.md`. All child work is leaf-only, with a standalone brief and isolated writable paths; the parent flattens dependent waves. Default delegation is independent same-model work, not model diversity. Publication, merges, configuration, installs, destructive cleanup and durable scheduling require explicit relevant scope. A missing runtime capability is a gap. Use bullets instead of markdown tables on Discord.
