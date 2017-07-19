# -*- coding: utf-8 -*-
# @Time    : 2017/7/18 14:11
# @Author  : Charles
# @File    : test_ApiSuite.py
# @Software: PyCharm


import unittest
import HTMLTestRunner
import HTMLTestRunner1
import time
import unittest
import requests
import CaseGoto
import CaseInteg
import UserParam
import FileController
import ddt

"""
requests库的session对象能够帮我们跨请求保持某些参数，也会在同一个session实例发出的所有请求之间保持cookies。
"""
# 用例通用字典
udatadic = {}
case_result_list = []
# 获取基础用例集合
cago = CaseGoto.case_goto()
usrconfig = cago[0]
configdatadic = cago[1]
case_lines_list = cago[2]
config = cago[3]
# 用户全局变量
udatadic.update(configdatadic)


@ddt.ddt
class ServerTest(unittest.TestCase):
    def setUp(self):
        self.api_client = requests.Session()

    @ddt.data(*case_lines_list)
    def test_api_rq(self, case_line):
        uspa = UserParam.param_generate()
        case_result = CaseInteg.case_Prepare(self.api_client, case_line, udatadic, uspa, usrconfig, config)
        case_result_list.append(case_result[0][0])
        udatadic.update(case_result[1])
        FileController.write_result_to_excel(config['tempfile'], case_result_list)

        sfdsf



    def tearDown(self):
        self.api_client.close()


def suite():
    suite = unittest.TestLoader().loadTestsFromTestCase(ServerTest)
    return suite


if __name__ == '__main__':
    today = time.strftime('%Y%m%d%H%m%S', time.localtime(time.time()))
    reportPath = 'D:/GitPro/Python/PythonApiTest/output/' + today + '.html'
    # with open(reportPath, 'wb') as fp:
    fp = open(reportPath, mode='wb')
    runner = HTMLTestRunner1.HTMLTestRunner(stream=fp, title='Api Test Report', description='接口测试报告')
    runner.run(suite())
    fp.close()
