import re
import subprocess

import unittest
from gradescope_utils.autograder_utils.decorators import weight, number
#from hwXX import main
from config import filenames

FILENAME = 'ex04_1.py'

def N(x):
    if isinstance(x, str):
        return str(x) + '\n'
    if hasattr(x, '__iter__'):
        return ''.join(N(v) for v in x)
    return str(x) + '\n'

def ANS(n):
    ans = ''
    for k in range(1, n+1):
        ans += '#' * k + '\n'
    return ans


class TestLoopTriangle(unittest.TestCase):
    def _subproc(self, filename, sinput):
        p = subprocess.Popen(
            ['python3', filename],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        sout, serr = p.communicate(input=sinput.encode())
        self.assertEqual(serr.decode(), '')
        return p.returncode, sout.decode(), serr.decode()

    def setUp(self):
        pass

    @weight(1)
    @number("1.1")
    def test_1(self):
        """Ex04-1: Case 1"""
        n = 3
        ret, sout, serr = self._subproc(FILENAME, sinput=N(n))
        expected = ANS(n)
        self.assertEqual(sout, expected)

    @weight(1)
    @number("1.2")
    def test_2(self):
        """Ex04-1: Case 2"""
        n = 5
        ret, sout, serr = self._subproc(FILENAME, sinput=N(n))
        expected = ANS(n)
        self.assertEqual(sout, expected)

    @weight(1)
    @number("1.3")
    def test_3(self):
        """Ex04-1: Case 3"""
        n = 10
        ret, sout, serr = self._subproc(FILENAME, sinput=N(n))
        expected = ANS(n)
        self.assertEqual(sout, expected)
