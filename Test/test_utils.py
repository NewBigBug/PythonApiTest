import os
import unittest

import utils


class UtilsTest(unittest.TestCase):

    def test_load_testcasesfile(self):

        # absolute file path
        path = 'TestData\demo1.yaml'
        testset_list = utils.load_testcasesfile(path)
        test1=testset_list['test1']

        #print(type(test1))
        #print(test1['name'])

    def test_load_testcases_by_path(self):

        path = 'TestData\demo1.yaml'
        testset_list = utils.load_testcases_by_path(path)
        test1 = testset_list[1]

        print(type(test1))
        print(test1['name'])