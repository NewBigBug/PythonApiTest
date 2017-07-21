# -*- coding: utf-8 -*-
# @Time    : 2017/7/12 11:53
# @Author  : Charles
# @File    : Utils.py
# @Software: PyCharm
import time

import simplejson

import LogMsg


# 生成当前时间
def time_generate():
    tm = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    return tm


def time_generate1():
    tm = time.strftime('%Y%m%d', time.localtime(time.time()))
    return tm


# 遍历字典
def list_all_dict(key, dict_a):
    key_value = ''
    if isinstance(dict_a, dict):
        if key in dict_a:
            key_value = dict_a[key]
            return key_value
        else:
            for keyset in dict_a:
                valueset = dict_a[keyset]
                #print(valueset)
                list_all_dict(key, valueset)
    elif isinstance(dict_a, str):
        print(dict_a)
        if ':' in dict_a:
            value = simplejson.loads(dict_a)
            # print(value)
            # print(type(value))
            list_all_dict(key, value)
        else:
            LogMsg.logger.info(key + '  in  ' + dict_a + '  遍历结束')


# 生成手机号



# 生成身份证
