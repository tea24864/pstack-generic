"""Behavior checks for setup-time specialization, isolated from installed profiles."""
from pathlib import Path
import importlib.util
import json
import os
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]


class Specialization(unittest.TestCase):
    def setUp(self):
        path = ROOT / 'tools/specialize.py'
        self.assertTrue(path.exists(), 'Setup-time deterministic specializer is not implemented')
        spec = importlib.util.spec_from_file_location('pstack_specialize', path)
        self.module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(self.module)
        self.temp = tempfile.TemporaryDirectory(prefix='pstack-specialize-', dir=os.environ.get('TMPDIR'))
        self.addCleanup(self.temp.cleanup)
        self.base = Path(self.temp.name)
        self.core = self.base / 'core'
        self.skill = self.core / 'pstack-demo'
        self.skill.mkdir(parents=True)
        (self.skill / 'SKILL.md').write_text('---\nname: pstack-demo\ndescription: "Read a fixture."\nlicense: MIT\n---\n# Demo\n\n{{runtime.files}}\n')
        self.adapter = self.base / 'adapter.json'
        self.mapping = {'schema_version': 1, 'id': 'test-native', 'identity_tools': ['native_read'],
                        'capabilities': {'independent_delegation': False}, 'limits': ['fixture adapter'],
                        'snippets': {k: 'Native instruction for ' + k for k in self.module.SLOTS}}
        self.adapter.write_text(json.dumps(self.mapping))

    def test_detect_uses_observed_tools_not_a_runtime_hint(self):
        result = self.module.detect({'tool_names': ['native_read'], 'runtime_hint': 'something-else'}, [self.adapter])
        self.assertEqual(result['runtime'], 'test-native')
        self.assertFalse(result['needs_selection'])

    def test_install_verifies_files_and_refuses_existing_skills(self):
        output = self.base / 'output'
        self.module.build(self.core, self.adapter, output)
        target = self.base / 'another agent skills'
        result = self.module.install(output, target)
        self.assertEqual(result['installed_skills'], 1)
        self.assertEqual((target / 'pstack-demo/SKILL.md').read_bytes(), (output / 'skills/pstack-demo/SKILL.md').read_bytes())
        self.assertTrue((target / '.pstack-runtime.json').is_file())
        with self.assertRaisesRegex(ValueError, 'existing'):
            self.module.install(output, target)

    def test_cli_rejects_unknown_runtime_without_writing(self):
        import subprocess
        import sys
        output = self.base / 'unknown output'
        process = subprocess.run([sys.executable, str(ROOT / 'tools/setup.py'), 'build', '--runtime', 'unreviewed-runtime', '--output', str(output)], capture_output=True, text=True)
        self.assertNotEqual(process.returncode, 0)
        self.assertIn('reviewed adapter', process.stderr)
        self.assertFalse(output.exists())

    def test_output_is_deterministic_across_locations(self):
        for folder in ('one', 'two with spaces'):
            self.module.build(self.core, self.adapter, self.base / folder)
        for rel in ('distribution.json', 'skills/pstack-demo/SKILL.md'):
            self.assertEqual((self.base / 'one' / rel).read_bytes(), (self.base / 'two with spaces' / rel).read_bytes())

    def test_unknown_and_ambiguous_detection_require_selection(self):
        result = self.module.detect({'tool_names': ['unrecognized']}, [self.adapter])
        self.assertIsNone(result['runtime'])
        self.assertTrue(result['needs_selection'])
        duplicate = self.base / 'second-adapter.json'
        duplicate.write_text(json.dumps(dict(self.mapping, id='second-native')))
        result = self.module.detect({'tool_names': ['native_read']}, [duplicate, self.adapter])
        self.assertIsNone(result['runtime'])
        self.assertEqual(result['candidates'], ['second-native', 'test-native'])

    def test_missing_adapter_slot_is_refused(self):
        del self.mapping['snippets']['files']
        self.adapter.write_text(json.dumps(self.mapping))
        with self.assertRaisesRegex(ValueError, 'insertion points'):
            self.module.build(self.core, self.adapter, self.base / 'output')
        self.assertFalse((self.base / 'output').exists())

    def test_unknown_source_slot_is_refused(self):
        (self.skill / 'reference.md').write_text('{{runtime.unreviewed}}')
        with self.assertRaisesRegex(ValueError, 'Unknown insertion point'):
            self.module.build(self.core, self.adapter, self.base / 'output')
        self.assertFalse((self.base / 'output').exists())

    def test_other_template_syntax_is_refused(self):
        (self.skill / 'reference.md').write_text('{{arbitrary.expression}}')
        with self.assertRaisesRegex(ValueError, 'Unresolved template'):
            self.module.build(self.core, self.adapter, self.base / 'output')

    def test_core_symlink_is_refused(self):
        (self.skill / 'linked.md').symlink_to(self.skill / 'SKILL.md')
        with self.assertRaisesRegex(ValueError, 'Symlink'):
            self.module.build(self.core, self.adapter, self.base / 'output')

    def test_existing_build_output_is_preserved(self):
        output = self.base / 'output'
        output.mkdir()
        (output / 'user.txt').write_text('untouched')
        with self.assertRaisesRegex(ValueError, 'existing output'):
            self.module.build(self.core, self.adapter, output)
        self.assertEqual((output / 'user.txt').read_text(), 'untouched')

    def test_modified_distribution_is_refused(self):
        output = self.base / 'output'
        self.module.build(self.core, self.adapter, output)
        (output / 'skills/pstack-demo/SKILL.md').write_text('modified after generation')
        with self.assertRaisesRegex(ValueError, 'artifact changed'):
            self.module.install(output, self.base / 'target')
        self.assertFalse((self.base / 'target').exists())

    def test_additional_distribution_artifact_is_refused(self):
        output = self.base / 'output'
        self.module.build(self.core, self.adapter, output)
        (output / 'skills/pstack-demo/unexpected.md').write_text('new unreviewed file')
        with self.assertRaisesRegex(ValueError, 'artifact set changed'):
            self.module.install(output, self.base / 'target')

    def test_generic_requires_explicit_limit_acknowledgement(self):
        output = self.base / 'output'
        self.mapping.update(id='generic', requires_acknowledgement=True)
        self.adapter.write_text(json.dumps(self.mapping))
        self.module.build(self.core, self.adapter, output)
        with self.assertRaisesRegex(ValueError, 'acknowledgement'):
            self.module.install(output, self.base / 'target')
        self.assertFalse((self.base / 'target').exists())
        result = self.module.install(output, self.base / 'target', acknowledge_limits=True)
        self.assertEqual(result['runtime'], 'generic')

    def test_partial_copy_failure_rolls_back_only_owned_trees(self):
        from unittest.mock import patch
        output = self.base / 'output'
        self.module.build(self.core, self.adapter, output)
        target = self.base / 'target'
        unrelated = target / 'existing'
        unrelated.mkdir(parents=True)
        (unrelated / 'SKILL.md').write_text('user content')
        def fail(src, dest, **kwargs):
            (dest / 'partial.txt').write_text('partial copy')
            raise OSError('simulated disk failure')
        with patch.object(self.module.shutil, 'copytree', side_effect=fail):
            with self.assertRaisesRegex(OSError, 'simulated disk failure'):
                self.module.install(output, target)
        self.assertFalse((target / 'pstack-demo').exists())
        self.assertFalse((target / '.pstack-runtime.json').exists())
        self.assertEqual((unrelated / 'SKILL.md').read_text(), 'user content')

    def test_collision_in_another_category_preserves_local_edit(self):
        output = self.base / 'output'
        self.module.build(self.core, self.adapter, output)
        existing = self.base / 'target/other-category/pstack-demo'
        existing.mkdir(parents=True)
        (existing / 'SKILL.md').write_text('local edit')
        with self.assertRaisesRegex(ValueError, 'existing skills'):
            self.module.install(output, self.base / 'target')
        self.assertEqual((existing / 'SKILL.md').read_text(), 'local edit')
        self.assertFalse((self.base / 'target/pstack-demo').exists())

    def test_missing_description_is_refused_before_output_write(self):
        (self.skill / 'SKILL.md').write_text('---\nname: pstack-demo\nlicense: MIT\n---\n# Incomplete\n')
        with self.assertRaisesRegex(ValueError, 'description'):
            self.module.build(self.core, self.adapter, self.base / 'output')
        self.assertFalse((self.base / 'output').exists())

    def test_cli_build_verify_and_install_use_explicit_destinations(self):
        import subprocess
        import sys
        output = self.base / 'generic output with spaces'
        target = self.base / 'different agent skills'
        commands = [
            ['build', '--runtime', 'generic', '--core', str(self.core), '--output', str(output)],
            ['verify', '--distribution', str(output)],
            ['install', '--distribution', str(output), '--skills-dir', str(target), '--acknowledge-limits'],
        ]
        results = []
        for arguments in commands:
            process = subprocess.run([sys.executable, '-I', str(ROOT / 'tools/setup.py'), *arguments], capture_output=True, text=True)
            self.assertEqual(process.returncode, 0, process.stderr)
            results.append(json.loads(process.stdout))
        self.assertEqual(results[-1]['installed_skills'], 1)
        self.assertEqual(results[-1]['skills_dir'], str(target))
        self.assertFalse((self.base / 'config.yaml').exists())

    def test_native_metadata_is_added_without_changing_authored_core(self):
        before = (self.skill / 'SKILL.md').read_bytes()
        self.mapping['metadata_namespace'] = 'test-native'
        self.mapping['metadata_by_skill'] = {'pstack-demo': {'config': [{'key': 'pstack.panel_size', 'default': 3}]}}
        self.adapter.write_text(json.dumps(self.mapping))
        self.module.build(self.core, self.adapter, self.base / 'output')
        text = (self.base / 'output/skills/pstack-demo/SKILL.md').read_text()
        self.assertIn('  test-native:', text)
        self.assertIn('"pstack.panel_size"', text)
        self.assertEqual((self.skill / 'SKILL.md').read_bytes(), before)

    def test_shared_native_metadata_blocks_are_resolved(self):
        self.mapping['metadata_namespace'] = 'test-native'
        self.mapping['metadata_by_skill'] = {'pstack-demo': 'panel-policy'}
        self.mapping['metadata_blocks'] = {'panel-policy': {'config': [{'key': 'pstack.panel_size', 'default': 3}]}}
        self.adapter.write_text(json.dumps(self.mapping))
        self.module.build(self.core, self.adapter, self.base / 'output')
        text = (self.base / 'output/skills/pstack-demo/SKILL.md').read_text()
        self.assertIn('"pstack.panel_size"', text)
        self.assertNotIn('test-native: "panel-policy"', text)

    def test_observed_runtime_version_is_recorded_at_installation(self):
        import inspect
        self.assertIn('runtime_version', inspect.signature(self.module.build).parameters)
        output = self.base / 'output'
        self.module.build(self.core, self.adapter, output, runtime_version='fixture-1.2.3')
        self.module.install(output, self.base / 'target')
        profile = json.loads((self.base / 'target/.pstack-runtime.json').read_text())
        self.assertEqual(profile['runtime_version'], 'fixture-1.2.3')

    def test_adapter_identity_requires_an_observed_tool_list(self):
        self.mapping['identity_tools'] = 'native_read'
        self.adapter.write_text(json.dumps(self.mapping))
        with self.assertRaisesRegex(ValueError, 'identity_tools'):
            self.module.detect({'tool_names': ['native_read']}, [self.adapter])

    def test_copy_addition_is_refused_and_owned_tree_rolled_back(self):
        from unittest.mock import patch
        output = self.base / 'output'
        self.module.build(self.core, self.adapter, output)
        original = self.module.shutil.copytree
        def injected(src, dest, **kwargs):
            result = original(src, dest, **kwargs)
            (dest / 'unreviewed.py').write_text('raise RuntimeError("unreviewed")')
            return result
        with patch.object(self.module.shutil, 'copytree', side_effect=injected):
            with self.assertRaisesRegex(ValueError, 'Installed artifact set'):
                self.module.install(output, self.base / 'target')
        self.assertFalse((self.base / 'target/pstack-demo').exists())

    def test_native_metadata_stays_inside_its_yaml_mapping(self):
        (self.skill / 'SKILL.md').write_text('---\nname: pstack-demo\ndescription: "Read a fixture."\nlicense: MIT\nmetadata:\n  author: "Fixture"\nallowed-tools: native_read\n---\n# Demo\n')
        self.mapping['metadata_namespace'] = 'test-native'
        self.mapping['metadata_by_skill'] = {'pstack-demo': {'tags': ['fixture']}}
        self.adapter.write_text(json.dumps(self.mapping))
        self.module.build(self.core, self.adapter, self.base / 'output')
        text = (self.base / 'output/skills/pstack-demo/SKILL.md').read_text()
        self.assertLess(text.index('  test-native:'), text.index('allowed-tools:'))

    def test_build_specializes_only_relevant_instructions(self):
        result = self.module.build(self.core, self.adapter, self.base / 'output')
        text = (self.base / 'output/skills/pstack-demo/SKILL.md').read_text()
        self.assertIn('Native instruction for files', text)
        self.assertNotIn('Native instruction for delegation', text)
        self.assertNotIn('{{', text)
        self.assertEqual(result['runtime'], 'test-native')
        self.assertEqual(result['skills'], 1)
        self.assertTrue((self.base / 'output/distribution.json').is_file())


if __name__ == '__main__':
    unittest.main()
