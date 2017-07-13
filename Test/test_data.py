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
        self.cookie = ''

    def test_case_requests(self):

        url = 'http://172.16.5.33:8080/nauth/login'
        method = 'get'

        resp_obj = self.api_client.request(method, url)
        print(resp_obj.cookies)
        cookie=resp_obj.cookies




        url = 'http://172.16.5.33:8080/nauth/login'
        method = 'post'
        req_kwargs = {}
        req_kwargs['data'] = {
            'username': 'shuangshuangwei',
            'password': 'qwer@123'
        }
        req_kwargs['cookies']=cookie

        resp_obj = self.api_client(method, url, **req_kwargs)
        ind=resp_obj.text.index('魏双双')
        cutslice = resp_obj.text[ind - 10:ind + 10]
        print(cutslice)

        #print(resp_obj.history[])
        # api_client.close()

        url = 'http://172.16.5.33:8080/nauth/sys/user/info'
        method = 'get'
        req_kwargs['cookies'] = cookie
        resp_obj = self.api_client(method, url, **req_kwargs)
        print(resp_obj.status_code)
        print(resp_obj.history)

        print(type(resp_obj))



    def tearDown(self):
        #self.api_client.close()
        pass

