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
    @leaderboard("実行時間（演習4-2）", "asc")
    def test_5(self):
        """Ex04-2: Case 5"""
        pairs = [
            (1 << 25, 26),
            (4567*4591, 4),
            (14794688, 2),
        ]
        total_time = 0
        for x, y in pairs:
            start_time = time.time()
            ret, sout, serr = self._subproc(FILENAME, N(x))
            total_time += time.time() - start
            expected = N(y)
            self.assertEqual(sout, expected)
        set_leaderboard_value(total_time)
