# Code Archaeology (git + in-repo)

## Hermes execution contract

Read the owning skill's `references/hermes-runtime.md` first. This reference is a procedure/prompt, not authority to change state. Use `read_file`, `search_files`, and `terminal` for local read-only evidence. Discover deferred tools with `hermes_tool_search`/`tool_describe` before `tool_call`; use only authenticated read operations actually present. Service names identify conditional evidence categories, not guaranteed tools. Missing access, unsupported searches, retention limits, and incomplete pagination are explicit gaps.

For delegation, the parent supplies this full prompt, repository/session scope, and all evidence needed in `delegate_task` goal/context tasks. Children cannot delegate or ask the user and must not write files or external state. They share the filesystem; read-only is a behavior contract, not enforced sandboxing. Return findings in the tool response. The parent owns subsequent waves; async results arrive after the parent yields, never through transcript polling. Role lenses inherit the parent model, so never claim model diversity from role labels.

## What this source contains

- Commit history (messages, dates, authors, diffs)
- PR descriptions, review comments, and discussion threads (via `gh`)
- Inline code comments, TODOs, FIXMEs, deprecation notes
- ADRs (architectural decision records) if the repo keeps them
- Tests. Names and assertions often encode the edge cases that motivated a change
- Related files modified in the same commits (co-change signal)
- CHANGELOG entries, release notes in the repo
- Issue/ticket IDs mentioned in commit messages and PR bodies

The most trustworthy source, tied directly to the code, and the most complete. Everything that went through the repo should be here.

## How to search it

Check the actual checkout, shallow history, git, and gh authentication. Missing history/auth is a gap. Expand the seed commit list via `terminal(command=..., workdir=<repo>)`; substitute observed values in the command templates below:

```bash
# Full history of the file through renames
git log --follow --oneline -- <file>

# Pickaxe: commits that added or removed this exact text
git log -S '<exact_string_from_code>' -- <file>

# Or for patterns:
git log -G '<regex>' -- <file>

# Who wrote each line and when
git blame -L <start>,<end> <file>

# The full diff of a specific commit
git show <hash>

# Commits between two points affecting this file
git log <old>..<new> -p -- <file>
```

For each substantive commit, pull the PR context:

```bash
# Find the PR number from the merge commit or branch
git log -1 --format=%B <hash>

# Full PR context: body, review comments, linked issues
gh pr view <number> --json title,body,author,createdAt,mergedAt,labels,closingIssuesReferences,comments,reviews,files

# The --json reviews and comments fields are where the real signal is
```

Look for out-of-band docs:

Use `search_files` for local text discovery, then `read_file` for each relevant full source:

- ADRs: content pattern `architecture.decision`, file glob `*.md`.
- Nearby notes: pattern `(TODO|FIXME|HACK|XXX|NOTE)` scoped to the target file with context.
- Related tests: the target symbol as a content pattern and `*test*` file glob.

## What good evidence looks like here

- A PR description that explains the problem being solved, not just the change ("This fixes the pagination bug that caused X")
- A long review thread where alternatives were debated
- An inline comment near the target line that explains a non-obvious constraint
- A test named `test_handles_edge_case_when_X` that reveals an edge case motivating the code
- A commit message that references a ticket or incident ID
- A CHANGELOG entry that summarizes the user-visible rationale

## Common pitfalls

- **Squash-merge flatlands.** If the repo squashes PRs, individual commits in the branch history are lost. Fall back to PR body and comments.
- **Misleading commit messages.** "Small refactor" sometimes hides an intentional behavior change. Look at the diff, not the message.
- **Cargo-culted patterns.** The author may have copied a pattern without understanding why. Check if the pattern originated earlier in the codebase and investigate *that* commit.
- **Bot commits and auto-merges.** Dependabot, Renovate, and automated backports usually don't carry motivation. Skip them when trying to find intent.
- **Treating code as evidence of intent.** The code itself isn't evidence for why it exists. Evidence comes from commit messages, PRs, comments, tests, docs. Don't cite "the function is named X" as evidence of intent.

## What to return

Every commit/PR/comment that bears on the question, with:
- The exact text (quoted)
- The hash / PR number / file:line
- Author and date
- Whether it's direct (explicitly addresses the question) or circumstantial
