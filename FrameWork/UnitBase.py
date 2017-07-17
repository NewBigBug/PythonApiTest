# -*- coding: utf-8 -*-
# @Time    : 2017/7/14 11:39
# @Author  : Charles
# @File    : UnitBase.py
# @Software: PyCharm

import unittest
import requests

class UnitBase(unittest.TestCase):


    def setUpClass(cls):
        cls.api_client = requests.Session()











