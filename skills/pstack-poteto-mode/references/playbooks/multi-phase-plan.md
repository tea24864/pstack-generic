### Multi-phase or multi-PR plan

**You own the plan, not the code. The plan is a checklist an owner runs box by box and the operator audits from the evidence.** The plan is the deliverable. Do not implement.

1. When the change is one or two files with an obvious approach, skip the plan. Say so and stop.
2. Settle open questions by prototype before you write. Run `references/playbooks/prototype.md` for each. Keep the branch, the SHA, and the screenshots for Appendix A. Ask the operator only about a product or preference call that no run can settle. Give options (the **pstack-principle-never-block-on-the-human** principle skill).
3. Explore in subagents through the parent's native `delegate_task(tasks=[{"goal": "Explore a scoped subsystem", "context": "Exact paths, read-only instructions, required conventions/test commands, no delegation; return evidence pointers."}])` with inherited/global-pinned model (the **pstack-principle-guard-the-context-window** principle skill). Each returns file pointers, conventions, test commands, and entry points. No inlined dumps.
4. Copy the skeleton below into the plan file and fill every placeholder. Unless the operator names a path, write the file under a user-approved project `.hermes/pstack/docs/` directory. Keep every heading and every sub-block in the order shown. One section per PR. One PR is one change with its own evidence (the **pstack-principle-sequence-verifiable-units** principle skill). Name the execution playbook in **How to read this**. Pick between `references/playbooks/autopilot-full.md` and `references/playbooks/autopilot-stack.md` per the rule at the end of `references/playbooks/autopilot-stack.md`. A standing program takes `references/playbooks/orchestrate.md`.
5. Write under `pstack-technical-writing` in full, then `pstack-unslop`. The body is one Diátaxis mode, how-to. Appendices hold explanation and reference. Each heading states the task or the finding. No long dashes. No mid-sentence colons.
6. Run `terminal(command="node <skill-dir>/scripts/check-plan.mjs <plan.md>")` after resolving this skill directory and fix every line it prints (the **pstack-principle-encode-lessons-in-structure** principle skill).
7. Hand back. Post the plan path and the script's output, then stop. Execution starts on the operator's explicit go, under the execution playbook the plan names.

**Verification.** Tests alone are not sufficient verification. A PR is verified only when its unit, live, and perf boxes are all checked (the **pstack-principle-prove-it-works** principle skill). That sentence is the verification rule. Every verification block opens with it. The live block is mandatory. Ten independent lanes at the PR head drive the real surface through the verified driver under pstack-swarm, on the inherited/global-pinned model. These are coverage lanes, not ten diverse models. Each lane is one box with a concrete scenario, the screenshot it saves, and its pass predicate. One lane is the **Regression lane against trunk.** It runs the same load-bearing scenario on trunk and head. If trunk does not have the feature, the lane records that fact and gates the behavior the diff adds plus the end state the user waits for instead of inventing a trunk result. The perf gate is dual-sided. Trunk and head must both produce the named metric. If trunk lacks the feature, also isolate the work the diff adds and set an absolute budget for that work plus the end-to-end state the user waits for. Do not claim a ratio between unlike scenarios. The perf block names the metric, the interleaved probe, the trunk baseline measured first, and the rule with the number that fails. A PR that changes an interaction is review-gated. The operator reviews it in chat with screenshots and a video before merge. A PR that changes no interaction writes `**Review gate.** None. <PR id> is not review-gated.` and no boxes under it.

**Surface driver.** Browser/Electron/web uses the available browser tooling; native desktop/TUI uses computer-use when available; CLI uses terminal; native mobile needs a verified existing simulator driver. Name missing drivers as risks, never install or fake them. Two surfaces need scenarios on both.

````markdown
# <Program> plan

<Under ten lines. What changes, for whom, the rule the program enforces, and the PR ids in order.>

## How to read this

One box is one unit of work. Every box names the evidence that checks it. A nested box is a sub-step of the box above it. Check a box only when its evidence exists, a file, a log line, a screenshot, a test run, or a SHA. The body is a how-to. The appendices explain and record.

The program runs `references/playbooks/<execution playbook>.md` in pstack-poteto-mode. <Who merges, and which PR ids are the operator's items that stop at merge-ready.>

Tests alone are not sufficient verification. A PR is verified only when its unit, live, and perf boxes are all checked.

## Program checklist

### Arm the program

- [ ] State the protocol and this plan to the operator, then stop. Start execution only on the operator's explicit go.
- [ ] Read the approved installed/project skill versions at program start. Re-read them at every audit checkpoint. Never assume these skills live on the target repo trunk.
  - [ ] `skill_view` on pstack-poteto-mode with the chosen `references/playbooks/<execution playbook>.md`
  - [ ] `skill_view(name="pstack-swarm")`
  - [ ] the available surface-driver skill and its current instructions
  - [ ] `skill_view(name="pstack-poteto-mode", file_path="references/playbooks/opening-a-pr.md")`
  - [ ] `skill_view` on each other namespaced leaf skill the program uses
- [ ] On the operator's go, arm the audit tick as a separately authorized hourly cron/process audit, or bounded session audit checkpoints with the tick prompt below. Never leave the cadence to memory.
- [ ] Use this tick prompt, verbatim. "Re-read the approved execution playbook through skill_view. Audit the operation against it and fix drift in this tick. Inspect actual returned evidence and supported lifecycle state for each lane. A missing update alone does not prove death. Confirm a writer stopped before replacing it, or use a separate worktree and reject stale integration. Then post a short status message to the operator in chat only when the audit found a tracked change that no earlier status message reported, such as a PR opened, a code-ready head, a round launched or closed, a verdict, a merge, a stuck agent and the action taken, a blocker added or cleared, or a decision only the operator can make. Name every such change and nothing else. Do not repeat a table, the merged list, or an unchanged blocker. If the audit found none, end the turn with no reply text. Either way, log this tick's row in your decision trail. The row names the items reported, or none."
- [ ] On the operator's hold, launch nothing new, stop through supported controls, reconcile stopped bounded children and write a safe checkpoint. Do not pretend a child messaging control exists.

### Spawn owners

- [ ] Spawn one owner per PR with the full lifecycle the execution playbook names.
- [ ] Follow this dependency graph. Start dependent work only after its parent merges, or base it on the parent branch when the execution playbook stacks.
  - [ ] <PR id> and <PR id> are independent and first. Both branch from `main`.
  - [ ] <PR id> after <PR id>.
- [ ] Hold the file boundaries. <PR id or class> touches only `<glob>`.
- [ ] Hold the review gate. <PR ids> change an interaction. They wait for the operator's review in chat with screenshots and a video before merge.

### PR mechanics, for every PR

- [ ] Verify installed gh, repo and auth through read commands. No Origin or Graphite is required; no dependency installation is implied.
- [ ] Open a ready PR only under explicit publication grant per Opening a PR; respect a requested draft. With verified gh create using explicit repo/base/title/body file, then read back state, isDraft, base and head. Stack child targets parent.
- [ ] Run the repo's lint and typecheck once before the PR-facing push. Push with hooks on.
- [ ] Run the applicable available simplify-code/requesting-code-review workflow before each commit and `skill_view(name="pstack-no-comments")` before review.
- [ ] Triage every Bugbot and security-reviewer comment per `references/bugbot-triage.md`.
- [ ] Rebase onto current trunk before the code-ready report and babysit. Keep that merge base in fix rounds. Rebase again only at merge prep, on a `git merge-tree` conflict with trunk, or on a CI failure that comes from a change on trunk.

### Verdict and merge, for every PR

- [ ] At the code-ready head SHA and at each later push that changes the patch, run the swarm per `skill_view(name="pstack-swarm")`. One gates lane. The ten live lanes from the PR's **Verify, live** block. The perf lane from its **Verify, perf** block. Two or more audit lanes, each with its own focus, that read the diff and the receipts and distrust the PR body. The root audits the receipts in the merge-ready report before the verdict.
- [ ] Clean only when every lane is `PASS`. Findings go back to the owner, including a defect that a lane filed as a note. A new head gets a fresh swarm and a fresh verdict, except for results that stay valid under the patch-id rule in `references/playbooks/shipping.md`.
- [ ] <The merge or append rule from the execution playbook, with the patch-id rule from `references/playbooks/shipping.md`.>

### Boot recipe, for every live lane

Each live lane uses its own isolated worktree/environment at the exact PR head. Drive through the available browser/computer-use/terminal capability. Runtime/environment isolation is prepared by the parent, not a delegate parameter.

- [ ] `git fetch origin <head-branch> && git checkout <head SHA>`.
- [ ] <Start the backend and the surface. Wait for ready.>
- [ ] <Deliver input only through the verified surface driver's commands. Name the read-only diagnostics.>
- [ ] Save every screenshot to `$TMPDIR/swarm-<pr-id>/worker-<n>/<slug>.png` or the approved evidence directory and return the paths with the report.

## <Task as a verb phrase> (<PR id>)

**Depends on.** <PR id, or None.>

**Files.**

- [ ] Edit `<path>`.
- [ ] Create `<path>`.
- [ ] Delete `<path>`.

**Build.**

- [ ] <One change. Name the symbol and the file.>

**You see.**

- [ ] <One observable result, with the exact log line or screen state.>

**Verify, unit.** Tests alone are not sufficient verification. A PR is verified only when its unit, live, and perf boxes are all checked.

- [ ] <Test file and the case it gains.> Run `<command>`.

**Verify, live.** Tests alone are not sufficient verification. A PR is verified only when its unit, live, and perf boxes are all checked. Ten lanes on `inherit-parent` at the PR head, per the boot recipe.

- [ ] Lane 1. Regression lane against trunk. Run <the same load-bearing scenario> at trunk and head. If trunk lacks the feature, record that and gate <the behavior the diff adds plus the end state the user waits for>. Save `<slug>.png`. Pass when <predicate>.
- [ ] Lane 2. <Scenario.> Save `<slug>.png`. Pass when <predicate>.
- [ ] Lane 3. <Scenario.> Save `<slug>.png`. Pass when <predicate>.
- [ ] Lane 4. <Scenario.> Save `<slug>.png`. Pass when <predicate>.
- [ ] Lane 5. <Scenario.> Save `<slug>.png`. Pass when <predicate>.
- [ ] Lane 6. <Scenario.> Save `<slug>.png`. Pass when <predicate>.
- [ ] Lane 7. <Scenario.> Save `<slug>.png`. Pass when <predicate>.
- [ ] Lane 8. <Scenario.> Save `<slug>.png`. Pass when <predicate>.
- [ ] Lane 9. <Scenario.> Save `<slug>.png`. Pass when <predicate>.
- [ ] Lane 10. <Scenario.> Save `<slug>.png`. Pass when <predicate>.

**Verify, perf.** Tests alone are not sufficient verification. A PR is verified only when its unit, live, and perf boxes are all checked.

- [ ] Metric. <What is measured at both trunk and head. If trunk lacks the feature, also name the diff-added work and the end-to-end state the user waits for.>
- [ ] Probe. <The command or procedure, run at trunk and at the head, interleaved. Both sides must produce the metric.>
- [ ] Baseline. Record the trunk <value> first.
- [ ] Rule. <Head against trunk, with the number that fails. If the scenarios differ, add absolute budgets for the diff-added work and the user-visible end state instead of an invalid ratio.>

**Review gate.** The operator reviews before merge.

- [ ] Copy lane <n> screenshots into `<media path>/<pr-id>-review-<slug>.png`.
- [ ] Record a 30 to 60 second video of the change on an isolated lane environment. Save it as `<media path>/<pr-id>-review.mp4`.
- [ ] Post the screenshots and the video in chat. Stop at merge-ready. Wait for the operator's click.

**Merge.**

- [ ] Root's clean verdict at the exact head SHA.
- [ ] Bugbot triage done.
- [ ] Rebased onto current trunk after the verdict, patch-id unchanged.
- [ ] <The owner squash-merges its own PR, or the root appends it to the base-branch stack and the operator lands it bottom-up.>

## Close the program

- [ ] Every box above is checked with its evidence.
- [ ] Reply to the operator with the report the execution playbook names.

## Appendix A. Prototype evidence

<Each open question a prototype answered, with the branch, the SHA, and the artifact links. Each question that stays unproven.>

## Appendix B. Alternatives rejected

<Each approach weighed and why it lost.>

## Appendix C. Risks

<Each risk with the PR it lands in and what the owner watches.>

## Appendix D. Links and reading list

<Docs to read before editing. Which PRs get `skill_view(name="pstack-how")` and `skill_view(name="pstack-interrogate")`. The trail per `skill_view(name="pstack-show-me-your-work")`.>
````

**Reply:** the plan path, the PR ids with their dependencies and the review-gated set, what the prototypes proved and what stays unproven, and the check script's output.


**Hermes boundaries.** Read this skill's `references/hermes-runtime.md`. All child work is leaf-only, with a standalone brief and isolated writable paths; the parent flattens dependent waves. Default delegation is independent same-model work, not model diversity. Publication, merges, configuration, installs, destructive cleanup and durable scheduling require explicit relevant scope. A missing runtime capability is a gap. Use bullets instead of markdown tables on Discord.
