# -*- coding: utf-8 -*-
# @Time    : 2017/7/14 13:18
# @Author  : Charles
# @File    : CaseGoto.py
# @Software: PyCharm
import os

import copy

import FileController
import LogMsg

"""
#请求host地址
Host: http://127.0.0.1:5000
#用例文件路径
Casefile: D:\GitPro\Python\PythonApiTest\TestCase\TestData
#临时文件路径
tempfile: D:\GitPro\Python\PythonApiTest\output\\tempyaml.yaml
#请求header内容
Header:
  test1: '123456'
  test2: '123456'
#秘钥
Secrete:
#用户自定义参数
UserParm:
  $username: '123456789'
  $password': '123456789'
"""


def case_goto(configpath):

    testconfig = FileController.load_yaml_file(configpath)
    LogMsg.logger.info('加载配置文件：' + configpath)
    # 创建临时yaml文件
    path=testconfig['tempfile']
    if os.path.exists(path):
        os.remove(path)
        FileController.create_yaml_file(path)
    else:
        FileController.create_yaml_file(path)
    LogMsg.logger.info('临时文件成功： ' + path)

    # 分割config数据
    usrconfig = {
        'Host': testconfig.pop('Host')
    }
    if 'Header' in testconfig:
        usrconfig['Header'] = testconfig.pop('Header')
    else:
        LogMsg.logger.info('Header 配置文件中未配置，可能引起出错')

    # config参数数据
    configdatadic = {}
    if 'UserParm' in testconfig and testconfig['UserParm']:
        UserParm = testconfig.pop('UserParm')
        for key, value in UserParm.items():
            configdatadic[key] = UserParm[key]
    else:
        LogMsg.logger.info('配置文件中无用户参数化数据')
    # 处理用例库
    caselibrarypath = testconfig.pop('Casefile')
    #caselibrary = FileController.load_case_by_path(caselibrarypath)
    case_lines_list = g_case_list(caselibrarypath)
    return usrconfig, configdatadic, case_lines_list, testconfig
    # config中host和header    # config中配置的用户参数字典    # 用例列表    # config剩余配置内容


# 重写用例处理参数，将测试接口的依赖接口插入列表中，并在每条用例后添加Flag，是否为依赖关系插入执行的接口 DP=False/True
def g_case_list(caselibrarypath):
    case_lines_list = []
    case_lines_L = []
    case_lines_D = {}
    caselibrary = FileController.load_case_by_path(caselibrarypath)
    for key, value in caselibrary.items():
        file_path = str(key)
        for key1, value1 in value.items():
            case_line = {'CasePath': file_path, 'CaseNo': key1}
            case_line.update(value1)
            case_lines_D[value1['Request_Url']+'_' + key1.split('.')[1]] = copy.deepcopy(case_line)
            case_lines_L.append(case_line)

    for i in range(len(case_lines_L)):
        flag1 = case_lines_L[i]['Active']
        if flag1 == 'TRUE':
            # 原测试的接口DP=False,依赖插入的接口DP=True
            case_lines_L[i]['DP'] = False
            if case_lines_L[i]['Depends']:
                depends_api = []
                depends = case_lines_L[i]['Depends'].split(',')
                for j in range(len(depends)):
                    if depends[j] in case_lines_D:
                        api = case_lines_D[depends[j]]
                        api['DP'] = True
                        depends_api.append(api)
                        LogMsg.logger.info('CaseList: ' + str(api))
                    else:
                        LogMsg.logger.error('未找到依赖接口: ' + depends[j])
                case_lines_list.extend(depends_api)
                case_lines_list.append(case_lines_L[i])
                LogMsg.logger.info('CaseList: ' + str(case_lines_L[i]))
            else:
                case_lines_list.append(case_lines_L[i])
                LogMsg.logger.info('CaseList: ' + str(case_lines_L[i]))
        else:
            LogMsg.logger.info('用例非活动状态: ' + str(case_lines_L[i]))
    return case_lines_list

