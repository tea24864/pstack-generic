"""Run portable package/helper checks; installed-state audit is opt-in."""
from pathlib import Path
import argparse
import hashlib
import json
import re
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]


def installed_check(validation):
    path = ROOT / 'reports/install.json'
    if not path.exists():
        raise ValueError('No local install report; install into a selected home first')
    install = json.loads(path.read_text())
    home, category = Path(install['home']), Path(install['category'])
    compared = []
    for record in validation['files']:
        target = category / Path(record['path']).relative_to('skills')
        if not target.is_file() or hashlib.sha256(target.read_bytes()).hexdigest() != record['sha256']:
            raise ValueError('Installed content differs from package: ' + str(target))
        compared.append(str(target))
    changed, telemetry = [], []
    for rel, digest in install['before']['files'].items():
        p = home / rel
        if not p.is_file() or hashlib.sha256(p.read_bytes()).hexdigest() != digest:
            (telemetry if Path(rel).name in ('.usage.json', '.curator_ledger.jsonl') else changed).append(rel)
    config = home / 'config.yaml'
    config_hash = hashlib.sha256(config.read_bytes()).hexdigest() if config.exists() else None
    unchanged = config_hash == install['before']['config_sha256']
    return {'success': not changed and unchanged,
            'installed_files_matching_latest_package': len(compared),
            'existing_skill_content_unchanged': not changed,
            'existing_content_changes': changed, 'config_unchanged': unchanged,
            'expected_usage_telemetry_updated': telemetry}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--installed', action='store_true', help='Also check the explicitly recorded local installation')
    args = parser.parse_args()
    checks = [
        ['hermes', '--run-module', 'unittest', 'discover', '-s', str(ROOT / 'tests'), '-p', 'test_*.py', '-v'],
        [sys.executable, '-B', str(ROOT / 'skills/pstack-poteto-mode/scripts/test-helpers.py')],
        [sys.executable, '-B', str(ROOT / 'skills/pstack-show-me-your-work/scripts/test_log.py')],
        ['node', '--check', str(ROOT / 'skills/pstack-poteto-mode/scripts/check-plan.mjs')],
        ['bash', '-n', str(ROOT / 'skills/pstack-poteto-mode/scripts/worktree-audit.sh')],
        ['bash', '-n', str(ROOT / 'skills/pstack-show-me-your-work/scripts/log.sh')],
    ]
    results = []
    for command in checks:
        r = subprocess.run(command, cwd=ROOT, capture_output=True, text=True, timeout=120)
        count = re.search(r'Ran (\d+) tests? in', r.stderr + r.stdout)
        record = {'command': command, 'returncode': r.returncode,
                  'tests': int(count.group(1)) if count else 0, 'stdout': r.stdout, 'stderr': r.stderr}
        results.append(record)
        print(json.dumps({k: v for k, v in record.items() if k not in ('stdout', 'stderr')}), flush=True)
    validation = json.loads((ROOT / 'reports/validation.json').read_text())
    installed = installed_check(validation) if args.installed else None
    out = {'success': all(r['returncode'] == 0 for r in results) and validation['success'] and (installed is None or installed['success']),
           'tests_passed': sum(r['tests'] for r in results if r['returncode'] == 0),
           'checks': results, 'installed_check': installed,
           'security_summary': {'validation_errors': len(validation['errors']), 'advisories': validation['warnings']},
           'live_checks': 'Run separately with explicit provider/model; not inferred from automated tests.'}
    (ROOT / 'reports').mkdir(exist_ok=True)
    (ROOT / 'reports/verification.json').write_text(json.dumps(out, indent=2) + '\n')
    print(json.dumps({k: v for k, v in out.items() if k not in ('checks', 'security_summary')}, indent=2))
    if not out['success']:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
