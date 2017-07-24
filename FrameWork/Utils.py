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
    global key_value
    if isinstance(dict_a, dict) or (isinstance(dict_a, str) and '{' in dict_a):
        if isinstance(dict_a, str):
            value_dict = simplejson.loads(dict_a)
        else:
            value_dict = dict_a

        for key_set in value_dict:
            if key in value_dict:
                key_value = value_dict[key]
                break
            else:
                value_set = value_dict[key_set]
                list_all_dict(key, value_set)
    return str(key_value)

# 生成手机号

# 生成身份证
