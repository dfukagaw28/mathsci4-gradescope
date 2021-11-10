from decimal import Decimal
from itertools import permutations
import random
import re
import subprocess

import unittest
from gradescope_utils.autograder_utils.decorators import weight, number

FILENAME = 'hw06.py'

def N(x):
    if isinstance(x, str):
        return str(x) + '\n'
    if hasattr(x, '__iter__'):
        return ''.join(N(v) for v in x)
    return str(x) + '\n'

def random_float_str(a=0.0, b=1.0, prec=5):
    x = a + random.random() * (b - a)
    return f'{x:.{prec}f}'

def isFloat(s):
    try:
        float(s)
    except:
        return False
    return True

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

    def _check(self, sin, sout):
        x, eps = map(float, sin.split())
        self.assertTrue(isFloat(sout))
        ans = float(sout)
        err = abs(ans ** 3 - x)
        self.assertTrue(err < eps)

    def setUp(self):
        pass

    @weight(1)
    @number("1")
    def test_case1(self):
        """Case 1"""
        sinput = '27\n0.01\n'
        ret, sout, serr = self._subproc(FILENAME, sinput)
        self._check(sinput, sout)

    @weight(1)
    @number("2")
    def test_case2(self):
        """Case 2"""
        sinput = '0.125\n0.01\n'
        ret, sout, serr = self._subproc(FILENAME, sinput)
        self._check(sinput, sout)

    @weight(8)
    @number("3")
    def test_case3(self):
        """Case 3"""
        for k in range(1,11):
            x_str = random_float_str(-1e5, 1e5, 5)
            x = float(x_str)
            eps = 1e-9
            sinput = f'{x_str}\n{eps}\n'
            ret, sout, serr = self._subproc(FILENAME, sinput)
            self._check(sinput, sout)
