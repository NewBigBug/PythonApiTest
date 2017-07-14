# -*- coding: utf-8 -*-
# @Time    : 2017/7/12 14:14
# @Author  : Charles
# @File    : CaseInteg.py
# @Software: PyCharm

import DataGenerate
import RequestGenerate
import ResponseParse
import ResultGenerate
import LogMsg

"""
传入单条用例，分别执行 DataGenerate,RequestGenerate,RespenseParse,ResultGenerate
"""

"""
{
    'CasePath':'..\\TestCase\\TestData\\case.yaml',
    'CaseNo':'No.1',     
    'API_Purpose': 'login',
    'Request_Url': '/api/users',
    'Request_method': 'POST',
    'Header': {'Accept': '', 'Accept-Encoding': '', 'Accept-Language': '', 'User-Agent': ''},
    'Body_Type': 'Forms',
    'Request_Body': {'name': 'user1', 'password': '123456'},
    #'Need_Cookie': 'TRUE',
    #'Need_Sign': 'TRUE',
    'Need_Collection': {'param1': '123', 'param2': '123'},
    #'Depends': '/api/login,/api/reg',
    'Response_Type': 'Html',
    'Checkpoint': {'param1': '123', 'param2': '123'},
    #'Active': 'TRUE'        
}
"""


def case_Prepare(client, caselines, udatadic, usrconfig):
    if caselines['CasePath'] == 'TRUE':
        LogMsg.logger.info(caselines)
        # 分割用例数据
        case_info = {
            'CasePath': caselines['CasePath'],
            'CaseNumb': caselines['CaseNo'],
            'CaseName': caselines['API_Purpose'],
            'Request_Url': caselines['Request_Url'],
            'Temp_Filepath': caselines['Request_Url']
        }

        case_request = {
            'Request_Url': caselines['Request_Url'],
            'Request_method': caselines['Request_method'],
            'Header': caselines['Header'],
            'Body_Type': caselines['Body_Type'],
            'Request_Body': caselines['Request_Body'],
        }

        case_response = {
            'Need_Collection': caselines['Need_Collection'],
            'Response_Type': caselines['Response_Type'],
            'Checkpoint': caselines['Checkpoint']
        }

        # 处理请求的表单数据
        case_dg = DataGenerate.data_generate(case_request, udatadic)
        LogMsg.logger.info('请求表单已处理')

        """
        # 处理请求数据
        case_rq = RequestGenerate.request_generate(case_dg, usrconfig)
        LogMsg.logger.info('请求数据已解析')

        # 发送请求
        case_sd = RequestGenerate.request_send(client, case_rq)
        LogMsg.logger.info('请求数据已发送')
        # 处理返回数据
        case_rp = ResponseParse.response_parse(case_sd, case_response)
        LogMsg.logger.info('已获取请求返回值')
        # 处理结果内容
        case_rs = ResultGenerate.result_generate(case_info, case_rp[1])
        LogMsg.logger.info('返回值已处理')
        

        case_intline = [case_rp[0], case_rs[0]]

        return case_intline
        """
    else:
        LogMsg.logger.info('用例非活动状态 '+ caselines['CasePath'] + caselines['CaseNo'] + caselines['API_Purpose'])

