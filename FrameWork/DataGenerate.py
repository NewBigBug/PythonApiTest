# -*- coding: utf-8 -*-
# @Time    : 2017/7/12 14:14
# @Author  : Charles
# @File    : DataGenerate.py
# @Software: PyCharm
import sys

import LogMsg
import re
import UserParam


"""
根据不同的request类型，分别处理请求数据
目前使用request库，不需要对data类型数据进行urlencode转码
处理请求中的参数化字段
"""

#将需要参数化的值用Utils中的参数化方法替换掉，%标识的包括，程序生成变量，返回值参数，用户自定义参数
#将依赖其他接口返回收集值的参数替换，$标识的为依赖参数
"""
datadic  用例数据
udatadic 用户参数化数据
requestdict={
    'Request_Url': '/api/users', 
    'Request_method': 'POST', 
    'Header': {'Accept': '', 'Accept-Encoding': '', 'Accept-Language': '', 'User-Agent': ''}, 
    'Body_Type': 'Data', 
    'Request_Body': {'name': 'user1', 'password': '123456'}, 
    #'Need_Cookie': 'TRUE', 
    #'Need_Sign': 'TRUE'
}
"""
sys.setrecursionlimit(10000)


def data_generate(datadict, udatadic):
    if 'Request_Body' in datadict.keys() and datadict['Request_Body']:
        data_dict = datadict.pop('Request_Body')
        #print(type(data_dict['PRE_APP_CONTACT'][0]))

        data_dict = param_replace(data_dict, udatadic)

        if '$' in str(data_dict):
            LogMsg.logger.info('获取参数值失败,可能含有二次包装数据,请调试 ' + str(data_dict))
        else:
            LogMsg.logger.info(data_dict)
        datadict['Request_Body'] = data_dict
    else:
        LogMsg.logger.warn('用例无请求数据')
    return datadict


def param_replace(data_dict, udatadic):
    for key, value in data_dict.items():
        if isinstance(value, dict):
            param_replace(value, udatadic)

        elif isinstance(value, list):
            for i in range(len(value)):
                param_replace(value[i], udatadic)

        elif isinstance(value, str):
            if '$' in value:
                D_L = re.findall(r'(\$.*?\$)', value)
                udata = UserParam.param_generate(D_L)
                udatadic.update(udata)
                for ukey, uvalue in udatadic.items():
                    if ukey in value:
                        data_dict[key] = value.replace(ukey, uvalue)
        else:
            break
    return data_dict

"""
def type_recur(data, udata):
    if isinstance(data, dict):
        param_replace(value, udatadic)

    elif isinstance(value, list):
        for i in range(len(value)):
            param_replace(value[i], udatadic)

    elif isinstance(value, str):
        if '$' in value:
            D_L = re.findall(r'(\$.*?\$)', value)
            udata = UserParam.param_generate(D_L)
            udatadic.update(udata)
            for ukey, uvalue in udatadic.items():
                if ukey in value:
                    data_dict[key] = value.replace(ukey, uvalue)
    else:
        print(value)
        value = str(value)
        param_replace(value, udatadic)
    
"""




