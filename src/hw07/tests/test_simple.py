from decimal import Decimal
from itertools import permutations
import random
import re
import subprocess

import unittest
from gradescope_utils.autograder_utils.decorators import weight, number

from hw07 import souwa

FILENAME = 'hw07.py'

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
    @number("0")
    def test_case0(self):
        """Case 0"""
        self.assertTrue(callable(souwa))

    @weight(3)
    @number("1")
    def test_case1(self):
        """Case 1"""
        self.assertEqual(souwa(10), 55)

    @weight(3)
    @number("2")
    def test_case2(self):
        """Case 2"""
        self.assertEqual(souwa(100), 5050)

    @weight(3)
    @number("3")
    def test_case3(self):
        """Case 3"""
        self.assertEqual(souwa(500), 125250)
