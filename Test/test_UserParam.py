# -*- coding: utf-8 -*-
# @Time    : 2017/7/14 15:27
# @Author  : Charles
# @File    : test_UserParam.py
# @Software: PyCharm


import unittest
import UserParam
import DataGenerate


class Test_UsrPara(unittest.TestCase):
    """
    def test_sign_generate(self):

        datadic={
            'name': '$name',
            'password': '$password',
            'pm1': '$child',
            'pm2': '23423',
            'pm3': {'k1':{'k2':{'k3':{'k4':'$k4'}}}}
        }

        secret='fsafdsfr345525'

        cc=UserParam.sign_generate(datadic, secret)
        print(cc)
    """
    def test_01(self):

        up = UserParam.param_generate()

        datadic = {'Request_Body': {
            'name': '$tm',
            'password': '$tm'
        }
        }

        cc = DataGenerate.data_generate(datadic, up)
        print(cc)