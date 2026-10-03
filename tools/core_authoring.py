"""Shared neutral frontmatter authoring for runtime-specialized pstack."""
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]
DATA = json.loads((ROOT / 'inventory.json').read_text())
SLOTS = frozenset('files delegation task_tracking history skill_loading skill_maintenance configuration integrations persistent_work web setup'.split())


def save(name, description, body, *, compatibility=None):
    """Write one standard-format authored core entrypoint, never installed skills."""
    assert name in {e['name'] for e in DATA['skills']}
    assert description and len(description) <= 60
    lines = ['---', 'name: ' + name, 'description: ' + json.dumps(description), 'license: MIT']
    if compatibility:
        lines.append('compatibility: ' + json.dumps(compatibility))
    lines += ['metadata:', '  author: "Lauren Tan (poteto), tea24864"',
              '  version: "0.2.0"', '  source-revision: ' + json.dumps(DATA['revision']),
              '---', '', body.rstrip(), '']
    path = ROOT / 'core/skills' / name / 'SKILL.md'
    path.write_text('\n'.join(lines))
    return path
