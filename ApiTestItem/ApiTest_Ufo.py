# -*- coding: utf-8 -*-
# @Time    : 2017/8/8 9:20
# @Author  : Charles
# @File    : ApiTest_Ufo.py
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
class UfoApiTest(TestBase):
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
    # 存入依赖接口执行状态
    depends_api_status = {}
    # Session实例
    client = None

    def setUp(self):
        super(UfoApiTest, self).creat_session()

    @ddt.data(*case_lines_list)
    def test_api_rq_qone(self, case_line):
        # 继承测试基类
        test_base = super(UfoApiTest, self)
        # 获取当前执行用例下标
        self.caseindex = sys._getframe().f_code.co_name + '_' + str(
            UfoApiTest.case_lines_list.index(case_line) + 1001)
        LogMsg.logger.info('caseindex: ' + self.caseindex)
        # 执行基类测试方法
        test_base.casetestBase(self.client, UfoApiTest.configdatadic, UfoApiTest.udatadic_colle, case_line,
                               UfoApiTest.usrconfig, UfoApiTest.config, UfoApiTest.depends_api_status)

        # 处理测试结果
        ResultGenerate.result_generate(self.caseindex, self.case_info, self.check_diff, UfoApiTest.run_load_list,
                                       UfoApiTest.depends_api_status)

    def tearDown(self):
        super(UfoApiTest, self).close_session()

    @classmethod
    def tearDownClass(cls):
        UfoApiTest.client.close()
        ResultGenerate.write_to_tempfile(UfoApiTest.run_load_list, UfoApiTest.config['tempfile'])

