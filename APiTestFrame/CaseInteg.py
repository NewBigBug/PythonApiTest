# -*- coding: utf-8 -*-
# @Time    : 2017/7/12 14:14
# @Author  : Charles
# @File    : CaseInteg.py
# @Software: PyCharm

import DataGenerate
import RequestGenerate
import LogMsg
import UserParam

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


def spilt_case(api_client, caselines, udatadic, usrconfig, config):
    caselinespilt = []
    LogMsg.logger.info(caselines)
    # 分割用例数据
    case_info = {
        'CasePath': caselines['CasePath'],
        'CaseNumb': caselines['CaseNo'],
        'CaseName': caselines['API_Purpose'],
        'Request_Url': caselines['Request_Url'],
        'Checkpoint': caselines['Checkpoint'],
        'DP': caselines['DP']
    }
    caselinespilt.append(case_info)
    case_request = {
        'Request_Url': caselines['Request_Url'],
        'Request_method': caselines['Request_method'],
        'Header': caselines['Header'],
        'Body_Type': caselines['Body_Type'],
        'Request_Body': caselines['Request_Body'],
    }
    caselinespilt.append(case_request)
    case_response = {
        'Need_Collection': caselines['Need_Collection'],
        'Response_Type': caselines['Response_Type'],
        'Checkpoint': caselines['Checkpoint']
    }
    caselinespilt.append(case_response)

    # 处理请求的表单数据
    #print(udatadic)
    LogMsg.logger.info('开始处理请求数据：*********')
    case_dg = DataGenerate.data_generate(caselinespilt[1], udatadic)
    LogMsg.logger.info(case_dg)
    # 生成sign值
    if 'Secrete' in config and config['Secrete']:
        udatadic['$sign$'] = UserParam.sign_generate(case_dg, config['Secrete'])
        # 重新调用一次
        case_dg = DataGenerate.data_generate(case_dg, udatadic)
    # 处理请求数据
    LogMsg.logger.info('开始处理请求数据：**********')
    case_rq = RequestGenerate.request_generate(case_dg, usrconfig)
    LogMsg.logger.info(case_rq)
    # 发送请求
    LogMsg.logger.info('开始发送请求：**********')
    case_sd = RequestGenerate.request_send(api_client, case_rq)
    LogMsg.logger.info('请求返回数据：' + str(case_sd))

    return case_sd, caselinespilt[2], caselinespilt[0]


def case_Prepare(api_client, caselines, udatadic, usrconfig, config, depends_api_status):
    #udatadic.update(uspa)
    if caselines is not None:
        if not caselines['DP']:
            if not caselines['Depends']:
                return spilt_case(api_client, caselines, udatadic, usrconfig, config)
            else:
                depends = caselines['Depends'].split(',')
                load_list = depends_api_status
                flag = False
                for i in range(len(depends)):
                    for key in load_list:
                        r = load_list[key].split(';')
                        if depends[i] in r:
                            re = r[len(r) - 1]
                            if re == 'Pass':
                                flag = True
                                break
                if flag:
                    return spilt_case(api_client, caselines, udatadic, usrconfig, config)
                else:
                    LogMsg.logger.error('依赖API接口:' + str(depends) + '执行失败，当前接口将不会执行：' + str(caselines['Request_Url']))
            depends_api_status.clear()
        else:
            return spilt_case(api_client, caselines, udatadic, usrconfig, config)
    else:
        LogMsg.logger.error('无用例数据')

