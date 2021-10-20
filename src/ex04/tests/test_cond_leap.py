import random
import re
import subprocess

import unittest
from gradescope_utils.autograder_utils.decorators import weight, number
#from hwXX import main
from config import filenames

class TestCondLeap(unittest.TestCase):
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
    @number("2.1")
    def test_1(self):
        """Ex03-2: Case 1"""
        ret, sout, serr = self._subproc('ex03_2.py', '2021')
        expected = 'No\n'
        self.assertEqual(sout, expected)

    @weight(1)
    @number("2.2")
    def test_2(self):
        """Ex03-2: Case 2"""
        ret, sout, serr = self._subproc('ex03_2.py', '2024')
        expected = 'Yes\n'
        self.assertEqual(sout, expected)

    @weight(1)
    @number("2.3")
    def test_3(self):
        """Ex03-2: Case 3"""
        ret, sout, serr = self._subproc('ex03_2.py', '1900')
        expected = 'No\n'
        self.assertEqual(sout, expected)

    @weight(1)
    @number("2.4")
    def test_4(self):
        """Ex03-2: Case 4"""
        ret, sout, serr = self._subproc('ex03_2.py', '2000')
        expected = 'Yes\n'
        self.assertEqual(sout, expected)

    @weight(1)
    @number("2.5")
    def test_5(self):
        """Ex03-2: Case 5"""
        for _ in range(20):
            y = random.randint(1, 3000)
            ret, sout, serr = self._subproc('ex03_2.py', str(y))
            if y % 400 == 0:
                expected = 'Yes\n'
            elif y % 100 == 0:
                expected = 'No\n'
            elif y % 4 == 0:
                expected = 'Yes\n'
            else:
                expected = 'No\n'
            self.assertEqual(sout, expected)
