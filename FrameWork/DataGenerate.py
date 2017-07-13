# -*- coding: utf-8 -*-
# @Time    : 2017/7/12 14:14
# @Author  : Charles
# @File    : DataGenerate.py
# @Software: PyCharm

import LogMsg

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





def data_generate(datadict, udatadic):
    data_dict={}
    if 'Request_Body' in datadict.keys() and (datadict['Request_Body'] is not None):
        data_dict = datadict['Request_Body']
        for key, value in data_dict.items():
            # 只遍历4层，超出4层不考虑
            if isinstance(value, dict):
                for key1, value1 in value.items():
                    if isinstance(value1, dict):
                        for key2, value2 in value1.items():
                            if isinstance(value2, dict):
                                for key3, value3 in value2.items():
                                    if isinstance(value3, dict):
                                        LogMsg.logger.error('参数嵌套层数过多')
                                    else:
                                        if '$' in value3:
                                            if value3 in udatadic.keys():
                                                value2[key3] = udatadic[value3]
                                            else:
                                                LogMsg.logger.error('获取参数值失败 ' + value3)
                            else:
                                if '$' in value2:
                                    if value2 in udatadic.keys():
                                        value1[key2] = udatadic[value2]
                                    else:
                                        LogMsg.logger.error('获取参数值失败 ' + value2)
                    else:
                        if '$' in value1:
                            if value1 in udatadic.keys():
                                value[key1] = udatadic[value1]
                            else:
                                LogMsg.logger.error('获取参数值失败 ' + value1)
            else:
                if '$' in value:
                    if value in udatadic.keys():
                        data_dict[key] = udatadic[value]
                    else:
                        LogMsg.logger.error('获取参数值失败 ' + value)
        return data_dict
    else:
        LogMsg.logger.warn('用例无请求数据')
        return data_dict






