# -*- coding: utf-8 -*-
# @Time    : 2017/7/14 17:27
# @Author  : Charles
# @File    : test_CaseGoto.py
# @Software: PyCharm



import unittest
import CaseGoto


class Test_CaseGoto(unittest.TestCase):
    def test_case_goto(self):
        cc = CaseGoto.case_goto()
        print(cc[0])
        print(cc[1])
        print(cc[2])