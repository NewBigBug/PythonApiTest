import os
import unittest

import utils


class UtilsTest(unittest.TestCase):

    """
    def test_load_testcasesfile(self):

        # absolute file path
        path = '..\TestCase\TestData\demo1.yaml'
        testset_list = utils.load_testcasesfile(path)
        test1=testset_list['test1']

        #print(type(test1))
        #print(test1['name'])


    def test_load_testcases_by_path_foler(self):

        path = '..\TestCase\TestData'
        testset_list = utils.load_case_by_path(path)
        #test1 = testset_list[1]

        #print(type(test1))
        print(testset_list)




    def test_load_case_file(self):
        path = '..\TestCase\TestData\case.yaml'

        test1 = utils.load_case_file(path)

        # print(type(test1))
        print(type(test1))
        print(test1['No.2'])
    """
    def test_load_testcases_by_path_file_yaml(self):

        path = '..\TestCase\TestData\case.yaml'
        testset_list = utils.load_case_by_path(path)
        #test1 = testset_list[1]

        #print(type(test1))
        print(testset_list)




    def test_load_testcases_by_path_file_excel(self):

        path = '..\TestCase\TestData\case.xlsx'
        testset_list = utils.load_case_by_path(path)
        #test1 = testset_list[1]

        #print(type(test1))
        print(testset_list)