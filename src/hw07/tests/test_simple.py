from decimal import Decimal
from itertools import permutations
import random
import re
import subprocess

import unittest
from gradescope_utils.autograder_utils.decorators import weight, number

from hw07 import souwa

class TestSimple(unittest.TestCase):
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
