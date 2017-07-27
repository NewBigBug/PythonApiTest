# -*- coding: utf-8 -*-
# @Time    : 2017/7/14 13:18
# @Author  : Charles
# @File    : CaseGoto.py
# @Software: PyCharm
import os

import FileController
import LogMsg


# 创建临时yaml文件
def tempfile_generate(path):
    if os.path.exists(path):
        os.remove(path)
        FileController.create_yaml_file(path)
    else:
        FileController.create_yaml_file(path)
    LogMsg.logger.info('临时文件成功： ' + path)


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


# caselines, udatadic, usrconfig

def     case_goto():
    configpath='../TestCase/Config/config.yaml'
    testconfig = FileController.load_yaml_file(configpath)
    LogMsg.logger.info('加载配置文件：' + configpath)
    # 创建临时yaml文件
    tempfile_generate(testconfig['tempfile'])

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
    if 'UserParm' in testconfig:
        UserParm = testconfig.pop('UserParm')
        for key, value in UserParm.items():
            configdatadic[key] = UserParm[key]
    else:
        LogMsg.logger.info('配置文件中无用户参数化数据')

    # 处理用例库
    case_lines_list = []
    caselibrarypath = testconfig.pop('Casefile')
    caselibrary = FileController.load_case_by_path(caselibrarypath)
    for key, value in caselibrary.items():
        file_path = str(key)
        for key1, value1 in value.items():
            flag = value1['Active']
            if flag == 'TRUE':
                case_line = {'CasePath': file_path, 'CaseNo': key1}
                case_line.update(value1)
                case_line['Temp_Filepath'] = testconfig['tempfile']
                LogMsg.logger.info('CaseList: ' + str(case_line))
                case_lines_list.append(case_line)
            else:
                LogMsg.logger.info('用例非活动状态: ' + value1['API_Purpose'] + value1['Request_Url'])

    return usrconfig, configdatadic, case_lines_list, testconfig



