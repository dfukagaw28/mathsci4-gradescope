from decimal import Decimal
from itertools import permutations
import random
import re
import subprocess

import unittest
from gradescope_utils.autograder_utils.decorators import weight, number

FILENAME = 'hw05.py'

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

def random_float_str(a=0.0, b=1.0, prec=5):
    x = a + random.random() * (b - a)
    return f'{x:.{prec}f}'

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
    def test_case1(self):
        """Case 1"""
        sinput = '1.23,2.4,3.123\n'
        ret, sout, serr = self._subproc(FILENAME, sinput)
        expected = '6.753\n'
        self.assertEqual(sout, expected)

    @weight(1)
    @number("2")
    def test_case2(self):
        """Case 2"""
        sinput = '0.2,0.2,0.3\n'
        ret, sout, serr = self._subproc(FILENAME, sinput)
        expected = '0.7\n'
        self.assertEqual(sout, expected)

    #@weight(0)
    #@number("3")
    #def test_case3(self):
    #    """Case 3"""
    #    sinput = '0.2,0.2,0.2\n'
    #    ret, sout, serr = self._subproc(FILENAME, sinput)
    #    expected = '0.6\n'
    #    self.assertEqual(sout, expected)

    @weight(8)
    @number("4")
    def test_case4(self):
        """Case 4"""
        for k in range(1,11):
            x = [random_float_str(0, 10, 5) for _ in range(k)]
            y = [Decimal(xj) for xj in x]
            s = ','.join(x)
            sinput = s + '\n'
            ret, sout, serr = self._subproc(FILENAME, sinput)
            sout = Decimal(sout)
            expected = sum(y)
            self.assertTrue(abs(sout - expected) < 1e-10)
