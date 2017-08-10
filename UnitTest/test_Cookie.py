# -*- coding: utf-8 -*-
# @Time    : 2017/8/9 17:36
# @Author  : Charles
# @File    : test_Cookie.py
# @Software: PyCharm
import unittest

import requests


class Test_CaseGoto(unittest.TestCase):

    def setUp(self):
        self.client = requests.Session()

    def test_cookie(self):
        url1 = 'http://172.16.5.33:8080/nauth/login'
        url2 = 'http://172.16.5.33:8080/nauth/sys/user/info'

        data={
            'username': 'shuangshuangwei',
            'password': 'qwer@1234'
        }

        s1 = self.client.request(method='POST', url=url1, data=data)
        #print(s1.text)
        s2 = self.client.request(method='GET', url=url2, data='')
        self.assertIn('台州门店', s2.text)
        #print(s2.text)

    def tearDown(self):
        self.client.close()
