#!/usr/bin/env python3
"""Read-only, offline worktree inventory. No activity/merge inference."""
import argparse
import json
import os
from pathlib import Path
import subprocess


def git(repo, *args, allow_failure=False):
    result = subprocess.run(["git", "--no-optional-locks", "-C", str(repo), *args], capture_output=True)
    if result.returncode and not allow_failure:
        raise RuntimeError(result.stderr.decode(errors="replace").strip())
    return result.stdout.decode(errors="surrogateescape") if not result.returncode else None


def records(raw):
    rows, row = [], {}
    for item in raw.split("\0"):
        if not item:
            if row:
                rows.append(row)
                row = {}
            continue
        key, _, value = item.partition(" ")
        row[key] = value
    if row:
        rows.append(row)
    return rows


def size(path):
    total, failures = 0, 0
    def onerror(error):
        nonlocal failures
        failures += 1
    for base, dirs, files in os.walk(path, followlinks=False, onerror=onerror):
        for name in files:
            try:
                total += os.lstat(Path(base) / name).st_size
            except OSError:
                failures += 1
    return total, failures


def inventory(repo):
    rows = records(git(repo, "worktree", "list", "--porcelain", "-z"))
    result = []
    for index, row in enumerate(rows):
        path = Path(row["worktree"])
        changes = git(path, "status", "--porcelain=v1", "-z", "--untracked-files=all", "--ignored", allow_failure=True)
        status = None
        if changes is not None:
            status = {"tracked": 0, "untracked": 0, "ignored": 0}
            tokens = iter(changes.split("\0"))
            for token in tokens:
                if not token:
                    continue
                flag = token[:2]
                status["untracked" if flag == "??" else "ignored" if flag == "!!" else "tracked"] += 1
                if "R" in flag or "C" in flag:
                    next(tokens, None)
        upstream = git(path, "rev-parse", "--symbolic-full-name", "@{upstream}", allow_failure=True)
        divergence = git(path, "rev-list", "--left-right", "--count", "HEAD...@{upstream}", allow_failure=True) if upstream else None
        bytes_, errors = size(path)
        result.append({"path": str(path), "primary": index == 0, "head": row.get("HEAD"), "branch": row.get("branch"), "locked": "locked" in row, "prunable": "prunable" in row, "status_counts": status, "upstream": upstream.strip() if upstream else None, "ahead_behind_tracking_ref": divergence.strip() if divergence else None, "size_bytes": bytes_, "size_errors": errors, "activity": "UNKNOWN: verify active sessions/processes explicitly", "pr_state": "UNKNOWN: no network query", "bucket": "hold-primary" if index == 0 else "hold-dirty" if status is None or any(status.values()) else "review-required", "deletion_authorized": False})
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("repo", nargs="?", default=".")
    args = parser.parse_args()
    try:
        rows = inventory(Path(args.repo).resolve())
    except (RuntimeError, OSError) as error:
        parser.exit(1, str(error) + "\n")
    print(json.dumps({"worktrees": rows, "count": len(rows), "offline": True, "deletion_authorized": False}, ensure_ascii=True, indent=2))


if __name__ == "__main__":
    main()
