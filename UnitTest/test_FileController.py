# -*- coding: utf-8 -*-
# @Time    : 2017/7/12 13:51
# @Author  : Charles
# @File    : test_FileController.py
from unittest import TestCase
import FileController

# @Software: PyCharm
class TestLoad_case_by_path(TestCase):


    """
    def test_load_testcases_by_path_file_yaml(self):

        path = '..\TestCase\TestData\data1\case.yaml'
        testset_list = FileController.load_case_by_path(path)
        #test1 = testset_list[1]

        #print(type(test1))
        print(testset_list)
        #d1=testset_list['..\\TestCase\\TestData\\case.yaml']['No.1']
        #print(type(d1['Active']))



    def test_load_testcases_by_path_file_01(self):

        path = '/Users/Sky/developer/PycharmProjects/PythonApiTest/TestCase/TestData/data1'
        testset_list = FileController.load_case_by_path(path)
        #test1 = testset_list[1]

        #print(type(test1))
        print(testset_list)
        #d1=testset_list['..\\TestCase\\TestData\\case.yaml']['No.1']
        #print(type(d1['Active']))





    def test_load_testcases_by_path_file_02(self):

        path = 'D:\GitPro\Python\PythonApiTest\TestCase\Qone1.xlsx'
        testset_list = FileController.load_case_by_path(path)

        #test1 = testset_list[1] Request_Body

        #d2 = testset_list['..\\TestCase\\TestData\\case.xlsx_case']['No.1']
        print(type(testset_list))
        print(type(testset_list['D:\\GitPro\\Python\\PythonApiTest\\TestCase\\Qone1.xlsx_case']))
        print(type(testset_list['D:\\GitPro\\Python\\PythonApiTest\\TestCase\\Qone1.xlsx_case']['No.1']))
        print(type(testset_list['D:\\GitPro\\Python\\PythonApiTest\\TestCase\\Qone1.xlsx_case']['No.1']['Request_Body']))
        print(type(testset_list['D:\\GitPro\\Python\\PythonApiTest\\TestCase\\Qone1.xlsx_case']['No.1']['Request_Body']['DEVICE_VERSION']))
        #print(type(d2['Active']))



    def test_load_yaml_file(self):
        path = 'D:\GitPro\Python\PythonApiTest\output\\tempyaml.yaml'
        testset_list = FileController.load_yaml_file(path)
        print(type(testset_list))
        
    """

    def test_write_result_to_excel(self):
        tempfile = 'D:\GitPro\Python\PythonApiTest\output\\tempyaml.yaml'
        DC_PATH = 'districtcode.txt'
        codelist = []
        with open(DC_PATH) as file:
            data = file.read()
            districtlist = data.split('\n')
            print(districtlist)
        for node in districtlist:
            if node[10:11] != ' ' and node[10:11] != ' ':
                state = node[10:].strip()
            if node[10:11] == ' ' and node[12:13] != ' ':
                city = node[12:].strip()
            if node[10:11] == ' ' and node[12:13] == ' ':
                district = node[14:].strip()
                code = node[0:6]
                codelist.append({"state": state, "city": city, "district": district, "code": code})
        FileController.write_result_to_excel(tempfile, codelist)
        print(codelist)