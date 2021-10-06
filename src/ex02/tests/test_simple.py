import re
import subprocess

import unittest
from gradescope_utils.autograder_utils.decorators import weight, number
#from hwXX import main
from config import filenames

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

    def setUp(self):
        pass

    @weight(1)
    @number("2.1")
    def test_four_fours_make_zero_to_nine(self):
        """Evaluate 演習2-1"""
        ret, sout, serr = self._subproc('ex02_1.py', '')
        expected = ''.join(map(lambda x: str(x) + '\n', range(10)))
        self.assertEqual(sout, expected)

    @weight(1)
    @number("2.2")
    def test_four_fours_make_ten(self):
        """Evaluate 演習2-2"""
        ret, sout, serr = self._subproc('ex02_2.py', '')
        expected = '10\n'
        self.assertEqual(sout, expected)
