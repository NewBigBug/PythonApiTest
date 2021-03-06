# -*- coding: utf-8 -*-
# @Time    : 2017/7/14 11:39
# @Author  : Charles
# @File    : UserParam.py
# @Software: PyCharm

import hashlib
import Utils
import LogMsg
import copy


def param_generate():
    paramdict = {
        '$tm$': Utils.time_generate()
    }
    return paramdict


"""

    Request_Body': {
        'name': 'user1',
        'password': '123456'
        'key1':'value1'
        'key1':'value2'
        }
    
"""


# 生成sign值
def sign_generate(case_lines, secret):
    caselines = copy.deepcopy(case_lines['Request_Body'])
    if 'SIGN' in caselines:
        del caselines['SIGN']
    new_caseline = sorted(caselines)
    #print(new_caseline)
    #print(new_caseline)
    secretStr = ''
    for i in range(len(new_caseline)):
        key = new_caseline[i]
        secretStr = secretStr + key + str(caselines[key])
    scStr = secret + secretStr + secret
    LogMsg.logger.info(scStr)
    m = hashlib.md5(scStr.encode(encoding='utf-8'))
    md5Str = m.hexdigest().upper()
    return md5Str
