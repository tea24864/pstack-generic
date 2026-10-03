"""Shared authoring helpers for the Hermes pstack port (stdlib only)."""
from pathlib import Path
import json
import re

ROOT = Path(__file__).resolve().parents[1]
INVENTORY = json.loads((ROOT / 'inventory.json').read_text())
ENTRIES = INVENTORY['skills']
NAMES = {e['slug']: e['name'] for e in ENTRIES}


def source(slug):
    entry = next(e for e in ENTRIES if e['slug'] == slug)
    return ROOT / 'upstream/pstack' / entry['source']


def body(slug):
    text = source(slug).read_text()
    return text.split('\n---\n', 1)[1].lstrip()


def transform(text):
    from prepare import adapt_text
    return adapt_text(text, ENTRIES)


def save(slug, description, content, *, platforms=('linux', 'macos'), related=()):
    name = NAMES[slug]
    assert len(description) <= 57 and description.endswith('.'), (name, description)
    directory = ROOT / 'skills' / name
    directory.mkdir(parents=True, exist_ok=True)
    fm = '\n'.join([
        '---', 'name: ' + name, 'description: ' + json.dumps(description),
        'version: 0.1.0', 'author: "Lauren Tan (poteto), tea24864, Hermes Agent"',
        'license: MIT', 'platforms: ' + json.dumps(list(platforms)),
        'metadata:', '  hermes:', '    tags: [pstack, engineering, workflow]',
        '    related_skills: ' + json.dumps([NAMES.get(r,r) for r in related]),
        '---', '',
    ])
    (directory / 'SKILL.md').write_text(fm + content.rstrip() + '\n')


def standard(slug, description, content, *, triggers=None, pitfalls=None, verification=None, related=()):
    """Preserve the specific procedure and surround it with native skill contracts."""
    text = transform(content)
    first, sep, rest = text.partition('\n')
    if first.startswith('# '):
        title = first
        text = rest.lstrip()
    else:
        title = '# ' + NAMES[slug]
    start = title + '\n\n## When to Use\n\n'
    start += (triggers or description) + '\n\n'
    start += '## Prerequisites\n\nRead `references/hermes-runtime.md` with `skill_view` before executing this workflow. '
    start += 'Use only tools and credentials actually available in this session. '
    start += 'Invoking this skill does not authorize publication, merges, destructive cleanup, or configuration changes.\n\n'
    text = start + '## Procedure\n\n' + text
    if '## Pitfalls' not in text:
        text += '\n\n## Pitfalls\n\n' + (pitfalls or 'Keep the user\'s scope and explicit checkpoints. Missing evidence or unavailable dependencies are gaps, not passes. Do not replace a working existing skill or change another profile.')
    if '## Verification' not in text:
        text += '\n\n## Verification\n\n' + (verification or 'Check each promised artifact and claim against a real tool result. Report evidence, skipped checks, and limitations. A child\'s self-report is not independent verification.')
    text += '\n\n## Attribution\n\nAdapted from Lauren Tan\'s MIT-licensed pstack ' + INVENTORY['plugin_version'] + ', source revision `' + INVENTORY['revision'] + '`. See `references/license.md`.\n'
    save(slug, description, text, related=related)
