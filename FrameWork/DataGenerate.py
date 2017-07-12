# -*- coding: utf-8 -*-
# @Time    : 2017/7/12 14:14
# @Author  : Charles
# @File    : DataGenerate.py
# @Software: PyCharm

"""
根据不同的request类型，分别处理请求数据
目前使用request库，不需要对data类型数据进行urlencode转码
处理请求中的参数化字段
"""

#将需要参数化的值用Utils中的参数化方法替换掉，%标识的为需要参数化的数据
#将依赖其他接口返回收集值的参数替换，$标识的为依赖参数

def data_para(datadic):
    for key,value in  datadic:
        if '%' in value:

    pass

def data_froms(datahavapara):
    pass

def data_json(datahavapara):
    pass

def generate_data(datatype, datadic):
    datahavapara=data_para(datadic)
    typestr_forms = ('Forms', 'forms', 'FORMS')
    typestr_json=('Json','json','JSON')
    if type in typestr_forms:
        requestdata=data_froms(datahavapara)
    else:
        requestdata=data_json(datahavapara)
    return


