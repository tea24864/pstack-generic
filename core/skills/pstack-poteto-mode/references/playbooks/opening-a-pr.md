### Opening a PR

Invoke only when the task explicitly includes publication. Local-only and read-only work stop before this playbook.

**Worktree.** Use an exclusive worktree and branch at the resolved base for each concurrent writer. Child contexts share filesystem, not isolation. Never reset, patch out or discard unrelated dirty work. Preserve it and create a fresh scoped worktree; destructive resets require explicit authorization.

**Commits.** Commit liberally. Rebase into small, ordered commits before opening PRs. Each commit is a future PR: landable, ordered to tell the story. Amend when the fix belongs in a just-made commit. New commit when separable.

**PRs.** Load available `simplify-code` or `requesting-code-review` when applicable before commit, and pstack-no-comments before review. Write titles/descriptions/commit bodies under pstack-technical-writing then pstack-unslop. Keep the technical-writing layers except Diátaxis for these short briefings. No external deslop plugin is assumed.

**Titles.** Use Conventional Commits in the form `type(scope): subject`. Use `feat`, `fix`, `docs`, `refactor`, `test`, `chore`, or `perf` as the type. Use the changed area, such as `pstack` or `pstack-poteto-mode`, as the scope. Keep the subject short and imperative. Name a real symbol when one carries the change. For example, `fix(pstack): retarget opening-a-pr babysit trigger`. Do not add a trailing period.

**Descriptions.** The PR body is a briefing, not the lab notebook. A reviewer who has the diff should learn why the change exists, what it leaves out, what it could break, and how you proved it works, in under a minute. Write short, simple sentences with few identifiers. Do not write walls of text. The squash commit body is the PR body. If the body would make the squash commit longer than about 40 lines, cut the body.

Put each section under a `##` heading, not a bold lead-in, so the sections stand apart. Use these sections in order. Drop a section when it has nothing to say.

- `## Why` gives the problem and the approach in one to three short sentences. Do not list SHAs or rebase genealogy. Do not add a "based on main" preamble.
- `## What changed` has one to three short bullets. Name a real symbol or path only when it carries the change. Name both sides of a rename or retarget.
- `## Scope` always names what the PR covers and what it deliberately leaves out, for example a related follow-up or a known gap. Use one to three short items. Do not list symbols or paths, and do not write a file-by-file essay.
- `## Tradeoffs` names only rejected alternatives that a reviewer would otherwise ask about. Skip this section when there was no real choice.
- `## Blast Radius` gives one or two sentences on who or what the change touches and why that is safe or risky. If main is red, state the cost of leaving it red.
- `## Verification` has one to three bullets. Each bullet names a real run path and its outcome. For a performance change, report one primary number with its unit in `before → after` form. Link the arena or swarm directory for the remaining evidence. Do not include sample-size methodology, swarm recitals, or metric tables.

After these sections, attach videos or screenshots when they prove a claim. Do not paste full SHAs, swarm or arena lane recitals, lever-correction essays, file-by-file checklists, or "CLEAN" verdicts. Put these details in a linked artifact. A commit body does not restate its subject.

**Forge.** Verify installed `gh` and repository/auth context through read commands. Use it for this GitHub workflow; no Origin or Graphite requirement. Do not install missing tools or guess credentials. Publication is BLOCKED until a supported authorized path exists.

**PR tools.** Use a discovered supported PR tool only if its live schema and instructions cover the operation; otherwise verified `gh`. Never invent a built-in PR tool. Set fields explicitly and read back the exact target after create/edit/retarget/ready/post.

**Size and stacks.** Prefer narrow reviewable PRs. Root targets resolved trunk, each dependent child targets its parent branch at the exact parent tip. Branch from trunk only for independent work. Retarget/rebase only within explicit grant; with verified `gh` use `pr create --base <parent-branch>` or `pr edit <pr> --base <parent-branch>`, then read back exact base/head.

**Readiness.** This workflow prefers ready PRs when publication is authorized; respect a user-requested draft. With a supported API explicitly set draft false unless requested; with `gh` omit `--draft` for ready. Read back `state,isDraft,baseRefName,headRefOid,url` before claiming readiness. Mark ready only within grant, then read it back. Opening never grants merge authority.

**Babysit.** Opening a PR does not start a babysit. Post the URL and keep building. Finish the phase or stack first. Run a separate babysit pass only when the user asks for one after the whole stack exists. A babysit for each new PR stalls the build and spends checks on commits that later waves restart. Push back when feedback drifts from intent.

A leaf authorized to open a PR applies the review rubric itself and returns its diff/evidence/actual URL for separate parent review. The parent coordinates pstack-interrogate waves; the leaf cannot recurse. Opening does not start Babysit unless expressly assigned in an Autopilot lifecycle brief. No merge or auto-merge follows from opening.


**Permission boundary.** Publication, merges, configuration changes, installs, destructive cleanup and durable scheduling require explicit relevant scope. Missing evidence or capability is a gap, not a pass. Concurrent writers need exclusive ownership; the coordinator relays dependencies. Use bullets instead of Markdown tables where the delivery surface does not support tables.
