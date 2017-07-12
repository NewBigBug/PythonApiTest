# -*- coding: utf-8 -*-
# @Time    : 2017/7/12 14:54
# @Author  : Charles
# @File    : test_data.py
# @Software: PyCharm
import unittest

import requests


class UtilsTest(unittest.TestCase):

    def setUp(self):
        self.api_client = requests.Session()

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

        resp_obj = self.api_client.post(url, data, headers)
        print(resp_obj)
        #api_client.close()


    def test_case_requests_get(self):
        url = 'http://172.16.5.33:8080/nauth/sys/user/info'
        method = 'POST'
        headers = {
           'Content-Type': 'application/x-www-form-urlencoded'
        }


        resp_obj = self.api_client.get(url)
        print(resp_obj)



    def tearDown(self):
        self.api_client.close()