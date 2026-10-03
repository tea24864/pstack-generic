"""Verify/refresh the portable source-to-port ledger; no worker reports required."""
from pathlib import Path
from collections import Counter
import hashlib
import json

ROOT = Path(__file__).resolve().parents[1]


def main():
    inv = json.loads((ROOT / 'inventory.json').read_text())
    ledger_path = ROOT / 'provenance/coverage.json'
    previous = json.loads(ledger_path.read_text())
    rows = {r['source']: r for r in previous['files']}
    originals = {r['path']: r for r in inv['files']}
    if rows.keys() != originals.keys() or len(rows) != len(previous['files']):
        raise ValueError('Coverage must account for every original source exactly once')
    for source, row in rows.items():
        original = ROOT / 'upstream/pstack' / source
        if hashlib.sha256(original.read_bytes()).hexdigest() != originals[source]['sha256']:
            raise ValueError('Pinned upstream source changed: ' + source)
        target = ROOT / row['target']
        if not target.is_file():
            raise ValueError('Missing coverage target: ' + row['target'])
        row['source_sha256'] = originals[source]['sha256']
        row['target_sha256'] = hashlib.sha256(target.read_bytes()).hexdigest()
        row['target_bytes'] = target.stat().st_size
    names = {p.parent.name for p in (ROOT / 'skills').glob('*/SKILL.md')}
    if names != {e['name'] for e in inv['skills']}:
        raise ValueError('Namespaced skill coverage differs from source inventory')
    previous['files'] = [rows[r['path']] for r in inv['files']]
    previous['dispositions'] = dict(Counter(r['disposition'] for r in rows.values()))
    ledger_path.write_text(json.dumps(previous, indent=2) + '\n')
    print(json.dumps({k: v for k, v in previous.items() if k != 'files'}, indent=2))


if __name__ == '__main__':
    main()
