import re
import subprocess

import unittest
from gradescope_utils.autograder_utils.decorators import weight, number
#from hwXX import main
from config import filenames

class TestSimple(unittest.TestCase):
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
    @number("example1")
    def test_example1(self):
        """Evaluate 入力例1"""
        ret, sout, serr = self._subproc('hw02.py', '7\n2\n')
        expected = '''\
7 + 2 = 9
7 - 2 = 5
7 * 2 = 14
7 // 2 = 3
7 / 2 = 3.5
7 % 2 = 1
7 ** 2 = 49
'''
        self.assertEqual(sout, expected)

    @weight(1)
    @number("example2")
    def test_example2(self):
        """Evaluate 入力例1"""
        ret, sout, serr = self._subproc('hw02.py', '12\n34\n')
        expected = '''\
12 + 34 = 46
12 - 34 = -22
12 * 34 = 408
12 // 34 = 0
12 / 34 = 0.35294117647058826
12 % 34 = 12
12 ** 34 = 4922235242952026704037113243122008064
'''
        self.assertEqual(sout, expected)

    @weight(1)
    @number("example2")
    def test_example2(self):
        """Evaluate 入力例1"""
        ret, sout, serr = self._subproc('hw02.py', '0\n2\n')
        expected = '''\
0 + 2 = 2
0 - 2 = -2
0 * 2 = 0
0 // 2 = 0
0 / 2 = 0.0
0 % 2 = 0
0 ** 2 = 0
'''
        self.assertEqual(sout, expected)
