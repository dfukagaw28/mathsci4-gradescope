import datetime
from dateutil import tz
import os
from resource import getrusage, RUSAGE_CHILDREN
import subprocess

import unittest
from gradescope_utils.autograder_utils.decorators import leaderboard

from config import filenames

def N(x):
    if isinstance(x, str):
        return str(x) + '\n'
    if hasattr(x, '__iter__'):
        return ''.join(N(v) for v in x)
    return str(x) + '\n'

def get_clock():
    return getrusage(RUSAGE_CHILDREN).ru_utime

def get_clock2():
    return getrusage(RUSAGE_CHILDREN).ru_stime


class TestLeaderboard(unittest.TestCase):
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

    #@leaderboard("提出日時", "asc")
    #def test_leaderboard_submission_time(self, set_leaderboard_value=None):
    #    """Sets a leaderboard value"""
    #    JST = tz.gettz('Asia/Tokyo')
    #    value = datetime.datetime.now().timestamp()
    #    value = max([os.stat(fn).st_mtime for fn in filenames], default=value)
    #    value = datetime.datetime.fromtimestamp(value, tz=JST)
    #    value = value.strftime('%Y-%m-%d %H:%M:%S')
    #    set_leaderboard_value(value)

    @leaderboard("行数", "asc")
    def test_leaderboard_num_lines(self, set_leaderboard_value=None):
        """Sets a leaderboard value"""
        value = sum([len(open(fn).readlines()) for fn in filenames])
        set_leaderboard_value(value)

    @leaderboard("ファイルサイズ", "asc")
    def test_leaderboard_num_bytes(self, set_leaderboard_value=None):
        """Sets a leaderboard value"""
        value = sum([os.stat(fn).st_size for fn in filenames])
        set_leaderboard_value(value)

    #@leaderboard("実行時間（演習4-2）", "asc")
    #def test_leaderboard_exec_time(self, set_leaderboard_value=None):
    #    """Sets a leaderboard value"""
    #    pairs = [
    #        (1 << 25, 26),
    #        (4567*4591, 4),
    #        (14794688, 2),
    #    ]
    #    total_time = 0
    #    for x, y in pairs:
    #        start_time = get_clock()
    #        xxx = get_clock2()
    #        ret, sout, serr = self._subproc('ex04_2.py', N(x))
    #        total_time += get_clock() - start_time
    #        total_time += get_clock2() - xxx
    #    set_leaderboard_value(total_time)
