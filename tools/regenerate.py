"""Regenerate only unchanged, owned Hermes distribution artifacts in a checkout."""
from pathlib import Path
import json
import shutil
import tempfile
from specialize import ROOT, build, digest, file_paths


def regenerate(root=ROOT):
    root = Path(root).resolve()
    ledger = root / 'provenance/hermes-distribution.json'
    previous = json.loads(ledger.read_text())
    expected = {row['path']: row['sha256'] for row in previous['files']}
    actual = {p.relative_to(root).as_posix(): digest(p.read_bytes()) for p in file_paths(root / 'skills')}
    if actual != expected:
        raise ValueError('Generated files have local edits/additions; review them before regeneration')
    (root / 'build').mkdir(exist_ok=True)
    with tempfile.TemporaryDirectory(prefix='regenerate-', dir=root / 'build') as folder:
        folder = Path(folder)
        output = folder / 'distribution'
        result = build(root / 'core/skills', root / 'adapters/hermes.json', output)
        backup = folder / 'previous-skills'
        before = ledger.read_bytes()
        (root / 'skills').rename(backup)
        try:
            (output / 'skills').rename(root / 'skills')
            shutil.copyfile(output / 'distribution.json', ledger)
        except Exception:
            if (root / 'skills').exists():
                shutil.rmtree(root / 'skills')
            backup.rename(root / 'skills')
            ledger.write_bytes(before)
            raise
    return {k: v for k, v in result.items() if k != 'output'}


if __name__ == '__main__':
    print(json.dumps(regenerate(), indent=2))
