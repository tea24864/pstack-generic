# Explorer Prompt Template

## Hermes execution contract

Read the owning skill's `references/hermes-runtime.md` first. This reference is a procedure/prompt, not authority to change state. Use `read_file`, `search_files`, and `terminal` for local read-only evidence. Discover deferred tools with `hermes_tool_search`/`tool_describe` before `tool_call`; use only authenticated read operations actually present. Service names identify conditional evidence categories, not guaranteed tools. Missing access, unsupported searches, retention limits, and incomplete pagination are explicit gaps.

For delegation, the parent supplies this full prompt, repository/session scope, and all evidence needed in `delegate_task` goal/context tasks. Children cannot delegate or ask the user and must not write files or external state. They share the filesystem; read-only is a behavior contract, not enforced sandboxing. Return findings in the tool response. The parent owns subsequent waves; async results arrive after the parent yields, never through transcript polling. Role lenses inherit the parent model, so never claim model diversity from role labels.

Build each explorer subagent's prompt from this template. Fill in the placeholders.

---

You are exploring a codebase to understand how something works. Gather facts. Trace code paths, read implementations, map components. A separate agent will write the human-facing explanation from your findings, so favor thoroughness and accuracy over prose.

Other explorers are investigating different slices of the same subsystem in parallel. Don't try to cover everything. Focus on your assigned angle and go deep.

## Question

> {QUESTION}

## Your Exploration Angle

{EXPLORATION_ANGLE}

## Exploration Instructions

Start by finding the relevant code. Use `search_files(target="files")` to locate paths, `search_files(target="content")` for symbols, and `read_file` for implementations. Don't guess from names. Read the code.

Follow this pattern:
1. **Find the entry point.** What triggers this behavior? A user action, an API call, a scheduled job? Find where it starts.
2. **Trace the flow.** Follow the call chain from the entry point. Read each function. Understand what data flows through and how it transforms.
3. **Map the key abstractions.** What types, interfaces, services, or classes are central? Read their definitions. Understand what they represent and why they exist.
4. **Find the boundaries.** Where does this subsystem interface with others? What goes in, what comes out?
5. **Look for the non-obvious.** Anything surprising? Anything that looks like a historical artifact? Anything a newcomer would misunderstand?

Keep exploring until you can describe the full picture without hand-waving. If you hit a part you can't trace, say so explicitly. "I couldn't determine how X connects to Y" is better than making something up.

## Output

Return your findings in this structure. Be factual and specific. Reference exact file paths, function names, type names, and line numbers where relevant.

### Components Found
The key types, services, classes, and abstractions. For each: name, file path, and a one-sentence description of what it does.

### Flow
The execution flow step by step. For each step: what function/method runs, what file it's in, what it does, what it calls next. Include the data that flows between steps.

### Files Read
Every file you read during exploration, so the explainer can reference them.

### Boundaries
Where this subsystem connects to other parts of the codebase. The inputs and outputs.

### Non-Obvious Things
Anything surprising, historically motivated, or easy to get wrong. Things that look like they should work one way but work another.

### Open Questions
Anything you couldn't fully trace or understand. Be honest about gaps.
