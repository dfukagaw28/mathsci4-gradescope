import math

import pandas as pd

import unittest
from gradescope_utils.autograder_utils.decorators import weight, number

import hw12

COLUMNS_1 = (
    'sales_ymd',
    'sales_epoch',
    'store_cd',
    'receipt_no',
    'receipt_sub_no',
    'customer_id',
    'product_cd',
    'quantity',
    'amount',
)

class TestSimple(unittest.TestCase):
    def setUp(self):
        self.df_receipt = hw12.load_csv('receipt')

    @weight(5)
    @number("0")
    def test_case0(self):
        """Case 0"""
        for i in range(1, 6):
            name = 'P%03d' % i
            self.assertIn(name, dir(hw12), f'{name}が見つかりません')
            self.assertTrue(callable(hw12.__dict__[name]), f'{name}は関数でなければなりません')

    @weight(1)
    @number("1")
    def test_case1(self):
        """P-001"""
        df = hw12.P001(self.df_receipt)
        self.assertIsInstance(df, pd.core.frame.DataFrame)
        self.assertEqual(len(df), 10)
        self.assertEqual(tuple(df.columns), COLUMNS_1)

    @weight(1)
    @number("2")
    def test_case2(self):
        """P-002"""
        COLUMNS = ('sales_ymd', 'customer_id', 'product_cd', 'amount')
        df = hw12.P002(self.df_receipt)
        self.assertIsInstance(df, pd.core.frame.DataFrame)
        self.assertEqual(len(df), 10)
        self.assertEqual(tuple(df.columns), COLUMNS)

    @weight(1)
    @number("3")
    def test_case3(self):
        """P-003"""
        COLUMNS = ('sales_date', 'customer_id', 'product_cd', 'amount')
        df = hw12.P003(self.df_receipt)
        self.assertIsInstance(df, pd.core.frame.DataFrame)
        self.assertEqual(len(df), 10)
        self.assertEqual(tuple(df.columns), COLUMNS)

    @weight(1)
    @number("4")
    def test_case4(self):
        """P-004"""
        COLUMNS = ('sales_ymd', 'customer_id', 'product_cd', 'amount')
        INDEX = (
            36, 9843, 21110, 27673, 27840, 28757,
            39256, 58121, 68117, 72254, 88508, 91525
        )
        df = hw12.P004(self.df_receipt)
        self.assertIsInstance(df, pd.core.frame.DataFrame)
        self.assertEqual(len(df), len(INDEX))
        self.assertEqual(tuple(df.columns), COLUMNS)
        self.assertEqual(tuple(df.index), INDEX)

    @weight(1)
    @number("5")
    def test_case5(self):
        """P-005"""
        COLUMNS = ('sales_ymd', 'customer_id', 'product_cd', 'amount')
        INDEX = (36, 68117, 72254)
        df = hw12.P005(self.df_receipt)
        self.assertIsInstance(df, pd.core.frame.DataFrame)
        self.assertEqual(len(df), len(INDEX))
        self.assertEqual(tuple(df.columns), COLUMNS)
        self.assertEqual(tuple(df.index), INDEX)
