### Bug fix

**You own this task. Plan, review, verify.** Delegate investigation and the fix to subagents, stay in the lead.

Be scientific. Every shipped line traces to runtime evidence. Belt-and-suspenders that "might help" is a hypothesis, not a fix. It does not ship. When evidence refutes a hypothesis, revert what it motivated. The smallest change the evidence justifies ships, nothing more.

{{runtime.web}}

1. Reproduce it yourself on the matching surface via the verified browser, desktop, or shell surface driver, even when a debug or instrumentation protocol says to ask the user to reproduce. Ask the user only with a stated, specific reason the control surface cannot reach the target, and only after driving it as far as it goes. If it won't reproduce directly, synthesize the trigger, tighten conditions, or instrument until it fires.
2. Binary-search the cause. Form the candidate hypotheses, then rule them out until one survives. Seed them with `pstack-how` over the affected subsystem and the **pstack-why** skill for regression history. Each pass, take the split that cuts the most remaining problem space, get runtime evidence, eliminate. When program state is unclear, add instrumentation or logging and read it as the code runs. Don't guess. Drive a long or stubborn hunt with bounded current-session iterations with an explicit budget and stop predicate. Confirm the surviving *mechanism* with runtime evidence before the step-3 architect/interrogate fan-out.
3. Plan the fix. If it crosses a function boundary, `pstack-architect` first. Assign the specific implementation scope to a bounded leaf where supported; otherwise do it directly and disclose missing independent execution.

{{runtime.delegation}}
4. Verify on the same surface. The original repro now passes. "Inconclusive" or wrong-surface is not a pass. Flag it. Unit tests show branch behavior, not bug absence.
5. Stage the commits so the failing repro lands before the fix in git history. See the **pstack-tdd** skill for the failing-test-first cadence when the bug has a cheap local test path. Skip it when the test would be expensive, integration-heavy, or unclear.
   This is the canonical **pstack-principle-sequence-verifiable-units** principle skill, the failing test first and the fix on top.
6. Run **Opening a PR** only if publication is explicitly in scope; otherwise deliver the verified local artifact.

**Reply:** what was broken, root cause, fix, how you verified. Paste failing-then-passing repro output verbatim.


**Permission boundary.** Publication, merges, configuration changes, installs, destructive cleanup and durable scheduling require explicit relevant scope. Missing evidence or capability is a gap, not a pass. Concurrent writers need exclusive ownership; the coordinator relays dependencies. Use bullets instead of Markdown tables where the delivery surface does not support tables.
