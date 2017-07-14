# -*- coding: utf-8 -*-
# @Time    : 2017/7/14 13:18
# @Author  : Charles
# @File    : CaseGoto.py
# @Software: PyCharm
import os

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

#caselines, udatadic, usrconfig

def case_goto():
    testconfig = FileController.load_yaml_file('../Config/Config.yaml')

    # 分割config数据
    usrconfig={
        'Host': testconfig['Host'],
        'Header': testconfig['Header']
    }

    configdatadic={}
    UserParm = testconfig['UserParm']
    for key, value in UserParm.items():
        configdatadic[key] = UserParm[key]






    return testconfig


# 创建临时yaml文件
def tempfile_generate(path):
    if os.path.exists(path):
        os.remove(path)
        createstream = FileController.create_yaml_file(path)
    else:
        createstream = FileController.create_yaml_file(path)
    LogMsg.logger.info('临时文件成功： '+path)

