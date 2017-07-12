# -*- coding: utf-8 -*-
# @Time    : 2017/7/12 14:54
# @Author  : Charles
# @File    : test_data.py
# @Software: PyCharm
import unittest

import requests


class UtilsTest(unittest.TestCase):

    def test_case_requests(self):
        url = 'http://172.16.5.33:8080/nauth/login'
        method = 'POST'
        headers = {
           'Content-Type': 'application/x-www-form-urlencoded'
        }
        data={
            'username': 'shuangshuangwei',
            'password': 'qwer@123'
        }
        #req_kwargs=(headers,data)
        api_client = requests.Session()
        resp_obj = api_client.post(url, data, headers)
        print(resp_obj)
        api_client.close()
