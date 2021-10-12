import re
import subprocess

import unittest
from gradescope_utils.autograder_utils.decorators import weight, number
#from hwXX import main
from config import filenames

class TestCondGreet(unittest.TestCase):
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
    @number("1.1")
    def test_1(self):
        """Ex03-1: Case 1"""
        ret, sout, serr = self._subproc('ex03_1.py', '13')
        expected = 'こんにちは\n'
        self.assertEqual(sout, expected)

    @weight(1)
    @number("1.2")
    def test_2(self):
        """Ex03-1: Morning"""
        for h in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]:
            ret, sout, serr = self._subproc('ex03_1.py', str(h))
            expected = 'おはようございます\n'
            self.assertEqual(sout, expected)

    @weight(1)
    @number("1.3")
    def test_3(self):
        """Ex03-1: Noon"""
        for h in [12]:
            ret, sout, serr = self._subproc('ex03_1.py', str(h))
            expected = 'お昼です\n'
            self.assertEqual(sout, expected)

    @weight(1)
    @number("1.4")
    def test_4(self):
        """Ex03-1: Afternoon"""
        for h in [13, 14, 15, 16, 17, 18]:
            ret, sout, serr = self._subproc('ex03_1.py', str(h))
            expected = 'こんにちは\n'
            self.assertEqual(sout, expected)

    @weight(1)
    @number("1.5")
    def test_5(self):
        """Ex03-1: Evening"""
        for h in [19, 20, 21, 22, 23]:
            ret, sout, serr = self._subproc('ex03_1.py', str(h))
            expected = 'こんばんは\n'
            self.assertEqual(sout, expected)

    @weight(1)
    @number("1.6")
    def test_6(self):
        """Ex03-1: Invalid"""
        for h in [-1, 24]:
            ret, sout, serr = self._subproc('ex03_1.py', str(h))
            expected = '範囲外です\n'
            self.assertEqual(sout, expected)
