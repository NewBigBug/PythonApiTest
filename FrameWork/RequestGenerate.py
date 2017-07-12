# -*- coding: utf-8 -*-
# @Time    : 2017/7/12 14:36
# @Author  : Charles
# @File    : RequestGenerate.py
# @Software: PyCharm
import LogMsg
from FileController import load_yaml_file


#处理请求类型
def generate_requestmethod(type):
    typestr_p=('POST','Post','post')
    typestr_g=('Get','GET','get')
    if type in typestr_p:

    return

"""
该参数应为示例字典格式
requestdict{
    'Request_Url': '/api/users', 
    'Request_method': 'POST', 
    'Header': {'Accept': '', 'Accept-Encoding': '', 'Accept-Language': '', 'User-Agent': ''}, 
    'Body_Type': 'Forms', 
    'Request Body': {'name': 'user1', 'password': '123456'}, 
    'Need_Cookie': 'TRUE', 
    'Need_Sign': 'TRUE', 
}
"""
def request_generate(requestdict):
    #usrconfig为字典类型
    usrconfig = load_yaml_file('../Config/config.yaml')

    #处理url
    if 'host' in usrconfig.keys():
        if 'Request_Url' in requestdict.keys() and (requestdict['Request_Url']==0) :
            if 'http' in requestdict['Request_Url']:
                Url=requestdict['Request_Url']
            else:
                Url=usrconfig['host']+requestdict['Request_Url']
        else:
            LogMsg.logger.error('用例文件中缺失 Request_Url 数据')
    else:
        if 'Request_Url' in requestdict.keys() and (requestdict['Request_Url'] == 0):
            if 'http' in requestdict['Request_Url']:
                Url = requestdict['Request_Url']
            else:
                LogMsg.logger.error('config配置文件中缺失 host 配置')
        else:
            LogMsg.logger.error('用例文件中缺失 Request_Url 数据')
            LogMsg.logger.error('config配置文件中缺失 host 配置')


















