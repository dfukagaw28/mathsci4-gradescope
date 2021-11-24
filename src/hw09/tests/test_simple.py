import math

import unittest
from gradescope_utils.autograder_utils.decorators import weight, number

from hw09 import Cylinder

def ANS(r, h):
    return r * r * math.pi * h

class TestSimple(unittest.TestCase):
    def setUp(self):
        pass

    @weight(7)
    @number("0")
    def test_case0(self):
        """Case 0a"""
        self.assertTrue(callable(Cylinder))
        self.assertTrue(isinstance(Cylinder, type))

    @weight(1)
    @number("1")
    def test_has_attributes(self):
        """Case 0b"""
        r, h = 123, 456
        a = Cylinder(r, h)
        self.assertTrue(hasattr(a, 'radius'))
        self.assertTrue(hasattr(a, 'height'))
        self.assertTrue(hasattr(a, 'volume'))
        self.assertEqual(a.radius, r)
        self.assertEqual(a.height, h)
        self.assertTrue(callable(a.volume))
        self.assertEqual(a.volume(), ANS(r, h))

    @weight(1)
    @number("2")
    def test_case1(self):
        """Case 1"""
        r, h = 3, 3
        a = Cylinder(r, h)
        self.assertEqual(a.radius, r)
        self.assertEqual(a.height, h)
        self.assertEqual(a.volume(), ANS(r, h))

    @weight(1)
    @number("3")
    def test_case2(self):
        """Case 2"""
        r, h = 10, 5
        a = Cylinder(r, h)
        self.assertEqual(a.radius, r)
        self.assertEqual(a.height, h)
        self.assertEqual(a.volume(), ANS(r, h))
