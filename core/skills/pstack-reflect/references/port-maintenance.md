# Maintaining a third-party skill port

Use when reflecting on an imported skill suite or preparing an upstream update. This is a porting procedure, not permission to install, configure, or publish changes.

1. Pin the source repository revision and preserve its license. Inventory every original file, every entrypoint, and supporting playbooks/scripts. Keep machine-readable counts and hashes; source snapshot integrity is independent of whether the port behaves correctly.
2. Audit the actual host tool schemas and current official documentation. Similar tool names do not imply matching parameters. In particular, read-only prompts are not filesystem isolation, same-model workers are not cross-model diversity, and bounded delegates are not persistent jobs.
3. Classify each file as adapted, preserved, reference-only, or metadata-only. Give every upstream file an existing target or explicit exclusion reason. Move unsupported executables out of supported scripts; retain a fail-closed limitation instead of inventing an integration.
4. Namespace entrypoints and rewrite exact identifiers, links, templates, and nested references. Do not blindly replace ordinary words like 'how' or 'why'. Keep framework rules, prompts and large playbooks as on-demand references without reducing the workflow to an empty router.
{{runtime.configuration}}

5. Resolve optional policy preferences through actually supported configuration or targeted non-secret lookups. A preference is not proof of a per-role scheduler or external model runner. Defaults must work without mutating user configuration; generic fallback claims no runtime settings capability.
6. Use a staging package and independent ownership scopes. Preserve existing skill names, other profiles, and local edits. For concurrent workers, use disjoint target directories or separate worktrees. The parent owns aggregate coverage, installation, and verification.
7. Check all active files, not just SKILL.md, for unported runtime assumptions and accidental inline-shell syntax. A negated danger or an illustrative localhost URL can trigger a scanner advisory; inspect and document it rather than disabling scanning. A harmless code operator written next to backticks can resemble an auto-executable snippet, so rewrite the prose when ambiguous.
{{runtime.skill_loading}}

8. Exercise the actual frontmatter validator, security scanner, catalog loader, supporting-file loader, and invocation renderer where supported. Inspect the runtime's available dependency environment rather than assuming a system interpreter has optional packages. Report unsupported validation/loading surfaces as limits.
9. Test helper behavior and failure paths against disposable fixtures. Logs need append preservation, field escaping, concurrent-writer tests and symlink/header refusal. A read-only git audit should disable optional git locks and prove index metadata is unchanged, not merely that tracked file contents match.
{{runtime.setup}}

10. Before installation, refuse collisions and post-scan artifact changes. Record hashes of preexisting files and the live configuration. Copy only authorized new namespaced directories. Roll back only directories claimed exclusively by this install if a copy fails.
{{runtime.skill_maintenance}}

11. Read back exact installed targets through the supported loader and compare bytes with the scanned package. If correcting a newly installed port, update both the approved installed copy and its source package; rerun validation/hash comparisons. Do not silently update unrelated preexisting skills.
12. Run representative live workflows with isolated fixtures and explicit budgets. Review tool traces semantically: evidence-based investigation, a real design checkpoint, independent review with truthful model labels, and failing-before/passing-after bug-fix checks. Exit zero alone is not behavioral success. Report any blocked or unfinished integration honestly.
{{runtime.delegation}}

13. Budget the full delegation graph, including later judges and synthesis. Concurrent-child limits and one-shot total-child budgets are different constraints. Once exhaustion is verified, finish the authorized lenses inline and disclose the loss of independence; splitting or retrying cannot replenish a run-wide budget. Keep fixture artifacts compact enough to reach the user checkpoint.
14. Preserve failed and retried live attempts under distinct report names. A later serial-fallback pass does not turn a failed independent-panel run into a pass; report each exercised phase and its evidence separately.
15. Deliver the usage command, location, source revision, independent verification and limits. Keep port progress and raw transcripts in task artifacts, not global memory. Future upstream updates require a reviewed diff and backup; a collision-refusing fresh installer should not be turned into a blind overwrite mechanism.

## Setup-time specialization

- Keep one neutral authored core and reviewed runtime adapter facts. Generate native output deterministically; do not teach a permanent global mapping or freely rewrite the suite during installation. Pure principles need no runtime insertion points.
- Localize native instructions at the operation boundary. Preserve the full method, templates and approval gates without attaching an irrelevant execution manual to every skill.
- Audit scripts and their tests as well as Markdown. Structural checkers must validate workflow evidence, not require the name of one host's loading API. Prove the neutral fixture goes red before repairing that boundary.
- Test the setup CLI in isolated Python and paths with spaces: sibling imports must resolve from the explicitly trusted script directory, not an incidental working directory or environment path.
- Verify exact installed artifact sets and hashes inside the rollback scope. An injected extra file or post-copy mismatch must remove only exclusively owned targets and preserve unrelated skills/settings.
- Record selected runtime, actual observed version or an explicit unreported value, source/adapter hashes and capability limits. Supported adapter facts are not evidence that every facility is enabled in the active session.
- Test fresh generated instruction files separately from native catalog loading. A generic fallback exercised on one host proves that restricted workflow only, not support for every agent product or independent delegation. Keep incomplete attempts visible and verify the final checkpoint rather than relying on exit status.
