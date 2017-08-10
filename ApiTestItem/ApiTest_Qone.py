import sys
import requests
import CaseGoto
import unittest
import ddt
import LogMsg
import ResultGenerate
from TestBase import TestBase

"""
requests库的session对象能够帮我们跨请求保持某些参数，也会在同一个session实例发出的所有请求之间保持cookies。
"""


@ddt.ddt
class QoneApiTest(TestBase):
    # 配置文件路径
    configpath = '../ApiTestItem/Config/config_qone.yaml'
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
    # Session实例
    client = None

    @classmethod
    def setUpClass(cls):
        QoneApiTest.client = requests.Session()
        # 是否开启verify,fiddler抓包需取消注释
        # self.api_client.verify = False

    def setUp(self):
        self.client = QoneApiTest.client

    @ddt.data(*case_lines_list)
    def test_api_rq_qone(self, case_line):
        # 继承测试基类
        test_base = super(QoneApiTest, self)
        # 获取当前执行用例下标
        self.caseindex = sys._getframe().f_code.co_name + '_' + str(
            QoneApiTest.case_lines_list.index(case_line) + 1001)
        LogMsg.logger.info('caseindex: ' + self.caseindex)
        # 执行基类测试方法
        test_base.casetestBase(self.client, QoneApiTest.configdatadic, QoneApiTest.udatadic_colle, case_line,
                               QoneApiTest.usrconfig, QoneApiTest.config, QoneApiTest.run_load_list)

    def tearDown(self):
        case_rs = ResultGenerate.result_generate(self.caseindex, self.case_info, self.check_diff)
        QoneApiTest.run_load_list.update(case_rs)

    @classmethod
    def tearDownClass(cls):
        QoneApiTest.client.close()
        ResultGenerate.write_to_tempfile(QoneApiTest.run_load_list, QoneApiTest.config['tempfile'])


