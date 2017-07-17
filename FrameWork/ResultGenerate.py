# -*- coding: utf-8 -*-
# @Time    : 2017/7/13 14:04
# @Author  : Charles
# @File    : ResultGenerate.py
# @Software: PyCharm

import LogMsg
import FileController


"""
生成测试结果
传递参数：CaseInteg-case_info_dic
传递参数：CaseInteg-ResponseParse-responseparse[1]-check_diff_dic
"""


def result_generate(case_info, check_diff):

    case_info['CheckResult'] = check_diff

    """
    workbook = write_excle_file()
    sheetname = ''
    if '\\' in case_info['CasePath']:
        pathspilt=case_info['CasePath'].split('\\')
        sheetname=pathspilt[len(pathspilt)-1]
    elif '/' in case_info['CasePath']:
        pathspilt = case_info['CasePath'].split('/')
        sheetname = pathspilt[len(pathspilt) - 1]
    else:
        LogMsg.logger.error('文件路径截取出错，无法创建结果sheet表 ' + case_info['CasePath'])

    workbooksheet = workbook.add_sheet(sheetname)
    
    """
    """
    case_info={
        'CasePath': caselines['CasePath'],
        'CaseNumb': caselines['CaseNo'],
        'CaseName': caselines['API_Purpose']
        'Request_Url': '/api/login'
        'Temp_Filepath' ''
        'CheckResult'  : check_diff[key]={
                        'respdata': resppame,
                        'checkdata': point,
                        'checkresult': True
                        }
    }
    """

    rmg = ''
    for key, value in case_info.items():
        rmg = rmg + str(key) + ':' + str(value)+'\t'

    for key, value in case_info['CheckResult'].items():
        CaseResult = 'Pass'
        if not value['checkresult']:
            CaseResult = 'Fail'
            break
    mssge = rmg + 'CaseResult:' + CaseResult
    LogMsg.logger.info('测试结果：' + mssge)
    case_info['CaseResult'] = CaseResult

    resultlist=[case_info, mssge]

    #写入执行记录
    recode = {
        case_info['Request_Url']: case_info['CaseResult']
    }
    FileController.write_yaml_file(recode, case_info['Temp_Filepath'])

    return resultlist

