import os
import unittest

import casebase


class UtilsTest(unittest.TestCase):

    def test_load_testconfig(self):

        # absolute file path
        file=casebase.load_testconfig()
        print(file)
        #print(type(test1))
        #print(test1['name'])

