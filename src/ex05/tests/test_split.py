import random
import re
import string
import subprocess

import unittest
from gradescope_utils.autograder_utils.decorators import weight, number
#from hwXX import main
from config import filenames

FILENAME = 'ex05_2.py'

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
    @number("2.1")
    def test_case1(self):
        """Ex05-2: Case 1"""
        sinput = 'apple,orange,banana\n'
        ret, sout, serr = self._subproc(FILENAME, sinput)
        expected = 'apple\norange\nbanana\n'
        self.assertEqual(sout, expected)

    @weight(1)
    @number("2.2")
    def test_case2(self):
        """Ex05-2: Case 2"""
        sinput = 'doshisha\n'
        ret, sout, serr = self._subproc(FILENAME, sinput)
        expected = 'doshisha\n'
        self.assertEqual(sout, expected)

    @weight(8)
    @number("2.3")
    def test_3(self):
        """Ex05-2: Case 3"""
        x = [random.randint(1,10) for _ in range(10)]
        x = [''.join([random.choice(string.ascii_letters) for _ in range(xj)]) for xj in x]
        for k in range(1, len(x) + 1):
            sinput = ','.join(x[:k]) + '\n'
            ret, sout, serr = self._subproc(FILENAME, sinput)
            #expected = sinput.translate(str.maketrans({',': '\n'}))
            expected = '\n'.join(x[:k]) + '\n'
            self.assertEqual(sout, expected)
