import os
import unittest

import requests

import casebase
import Utils

"""
requests库的session对象能够帮我们跨请求保持某些参数，也会在同一个session实例发出的所有请求之间保持cookies。
"""


class ServerTest(unittest.TestCase):
    def setUp(self):
        pass


    def test_creat_user(self):


        #生成用例，并发送请求给服务器
        caseresultmsg=casebase.case_generator_request()
        #处理用例执行结果的List
        msg = casebase.case_result(caseresultmsg)
        print(msg)



    def tearDown(self):
        pass
