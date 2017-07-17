# -*- coding: utf-8 -*-
# @Time    : 2017/7/17 15:00
# @Author  : Charles
# @File    : test_ResultGen.py
# @Software: PyCharm

import unittest
import ResultGenerate
class Test_RequestGen(unittest.TestCase):



    def test_write_result_to_excel(self):
        path='D:\GitPro\Python\PythonApiTest\output\\tempyaml.yaml'
        path2 = 'D:\GitPro\Python\PythonApiTest\TestCase\TestData\case.xlsx.case'
        ResultGenerate.write_result_to_excel(path2,path)
