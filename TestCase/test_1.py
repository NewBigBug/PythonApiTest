import unittest

import requests
import CaseGoto
import CaseInteg
import DataGenerate
import RequestGenerate
import ResponseParse
import ResultGenerate
import UserParam
import LogMsg

"""
requests库的session对象能够帮我们跨请求保持某些参数，也会在同一个session实例发出的所有请求之间保持cookies。
"""


class ServerTest(unittest.TestCase):
    def setUp(self):
        self.api_client = requests.Session()


    def test_api_rq(self):
        udatadic = {}
        cago=CaseGoto.case_goto()

        usrconfig = cago[0]
        configdatadic = cago[1]
        case_lines_list = cago[2]
        config = cago[3]
        #CaseGoto.tempfile_generate(config)
        uspa = UserParam.param_generate()
        udatadic.update(configdatadic)
        udatadic.update(uspa)

        for i in range(len(case_lines_list)):
            case_line = case_lines_list[i]
            caselinespilt = CaseInteg.case_Prepare(case_line)

            # 处理请求的表单数据
            case_dg = DataGenerate.data_generate(caselinespilt[1], udatadic)
            LogMsg.logger.info('请求表单已处理')
            LogMsg.logger.info(case_dg)
            #udatadic['$sign$'] = UserParam.sign_generate(case_dg, config['Secrete'])

            # 重新调用一次
            #case_dg = DataGenerate.data_generate(caselinespilt[1], udatadic)

            # 处理请求数据
            case_rq = RequestGenerate.request_generate(case_dg, usrconfig)
            LogMsg.logger.info('请求数据已解析')

            # 发送请求
            case_sd = RequestGenerate.request_send(self.api_client, case_rq)
            LogMsg.logger.info('请求数据已发送')
            # 处理返回数据
            case_rp = ResponseParse.response_parse(case_sd, caselinespilt[2])
            LogMsg.logger.info('已获取请求返回值')
            # 处理结果内容
            case_rs = ResultGenerate.result_generate(caselinespilt[0], case_rp[1])
            LogMsg.logger.info('返回值已处理')

            #print(case_rs[1])






    def tearDown(self):
        self.api_client.close()
