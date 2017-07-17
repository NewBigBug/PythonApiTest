# -*- coding: utf-8 -*-
# @Time    : 2017/7/12 11:53
# @Author  : Charles
# @File    : Utils.py
# @Software: PyCharm
import time


# 生成当前时间
def time_generate():
    tm = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    return tm


def time_generate1():
    tm = time.strftime('%Y%m%d', time.localtime(time.time()))
    return tm

# 生成手机号



# 生成身份证
