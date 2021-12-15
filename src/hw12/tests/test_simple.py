import math

import unittest
from gradescope_utils.autograder_utils.decorators import weight, number

from myawesomemodule import factorial

class TestSimple(unittest.TestCase):
    def setUp(self):
        pass

    @weight(5)
    @number("0")
    def test_case0(self):
        """Case 0"""
        self.assertTrue(callable(factorial))

    @weight(1)
    @number("1")
    def test_case1(self):
        """Case 1"""
        self.assertEqual(factorial(5), 120)

    @weight(1)
    @number("2")
    def test_case2(self):
        """Case 2"""
        self.assertEqual(factorial(1), 1)

    @weight(1)
    @number("3")
    def test_case3(self):
        """Case 3"""
        self.assertEqual(factorial(0), 1)

    @weight(1)
    @number("4")
    def test_case4(self):
        """Case 4"""
        self.assertEqual(factorial(10), 3628800)

    @weight(1)
    @number("5")
    def test_case5(self):
        """Case 5"""
        self.assertEqual(factorial(100), 93326215443944152681699238856266700490715968264381621468592963895217599993229915608941463976156518286253697920827223758251185210916864000000000000000000000000)
