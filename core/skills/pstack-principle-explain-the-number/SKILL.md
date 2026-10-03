---
name: pstack-principle-explain-the-number
description: "Validate what measured numbers actually demonstrate."
license: MIT
metadata:
  author: "Lauren Tan (poteto), tea24864"
  version: "0.2.0"
  source-revision: "23e4138daa01c42d4969f7a5465f82704e64f798"
---

# Explain the Number

## When to Use

Use before trusting, reporting, or acting on a measurement.

## Procedure

A measured number is a claim about a system. Before you trust it, report it, or act on it, find what limits it and rule out that it measured something else.

**Why:** A run that went wrong still prints a plausible number. Requests that failed, a cache that skipped the work, code that never ran, a side left on default settings, and run-to-run noise all produce results that look fine. If you cannot say why the number is not twice as good, you do not know what you measured.

**Pattern:**

- **Ask "why not double?"** Name the resource or code path that bounds the result, such as a core, a lock, the disk, the network, or the load generator itself. Get it from a profile or from system counters taken during a run, then map it to source. A guess from reading the code is not a limiter.
- **List what else the number could be measuring, and rule out each one with evidence.** The usual suspects are errors, skipped or cached work, an untuned side, noise, and a piece too small to matter end to end.
- **Keep the evidence with the number.** Put the run count, the spread, and the limiter in the notes or a linked artifact, so a reader can check the claim.

For a performance number, run the full procedure with the [benchmark-checklist](../pstack-benchmark-checklist/SKILL.md) skill. For an eval result, ask the same of the trials: did every run do the task, does the gap hold across trials and models, and does the scenario matter.

You skipped this when the evidence behind a number has no run count, no spread, or no named limiter, or when the time saved is larger than the time the changed piece took.

Distinct from [Prove It Works](../pstack-principle-prove-it-works/SKILL.md), which checks that an output is real. This checks that a measured number means what you say it means.

## Pitfalls

A plausible number or code-reading guess does not establish what ran or what limits it.

Stay within the user's task scope and available capabilities. This principle does not authorize publication, merges, destructive cleanup, or configuration changes; preserve approval gates and compatibility commitments.

## Verification

Report actual run count, spread, and an observed limiter mapped to source. Attach evidence excluding errors, cached/skipped work, unequal settings, and noise. Confirm claimed end-to-end savings cannot exceed the changed component's cost. State the decision changed, retain actual evidence, and disclose remaining uncertainty.

## Attribution

Adapted from Lauren Tan's MIT-licensed pstack 0.15.6, source revision `23e4138daa01c42d4969f7a5465f82704e64f798`. Port contributions: tea24864. See [MIT license](references/license.md).
