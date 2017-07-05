import os
import unittest

import flask_casebase


class UtilsTest(unittest.TestCase):

    def test_load_testconfig(self):

        # absolute file path
        file=flask_casebase.load_testconfig()
        print(file)
        #print(type(test1))
        #print(test1['name'])

