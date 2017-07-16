# -*- coding: utf-8 -*-
# @Time    : 2017/7/14 11:39
# @Author  : Charles
# @File    : UserParam.py
# @Software: PyCharm

import hashlib
import Utils


def param_generate():
    paramdict={
        '$tm': Utils.time_generate()
    }
    return paramdict





"""
caselines={
    Request_Body': {
        'name': 'user1',
        'password': '123456'
        'key1':'value1'
        'key1':'value2'
        }
    }
"""

# 生成sign值
def sign_generate(caselines, secret):
    new_caseline = sorted(caselines)
    secretStr = ''
    for i in range(len(new_caseline)):
        key = new_caseline[i]
        secretStr = secretStr + key + str(caselines[key])
    scStr = secret + secretStr + secret
    m = hashlib.md5(scStr.encode(encoding='utf-8'))
    md5Str = m.hexdigest().upper()
    return md5Str
