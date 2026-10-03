### Eval

**You own the experiment design. Plan, blind, run, synthesize.**

**Non-negotiables for blinding:**

- No `eval`, `test`, `judge`, `experiment`, `rubric`, `score`, `compare`, `benchmark`, `candidate`, `arena`, or `pstack-arena` in any directory, file, or prompt the candidate sees.
- The candidate prompt looks like an organic user request. State the goal, not the meta.
- No chain-eliciting cues. Don't ask the candidate to list which skills, principles, or files they applied. Ask for design notes generally and grade chain-following from code shape, not self-report.
- Sanitize directory and slug names. Use project-shaped names a user might pick.
- Don't tell the candidate other candidates exist.
- The judge can know it's judging but sees outputs by sanitized label only, never by model name.
- Comparing two variants: one judge scores both sets in a single pass on one scale, blind to which set each came from.

**Steps:**

1. **Frame.** State what variant is under test and what behavior counts as success. Write the rubric (3-6 concrete criteria) for the judge only. Hold it back from candidates.
2. **Set up sanitized environments.** Per-candidate working dir with the variant in place. Plant any context an organic task would have: a project skeleton, the skills the candidate would naturally read.
3. **Author one organic prompt.** What a user would type. No leakage of what's being measured.
4. **Spawn N parallel candidates** in independent contexts under the **pstack-arena** skill's Phase B. Each works in its own sanitized dir. Same prompt to each.
5. **Spawn one blinded judge** with a disclosed same-model limitation under the **pstack-arena** skill's Phase C. Judge sees outputs by sanitized label and the rubric, never a model name.
6. **Verify the chain from actual artifacts and available authorized execution receipts, not self-report.** Do not poll child transcripts. Completed trace evidence is usable only when the runtime exposes it and access is explicitly scoped to this evaluation. Inspect actual opened-file/tool receipts when available; otherwise mark chain-following unobservable and grade the artifact shape only. Never search unrelated sessions or infer tool use from a child's claims.
7. **Read every candidate output yourself** end to end. Compare to the judge's verdict. Disagreement means a model is biased or the rubric is ambiguous. Synthesize.

**Reply:** variant under test, rubric, per-candidate notes, judge's verdict, your synthesis, and a recommendation for whether to promote the variant.


**Hermes boundaries.** Read this skill's `references/hermes-runtime.md`. All child work is leaf-only, with a standalone brief and isolated writable paths; the parent flattens dependent waves. Default delegation is independent same-model work, not model diversity. Publication, merges, configuration, installs, destructive cleanup and durable scheduling require explicit relevant scope. A missing runtime capability is a gap. Use bullets instead of markdown tables on Discord.
