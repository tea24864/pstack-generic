---
name: pstack-create-verification-skill
description: "Create a proven project-local app verification skill."
version: 0.1.0
author: "Lauren Tan (poteto), tea24864, Hermes Agent"
license: MIT
platforms: ["linux", "macos"]
metadata:
  hermes:
    tags: [pstack, engineering, workflow]
    related_skills: ["pstack-maintain-verification-skill"]
---

# Create a verification skill

## When to Use

Use when a repo lacks a reproducible way to launch, drive, and prove real user-visible behavior. Requires explicit project artifact/verification scope, not installation permission.

## Prerequisites

Read `references/hermes-runtime.md` with `skill_view` before executing this workflow. Use only tools and credentials actually available in this session. Invoking this skill does not authorize publication, merges, destructive cleanup, or configuration changes.

## Procedure

Every serious project needs a scripted way to drive the real app and prove behavior: launch it, exercise a feature the way a user would, and capture evidence. This skill generates that as a project-local skill (`.hermes/skills/pstack-verify-<app>/`) tailored to the repo. You write the generator's output for the next agent, not for a human: it will be read cold, mid-task, by an agent that has never seen the app.

Read `references/skill-authoring.md` before writing. New repo artifacts use `write_file` within the approved project scope; `skill_manage` create is profile/configured-directory scoped, not automatically project-local. Existing trusted project skills can be patched in place with `skill_manage`. Do not change trust/configuration or permanent prompt/memory implicitly.

## 1. Interview the repo, not the user

Use `search_files` and `read_file` to inspect README/manifests/harnesses, then `terminal` for actual build/readiness checks. Answer these from the codebase and only ask the user what you cannot observe:

- **Surface:** what does a user actually touch? A web UI, a CLI/TUI, a desktop app, an API, a mobile app, a library? A repo can have several; pick the primary one and note the rest.
- **Run:** how does the app start locally? Prefer the repo's own documented dev command (package scripts, Makefile, README quickstart). Note ports, env vars, seed data, auth.
- **Drive:** how can an agent interact with it programmatically? Existing harnesses first — Playwright/Cypress specs, expect scripts, PTY helpers, curl-able endpoints, a debug port. Only then pick a generic recipe: `browser_exec` with DOM/CDP for web and Electron, the loaded `computer-use` skill where desktop interaction is needed, a verified tmux/PTY harness through `terminal` for CLI/TUI, plain HTTP through `terminal` for services.
- **Observe:** what evidence can be captured? Screenshots, terminal transcripts, response bodies, logs, exit codes, DB state.
- **Isolate:** can two instances run side by side (ports, data dirs, profiles)? If not, say so in the generated skill: refusing to double-drive a shared instance beats corrupting the user's session.

If the checkout doesn't build or start as-is, fix that first only within approved product-edit scope (or report it precisely and keep the generated artifact a draft) before generating; a skill written against a broken base teaches wrong steps. When an irrelevant missing asset blocks startup (a static dir the API never serves, a sample config), the generated skill may create it only within an authorized disposable verification scope, clearly marked as verification scaffolding, and remove it in cleanup.

## 2. Generate the skill

Write `.hermes/skills/pstack-verify-<app>/SKILL.md` with YAML frontmatter (`name: pstack-verify-<app>` and a `description` at most 57 characters ending with a period that names the app/surface trigger — without frontmatter the skill never registers) and these sections, each grounded in what the interview actually found (no placeholders left):

- **Launch:** the exact command that starts the app for verification, and how to tell it's ready (a log line, a port answering, a prompt). Include teardown. For a short-lived CLI or TUI there is no server to keep alive: launch means build the binary (or install deps) once, then start each drive in its own isolated PTY or tmux session.
- **Doctor:** one read-only check that answers "is this instance worth driving?" — process up, right version/build, port owned by us, auth valid. An agent runs this first whenever anything looks off.
- **Drive:** the harness recipe with real selectors/commands from this repo, not examples. Prefer stable handles (ARIA labels, data attributes, prompt strings, route paths) over coordinates and tab order.
- **Evidence:** what to capture for a proof and where it goes. State the proof standards: exercise the real user path, not internal setters or test-only endpoints; capture the action and the resulting state, not just the final screen; verify side effects (files written, rows inserted, messages sent) alongside what's visible; mocks only where a production boundary already isolates the external system. When the safe path is a dry-run or test mode, verify what it actually skips by observing (files, network, git refs) rather than trusting its name: some dry-runs still touch the network or open a browser.
- **Cleanup:** how to tear down instances the run created. Never kill by process name; kill what you started. Cleanup removes instances and scratch state, never the evidence: proof artifacts survive the teardown, in a location the skill names.
- **Hermes contract:** include When to Use, Prerequisites (exact dependencies and safe scope), Procedure, Pitfalls, Verification, author/license/version/platforms. Project skills need user-approved trust via `hermes skills trust`; do not auto-trust or promise current-session registration.
- **Helpers:** any script the skill ships is executable and its invocation is shown in the skill body. A helper the reader has to reverse-engineer is not a helper.

## 3. Seed the feature map

Create `.hermes/skills/pstack-verify-<app>/references/features/README.md` plus one reference file per user-facing feature you can identify (aim for the top 3-5 to start, from routes, commands, menus, or docs). Follow the shape in [`references/feature-map-example/`](references/feature-map-example/), with a README index and one file per feature. Each file answers, from the user's point of view: what the feature is, how to reach it, how to drive it with the harness, and what observable end state proves it works. The four H2s are `Sub-features`, `How to get to it (user POV)`, `Driving it with <harness>`, and `Gotchas`. The map is the repo's maintained verification source; a proof that drives one convenient entry point is incomplete when the map lists others.

## 4. Prove the generated skill before handing it over

Run its own instructions end to end once: launch, doctor, drive ONE mapped feature via a real user entry point (one is enough; the map exists so later runs can cover the rest), capture evidence, clean up. After cleanup, confirm the evidence still exists at the named location — a cleanup that eats the proof fails this step. Fix what fails, and run the generated cleanup after every failed iteration too, so broken attempts don't strand processes and ports. A generated skill that was never executed is a draft, not a deliverable.

## 5. Offer the maintenance loop

Point the user at `/pstack-maintain-verification-skill` for keeping the map honest as the app changes. Suggest a cadence only if they ask.


## Pitfalls

Never generate a claimed working skill against an unstarted app. Doctor failures, unowned processes, dry-run side effects, test-only setters, missing helper invocation, and cleanup that deletes proof invalidate delivery. Example harness commands are illustrative, not installed tools.

## Verification

Execute generated launch → doctor → one mapped real feature → evidence → cleanup, including cleanup after failures. Confirm evidence survives, helpers run as documented, no owned processes remain, and scope/trust requirements are explicit. Unexecuted output stays draft.

## Attribution

Adapted from Lauren Tan's MIT-licensed pstack 0.15.6, source revision `23e4138daa01c42d4969f7a5465f82704e64f798`. See `references/license.md`.
