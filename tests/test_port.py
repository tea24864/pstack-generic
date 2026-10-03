"""Artifact, native Hermes loading, and installer behavior tests; no live network."""
from pathlib import Path
import contextlib
import hashlib
import json
import os
import re
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT/'tools'))
import manage


class SourceContract(unittest.TestCase):
    def test_pinned_source_files_match_inventory(self):
        data=manage.inventory()
        actual={str(f.relative_to(ROOT/'upstream/pstack')) for f in (ROOT/'upstream/pstack').rglob('*') if f.is_file()}
        expected={f['path'] for f in data['files']}
        self.assertEqual(actual,expected)
        for f in data['files']:
            with self.subTest(file=f['path']):
                path=ROOT/'upstream/pstack'/f['path']
                self.assertEqual(manage.digest(path),f['sha256'])
                self.assertEqual(path.stat().st_size,f['bytes'])

    def test_source_and_port_have_identical_skill_coverage(self):
        entries=manage.inventory()['skills']
        source={str(f.relative_to(ROOT/'upstream/pstack')) for f in (ROOT/'upstream/pstack').rglob('SKILL.md')}
        self.assertEqual(source,{e['source'] for e in entries})
        self.assertEqual({e['name'] for e in entries},{f.parent.name for f in (ROOT/'skills').glob('*/SKILL.md')})
        self.assertEqual(len(entries),len({e['name'] for e in entries}))

    def test_every_playbook_has_an_adapted_counterpart(self):
        upstream={f.name for f in (ROOT/'upstream/pstack/skills/poteto-mode/playbooks').glob('*.md')}
        port={f.name for f in (ROOT/'skills/pstack-poteto-mode/references/playbooks').glob('*.md')}
        self.assertEqual(upstream,port)
        self.assertEqual(len(port),manage.inventory()['playbook_count'])

    def test_full_native_validation(self):
        result=manage.validate(native=True)
        self.assertTrue(result['success'],json.dumps(result['errors'],indent=2))

    def test_portable_manifest_matches_all_installable_artifacts(self):
        result=json.loads((ROOT/'package-manifest.json').read_text())
        manage.verify_artifacts(result)
        self.assertEqual(result['revision'],manage.inventory()['revision'])

    def test_runtime_contract_is_present_and_identical(self):
        expected=(ROOT/'docs/hermes-runtime.md').read_text()
        for entry in manage.inventory()['skills']:
            with self.subTest(skill=entry['name']):
                self.assertEqual((ROOT/'skills'/entry['name']/'references/hermes-runtime.md').read_text(),expected)

    def test_offline_audit_preserves_git_index_metadata(self):
        import importlib.util
        with tempfile.TemporaryDirectory(prefix='pstack-index-test-',dir=os.environ.get('TMPDIR')) as folder:
            repo=Path(folder)
            def git(*args):
                r=subprocess.run(['git','-C',str(repo),*args],text=True,capture_output=True)
                self.assertEqual(r.returncode,0,r.stderr)
                return r.stdout.strip()
            git('init','-q','-b','main')
            tracked=repo/'tracked.txt'
            tracked.write_text('unchanged contents\n')
            git('add','tracked.txt')
            git('-c','user.name=Fixture','-c','user.email=fixture@example.invalid','-c','commit.gpgsign=false','commit','-qm','fixture')
            index=repo/'.git/index'
            before=index.read_bytes()
            stat=tracked.stat()
            os.utime(tracked,ns=(stat.st_atime_ns,stat.st_mtime_ns+5_000_000_000))
            result=subprocess.run(['python',str(ROOT/'skills/pstack-poteto-mode/scripts/worktree-audit.py'),str(repo)],text=True,capture_output=True)
            self.assertEqual(result.returncode,0,result.stderr)
            rows=json.loads(result.stdout)['worktrees']
            self.assertEqual(rows[0]['status_counts'],{'tracked':0,'untracked':0,'ignored':0})
            self.assertEqual(index.read_bytes(),before)
            self.assertEqual(tracked.read_text(),'unchanged contents\n')

    def test_mit_attribution_is_retained(self):
        self.assertEqual((ROOT/'LICENSE').read_bytes(),(ROOT/'upstream/pstack/LICENSE').read_bytes())
        for e in manage.inventory()['skills']:
            with self.subTest(skill=e['name']):
                self.assertEqual((ROOT/'skills'/e['name']/'references/license.md').read_bytes(),(ROOT/'LICENSE').read_bytes())


class NativeHermesLoading(unittest.TestCase):
    def setUp(self):
        from tools import skills_tool
        self.tools=skills_tool
        self.stack=contextlib.ExitStack()
        self.stack.enter_context(patch.object(skills_tool,'_skill_search_dirs',return_value=([],[ROOT/'skills'],ROOT/'skills')))
        self.stack.enter_context(patch.object(skills_tool,'_get_disabled_skill_names',return_value=set()))
        self.stack.enter_context(patch.object(skills_tool,'_is_skill_disabled',return_value=False))
        self.stack.enter_context(patch.object(skills_tool,'_mark_background_review_read',return_value=None))
        self.stack.enter_context(patch.dict(skills_tool._SKILLS_CACHE,{},clear=True))
        self.addCleanup(self.stack.close)

    def test_catalog_discovers_every_namespaced_skill(self):
        expected={e['name'] for e in manage.inventory()['skills']}
        actual={s['name'] for s in self.tools._find_all_skills()}
        self.assertEqual(expected,actual)

    def test_each_main_skill_loads_exact_artifact(self):
        for e in manage.inventory()['skills']:
            with self.subTest(skill=e['name']):
                result=json.loads(self.tools.skill_view(e['name'],preprocess=False))
                self.assertTrue(result['success'],result)
                self.assertEqual(result['name'],e['name'])
                self.assertEqual(result['content'],(ROOT/'skills'/e['name']/'SKILL.md').read_text())

    def test_nested_playbooks_and_rubrics_load(self):
        samples=[('pstack-poteto-mode','references/playbooks/bug-fix.md'),
                 ('pstack-poteto-mode','references/playbooks/shipping.md'),
                 ('pstack-architect','references/rationale-template.md'),
                 ('pstack-interrogate','references/rubric.md'),
                 ('pstack-why','references/epistemics.md')]
        for name,rel in samples:
            with self.subTest(skill=name,file=rel):
                result=json.loads(self.tools.skill_view(name,file_path=rel,preprocess=False))
                self.assertTrue(result['success'],result)
                self.assertEqual(result['content'],(ROOT/'skills'/name/rel).read_text())

    def test_panel_policy_defaults_and_overrides_are_injected(self):
        from agent import skill_commands, skill_utils
        mapping={'pstack-arena':{'skill_dir':'pstack-arena'}}
        with patch.object(skill_commands,'get_skill_commands',return_value=mapping):
            with patch.object(skill_utils,'_load_raw_config',return_value={}):
                defaults=skill_commands.build_skill_invocation_message('pstack-arena','Design only.')
                self.assertIn('pstack.panel_size = 3',defaults)
                self.assertIn('pstack.model_strategy = inherit-parent',defaults)
            settings={'skills':{'config':{'pstack':{'panel_size':5,'model_strategy':'verified-external'}}}}
            with patch.object(skill_utils,'_load_raw_config',return_value=settings):
                changed=skill_commands.build_skill_invocation_message('pstack-arena','Design only.')
                self.assertIn('pstack.panel_size = 5',changed)
                self.assertIn('pstack.model_strategy = verified-external',changed)
                self.assertIn('Design only.',changed)

    def test_slash_invocation_preserves_task_and_renders_paths(self):
        from agent import skill_commands
        mapping={e['name']:{'skill_dir':e['name']} for e in manage.inventory()['skills']}
        with patch.object(skill_commands,'get_skill_commands',return_value=mapping):
            for name in ('pstack-tdd','pstack-architect','pstack-poteto-mode','pstack-interrogate'):
                with self.subTest(skill=name):
                    instruction='Read only. Stop before implementation.'
                    msg=skill_commands.build_skill_invocation_message(name,instruction)
                    self.assertIsNotNone(msg)
                    self.assertIn(instruction,msg)
                    self.assertIn(name,msg)
                    self.assertIn(str(ROOT/'skills'/name),msg)


class InstallerBehavior(unittest.TestCase):
    def setUp(self):
        scratch=os.environ.get('TMPDIR')
        self.temp=tempfile.TemporaryDirectory(prefix='pstack-installer-test-',dir=scratch)
        self.addCleanup(self.temp.cleanup)
        self.base=Path(self.temp.name)
        self.pkg=self.base/'package'
        self.home=self.base/'user/.hermes'
        self.skill=self.pkg/'skills/pstack-demo'
        self.skill.mkdir(parents=True)
        (self.skill/'SKILL.md').write_text('demo skill content\n')
        self.home.mkdir(parents=True)
        (self.home/'config.yaml').write_text('model: unchanged\n')
        old=self.home/'skills/software-development/existing'
        old.mkdir(parents=True)
        (old/'SKILL.md').write_text('existing skill\n')
        (self.pkg/'reports').mkdir()
        (self.pkg/'inventory.json').write_text(json.dumps({'skills':[{'name':'pstack-demo'}]}))
        self.record={'path':'skills/pstack-demo/SKILL.md','sha256':manage.digest(self.skill/'SKILL.md')}
        self.validation={'success':True,'native_validator':True,'files':[self.record]}
        self.write_validation()
        self.stack=contextlib.ExitStack()
        self.stack.enter_context(patch.object(manage,'ROOT',self.pkg))
        self.stack.enter_context(patch.object(Path,'home',return_value=self.base/'user'))
        self.addCleanup(self.stack.close)

    def write_validation(self):
        (self.pkg/'package-manifest.json').write_text(json.dumps(self.validation))

    def test_install_copies_exact_artifact_and_preserves_existing(self):
        result=manage.install(self.home)
        self.assertEqual((self.home/'skills/software-development/pstack-demo/SKILL.md').read_text(),'demo skill content\n')
        self.assertEqual((self.home/'skills/software-development/existing/SKILL.md').read_text(),'existing skill\n')
        self.assertEqual((self.home/'config.yaml').read_text(),'model: unchanged\n')
        self.assertEqual(result['installed_skills'],1)
        self.assertTrue(result['preexisting_unchanged'])
        self.assertTrue(result['config_unchanged'])

    def test_existing_skill_collision_is_not_overwritten(self):
        dest=self.home/'skills/other/pstack-demo'
        dest.mkdir(parents=True)
        (dest/'SKILL.md').write_text('custom local edit\n')
        with self.assertRaisesRegex(ValueError,'collision'):
            manage.install(self.home)
        self.assertEqual((dest/'SKILL.md').read_text(),'custom local edit\n')
        self.assertFalse((self.home/'skills/software-development/pstack-demo').exists())

    def test_explicit_home_installs_without_touching_other_profiles(self):
        other=self.base/'another-agent/home with spaces'
        other.mkdir(parents=True)
        (other/'config.yaml').write_text('profile: untouched\n')
        result=manage.install(other)
        self.assertEqual((other/'skills/software-development/pstack-demo/SKILL.md').read_text(),'demo skill content\n')
        self.assertEqual((other/'config.yaml').read_text(),'profile: untouched\n')
        self.assertEqual((self.home/'config.yaml').read_text(),'model: unchanged\n')
        self.assertFalse((self.home/'skills/software-development/pstack-demo').exists())
        self.assertTrue(result['config_unchanged'])

    def test_explicit_empty_home_can_be_initialized(self):
        other=self.base/'fresh-agent'
        result=manage.install(other)
        self.assertEqual(result['installed_skills'],1)
        self.assertFalse((other/'config.yaml').exists())
        self.assertTrue(result['config_unchanged'])

    def test_failed_validation_is_refused(self):
        self.validation['success']=False
        self.write_validation()
        with self.assertRaisesRegex(ValueError,'Native validation'):
            manage.install(self.home)
        self.assertFalse((self.home/'skills/software-development/pstack-demo').exists())

    def test_changed_artifact_is_refused(self):
        (self.skill/'SKILL.md').write_text('edited after scan\n')
        with self.assertRaisesRegex(ValueError,'artifact changed'):
            manage.install(self.home)
        self.assertFalse((self.home/'skills/software-development/pstack-demo').exists())

    def test_added_artifact_is_refused(self):
        (self.skill/'unexpected.md').write_text('not part of the native scan\n')
        with self.assertRaisesRegex(ValueError,'artifact set changed'):
            manage.install(self.home)
        self.assertFalse((self.home/'skills/software-development/pstack-demo').exists())

    def test_partial_copy_failure_rolls_back_only_owned_tree(self):
        def broken_copy(src,dest,**kwargs):
            (dest/'partial.txt').write_text('partial copy\n')
            raise OSError('simulated disk failure')
        with patch.object(manage.shutil,'copytree',side_effect=broken_copy):
            with self.assertRaisesRegex(OSError,'simulated disk failure'):
                manage.install(self.home)
        self.assertFalse((self.home/'skills/software-development/pstack-demo').exists())
        self.assertEqual((self.home/'skills/software-development/existing/SKILL.md').read_text(),'existing skill\n')
        self.assertEqual((self.home/'config.yaml').read_text(),'model: unchanged\n')

    def test_second_install_refuses_instead_of_destroying_local_edits(self):
        manage.install(self.home)
        dest=self.home/'skills/software-development/pstack-demo/SKILL.md'
        dest.write_text('subsequent local edit\n')
        with self.assertRaisesRegex(ValueError,'collision'):
            manage.install(self.home)
        self.assertEqual(dest.read_text(),'subsequent local edit\n')


if __name__=='__main__':unittest.main(verbosity=2)
