#!/usr/bin/env python3
"""Offline stdlib regression checks for supported runtime-neutral helpers."""
import importlib.util
import json
import os
from pathlib import Path
import shutil
import subprocess
import tempfile
import unittest

SCRIPTS = Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location("worktree_audit", SCRIPTS / "worktree-audit.py")
AUDIT = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(AUDIT)
RULE = "Tests alone are not sufficient verification. A PR is verified only when its unit, live, and perf boxes are all checked."


def invoke(*args, cwd=None):
    return subprocess.run(list(map(str, args)), cwd=cwd, capture_output=True, text=True)


def command(*args, cwd=None):
    result = invoke(*args, cwd=cwd)
    if result.returncode:
        raise AssertionError(result.stderr or result.stdout)
    return result.stdout


def plan():
    lanes = "\n".join(f"- [ ] Lane {n}. Exercise scenario {n}. Save `lane-{n}.png`. Pass when state persists." for n in range(1, 11))
    return f'''# Example program plan

Build a verified feature for library consumers.

## How to read this

One box is one unit of work. Every box names the evidence. Check a box only when its evidence exists.
Run `references/playbooks/autopilot-stack.md`. The operator lands the stack.
{RULE}

## Program checklist

### Arm the program

- [ ] Read the execution playbook with native file access. Use bounded audit checkpoints and report each changed status message.

### Spawn owners

- [ ] Assign one leaf with a separate worktree.

### PR mechanics

- [ ] Publish only under explicit grant and read back the PR.

### Verdict and merge

- [ ] Root checks every receipt at the exact head SHA.

### Boot recipe

- [ ] Exercise the installed CLI in an isolated fixture.

## Build the fixture (PR1)

**Depends on.** None.

**Files.**

- [ ] Edit `module.py`.

**Build.**

- [ ] Add the typed domain boundary.

**You see.**

- [ ] The command prints the expected state.

**Verify, unit.** {RULE}

- [ ] Run `python -m unittest` and save output.

**Verify, live.** {RULE} Ten lanes on `inherit-parent` at the PR head.

{lanes}

**Verify, perf.** {RULE}

- [ ] Metric. Elapsed runtime in seconds.
- [ ] Probe. Run baseline and head interleaved.
- [ ] Baseline. Record trunk before changes.
- [ ] Rule. Fail above the agreed absolute budget.

**Review gate.** None. PR1 is not review-gated.

**Merge.**

- [ ] Operator lands only after independent proof.

## Close the program

- [ ] Check all receipts and report gaps.

## Appendix A. Prototype evidence

The fixture established the behavior contract.
'''


class HelperTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="pstack-helper-test-", dir=os.environ.get("TMPDIR"))
        self.directory = Path(self.temp.name)

    def tearDown(self):
        self.temp.cleanup()

    def check_plan(self, text):
        file = self.directory / "plan.md"
        file.write_text(text)
        return invoke("node", SCRIPTS / "check-plan.mjs", file)

    def make_repo(self):
        repo = self.directory / "repo with spaces"
        repo.mkdir()
        command("git", "init", "-q", "-b", "main", repo)
        command("git", "-C", repo, "config", "user.name", "Helper Fixture")
        command("git", "-C", repo, "config", "user.email", "fixture@example.invalid")
        (repo / "tracked.txt").write_text("original\n")
        (repo / ".gitignore").write_text("ignored.txt\n")
        command("git", "-C", repo, "add", "tracked.txt", ".gitignore")
        command("git", "-C", repo, "commit", "-qm", "fixture")
        worktree = self.directory / "worker path with spaces"
        command("git", "-C", repo, "worktree", "add", "-q", "-b", "worker", worktree)
        return repo, worktree

    def test_valid_native_plan(self):
        result = self.check_plan(plan())
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("1 PR sections, 0 problems", result.stdout)

    def test_plan_rejects_missing_lane(self):
        text = "\n".join(line for line in plan().splitlines() if not line.startswith("- [ ] Lane 10."))
        result = self.check_plan(text)
        self.assertEqual(result.returncode, 1)
        self.assertIn("expected 1 to 10", result.stderr)

    def test_plan_rejects_missing_proof(self):
        result = self.check_plan(plan().replace("Save `lane-3.png`.", "No artifact."))
        self.assertEqual(result.returncode, 1)
        self.assertIn("names no screenshot", result.stderr)

    def test_neutral_playbook_loading_is_accepted(self):
        result = self.check_plan(plan().replace('with native file access', 'using the host skill loader'))
        self.assertEqual(result.returncode, 0, result.stderr)

    def test_plan_rejects_legacy_cadence(self):
        result = self.check_plan(plan().replace("Use bounded audit checkpoints", "Use an implicit cadence"))
        self.assertEqual(result.returncode, 1)
        self.assertIn('lacks "audit"', result.stderr)

    def test_plan_usage(self):
        result = invoke("node", SCRIPTS / "check-plan.mjs")
        self.assertEqual(result.returncode, 2)
        self.assertIn("Usage:", result.stderr)

    def test_records_preserve_whitespace(self):
        rows = AUDIT.records("worktree /a space/name\0HEAD aaaa\0branch refs/heads/main\0\0worktree /b\0locked held\0\0")
        self.assertEqual(rows, [{"worktree": "/a space/name", "HEAD": "aaaa", "branch": "refs/heads/main"}, {"worktree": "/b", "locked": "held"}])

    def test_audit_real_worktree_dirty_ignored_and_no_writes(self):
        repo, worktree = self.make_repo()
        (worktree / "tracked.txt").write_text("changed\n")
        (worktree / "untracked file.txt").write_text("keep\n")
        (worktree / "ignored.txt").write_text("retain\n")
        before = command("git", "-C", worktree, "status", "--porcelain=v1", "--ignored")
        result = invoke("bash", SCRIPTS / "worktree-audit.sh", repo)
        self.assertEqual(result.returncode, 0, result.stderr)
        payload = json.loads(result.stdout)
        self.assertEqual(payload["count"], 2)
        self.assertTrue(payload["offline"])
        row = next(row for row in payload["worktrees"] if row["path"] == str(worktree))
        self.assertEqual(row["status_counts"], {"tracked": 1, "untracked": 1, "ignored": 1})
        self.assertEqual(row["bucket"], "hold-dirty")
        self.assertFalse(row["deletion_authorized"])
        self.assertIsNone(row["upstream"])
        self.assertIn("UNKNOWN", row["activity"])
        self.assertEqual(command("git", "-C", worktree, "status", "--porcelain=v1", "--ignored"), before)
        self.assertTrue((worktree / "untracked file.txt").exists())
        self.assertTrue((worktree / "ignored.txt").exists())

    def test_audit_clean_and_rename_records(self):
        repo, worktree = self.make_repo()
        rows = AUDIT.inventory(repo)
        clean = next(row for row in rows if row["path"] == str(worktree))
        self.assertEqual(clean["bucket"], "review-required")
        self.assertFalse(clean["deletion_authorized"])
        command("git", "-C", worktree, "mv", "tracked.txt", "renamed file.txt")
        renamed = next(row for row in AUDIT.inventory(repo) if row["path"] == str(worktree))
        self.assertEqual(renamed["status_counts"], {"tracked": 1, "untracked": 0, "ignored": 0})

    def test_audit_invalid_repository(self):
        result = invoke("bash", SCRIPTS / "worktree-audit.sh", self.directory)
        self.assertEqual(result.returncode, 1)
        self.assertIn("not a git repository", result.stderr)


if __name__ == "__main__":
    if not shutil.which("git") or not shutil.which("node"):
        raise SystemExit("Tests require pre-existing git and Node; no installation is attempted.")
    unittest.main(verbosity=2)
