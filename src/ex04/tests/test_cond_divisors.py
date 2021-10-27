import random
import re
import subprocess
import time

import unittest
from gradescope_utils.autograder_utils.decorators import weight, number
from gradescope_utils.autograder_utils.decorators import leaderboard
#from hwXX import main
from config import filenames

FILENAME = 'ex04_2.py'

def N(x):
    if isinstance(x, str):
        return str(x) + '\n'
    if hasattr(x, '__iter__'):
        return ''.join(N(v) for v in x)
    return str(x) + '\n'

def ANS(n):
    count = 0
    for k in range(1, n+1):
        if n % k == 0:
            count += 1
    return N(count)


class TestLoopDivisors(unittest.TestCase):
    def _subproc(self, filename, input):
        p = subprocess.Popen(
            ['python3', filename],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        sout, serr = p.communicate(input=input.encode())
        self.assertEqual(serr.decode(), '')
        return p.returncode, sout.decode(), serr.decode()

    def setUp(self):
        pass

    @weight(1)
    @number("2.1")
    def test_1(self):
        """Ex04-2: Case 1"""
        sinput = '6\n'
        ret, sout, serr = self._subproc(FILENAME, sinput)
        expected = '4\n'
        self.assertEqual(sout, expected)

    @weight(1)
    @number("2.2")
    def test_2(self):
        """Ex04-2: Case 2"""
        sinput = '4\n'
        ret, sout, serr = self._subproc(FILENAME, sinput)
        expected = '3\n'
        self.assertEqual(sout, expected)

    @weight(1)
    @number("2.3")
    def test_3(self):
        """Ex04-2: Case 3"""
        sinput = '18751129\n'
        ret, sout, serr = self._subproc(FILENAME, sinput)
        expected = '2\n'
        self.assertEqual(sout, expected)

    @weight(1)
    @number("2.4")
    def test_4(self):
        """Ex04-2: Case 4"""
        sinput = '1\n'
        ret, sout, serr = self._subproc(FILENAME, sinput)
        expected = '1\n'
        self.assertEqual(sout, expected)

    @weight(1)
    @number("2.5")
    def test_5(self):
        """Ex04-2: Case 5"""
        x = 1 << 25
        y = 26
        ret, sout, serr = self._subproc(FILENAME, N(x))
        expected = N(y)
        self.assertEqual(sout, expected)

    @weight(1)
    @number("2.6")
    def test_6(self):
        """Ex04-2: Case 6"""
        x = 4567*4591
        y = 4
        ret, sout, serr = self._subproc(FILENAME, N(x))
        expected = N(y)
        self.assertEqual(sout, expected)

    @weight(1)
    @number("2.7")
    def test_7(self):
        """Ex04-2: Case 7"""
        x = 12345701
        y = 2
        ret, sout, serr = self._subproc(FILENAME, N(x))
        expected = N(y)
        self.assertEqual(sout, expected)
