# -*- coding: utf-8 -*-
# @Time    : 2017/7/12 13:51
# @Author  : Charles
# @File    : test_FileController.py
from unittest import TestCase
import FileController

# @Software: PyCharm
class TestLoad_case_by_path(TestCase):

    def test_load_testcases_by_path_file_yaml(self):

        path = '..\TestCase\TestData\case.yaml'
        testset_list = FileController.load_case_by_path(path)
        #test1 = testset_list[1]

        #print(type(test1))
        print(testset_list)
        #d1=testset_list['..\\TestCase\\TestData\\case.yaml']['No.1']
        #print(type(d1['Active']))




    def test_load_testcases_by_path_file_excel(self):

        path = '..\TestCase\TestData\case.xlsx'
        testset_list = FileController.load_case_by_path(path)
        #test1 = testset_list[1]
        #d2 = testset_list['..\\TestCase\\TestData\\case.xlsx_case']['No.1']
        print(testset_list)
        #print(type(d2['Active']))
    pass
