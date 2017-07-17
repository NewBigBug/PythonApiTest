import unittest

import requests
import CaseGoto
import CaseInteg
import UserParam
import FileController

"""
requests库的session对象能够帮我们跨请求保持某些参数，也会在同一个session实例发出的所有请求之间保持cookies。
"""


class ServerTest(unittest.TestCase):
    def setUp(self):
        self.api_client = requests.Session()

    def test_api_rq(self):
        udatadic = {}
        cago = CaseGoto.case_goto()
        usrconfig = cago[0]
        configdatadic = cago[1]
        #print(configdatadic)
        case_lines_list = cago[2]
        config = cago[3]
        uspa = UserParam.param_generate()
        udatadic.update(configdatadic)
        udatadic.update(uspa)
        case_result_list = []
        for i in range(len(case_lines_list)):
            case_line = case_lines_list[i]
            case_result = CaseInteg.case_Prepare(self.api_client, case_line, udatadic, usrconfig, config)
            case_result_list.append(case_result[0])
        FileController.write_result_to_excel(config['tempfile'],case_result_list)

    def tearDown(self):
        self.api_client.close()
