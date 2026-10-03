"""Exercise installed pstack workflows in bounded, isolated live Hermes sessions."""
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

ROOT=Path(__file__).resolve().parents[1]

FIXTURES={
 'how': {'service.py': 'def lookup(ids, fetch):\n    return [fetch(key) for key in ids]\n',
         'routes.py': 'from service import lookup\n\ndef handle(payload, fetch):\n    return {"items": lookup(payload["ids"], fetch)}\n'},
 'architect': {'cache.py': 'class Cache:\n    def __init__(self):\n        self.values = {}\n\n    def get(self, key):\n        return self.values.get(key)\n'},
 'review': {'ranges.py': 'def contains(lower, upper, value):\n    """Return whether value belongs to [lower, upper)."""\n    return lower <= value <= upper\n'},
 'tdd': {'slug.py': 'import re\n\ndef slugify(text):\n    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")\n',
         'test_slug.py': 'import unittest\nfrom slug import slugify\n\nclass SlugTests(unittest.TestCase):\n    def test_ascii(self):\n        self.assertEqual(slugify("Hello, World!"), "hello-world")\n\nif __name__ == "__main__":\n    unittest.main()\n'},
}
PROMPTS={
 'how': ('pstack-how', 'Use pstack-how to explain routes.handle and service.lookup in this tiny fixture. Trace input, calls, outputs, fetch count for three IDs, and errors. This is read-only. Do not edit any fixture files or configure anything. Evidence must come from reading or exercising the actual code. Keep the report concise. If using reviewers, label actual same-model limitations.'),
 'architect': ('pstack-architect', 'Use pstack-architect to design TTL expiration for this cache. The data shape and public get/set contract must be clear. Compare at least two structurally distinct candidates. Stop at the design checkpoint: do not implement, change cache.py, publish or configure anything. Candidate design artifacts may be written only into subdirectories of this fixture or the Hermes scratch directory. State observed versus unknown model diversity.'),
 'review': ('pstack-interrogate', 'Use pstack-interrogate to review ranges.py read-only. The required contract is lower-inclusive and upper-exclusive, including when value equals upper. Verify the behavior with an executable check and produce the synthesized verdict. Do not fix the code, publish, configure or edit fixture files. Use an independent same-model panel if available, and label its lack of model-family diversity.'),
 'tdd': ('pstack-tdd', 'Use pstack-tdd to fix this reported bug in slugify: underscore is a valid identifier character and must be preserved, so slugify("Hello_World") must return "hello_world". Existing ASCII behavior must still pass. Write a focused regression test first, demonstrate it fails for the intended reason, then fix and run all local tests. Modify only slug.py and test_slug.py in this fixture. Do not commit, publish, or change configuration. Report the exact failing-before and passing-after commands/results.'),
}


def fingerprint(folder):
    return {p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in folder.glob('*.py')}


def run_case(case, parent, args):
    folder=parent/case
    folder.mkdir()
    for name,text in FIXTURES[case].items():
        (folder/name).write_text(text)
    skill,prompt=PROMPTS[case]
    query=folder/'query.txt'
    query.write_text(prompt+'\n')
    before=fingerprint(folder)
    cmd=['hermes','chat','--provider',args.provider,'--model',args.model,'--skills',skill,
         '--query-file',str(query),'--oneshot','--format','stream-json','--max-turns','30',
         '--run-budget',str(args.budget),'--in',str(folder),'--source','tool']
    start=time.monotonic()
    process=subprocess.Popen(cmd,stdout=subprocess.PIPE,stderr=subprocess.PIPE,text=True,start_new_session=True)
    timeout=False
    try:
        stdout,stderr=process.communicate(timeout=args.budget+90)
    except subprocess.TimeoutExpired:
        timeout=True
        os.killpg(process.pid,signal.SIGTERM)
        try:stdout,stderr=process.communicate(timeout=15)
        except subprocess.TimeoutExpired:
            os.killpg(process.pid,signal.SIGKILL)
            stdout,stderr=process.communicate()
    report_dir=ROOT/'reports/live'
    report_dir.mkdir(parents=True,exist_ok=True)
    stem=case if args.attempt=='initial' else case+'.'+args.attempt
    (report_dir/(stem+'.jsonl')).write_text(stdout)
    (report_dir/(stem+'.stderr.txt')).write_text(stderr)
    events=[]
    for line in stdout.splitlines():
        try:events.append(json.loads(line))
        except (ValueError,TypeError):pass
    after=fingerprint(folder)
    result={'case':case,'attempt':args.attempt,'skill':skill,'command':cmd,'fixture':str(folder),
            'returncode':process.returncode,'timeout':timeout,'seconds':round(time.monotonic()-start,2),
            'before':before,'after':after,'code_unchanged':before==after,
            'events':len(events),'stdout_path':str(report_dir/(stem+'.jsonl')),
            'stderr_path':str(report_dir/(stem+'.stderr.txt'))}
    if case=='tdd':
        # Independently exercise the final implementation, not just the agent's reported suite.
        check=subprocess.run(['python','-m','unittest','discover','-v'],cwd=folder,text=True,capture_output=True)
        direct=subprocess.run(['python','-c','from slug import slugify; assert slugify("Hello_World") == "hello_world"; assert slugify("Hello, World!") == "hello-world"; print("both observable contracts pass")'],cwd=folder,text=True,capture_output=True)
        result['independent_tests']={'returncode':check.returncode,'stdout':check.stdout,'stderr':check.stderr}
        result['independent_contract']={'returncode':direct.returncode,'stdout':direct.stdout,'stderr':direct.stderr}
    # Tool traces still need semantic review by the parent; success exit is not sufficient.
    (report_dir/(stem+'.result.json')).write_text(json.dumps(result,indent=2)+'\n')
    return result


def main():
    p=argparse.ArgumentParser()
    p.add_argument('--provider',required=True)
    p.add_argument('--model',required=True)
    p.add_argument('--budget',type=int,default=240)
    p.add_argument('--workers',type=int,default=2)
    p.add_argument('--attempt',default='initial')
    p.add_argument('--architect-inline',action='store_true',help='Exercise disclosed serial fallback within a small run budget')
    p.add_argument('--cases',nargs='+',choices=tuple(PROMPTS),default=list(PROMPTS))
    args=p.parse_args()
    if args.architect_inline:
        skill,prompt=PROMPTS['architect']
        PROMPTS['architect']=(skill,prompt+' For this bounded smoke test no delegation is authorized. Use the disclosed serial/inline fallback: produce two structurally distinct compact designs directly, judge and synthesize inline, explicitly note that no independent candidates or cross-judge ran in this attempt. Return a complete design checkpoint in at most 650 words with types, get/set semantics, base/grafts/rejections and proposed acceptance cases; no exhaustive discovery for this six-line fixture. Do not create extra documents beyond one optional design.md. Finish within the available run budget.')
    scratch=os.environ.get('TMPDIR')
    if not scratch:
        raise SystemExit('TMPDIR must point at the Hermes scratch directory')
    parent=Path(tempfile.mkdtemp(prefix='pstack-live-',dir=scratch))
    results=[]
    with concurrent.futures.ThreadPoolExecutor(args.workers) as pool:
        futures=[pool.submit(run_case,c,parent,args) for c in args.cases]
        for f in concurrent.futures.as_completed(futures):
            r=f.result();results.append(r);print(json.dumps(r),flush=True)
    summary_path=ROOT/'reports/live-summary.json'
    previous=json.loads(summary_path.read_text()).get('results',[]) if summary_path.exists() else []
    keys={(r['case'],r.get('attempt','initial')) for r in results}
    history=[r for r in previous if (r['case'],r.get('attempt','initial')) not in keys]
    summary={'provider':args.provider,'model':args.model,'fixture_root':str(parent),'results':history+results}
    summary_path.write_text(json.dumps(summary,indent=2)+'\n')
    if any(r['returncode'] or r['timeout'] for r in results):raise SystemExit(1)


if __name__=='__main__':main()
