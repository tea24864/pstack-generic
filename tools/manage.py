"""Validate and safely install the namespaced pstack package into one profile."""
from pathlib import Path
from collections import Counter
import argparse
import hashlib
import json
import os
import re
import shutil
import sys

ROOT = Path(__file__).resolve().parents[1]


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def inventory():
    return json.loads((ROOT / 'inventory.json').read_text())


def sync_runtime():
    contract = (ROOT / 'docs/hermes-runtime.md').read_text()
    for entry in inventory()['skills']:
        target = ROOT / 'skills' / entry['name'] / 'references/hermes-runtime.md'
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(contract)
    return {'runtime_copies': inventory()['skill_count']}


def validate(*, native=False):
    errors, warnings, files = [], [], []
    data = inventory()
    entries = data['skills']
    names = {e['name'] for e in entries}
    actual = {p.parent.name for p in (ROOT / 'skills').glob('*/SKILL.md')}
    if names != actual:
        errors.append({'rule': 'coverage', 'missing': sorted(names-actual), 'extra': sorted(actual-names)})
    if native:
        from tools.skill_manager_tool import _validate_frontmatter
        from tools.skill_linter import lint_skill
        from agent.skill_utils import parse_frontmatter
        from tools.skills_guard import scan_skill
    for entry in entries:
        directory = ROOT / 'skills' / entry['name']
        md = directory / 'SKILL.md'
        if not md.exists():
            continue
        text = md.read_text()
        if not text.startswith('---\n') or '\n---\n' not in text[4:]:
            errors.append({'file': str(md.relative_to(ROOT)), 'rule': 'frontmatter'})
            continue
        head, content = text[4:].split('\n---\n', 1)
        try:
            name = re.search(r'^name: (.+)$', head, re.M).group(1)
            description = json.loads(re.search(r'^description: (.+)$', head, re.M).group(1))
            assert name == entry['name'] and re.fullmatch(r'[a-z0-9-]{1,64}',name)
            assert len(description) <= 60 and description.endswith('.')
        except Exception as ex:
            errors.append({'file': str(md.relative_to(ROOT)), 'rule': 'metadata', 'detail': str(ex)})
        for section in ('When to Use','Prerequisites','Procedure','Pitfalls','Verification'):
            if not re.search(r'^## ' + re.escape(section) + r'\b',content,re.M):
                errors.append({'file': str(md.relative_to(ROOT)), 'rule': 'section', 'missing': section})
        for f in sorted(directory.rglob('*')):
            if not f.is_file() or '__pycache__' in f.parts or f.suffix == '.pyc':
                continue
            files.append({'path': str(f.relative_to(ROOT)), 'sha256': digest(f), 'bytes': f.stat().st_size})
            if f.suffix not in ('.md','.tsv','.yaml','.json','.py','.sh','.ts','.mjs'):
                continue
            try:
                prose = f.read_text()
            except UnicodeDecodeError:
                continue
            # Explicitly labelled reference-only source is non-executable documentation.
            reference_only = '/upstream-helpers/' in str(f) or '/reference-only/' in str(f)
            if not reference_only:
                for match in re.finditer(r'\[[^\]]*\]\(([^)]+)\)',prose):
                    link = match.group(1).split('#')[0].split(' ')[0]
                    if not link or re.match(r'[a-z]+:',link) or link.startswith(('#','/')) or '<' in link or '$' in link:
                        continue
                    dest = (f.parent / link).resolve()
                    if not dest.exists():
                        errors.append({'file': str(f.relative_to(ROOT)), 'rule':'link', 'target':link})
                for match in re.finditer(r'(?<![\w-])pstack-(?:benny-)?[a-z][a-z0-9-]*',prose):
                    name = match.group(0)
                    # Brand/tool/path identifiers are not skill references.
                    if name in names or name in ('pstack-models','pstack-hermes','pstack-mode','pstack-audit','pstack-config'):
                        continue
                    if name.endswith('-') or name in ('pstack-setup','pstack-context'):
                        continue
                    warnings.append({'file':str(f.relative_to(ROOT)), 'rule':'identifier-review','token':name})
                for pattern in (r'/home/[A-Za-z0-9_.-]+/',r'~/.cursor/',r'claude-opus-5-5',r'gpt-5\.6-sol',r'grok-4\.7',r'\bTask\s*\('):
                    if re.search(pattern,prose):
                        errors.append({'file':str(f.relative_to(ROOT)), 'rule':'unresolved-runtime','pattern':pattern})
        if native:
            error = _validate_frontmatter(text, new_skill=True)
            if error:
                errors.append({'file':str(md.relative_to(ROOT)), 'rule':'hermes-frontmatter','detail':error})
            fm, _ = parse_frontmatter(text)
            related = fm.get('metadata',{}).get('hermes',{}).get('related_skills',[])
            for rel in related:
                if rel not in names:
                    # Existing Hermes skills are permitted only when they really resolve.
                    from tools.skills_tool import _locate_skill, _skill_search_dirs
                    pd,ad,_ = _skill_search_dirs()
                    err,_,_ = _locate_skill(rel,None,pd,ad)
                    if err:
                        errors.append({'file':str(md.relative_to(ROOT)), 'rule':'related-skill','target':rel})
            for finding in lint_skill(md):
                record={'file':str(md.relative_to(ROOT)), 'rule':finding.rule, 'detail':finding.message}
                (errors if finding.severity == 'error' else warnings).append(record)
            scan = scan_skill(directory, source='agent-created')
            if scan.verdict == 'dangerous':
                errors.append({'file':str(md.relative_to(ROOT)), 'rule':'security','findings':[vars(f) for f in scan.findings]})
            elif scan.findings:
                warnings.append({'file':str(md.relative_to(ROOT)), 'rule':'security-advisory','verdict':scan.verdict,'findings':[vars(f) for f in scan.findings]})
    result = {'success':not errors, 'expected_skills':len(names),'actual_skills':len(actual),
              'playbooks':len(list((ROOT/'skills/pstack-poteto-mode/references/playbooks').glob('*.md'))),
              'files':files,'errors':errors,'warnings':warnings,'native_validator':native}
    (ROOT/'reports').mkdir(exist_ok=True)
    (ROOT/'reports/validation.json').write_text(json.dumps(result,indent=2)+'\n')
    return result


def snapshot(home):
    skills=home/'skills'
    hashes={str(f.relative_to(home)):digest(f) for f in sorted(skills.rglob('*')) if f.is_file()}
    config=home/'config.yaml'
    return {'home':str(home),'files':hashes,'config_sha256':digest(config) if config.exists() else None}


def verify_artifacts(result):
    if not result['success'] or not result['native_validator']:
        raise ValueError('Native validation must pass before installation')
    # Reject additions as well as edits since the maintainer's native scan.
    actual={str(p.relative_to(ROOT)) for p in (ROOT/'skills').rglob('*')
            if p.is_file() and '__pycache__' not in p.parts and p.suffix != '.pyc'}
    expected={f['path'] for f in result['files']}
    if actual != expected:
        raise ValueError('Validated artifact set changed; regenerate the native-scanned package manifest')
    # Enforce exact artifact hashes, not a stale success bit.
    for f in result['files']:
        path=ROOT/f['path']
        if not path.is_file() or digest(path)!=f['sha256']:
            raise ValueError('Validated artifact changed: '+str(path))


def freeze_manifest():
    result=json.loads((ROOT/'reports/validation.json').read_text())
    verify_artifacts(result)
    manifest={'schema_version':1,'success':True,'native_validator':True,
              'revision':inventory()['revision'],'files':result['files']}
    (ROOT/'package-manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
    return {'manifest':'package-manifest.json','files':len(manifest['files'])}


def install(home):
    home=home.expanduser().resolve()
    # The caller chooses one explicit home; never modify sibling profiles.
    result=json.loads((ROOT/'package-manifest.json').read_text())
    verify_artifacts(result)
    category=home/'skills/software-development'
    names=[e['name'] for e in inventory()['skills']]
    collisions=[]
    for md in (home/'skills').rglob('SKILL.md'):
        if md.parent.name in names:
            collisions.append(str(md))
    if collisions:
        raise ValueError('Refusing existing skill collision: '+repr(collisions))
    for name in names:
        if (category/name).exists():
            raise ValueError('Refusing existing target: '+name)
    before=snapshot(home)
    category.mkdir(parents=True,exist_ok=True)
    installed=[]
    try:
        for name in names:
            src=ROOT/'skills'/name
            dest=category/name
            # Claim the destination exclusively before copying. A concurrent install
            # cannot be mistaken for our partial tree during rollback.
            dest.mkdir(exist_ok=False)
            installed.append(dest)
            shutil.copytree(src,dest,dirs_exist_ok=True,ignore=shutil.ignore_patterns("__pycache__","*.pyc"))
    except Exception:
        # Roll back only newly created package directories, never unrelated paths.
        for dest in reversed(installed):
            shutil.rmtree(dest)
        raise
    after=snapshot(home)
    unchanged=all(after['files'].get(p)==h for p,h in before['files'].items())
    config_unchanged=before['config_sha256']==after['config_sha256']
    verified=[]
    for record in result['files']:
        rel=Path(record['path']).relative_to('skills')
        target=category/rel
        if digest(target)!=record['sha256']:
            raise ValueError('Installed hash mismatch: '+str(target))
        verified.append(str(target))
    report={'home':str(home),'category':str(category),'installed_skills':len(installed),
            'installed_files':len(verified),'preexisting_files':len(before['files']),
            'preexisting_unchanged':unchanged,'config_unchanged':config_unchanged,
            'before':before,'targets':[str(d) for d in installed]}
    (ROOT/'reports').mkdir(exist_ok=True)
    (ROOT/'reports/install.json').write_text(json.dumps(report,indent=2)+'\n')
    if not unchanged or not config_unchanged:
        raise ValueError('Unrelated state changed during installation; inspect install report')
    return {k:v for k,v in report.items() if k not in ('before','targets')}


def main():
    p=argparse.ArgumentParser()
    p.add_argument('action',choices=('sync-runtime','validate','manifest','install'))
    p.add_argument('--native',action='store_true')
    p.add_argument('--write-manifest',action='store_true',help='Publish validated file hashes for portable offline installation; requires --native')
    p.add_argument('--home',default=os.environ.get('HERMES_HOME',str(Path.home()/'.hermes')))
    args=p.parse_args()
    if args.write_manifest and (args.action != 'validate' or not args.native):
        p.error('--write-manifest requires validate --native')
    if args.action=='sync-runtime': result=sync_runtime()
    elif args.action=='manifest': result=freeze_manifest()
    elif args.action=='validate':
        result=validate(native=args.native)
        if args.write_manifest and result['success']:
            freeze_manifest()
        result={k:v for k,v in result.items() if k!='files'}
    else: result=install(Path(args.home))
    print(json.dumps(result,indent=2))
    if result.get('success') is False: raise SystemExit(1)


if __name__=='__main__':main()
