import numpy as np

import unittest
from gradescope_utils.autograder_utils.decorators import weight, number

import hw13

class TestSimple(unittest.TestCase):
    def setUp(self):
        pass

    @weight(5)
    @number("0")
    def test_case0(self):
        """Case 0"""
        self.assertIn('solve', dir(hw13), f'solve が見つかりません')
        self.assertTrue(callable(hw13.solve), f'solve は関数でなければなりません')

    @weight(5)
    @number("1")
    def test_case1(self):
        """P-001"""
        x = hw13.solve()
        self.assertIsInstance(x, np.ndarray)
        self.assertEqual(x.shape, (2,))
        self.assertEqual(x.dtype, np.float64)
        self.assertAlmostEqual(x[0], 1, places=10)
        self.assertAlmostEqual(x[1], 1, places=10)
