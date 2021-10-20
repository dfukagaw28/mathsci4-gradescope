from itertools import permutations
import random
import re
import subprocess

import unittest
from gradescope_utils.autograder_utils.decorators import weight, number

def N(x):
    if isinstance(x, str):
        return str(x) + '\n'
    if hasattr(x, '__iter__'):
        return ''.join(N(v) for v in x)
    return str(x) + '\n'

def ANS(x):
    if x is not None and x > 0:
        return f'最も大きい奇数は {x} です。\n'
    else:
        return '奇数がありません。\n'

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
    @number("1")
    def test_1(self):
        """HW04: Case 1"""
        sinput = '15\n22\n23\n32\n30\n22\n4\n10\n38\n24\n'
        ret, sout, serr = self._subproc('hw04.py', sinput)
        expected = '最も大きい奇数は 23 です。\n'
        self.assertEqual(sout, expected)

    @weight(1)
    @number("2")
    def test_2(self):
        """HW04: Case 2"""
        sinput = '10\n20\n30\n40\n50\n60\n70\n80\n90\n100\n'
        ret, sout, serr = self._subproc('hw04.py', sinput)
        expected = '奇数がありません。\n'
        self.assertEqual(sout, expected)

    @weight(8)
    @number("3")
    def test_3(self):
        """HW04: Case 3"""
        for i in range(10):
            for j in range(10):
                if i != j:
                    x = [10,20,30,40,50,60,70,80,90,100]
                    random.shuffle(x)
                    x[i] = 33
                    x[j] = 55
                    sinput = N(x)
                    ret, sout, serr = self._subproc('hw04.py', sinput)
                    expected = ANS(55)
                    self.assertEqual(sout, expected)
