import datetime
from dateutil import tz
import os

import numpy as np

import unittest
from gradescope_utils.autograder_utils.decorators import leaderboard

from config import filenames

import hw13

class TestLeaderboard(unittest.TestCase):
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

    @leaderboard("誤差", "asc")
    def test_leaderboard_eps(self, set_leaderboard_value=None):
        """Sets a leaderboard value"""
        eps = 1e10
        try:
            x = hw13.solve()
            y = x - np.array([1,1], dtype=float)
            eps = np.linalg.norm(y)
        except:
            pass
        set_leaderboard_value(eps)
