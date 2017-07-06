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
    """

    def test_load_testcases_by_path_foler(self):

        path = '..\TestCase\TestData'
        testset_list = utils.load_case_by_path(path)
        #test1 = testset_list[1]

        #print(type(test1))
        print(testset_list)

    def test_load_testcases_by_path_file(self):

        path = '..\TestCase\TestData\demo1.yaml'
        testset_list = utils.load_case_by_path(path)
        #test1 = testset_list[1]

        #print(type(test1))
        print(type(testset_list))