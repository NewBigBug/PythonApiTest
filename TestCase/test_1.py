import os
import unittest

import requests

import flask_casebase
import utils

"""
requests库的session对象能够帮我们跨请求保持某些参数，也会在同一个session实例发出的所有请求之间保持cookies。
"""


class ServerTest(unittest.TestCase):
    def setUp(self):
        #self.api_client = requests.request
        self.host = 'http://127.0.0.1:5000'
        #self.clear_user()
    """
    def clear_user(self):
        url = "%s/api/users" % (self.host)
        method = 'DELETE'
        resp = self.api_client(method, url)
        return resp

    def creat_user(self, testcase):
        case_name = testcase['name']
        req_kwargs = testcase['request']
        check_point = testcase['Checkpoint']
        print("CaseName: " + case_name)
        url = self.host + req_kwargs.pop('url')
        method = req_kwargs.pop('method')
        resp_obj = self.api_client(method, url, **req_kwargs)
        result = utils.assertresult(resp_obj, check_point)
        return result
    """

    def test_creat_user(self):


        #testcase_file_path = os.path.join(os.getcwd(), 'TestData\demo1.yaml')
        testcases = utils.load_testcases_by_path(testcase_file_path)
        for i in range(len(testcases)):
            caseresult=flask_casebase.case_generator(i, self.host, testcases[i])
            msg=flask_casebase.case_result(testcase_file_path, caseresult)
            print(msg)


    def tearDown(self):
        pass
