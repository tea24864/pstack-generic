"""Fresh-session behavior probes using generated files, not the live installation.

Inputs are embedded verbatim, supporting files remain directly readable. Native
catalog loading is verified separately in test_port. This is not proof of
another product's support for the generic baseline.
"""
from pathlib import Path
import argparse
import concurrent.futures
import hashlib
import json
import os
import signal
import subprocess
import tempfile
import time
from live_smoke import FIXTURES, PROMPTS, fingerprint
from specialize import verify_distribution

ROOT = Path(__file__).resolve().parents[1]


def run_case(case, root, args):
    folder = root / case
    folder.mkdir()
    for name, text in FIXTURES[case].items():
        (folder / name).write_text(text)
    name, request = PROMPTS[case]
    if case == 'architect':
        request += ' For this six-line fixture, return a complete compact design checkpoint in at most 650 words: grounding, caller usage/types, two structurally distinct designs, rubric comparison, base/grafts/rejections and proposed acceptance cases. Keep candidates and synthesis inline; do not write exhaustive supporting reports. Read only directly relevant references, reserve time for synthesis and finish within the run budget.'
    source = args.distribution.resolve() / 'skills' / name
    text = (source / 'SKILL.md').read_text()
    query = folder / 'query.txt'
    preface = f'This is a bounded verification fixture for a generated, not yet installed skill. The exact selected SKILL.md is embedded below. Its supporting paths resolve beneath {source}. Use actual native file/shell operations on those references, not same-named skills from the live profile. Do not install, configure, publish, activate automation or modify this skill distribution. Report exact tool evidence.\n'
    if args.runtime == 'generic':
        preface += 'This run deliberately exposes file/shell capabilities only. No delegation is available or authorized: finish distinct perspectives and synthesis in this session, disclose no independent children/cross-judge, and do not spawn another process or simulate an absent API.\n'
    query.write_text(preface + '\nREQUEST\n' + request + '\nSELECTED GENERATED SKILL\n' + text)
    before = fingerprint(folder)
    command = ['hermes', 'chat', '--provider', args.provider, '--model', args.model,
               '--query-file', str(query), '--oneshot', '--format', 'stream-json',
               '--ignore-rules', '--ignore-user-config', '--toolsets', 'file,terminal',
               '--max-turns', '24', '--run-budget', str(args.budget), '--in', str(folder), '--source', 'tool']
    start = time.monotonic()
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, start_new_session=True)
    timeout = False
    try:
        stdout, stderr = process.communicate(timeout=args.budget + 60)
    except subprocess.TimeoutExpired:
        timeout = True
        os.killpg(process.pid, signal.SIGTERM)
        try:
            stdout, stderr = process.communicate(timeout=15)
        except subprocess.TimeoutExpired:
            os.killpg(process.pid, signal.SIGKILL)
            stdout, stderr = process.communicate()
    reports = ROOT / 'reports/specialized-live'
    reports.mkdir(parents=True, exist_ok=True)
    stem = args.runtime + '-' + case + '-' + args.attempt
    (reports / (stem + '.jsonl')).write_text(stdout)
    (reports / (stem + '.stderr.txt')).write_text(stderr)
    result = {'runtime': args.runtime, 'case': case, 'attempt': args.attempt, 'returncode': process.returncode,
              'timeout': timeout, 'seconds': round(time.monotonic() - start, 2), 'fixture': str(folder),
              'skill_sha256': hashlib.sha256(text.encode()).hexdigest(), 'before': before,
              'after': fingerprint(folder), 'code_unchanged': before == fingerprint(folder),
              'stdout_path': str(reports / (stem + '.jsonl')), 'command': command}
    if case == 'tdd':
        for key, cmd in [('independent_tests', ['python3', '-B', '-m', 'unittest', 'discover', '-v']),
                         ('independent_contract', ['python3', '-B', '-c', 'from slug import slugify; assert slugify("Hello_World") == "hello_world"; assert slugify("Hello, World!") == "hello-world"; print("both observable contracts pass")'])]:
            checked = subprocess.run(cmd, cwd=folder, capture_output=True, text=True)
            result[key] = {'returncode': checked.returncode, 'stdout': checked.stdout, 'stderr': checked.stderr}
    (reports / (stem + '.result.json')).write_text(json.dumps(result, indent=2) + '\n')
    return result


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--distribution', type=Path, required=True)
    p.add_argument('--provider', required=True)
    p.add_argument('--model', required=True)
    p.add_argument('--budget', type=int, default=180)
    p.add_argument('--attempt', required=True, help='Distinct label; old evidence must not be overwritten')
    p.add_argument('--cases', nargs='+', choices=tuple(FIXTURES), required=True)
    args = p.parse_args()
    args.runtime = verify_distribution(args.distribution)['runtime']
    if not args.attempt.replace('-', '').replace('_', '').isalnum():
        p.error('Use a plain attempt label')
    reports = ROOT / 'reports/specialized-live'
    if any((reports / f'{args.runtime}-{case}-{args.attempt}.result.json').exists() for case in args.cases):
        p.error('Attempt already recorded; use a new label')
    root = Path(tempfile.mkdtemp(prefix='pstack-specialized-live-', dir=os.environ['TMPDIR']))
    with concurrent.futures.ThreadPoolExecutor(max_workers=len(args.cases)) as pool:
        results = list(pool.map(lambda case: run_case(case, root, args), args.cases))
    print(json.dumps(results, indent=2))
    if any(row['returncode'] or row['timeout'] for row in results):
        raise SystemExit(1)


if __name__ == '__main__':
    main()
