# -*- coding: utf-8 -*-
# @Time    : 2017/7/14 11:39
# @Author  : Charles
# @File    : UnitBase.py
# @Software: PyCharm

import unittest
import FileController
import UserParam
import CaseGoto

class UnitBase(unittest.TestCase):


    def setUpClass(cls):
        cls.udatadic = {}
        cago = CaseGoto.case_goto()
        cls.usrconfig = cago[0]
        cls.configdatadic = cago[1]
        cls.case_lines_list = cago[2]
        cls.uspa = UserParam.param_generate()
        cls.udatadic.update(cls.case_lines_list)
        cls.udatadic.update(cls.uspa)










