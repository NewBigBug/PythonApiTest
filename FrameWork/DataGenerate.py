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
    #print(datadict)
    if 'Request_Body' in datadict.keys() and (datadict['Request_Body'] is not None and datadict['Request_Body'] != ''):
        data_dict = datadict.pop('Request_Body')
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
                                            for ukey, uvalue in udatadic.items():
                                                if ukey in value3:
                                                    value2[key3] = value3.replace(ukey, uvalue)

                            else:
                                if '$' in value2:
                                    for ukey, uvalue in udatadic.items():
                                        if ukey in value2:
                                            value1[key2] = value2.replace(ukey, uvalue)

                    else:
                        if '$' in value1:
                            for ukey, uvalue in udatadic.items():
                                if ukey in value1:
                                    value[key1] = value1.replace(ukey, uvalue)

            else:
                if '$' in value:
                    for ukey, uvalue in udatadic.items():
                        if ukey in value:
                            data_dict[key] = value.replace(ukey, uvalue)

        if '$' in str(data_dict):
            LogMsg.logger.error('获取参数值失败,可能含有二次包装数据,请再次调用 ' + str(data_dict))

        else:
            LogMsg.logger.info(data_dict)
        datadict['Request_Body'] = data_dict
        return datadict
    else:

        LogMsg.logger.warn('用例无请求数据')
        return datadict





