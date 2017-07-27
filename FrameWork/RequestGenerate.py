# -*- coding: utf-8 -*-
# @Time    : 2017/7/12 14:36
# @Author  : Charles
# @File    : RequestGenerate.py
# @Software: PyCharm
import json

import LogMsg
import requests

"""
该参数应为示例字典格式
        requestdict={
            'Request_Url': '/api/users', 
            'Request_method': 'POST', 
            'Header': {'Accept': '', 'Accept-Encoding': '', 'Accept-Language': '', 'User-Agent': ''}, 
            'Body_Type': 'Data', 
            'Request_Body': {'name': 'user1', 'password': '123456'}, 
            #'Need_Cookie': 'TRUE', 
            #Need_Sign: 'TRUE'
        }
"""


def request_generate(requestdict, usrconfig):
    requestkwargs = {}
    # usrconfig为字典类型
    # usrconfig = load_yaml_file('../Config/config.yaml')
    # print(requestdict)
    """
    # 处理url
    """
    if 'Host' in usrconfig and usrconfig['Host']:
        if 'Request_Url' in requestdict and requestdict['Request_Url']:
            if 'http' in requestdict['Request_Url']:
                Url = requestdict['Request_Url']
            else:
                Url = usrconfig['Host'] + requestdict['Request_Url']
        else:
            LogMsg.logger.error('用例文件中缺失 Request_Url 数据')
    else:
        if 'Request_Url' in requestdict and (requestdict['Request_Url'] is not None):
            if 'http' in requestdict['Request_Url']:
                Url = requestdict['Request_Url']
            else:
                LogMsg.logger.error('config配置文件中缺失 host 配置')
        else:
            LogMsg.logger.error('用例文件中缺失 Request_Url 数据')
            LogMsg.logger.error('config配置文件中缺失 host 配置')
    # 存入url
    requestkwargs['url'] = Url

    """
    # 处理请求方式
    """
    if requestdict['Request_method'] == 'POST':
        Method = 'post'
    elif requestdict['Request_method'] == 'GET':
        Method = 'get'
    elif requestdict['Request_method'] == 'DELETE':
        Method = 'delete'
    else:
        LogMsg.logger.error('用例提供的请求方法暂不支持 ' + requestdict['Request_method'])
    # 存入Method
    requestkwargs['method'] = Method

    """
    # 处理请求头文件
    """
    if 'Header' in requestdict and requestdict['Header']:
        Headers = requestdict['Header']
        requestkwargs['headers'] = Headers
    else:
        if 'Header' in usrconfig and usrconfig['Header']:
            Headers = usrconfig['Header']
            requestkwargs['headers'] = Headers
        else:
            LogMsg.logger.info('用例文件中缺失 Header 数据，如果请求需要Header，用例会失败')
            LogMsg.logger.info('config配置文件中缺失 Header 配置，如果请求需要Header，用例会失败')
    # 存入Header数据


    """
    # 处理请求数据
    # requestdict['Request_Body'],需要转成数据处理方法 DataGenerate
    """
    if 'Body_Type' in requestdict and requestdict['Body_Type'] is not None and requestdict['Body_Type'] != '':
        if requestdict['Body_Type'] == 'Data':
            requestkwargs['data'] = requestdict['Request_Body']
        elif requestdict['Body_Type'] == 'Json':
            requestkwargs['json'] = requestdict['Request_Body']

        else:
            LogMsg.logger.error('用例提供的参数类型暂不支持 ' + requestdict['Body_Type'])
    else:
        LogMsg.logger.info('config配置文件中缺失请求数据配置，如果请求需要，用例会失败')

    # 返回请求参数表
    # LogMsg.logger.info('3242432234234234')
    LogMsg.logger.info(requestkwargs)
    return requestkwargs


# 发送请求
def request_send(client, req_kwargs):
    url = req_kwargs.pop('url')
    # print(type(url))
    method = req_kwargs.pop('method')
    # session client
    # client = requests.Session
    resp = client.request(method, url, **req_kwargs)
    LogMsg.logger.info(resp)
    return resp


