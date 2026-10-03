"""Port pstack's 24 engineering principles, preserving their specific rules."""
from pathlib import Path
import json
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent))
from authoring import ROOT, ENTRIES, body, standard

DESCRIPTIONS = {
'attack-the-premise': 'Challenge shared assumptions after repeated failed fixes.',
'boundary-discipline': 'Validate at boundaries; keep domain logic independent.',
'build-the-lever': 'Build rerunnable tools for nontrivial work and checks.',
'encode-lessons-in-structure': 'Encode recurring corrections as durable mechanisms.',
'exhaust-the-design-space': 'Compare distinct designs before choosing a new shape.',
'experience-first': 'Choose scope and design for the consumer experience.',
'explain-the-number': 'Validate what measured numbers actually demonstrate.',
'fix-root-causes': 'Reproduce defects and fix their demonstrated cause.',
'foundational-thinking': 'Choose data structures before logic and shared state.',
'guard-the-context-window': 'Keep bulk payloads out of the main reasoning context.',
'laziness-protocol': 'Reduce code and complexity before adding abstractions.',
'make-operations-idempotent': 'Design operations to converge across retries and crashes.',
'migrate-callers-then-delete-legacy-apis': 'Migrate internal callers and remove obsolete APIs.',
'minimize-reader-load': 'Reduce tracing layers and hidden state in code.',
'model-the-domain': 'Represent domain invariants directly in data structures.',
'never-block-on-the-human': 'Decide reversible execution details within granted scope.',
'outcome-oriented-execution': 'Verify end states at explicit migration boundaries.',
'prove-it-works': 'Verify real artifacts before declaring work complete.',
'redesign-from-first-principles': 'Integrate new requirements into a coherent design.',
'separate-before-serializing-shared-state': 'Separate write ownership before locking shared state.',
'sequence-verifiable-units': 'Deliver work as small independently verifiable units.',
'subtract-before-you-add': 'Remove unnecessary complexity before building additions.',
' test-behavior-not-implementation': 'Test observable behavior, not implementation trivia.',
'type-system-discipline': 'Use types to prove invariants and exhaust variants.',
}
DESCRIPTIONS['test-behavior-not-implementation'] = DESCRIPTIONS.pop(' test-behavior-not-implementation')


def main():
    decisions = []
    for entry in ENTRIES:
        slug = entry['slug']
        if not slug.startswith('principle-'):
            continue
        key = slug.removeprefix('principle-')
        text = body(slug)
        # Qualify upstream short principle references without changing ordinary prose.
        for other in DESCRIPTIONS:
            text = text.replace('**' + other + '**', '**pstack-principle-' + other + '**')
        if key == 'fix-root-causes':
            text = text.replace('(grep for the same pattern, fix all instances)', '(use `search_files` for the same pattern and fix the in-scope instances)')
            text += '\n\nState-reset experiments need an isolated copy and explicit cleanup scope. Do not delete production caches or persistent state merely to test a hypothesis.'
        if key == 'never-block-on-the-human':
            text += '\n\nIn Hermes, reversibility is not authorization. Proceed only within the user\'s task scope. Explicit stop, plan-only, checkpoint, no-merge, and no-publication instructions override this principle. Never bypass a tool approval prompt or treat a missing credential as permission to guess it.'
        if key == 'boundary-discipline':
            text = text.replace('Trust internal code unconditionally.', 'Trust validated internal domain types; identify new trust boundaries when data enters dynamically or crosses a process.')
        if key == 'encode-lessons-in-structure':
            text = text.replace('One-off -> brain note.', 'One-off -> task artifact or session history, not persistent memory.')
            text = text.replace('a brain note about a lint rule', 'a temporary note about a lint rule')
        if key == 'guard-the-context-window':
            text = text.replace('finite and non-renewable within a session', 'finite; compression can lose detail within a session')
            text += '\n\nPrefer deterministic extraction with `execute_code` for mechanical bulk. Reload pruned skills with `skill_view` before relying on them, and write resumable evidence to the active workspace rather than assuming child contexts persist.'
        if key == 'sequence-verifiable-units':
            text += '\n\nDo not rebase, commit, push, or intentionally break a shared branch without the corresponding scope. Use isolated worktrees for staged failing tests and migration boundaries.'
        if key == 'test-behavior-not-implementation':
            text += '\n\nThese test smells are diagnostic, not a blanket deletion rule. Absence assertions, interaction contracts, and schema/prompt invariants can encode real behavior. Keep them when a relevant defect makes the check fail; do not weaken or delete tests merely to make a wrong implementation pass.'
        if key in ('migrate-callers-then-delete-legacy-apis', 'outcome-oriented-execution'):
            text += '\n\nHonor compatibility promises to external users and shared production uptime. Planned intermediate breakage belongs only in the explicitly approved isolated migration scope.'
        related = []
        import re
        for match in re.finditer(r'\.\./(?:pstack-)?(principle-[a-z-]+|benchmark-checklist)/SKILL\.md', text):
            related.append(match.group(1))
        standard(slug, DESCRIPTIONS[key], text,
                 triggers='Use when ' + DESCRIPTIONS[key][0].lower() + DESCRIPTIONS[key][1:] + ' Do not treat a design principle as a mandate to expand the task.',
                 pitfalls='Apply the rule to observed constraints, not as an absolute ban. Preserve approval gates, compatibility contracts, and higher-priority user instructions. The runtime contract defines tool and profile boundaries.',
                 verification='Name the concrete decision this principle changed and the artifact or evidence that supports it. For execution claims, use real tool output; for a design judgment, state its constraints and remaining uncertainty.',
                 related=tuple(dict.fromkeys(related)))
        decisions.append({'source': entry['source'], 'target': 'skills/' + entry['name'] + '/SKILL.md',
                          'status': 'adapted', 'reason': 'Preserved principle, namespaced links, native tooling and bounded authorization.'})
    report = {'group': 'principles', 'skill_count': len(decisions), 'files': decisions,
              'limitations': ['Principles are judgment procedures, not a runtime enforcement engine.'],
              'tests': ['Authoring enforces a self-contained description <=57 characters and known skill mappings.']}
    (ROOT / 'reports').mkdir(exist_ok=True)
    (ROOT / 'reports/principles.json').write_text(json.dumps(report, indent=2) + '\n')
    print(json.dumps({'ported': len(decisions), 'names': [e['target'] for e in decisions]}, indent=2))


if __name__ == '__main__':
    main()
