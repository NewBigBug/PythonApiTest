# -*- coding: utf-8 -*-
# @Time    : 2017/7/13 14:04
# @Author  : Charles
# @File    : ResultGenerate.py
# @Software: PyCharm
import json
import os

import LogMsg
import FileController

"""
生成测试结果
传递参数：CaseInteg-case_info_dic
传递参数：CaseInteg-ResponseParse-responseparse[1]-check_diff_dic
"""


def result_generate(case_info, check_diff):
    recode = {}
    print(check_diff)

    if check_diff:
        case_info.update(check_diff)
    else:
        case_info['caseresult'] = 'Fail'

    """
    case_info={
        'CasePath': caselines['CasePath'],
        'CaseNumb': caselines['CaseNo'],
        'CaseName': caselines['API_Purpose']
        'Request_Url': '/api/login'
        'Temp_Filepath' ''      
        'checkresult': Pass
                        
    }
    """

    rmg = ''
    for key, value in case_info.items():
        rmg = rmg + str(key) + ':' + str(value) + '\t'
    LogMsg.logger.info(rmg)
    resultlist = [case_info]
    # 写入执行记录
    mstr = case_info['CasePath'] + ',' + case_info['CaseNumb'] + ',' + case_info['CaseName'] + ',' + case_info['caseresult']
    recode[case_info['Request_Url']] = mstr

    FileController.write_yaml_file(recode, case_info['Temp_Filepath'])

    return resultlist
