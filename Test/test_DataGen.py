# -*- coding: utf-8 -*-
# @Time    : 2017/7/13 17:32
# @Author  : Charles
# @File    : test_DataGen.py
# @Software: PyCharm


import unittest
import DataGenerate


class Test_DataGen(unittest.TestCase):
    def test_data_generate(self):
        datadic={
            'name': '$name',
            'password': '$password',
            'pm1': '$child',
            'pm2': '23423',
            'pm3': {'k1':{'k2':{'k3':{'k4':'$k4'}}}}
        }



        udatadic={
            '$name':'n123456',
            '$password':'p123456',
            '$child':'c123456',
            '$k4':'k3_123456'
        }

        cc=DataGenerate.data_generate(datadic,udatadic)
        print(cc)


