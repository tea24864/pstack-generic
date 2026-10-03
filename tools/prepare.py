"""Stage a pinned pstack source snapshot and normalize supporting documents."""
from pathlib import Path
import hashlib
import json
import re
import shutil
import subprocess
import os

SOURCE = Path(os.environ.get('PSTACK_SOURCE', str(Path.home() / '.hermes/cache/scratch/pstack-hermes-source/pstack')))
ROOT = Path(__file__).resolve().parents[1]


def discover():
    result = []
    for md in sorted(SOURCE.rglob('SKILL.md')):
        rel = md.relative_to(SOURCE)
        slug = md.parent.name
        name = 'pstack-' + ('benny-' if str(rel).startswith('automations/') else '') + slug
        result.append({'source': str(rel), 'slug': slug, 'name': name})
    return result


def adapt_text(text, entries):
    # Rewrite exact skill identifiers, not ordinary words like how or why.
    for e in sorted(entries, key=lambda x: len(x['slug']), reverse=True):
        old, new = e['slug'], e['name']
        text = re.sub(r'(?<![\w-])/' + re.escape(old) + r'(?![\w-])', '/' + new, text)
        text = text.replace('**' + old + '**', '**' + new + '**')
        text = text.replace('`' + old + '`', '`' + new + '`')
        text = re.sub(r'(?<=\.\./)' + re.escape(old) + r'(?=/)', new, text)
        text = re.sub(r'(?<=skills/)' + re.escape(old) + r'(?=/)', new, text)
    text = text.replace('playbooks/', 'references/playbooks/')
    return text


def main():
    entries = discover()
    snapshot = ROOT / 'upstream' / 'pstack'
    if snapshot.exists():
        raise SystemExit('Refusing to overwrite existing source snapshot')
    shutil.copytree(SOURCE, snapshot)
    revision = subprocess.check_output(['git', '-C', str(SOURCE.parent), 'rev-parse', 'HEAD'], text=True).strip()
    plugin = json.loads((SOURCE / '.cursor-plugin/plugin.json').read_text())
    originals = []
    for f in sorted(SOURCE.rglob('*')):
        if f.is_file():
            originals.append({'path': str(f.relative_to(SOURCE)), 'bytes': f.stat().st_size,
                              'sha256': hashlib.sha256(f.read_bytes()).hexdigest()})
    inventory = {'repository': 'https://github.com/cursor/plugins', 'revision': revision,
                 'plugin_version': plugin['version'], 'skill_count': len(entries),
                 'playbook_count': len(list((SOURCE / 'skills/poteto-mode/playbooks').glob('*.md'))),
                 'skills': entries, 'files': originals}
    (ROOT / 'inventory.json').write_text(json.dumps(inventory, indent=2) + '\n')
    shutil.copy2(SOURCE / 'LICENSE', ROOT / 'LICENSE')
    for e in entries:
        src = SOURCE / e['source']
        dest = ROOT / 'skills' / e['name']
        dest.mkdir(parents=True, exist_ok=True)
        # Source SKILL.md is deliberately not installed; authors create native entrypoints.
        for f in sorted(src.parent.rglob('*')):
            if not f.is_file() or f == src:
                continue
            rel = f.relative_to(src.parent)
            if rel.parts[0] == 'playbooks':
                rel = Path('references') / rel
            target = dest / rel
            target.parent.mkdir(parents=True, exist_ok=True)
            if f.suffix in ('.md', '.tsv'):
                target.write_text(adapt_text(f.read_text(), entries))
            else:
                shutil.copy2(f, target)
        license_ref = dest / 'references/license.md'
        license_ref.parent.mkdir(parents=True, exist_ok=True)
        license_ref.write_text((SOURCE / 'LICENSE').read_text())
    print(json.dumps({'revision': revision, 'version': plugin['version'], 'skills': len(entries),
                      'playbooks': inventory['playbook_count'], 'source_files': len(originals),
                      'root': str(ROOT)}, indent=2))


if __name__ == '__main__':
    main()
