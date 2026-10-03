"""Whole-source invariants and real distribution generation; no live network."""
from pathlib import Path
import json
import os
import re
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'tools'))
import specialize

HOST = re.compile(r'\b(?:Hermes|Cursor|skill_view|skill_manage|delegate_task|tool_describe|tool_call|session_search|todo_list|HERMES_HOME|browser_vault_\w+)\b')


class CoreContract(unittest.TestCase):
    def test_all_52_core_entrypoints_have_standard_scalar_metadata(self):
        inv = json.loads((ROOT / 'inventory.json').read_text())
        paths = list((ROOT / 'core/skills').glob('*/SKILL.md'))
        self.assertEqual({p.parent.name for p in paths}, {s['name'] for s in inv['skills']})
        self.assertEqual(len(paths), 52)
        for path in paths:
            with self.subTest(skill=path.parent.name):
                fields = specialize.validate_frontmatter(path.read_text(), path.parent.name)
                self.assertEqual(fields['metadata']['source-revision'], inv['revision'])
                self.assertEqual(fields['metadata']['author'], 'Lauren Tan (poteto), tea24864')
                self.assertTrue(all(isinstance(v, str) for v in fields['metadata'].values()))

    def test_core_has_no_host_apis_or_machine_paths(self):
        for path in specialize.file_paths(ROOT / 'core/skills'):
            if path.suffix not in ('.md', '.py', '.mjs', '.sh', '.json'):
                continue
            text = path.read_text()
            with self.subTest(file=str(path.relative_to(ROOT))):
                self.assertIsNone(HOST.search(text))
                self.assertNotRegex(text, r'/home/[A-Za-z0-9_.-]+/|~/\.cursor/')
                self.assertTrue(set(specialize.SLOT.findall(text)) <= specialize.SLOTS)

    def test_all_24_principles_require_no_runtime_map(self):
        paths = list((ROOT / 'core/skills').glob('pstack-principle-*/SKILL.md'))
        self.assertEqual(len(paths), 24)
        for path in paths:
            self.assertNotIn('{{runtime.', path.read_text())
            self.assertIn('## Procedure', path.read_text())
            self.assertIn('## Verification', path.read_text())

    def test_playbook_set_and_licenses_are_preserved(self):
        original = ROOT / 'upstream/pstack/skills/poteto-mode/playbooks'
        core = ROOT / 'core/skills/pstack-poteto-mode/references/playbooks'
        self.assertEqual({p.name for p in original.glob('*.md')}, {p.name for p in core.glob('*.md')})
        self.assertEqual(len(list(core.glob('*.md'))), 23)
        license_bytes = (ROOT / 'LICENSE').read_bytes()
        for path in (ROOT / 'core/skills').glob('*/references/license.md'):
            self.assertEqual(path.read_bytes(), license_bytes)

    def test_rebuilding_hermes_reproduces_every_committed_artifact(self):
        with tempfile.TemporaryDirectory(prefix='pstack-rebuild-', dir=os.environ.get('TMPDIR')) as folder:
            output = Path(folder) / 'fresh distribution'
            specialize.build(ROOT / 'core/skills', ROOT / 'adapters/hermes.json', output)
            generated = {p.relative_to(output / 'skills').as_posix(): p.read_bytes() for p in specialize.file_paths(output / 'skills')}
            committed = {p.relative_to(ROOT / 'skills').as_posix(): p.read_bytes() for p in specialize.file_paths(ROOT / 'skills')}
            self.assertEqual(generated.keys(), committed.keys())
            for rel in generated:
                self.assertEqual(generated[rel], committed[rel], rel)
            self.assertEqual((output / 'distribution.json').read_bytes(), (ROOT / 'provenance/hermes-distribution.json').read_bytes())

    def test_generic_build_discloses_missing_capabilities_without_host_leakage(self):
        with tempfile.TemporaryDirectory(prefix='pstack-generic-', dir=os.environ.get('TMPDIR')) as folder:
            output = Path(folder) / 'fresh distribution'
            specialize.build(ROOT / 'core/skills', ROOT / 'adapters/generic.json', output)
            manifest = specialize.verify_distribution(output)
            self.assertFalse(manifest['capabilities']['independent_delegation'])
            self.assertTrue(manifest['requires_acknowledgement'])
            self.assertEqual(len(manifest['skills']), 52)
            for path in specialize.file_paths(output / 'skills'):
                if path.suffix == '.md':
                    text = path.read_text()
                    self.assertIsNone(HOST.search(text), str(path))
                    self.assertNotIn('{{', text)
            arena = (output / 'skills/pstack-arena/SKILL.md').read_text()
            self.assertIn('no independent subagents or cross-judge', arena)
            self.assertIn('same-agent perspectives', arena)

    def test_coverage_ledger_accounts_for_every_original_at_canonical_targets(self):
        inv = json.loads((ROOT / 'inventory.json').read_text())
        ledger = json.loads((ROOT / 'provenance/coverage.json').read_text())
        self.assertEqual(len(ledger['files']), 160)
        self.assertEqual({r['source'] for r in ledger['files']}, {r['path'] for r in inv['files']})
        for row in ledger['files']:
            self.assertTrue((ROOT / row['target']).is_file(), row['target'])
            self.assertFalse(row['target'].startswith('skills/'), row['target'])


if __name__ == '__main__':
    unittest.main()
