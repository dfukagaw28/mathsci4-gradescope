import re
import subprocess

import unittest
from gradescope_utils.autograder_utils.decorators import weight, number
#from hw01 import main
from config import filenames

class TestSimple(unittest.TestCase):
    def _subproc(self, input):
        p = subprocess.Popen(
            ['python3', filenames[0]],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        sout, serr = p.communicate(input=input.encode())
        self.assertEqual(serr.decode(), '')
        return p.returncode, sout.decode(), serr.decode()

    def setUp(self):
        #self.calc = Calculator()
        #self.output = main()
        ret, sout, serr = self._subproc('1.41')
        self.output = sout

    @weight(1)
    @number("1.1")
    def test_abc(self):
        """Evaluate 演習1-1"""
        regex = re.compile('^aaa\nbbb\nccc$', re.M)
        self.assertRegex(self.output, regex)

    @weight(1)
    @number("1.2")
    def test_abc2(self):
        """Evaluate 演習1-2"""
        regex = re.compile('.*^aaabbb\nccc$.*', re.M)
        self.assertRegex(self.output, regex)

    @weight(1)
    @number("1.3")
    def test_escape_quotations(self):
        """Evaluate 演習1-3"""
        regex = re.compile('^Tom said "I don\'t know"\\.$', re.M)
        self.assertRegex(self.output, regex)

    @weight(1)
    @number("1.4")
    def test_square_root(self):
        """Evaluate 演習1-4"""

        ret, sout, serr = self._subproc('1.4')
        regex = re.compile('-0.04000000000000026$', re.M)
        self.assertRegex(sout, regex)

        ret, sout, serr = self._subproc('1.5')
        regex = re.compile('0.25$', re.M)
        self.assertRegex(sout, regex)

    @weight(1)
    @number("All")
    def test_all(self):
        """Evaluate All"""

        def f(x):
            return f"""\
aaa
bbb
ccc
aaabbb
ccc
Tom said "I don't know".
.*{x*x-2}
"""

        x = 1.41
        ret, sout, serr = self._subproc(str(x))
        regex = re.compile(f(x), re.M)
        self.assertRegex(sout, regex)
