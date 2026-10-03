"""Exercise the real bash entrypoint; no network or global config."""
from pathlib import Path
import subprocess
import tempfile
import unittest

ENTRY = Path(__file__).with_name('log.sh')
HEADER = 'ts\tphase\tdecision\twhy\tevidence\tresult'

class LogTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix='pstack-log-test-')
        self.addCleanup(self.temp.cleanup)
        self.path = Path(self.temp.name) / 'decisions.tsv'

    def invoke(self, *fields, path=None):
        return subprocess.run(['bash', str(ENTRY), str(path or self.path), *fields], text=True, capture_output=True)

    def test_whitespace_formula_is_escaped(self):
        result = self.invoke('phase', ' \t=SUM(1,2)', 'why', 'proof', 'done')
        self.assertEqual(result.returncode, 0, result.stderr)
        decision = self.path.read_text().splitlines()[1].split('\t')[2]
        self.assertTrue(decision.startswith("'"), decision)
        self.assertEqual(decision, "'  =SUM(1,2)")

    def test_plain_row_has_utc_timestamp_and_header(self):
        result = self.invoke('build', 'tested', 'reason', 'file:1', 'green')
        self.assertEqual(result.returncode, 0, result.stderr)
        rows = self.path.read_text().splitlines()
        self.assertEqual(rows[0], HEADER)
        self.assertRegex(rows[1], r'^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z\t')
        self.assertEqual(len(rows[1].split('\t')), 6)

    def test_append_preserves_prior_bytes(self):
        self.assertEqual(self.invoke('one', 'first', 'why', 'proof', 'done').returncode, 0)
        before = self.path.read_bytes()
        self.assertEqual(self.invoke('two', 'second', 'why', 'proof', 'done').returncode, 0)
        self.assertTrue(self.path.read_bytes().startswith(before))
        self.assertEqual(self.path.read_text().count(HEADER), 1)

    def test_formula_prefixes(self):
        for marker in '=+-@':
            self.assertEqual(self.invoke(marker, marker+'evil', marker+'why', marker+'proof', marker+'result').returncode, 0)
        for row in self.path.read_text().splitlines()[1:]:
            self.assertTrue(all(x.startswith("'") for x in row.split('\t')[1:]))

    def test_tabs_newlines_carriage_and_unicode(self):
        result = self.invoke('a\tb', 'c\nd', 'e\rf', 'g\v h\f', 'café')
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(self.path.read_text().splitlines()[1].split('\t')[1:], ['a b','c d','e f','g  h ','café'])

    def test_wrong_argument_count_does_not_create_log(self):
        result = self.invoke('only-one')
        self.assertNotEqual(result.returncode, 0)
        self.assertFalse(self.path.exists())
        self.assertIn('usage:', result.stderr)

    def test_malformed_header_is_not_modified(self):
        self.path.write_text('not the header\nexisting data\n')
        before = self.path.read_bytes()
        result = self.invoke('a', 'b', 'c', 'd', 'e')
        self.assertNotEqual(result.returncode, 0)
        self.assertEqual(self.path.read_bytes(), before)

    def test_symlink_target_is_not_modified(self):
        target = self.path.with_name('target.tsv')
        target.write_text(HEADER+'\n')
        self.path.symlink_to(target)
        before = target.read_bytes()
        result = self.invoke('a','b','c','d','e')
        self.assertNotEqual(result.returncode, 0)
        self.assertEqual(target.read_bytes(), before)

    def test_concurrent_append_has_one_header_and_all_rows(self):
        procs = [subprocess.Popen(['bash', str(ENTRY), str(self.path), 'parallel', str(i), 'why', 'proof', 'done'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True) for i in range(24)]
        for proc in procs:
            _, error = proc.communicate(timeout=15)
            self.assertEqual(proc.returncode, 0, error)
        lines = self.path.read_text().splitlines()
        self.assertEqual(lines.count(HEADER), 1)
        self.assertEqual(len(lines), 25)
        self.assertEqual({r.split('\t')[2] for r in lines[1:]}, {str(i) for i in range(24)})
        self.assertTrue(all(len(r.split('\t'))==6 for r in lines))

    def test_path_spaces_and_parent_creation(self):
        path = self.path.parent/'space dir'/'decision log.tsv'
        result = self.invoke('a','b','c','d','e', path=path)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(len(path.read_text().splitlines()), 2)

if __name__ == '__main__':
    unittest.main(verbosity=2)
