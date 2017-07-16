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
        udatadic = {}
        cago = CaseGoto.case_goto()
        udatadic.update(cago[2])
        uspa = UserParam.param_generate()
        udatadic.update(uspa)










