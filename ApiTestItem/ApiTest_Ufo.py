# -*- coding: utf-8 -*-
# @Time    : 2017/8/8 9:20
# @Author  : Charles
# @File    : ApiTest_Ufo.py
# @Software: PyCharm


import unittest
import requests
import sys
import CaseGoto
from TestBase import TestBase
import ddt
import LogMsg

"""
requests库的session对象能够帮我们跨请求保持某些参数，也会在同一个session实例发出的所有请求之间保持cookies。
"""


@ddt.ddt
class UfoApiTest(unittest.TestCase):
    # 配置文件路径
    configpath = '../ApiTestItem/Config/config_ufo.yaml'
    # 获取基础用例集合
    cago = CaseGoto.case_goto(configpath)
    # config中host和header
    usrconfig = cago[0]
    # config中配置的用户参数字典
    configdatadic = cago[1]
    # 用例列表
    case_lines_list = cago[2]
    # config全配置内容
    config = cago[3]
    # 参数收集字典
    udatadic_colle = {}
    # 运行结果临时字典，供检查依赖接口状态
    run_load_list = {}

    def setUp(self):

        self.api_client = requests.Session()

        # self.api_client.verify = False

    @ddt.data(*case_lines_list)
    def test_api_rq_ufo(self, case_line):
        # 获取当前执行用例下标
        self.caseindex = sys._getframe().f_code.co_name + '_' + str(UfoAPiTest.case_lines_list.index(case_line) + 1001)
        LogMsg.logger.info('caseindex: ' + self.caseindex)
        # 执行测试
        TestBase.casetestBase(self, self.api_client, UfoAPiTest.configdatadic, UfoAPiTest.udatadic_colle, case_line,
                              UfoAPiTest.usrconfig, UfoAPiTest.config, UfoAPiTest.run_load_list)

    def tearDown(self):
        TestBase.endtest(self, self.caseindex, self.case_info, self.check_diff, UfoAPiTest.run_load_list)
        self.api_client.close()


