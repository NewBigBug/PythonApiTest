# -*- coding: utf-8 -*-
# @Time    : 2017/7/12 14:36
# @Author  : Charles
# @File    : RequestGenerate.py
# @Software: PyCharm

from FileController import load_yaml_file




#处理请求URL地址
def generate_url(host, api):
    if 'http' in api:
        url = api
    else:
        url = host+api
    return url


#处理请求类型
def generate_requestmethod(type):
    typestr_p=('POST','Post','post')
    typestr_g=('Get','GET','get')
    if type in typestr_p:

    return


def request_generate():
    usrconfig = load_yaml_file('../ProjectBase/config/config.yaml')
    for














