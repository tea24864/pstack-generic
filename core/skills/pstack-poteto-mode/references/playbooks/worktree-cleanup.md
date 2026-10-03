### Worktree and simulator cleanup

**Audit disk use and preserve user state.** Deletion requires an explicit approved set; neither a merged branch nor a helper suggestion grants it.

1. Snapshot disk use through `df -h .`. Run `bash <skill-dir>/scripts/worktree-audit.sh <repo>` with the resolved skill directory. The helper reads `git worktree list --porcelain -z`, preserves spaces in paths, and never fetches, scans transcripts, calls gh or deletes. It reports head, branch, dirty/ignored counts, tracked-remote relation, size and explicit activity/PR-state gaps. A stale tracking ref is not fresh PR truth.
2. Collect actual active/pinned sessions and process/worktree ownership from user-approved current project context. Verify exact PR state with authorized `gh` reads if available. Do not inspect unrelated profiles, private chats or globally inferred transcript directories. Recent mtime is not liveness. Every audit candidate remains review-required until activity and retained work are established.
3. For every proposed path, inspect tracked, untracked and ignored files, branch/remote commits, squash-merge evidence and active processes. Untracked/ignored files are not automatically disposable. A read-only leaf may inspect one authorized slice but returns evidence to the parent; it does not delete.
4. Present the exact deletion set and preservation plan. WIP, user-owned state, unresolved activity, unpushed commits and open PRs stay held. Obtain explicit approval before removal, even for clean merged worktrees. Do not treat a bucket as permission.
5. Remove only approved exact paths with ordinary `git worktree remove <path>` first. Force, recursive filesystem deletion, ref deletion and prune expansion need separately explicit scope. Read back worktree listing, retained refs/files and disk use. Do not infer reclaimed bytes from directory estimates alone.
6. Optional macOS-only simulator/cache cleanup is a separately gated step. Verify `xcrun` and live simulator ownership, show exact device/runtime/cache candidates, then delete only approved ids. Linux skips this branch. Never run delete-all, wipe app profiles or clear caches simply because they appear large.

**Reply:** before/after measured disk use, approved paths actually removed, evidence of preservation, each held item and why, and skipped platform-specific steps.
