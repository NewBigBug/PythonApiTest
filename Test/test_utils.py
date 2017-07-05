import os
import unittest

import utils


class UtilsTest(unittest.TestCase):

    #def setUp(self):


    #def tearDown(self):

    def test_load_testcases_by_path_files(self):

        testsets_list = []


        # absolute file path
        path = '../TestData/demo1.yaml'
        testset_list = utils.load_testcases_by_path(path)
        self.assertEqual(len(testset_list), 1)
        self.assertEqual(len(testset_list[0]["testcases"]), 1)
        testsets_list.extend(testset_list)
       # print (testset_list)