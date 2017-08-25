# -*- coding: utf-8 -*-
# @Time    : 2017/7/14 11:39
# @Author  : Charles
# @File    : UserParam.py
# @Software: PyCharm

import hashlib
import re

import Utils
import LogMsg
import copy


def param_generate(DL):
    # 参数化字典内容
    paramdict_str = {
        '$tm$': 'time_generate',
        '$tm1$': 'time_generate1',
        '$idcd$': 'identity_card',
        '$uname$': 'chinese_name',
        '$email$': 'email_generate',
        '$mobile$': 'phone_generate',
        '$adress$': 'address_generate',
        '$cpname$': 'company_name',
        '$fphone$': 'fixedline_phone'
    }
    paramdict = {}
    for i in range(len(DL)):
        if '(' in DL[i]:
            l = ''.join(re.findall(r'(\(.*?\))', DL[i]))
            D = DL[i].replace(l, '')
            L = l.replace('(', '').replace(')', '')
            if D in paramdict_str:
                paramdict[DL[i]] = getattr(Utils, paramdict_str[D])(L)
            else:
                LogMsg.logger.error('未在参数字典中找到对应索引内容    ' + DL[i])
        else:
            if DL[i] in paramdict_str:
                paramdict[DL[i]] = getattr(Utils, paramdict_str[DL[i]])()
            else:
                LogMsg.logger.error('未在参数字典中找到对应索引内容    ' + DL[i])
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
    secretStr = ''
    for i in range(len(new_caseline)):
        key = new_caseline[i]
        if isinstance(caselines[key], str):
            value = caselines[key]

        else:
            value = str(caselines[key]).replace('\'', '\"').replace(': ', ':').replace(', ', ',')
        secretStr = secretStr + key + value
    scStr = secret + secretStr + secret
    LogMsg.logger.info(scStr)
    m = hashlib.md5(scStr.encode(encoding='utf-8'))
    md5Str = m.hexdigest().upper()
    return md5Str


#############
def sign_generate_01(case_lines, secret):
    scStr = secret + case_lines + secret
    LogMsg.logger.info(scStr)
    m = hashlib.md5(scStr.encode(encoding='utf-8'))
    md5Str = m.hexdigest().upper()
    return md5Str
