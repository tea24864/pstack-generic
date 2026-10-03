---
name: pstack-bro
description: "Restate the last reply in plain concise language."
version: 0.1.0
author: "Lauren Tan (poteto), tea24864, Hermes Agent"
license: MIT
platforms: ["linux", "macos"]
metadata:
  hermes:
    tags: [pstack, engineering, workflow]
    related_skills: []
---
# Plain restatement

## When to Use

Use when the user asks to restate the last reply without jargon. Do not use for new research or code changes.

## Prerequisites

Read `references/hermes-runtime.md` with `skill_view` before executing this workflow. Use only tools and credentials actually available in this session. Invoking this skill does not authorize publication, merges, destructive cleanup, or configuration changes.

## Procedure

Read the immediately preceding assistant message in this conversation. Restate it more simply and concisely, like one human talking to another. Keep its actual point, caveats, uncertainty, and actionable next step. Preserve commands, identifiers, and values exactly. Do not rerun the task or add facts.

If the message being restated is unavailable, ask the caller for it rather than guessing. Return the restatement, not an explanation of the writing process.

## Pitfalls

Keep the user's scope and explicit checkpoints. Missing evidence or unavailable dependencies are gaps, not passes. Do not replace a working existing skill or change another profile.

## Verification

Compare with the previous reply. Nothing factual was added, no condition disappeared, and technical tokens remain exact.

## Attribution

Adapted from Lauren Tan's MIT-licensed pstack 0.15.6, source revision `23e4138daa01c42d4969f7a5465f82704e64f798`. See `references/license.md`.
