# -*- coding: utf-8 -*-
# @Time    : 2017/7/13 9:47
# @Author  : Charles
# @File    : test_RequestGen.py
# @Software: PyCharm
import unittest
from RequestGenerate import request_generate


class RequestGen(unittest.TestCase):
    """
    def test_request_generate(self):
        requestdict = {
            'Request_Url': '/api/users',
            'Request_method': 'POST',
            'Header': {'Accept': '', 'Accept-Encoding': '', 'Accept-Language': '', 'User-Agent': ''},
            'Body_Type': 'Data',
            'Request_Body': {'name': 'user1', 'password': '123456'},
            'Need_Cookie': 'TRUE',
            'Need_Sign': 'TRUE',
        }

        req = request_generate(requestdict)

        print(req)
    """
