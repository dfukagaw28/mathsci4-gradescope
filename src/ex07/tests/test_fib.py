import unittest
from gradescope_utils.autograder_utils.decorators import weight, number

from ex07_1 import fib

class TestSimple(unittest.TestCase):
    def setUp(self):
        pass

    @weight(1)
    @number("0")
    def test_case0(self):
        """Case 0"""
        self.assertTrue(callable(fib))

    @weight(3)
    @number("1")
    def test_case1(self):
        """Case 1"""
        self.assertEqual(fib(10), 55)

    @weight(3)
    @number("2")
    def test_case2(self):
        """Case 2"""
        self.assertEqual(fib(20), 6765)

    @weight(3)
    @number("3")
    def test_case3(self):
        """Case 3"""
        self.assertEqual(fib(30), 832040)
