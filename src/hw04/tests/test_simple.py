from itertools import permutations
import random
import re
import subprocess

import unittest
from gradescope_utils.autograder_utils.decorators import weight, number

def N(x):
    if isinstance(x, str):
        return str(x) + '\n'
    if hasattr(x, '__iter__'):
        return ''.join(N(v) for v in x)
    return str(x) + '\n'

def ANS(x):
    if x is not None and x > 0:
        return f'最も大きい奇数は {x} です。\n'
    else:
        return '奇数がありません。\n'

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
    @number("1")
    def test_1(self):
        """HW03: Case 1"""
        sinput = '32\n25\n9\n'
        ret, sout, serr = self._subproc('hw03.py', sinput)
        expected = '最も大きい奇数は 25 です。\n'
        self.assertEqual(sout, expected)

    @weight(1)
    @number("2")
    def test_2(self):
        """HW03: Case 2"""
        sinput = '22\n44\n66\n'
        ret, sout, serr = self._subproc('hw03.py', sinput)
        expected = '奇数がありません。\n'
        self.assertEqual(sout, expected)

    @weight(1)
    @number("3")
    def test_3(self):
        """HW03: Case 3"""
        # すべて奇数で異なる
        for case in permutations([11,33,55]):
            sinput = N(case)
            ret, sout, serr = self._subproc('hw03.py', sinput)
            expected = ANS(55)
            self.assertEqual(sout, expected)

    @weight(1)
    @number("4")
    def test_4(self):
        """HW03: Case 4"""
        # 異なる奇数2と偶数1
        for lst in [[25,15,30], [35,15,20], [35,10,25]]:
            ans = lst[0]
            for case in permutations(lst):
                sinput = N(case)
                ret, sout, serr = self._subproc('hw03.py', sinput)
                expected = ANS(ans)
                self.assertEqual(sout, expected)

    @weight(1)
    @number("5")
    def test_5(self):
        """HW03: Case 5"""
        # 奇数1と異なる偶数2
        for lst in [[15,20,30], [25,10,30], [35,10,20]]:
            ans = lst[0]
            for case in permutations(lst):
                sinput = N(case)
                ret, sout, serr = self._subproc('hw03.py', sinput)
                expected = ANS(ans)
                self.assertEqual(sout, expected)

    @weight(1)
    @number("6")
    def test_6(self):
        """HW03: Case 6"""
        # 奇,奇=奇
        for lst in [[33,11,11], [55,55,33]]:
            ans = lst[0]
            for case in permutations(lst):
                sinput = N(case)
                ret, sout, serr = self._subproc('hw03.py', sinput)
                expected = ANS(ans)
                self.assertEqual(sout, expected)

    @weight(1)
    @number("7")
    def test_7(self):
        """HW03: Case 7"""
        # 奇,偶=偶
        for lst in [[22,22,33], [33,44,44]]:
            ans = 33
            for case in permutations(lst):
                sinput = N(case)
                ret, sout, serr = self._subproc('hw03.py', sinput)
                expected = ANS(ans)
                self.assertEqual(sout, expected)

    @weight(1)
    @number("8")
    def test_8(self):
        """HW03: Case 8"""
        # 奇=奇,偶
        for lst in [[33,22,33], [33,44,44]]:
            ans = 33
            for case in permutations(lst):
                sinput = N(case)
                ret, sout, serr = self._subproc('hw03.py', sinput)
                expected = ANS(ans)
                self.assertEqual(sout, expected)

    @weight(1)
    @number("9")
    def test_9(self):
        """HW03: Case 9"""
        # 奇=奇=奇
        sinput = N([33,33,33])
        ans = 33
        ret, sout, serr = self._subproc('hw03.py', sinput)
        expected = ANS(ans)
        self.assertEqual(sout, expected)

    @weight(1)
    @number("10")
    def test_10(self):
        """HW03: Case 10"""
        # 偶,偶,偶
        for lst in [[22,22,22], [22,44,44], [22,22,44]]:
            for case in permutations(lst):
                sinput = N(case)
                ret, sout, serr = self._subproc('hw03.py', sinput)
                expected = ANS(None)
                self.assertEqual(sout, expected)