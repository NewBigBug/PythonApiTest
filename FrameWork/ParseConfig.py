# -*- coding: utf-8 -*-
# @Time    : 2017/7/12 14:03
# @Author  : Charles
# @File    : ParseConfig.py
# @Software: PyCharm
from FileController import load_yaml_file

def load_testconfig():
    testconfig = load_yaml_file('../ProjectBase/config/config.yaml')
    return testconfig