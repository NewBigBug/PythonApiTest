# -*- coding: utf-8 -*-
# @Time    : 2017/7/12 14:54
# @Author  : Charles
# @File    : test_data.py
# @Software: PyCharm
import unittest

import requests
import ResponseParse
import ResultGenerate


class UtilsTest(unittest.TestCase):
    def setUp(self):
        self.api_client = requests.request


    def test_case_requests(self):

        url = 'http://172.16.5.33:8080/nauth/login'
        method = 'get'



        resp_obj = self.api_client(method, url)
        print(resp_obj.cookies)
        cookie=resp_obj.cookies


        ck={'param1': '魏双双',
            'param2': '3435ddgggsgsdgs',
            'param3': '魏双双'
            }


        respdict = {
            'Response_Type': 'Html',
            'Checkpoint': ck
        }

        case_info = {
            'CasePath': '\Application\JetBrains\PyCharm 2017.1.4',
            'CaseNumb': '10001',
            'CaseName': 'DoTest',
            'Request_Url': '/api/login',
            'Temp_Filepath': 'D:\GitPro\Python\PythonApiTest\output\\tempyaml.yaml'
        }

        url = 'http://172.16.5.33:8080/nauth/login'
        method = 'post'
        req_kwargs = {}
        req_kwargs['data'] = {
            'username': 'shuangshuangwei',
            'password': 'qwer@123'
        }
        req_kwargs['cookies']=cookie

        resp_obj = self.api_client(method, url, **req_kwargs)
        t_resp=ResponseParse.response_parse(resp_obj,respdict)
        msg=ResultGenerate.result_generate(case_info, t_resp[1])

        #print(t_resp)
        print(msg[0])
        print(msg[1])

        #print(resp_obj.history[])
        # api_client.close()

        url = 'http://172.16.5.33:8080/nauth/sys/user/info'
        method = 'get'
        req_kwargs['cookies'] = cookie
        resp_obj = self.api_client(method, url, **req_kwargs)
        print(resp_obj.status_code)
        print(resp_obj.history)

        #print(type(resp_obj))



    def tearDown(self):
        #self.api_client.close()
        pass

# -*- coding: utf-8 -*-
# @Time    : 2017/7/13 15:33
# @Author  : Charles
# @File    : test_ResponseP.py
# @Software: PyCharm