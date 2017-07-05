import os
import unittest
import requests
import exception
import utils

"""
requests库的session对象能够帮我们跨请求保持某些参数，也会在同一个session实例发出的所有请求之间保持cookies。
"""
class ServerTest(unittest.TestCase):
    def setUp(self):
        self.host = "http://127.0.0.1:5000"
        self.api_client = requests.Session()
        print('setUp')

    def creatuser(self, testcase):

        req_kwargs = testcase['request']
        try:
            url = req_kwargs.pop('url')
            method = req_kwargs.pop('method')
        except KeyError:
            raise exception.ParamsError("Params Error")
        resp_obj = self.api_client(url=url, method=method, **req_kwargs)
        #diff_content = utils.diff_response(resp_obj, testcase['response'])
        #success = False if diff_content else True
        #return success, diff_content
        return resp_obj


    def test_creatuser(self):
        testcase_file_path = os.path.join(os.getcwd(), '../TestData/demo1.yaml')
        testcases = utils.load_testcases(testcase_file_path)
        res= self.creatuser(testcases['test'])
        print(res)

    def tearDown(self):
        self.api_client.close()
        print('tearDown')



if __name__ == '__main__':
    unittest.main()
