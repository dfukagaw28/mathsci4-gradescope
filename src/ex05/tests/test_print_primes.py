import random
import re
import subprocess
import time

import unittest
from gradescope_utils.autograder_utils.decorators import weight, number
from gradescope_utils.autograder_utils.decorators import leaderboard
#from hwXX import main
from config import filenames

FILENAME = 'ex05_1.py'

def N(x):
    if isinstance(x, str):
        return str(x) + '\n'
    if hasattr(x, '__iter__'):
        return ''.join(N(v) for v in x)
    return str(x) + '\n'

def is_prime(n):
    for m in range(2, n):
        if n % m == 0:
            return False
    return True

def ANS(n):
    x = []
    for m in range(2,n+1):
        if is_prime(m):
            x.append(m)
    x = map(lambda a: str(a) + '\n', x)
    return ''.join(x)


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
    @number("1.1")
    def test_case1(self):
        """Ex05-1: Case 1"""
        sinput = '10\n'
        ret, sout, serr = self._subproc(FILENAME, sinput)
        expected = '2\n3\n5\n7\n'
        self.assertEqual(sout, expected)

    @weight(1)
    @number("1.2")
    def test_case2(self):
        """Ex05-1: Case 2"""
        sinput = '13\n'
        ret, sout, serr = self._subproc(FILENAME, sinput)
        expected = '2\n3\n5\n7\n11\n13\n'
        self.assertEqual(sout, expected)

    @weight(1)
    @number("1.3")
    def test_case3(self):
        """Ex05-1: Case 3"""
        sinput = '2\n'
        ret, sout, serr = self._subproc(FILENAME, sinput)
        expected = '2\n'
        self.assertEqual(sout, expected)

    @weight(7)
    @number("1.4")
    def test_case4(self):
        """Ex05-1: Case 4"""
        for _ in range(10):
            n = random.randint(2, 10000)
            sinput = f'{n}\n'
            ret, sout, serr = self._subproc(FILENAME, sinput)
            expected = ANS(n)
            self.assertEqual(sout, expected)
