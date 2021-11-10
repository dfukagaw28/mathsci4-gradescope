import unittest
from gradescope_utils.autograder_utils.decorators import weight, number

from ex07_2 import tarai

class TestSimple(unittest.TestCase):
    def setUp(self):
        pass

    @weight(1)
    @number("0")
    def test_case0(self):
        """Case 0"""
        self.assertTrue(callable(tarai))

    @weight(3)
    @number("1")
    def test_case1(self):
        """Case 1"""
        self.assertEqual(tarai(2,1,0), 2)

    @weight(3)
    @number("2")
    def test_case2(self):
        """Case 2"""
        self.assertEqual(tarai(8,4,0), 8)

    @weight(3)
    @number("3")
    def test_case3(self):
        """Case 3"""
        self.assertEqual(tarai(12,6,0), 12)
