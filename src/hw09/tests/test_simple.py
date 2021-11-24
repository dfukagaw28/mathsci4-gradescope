from decimal import Decimal
from itertools import permutations
import random
import re
import subprocess

import unittest
from gradescope_utils.autograder_utils.decorators import weight, number

from hw08 import sum_digits

class TestSimple(unittest.TestCase):
    def setUp(self):
        pass

    @weight(2)
    @number("0")
    def test_case0(self):
        """Case 0"""
        self.assertTrue(callable(sum_digits))

    @weight(2)
    @number("1")
    def test_case1(self):
        """Case 1"""
        self.assertEqual(sum_digits('54321'), 15)

    @weight(2)
    @number("2")
    def test_case2(self):
        """Case 2"""
        self.assertEqual(sum_digits('a2b3c'), 5)

    @weight(2)
    @number("3")
    def test_case3(self):
        """Case 3"""
        with self.assertRaises(ValueError):
            sum_digits('hello')

    @weight(2)
    @number("4")
    def test_case4(self):
        """Case 4"""
        with self.assertRaises(TypeError):
            sum_digits(54321)
