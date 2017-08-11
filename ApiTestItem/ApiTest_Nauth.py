# -*- coding: utf-8 -*-
# @Time    : 2017/8/8 9:21
# @Author  : Charles
# @File    : ApiTest_Nauth.py
# @Software: PyCharm

import unittest
import requests
import sys
import CaseGoto
import ResultGenerate
from TestBase import TestBase
import ddt
import LogMsg

"""
requests库的session对象能够帮我们跨请求保持某些参数，也会在同一个session实例发出的所有请求之间保持cookies。
"""


@ddt.ddt
class NauthApiTest(TestBase):
    # 配置文件路径
    configpath = '../ApiTestItem/Config/config_nauth.yaml'
    # 获取基础用例集合
    cago = CaseGoto.case_goto(configpath)
    # config中host和header
    usrconfig = cago[0]
    # config中配置的用户参数字典,UserParm
    configdatadic = cago[1]
    # 用例列表
    case_lines_list = cago[2]
    # config中tempfile
    config = cago[3]
    # 参数收集字典
    udatadic_colle = {}
    # 运行结果临时字典,执行完毕存入yaml临时文件
    run_load_list = {}
    # 存入依赖接口执行状态
    depends_api_status = {}

    def setUp(self):
        super(NauthApiTest, self).creat_session()

    @ddt.data(*case_lines_list)
    def test_api_rq_qone(self, case_line):
        # 继承测试基类
        test_base = super(NauthApiTest, self)
        # 获取当前执行用例下标
        self.caseindex = sys._getframe().f_code.co_name + '_' + str(
            NauthApiTest.case_lines_list.index(case_line) + 1001)
        LogMsg.logger.info('caseindex: ' + self.caseindex)
        # 执行基类测试方法
        test_base.casetestBase(self.client, NauthApiTest.configdatadic, NauthApiTest.udatadic_colle, case_line,
                               NauthApiTest.usrconfig, NauthApiTest.config, NauthApiTest.depends_api_status)

    def tearDown(self):
        super(NauthApiTest, self).close_session()
        ResultGenerate.result_generate(self.caseindex, self.case_info, self.check_diff, NauthApiTest.run_load_list,
                                       NauthApiTest.depends_api_status)

    @classmethod
    def tearDownClass(cls):
        ResultGenerate.write_to_tempfile(NauthApiTest.run_load_list, NauthApiTest.config['tempfile'])
