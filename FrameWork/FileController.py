# -*- coding: utf-8 -*-
# @Time    : 2017/7/12 11:53
# @Author  : Charles
# @File    : FileController.py
# @Software: PyCharm

import ast
import os

import xlrd as xlrd
import xlwt
import yaml
import LogMsg


# 加载yaml
def load_yaml_file(yaml_file):
    with open(yaml_file, mode='r', encoding='utf-8') as stream:
        LogMsg.logger.info('读取yaml文件：' + yaml_file)
        return yaml.load(stream)


# 创建yaml文件
def create_yaml_file(yaml_file):
    with open(yaml_file, mode='x', encoding='utf-8'):
        LogMsg.logger.info('创建yaml文件：' + yaml_file)


# 写入yaml文件
def write_yaml_file(data, yaml_file):
    with open(yaml_file, mode='a', encoding='utf-8') as stream:
        LogMsg.logger.info('写入yaml文件：' + yaml_file)
        return yaml.dump(data, stream)


# 加载excel
def load_excel_file(excel_file):
    with xlrd.open_workbook(excel_file) as stream:
        LogMsg.logger.info('读取excel文件：' + excel_file)
        return stream


# 写入excel
def write_excle_file():
    workbook = xlwt.Workbook()
    return workbook


# 加载传入yamlcase文件夹
def load_foler_files(folder_path):
    file_list = []
    LogMsg.logger.info('读取用例文件夹：' + folder_path)
    for dirpath, dirnames, filenames in os.walk(folder_path):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            LogMsg.logger.info('用例文件列表: ' + file_path)
            file_list.append(file_path)
    return file_list


# 根据传入的路径类型处理用例文件，文件夹(仅支持yaml)/单个文件,同时将filepaht作为key，用例内容dict作为value，返回值为dict
# 如果文件为excel，会有存在多个sheet页测试数据的情况，每个sheet页做一个键值对
# yaml和excel输出的均为字典类型，完全一致
"""
若需增加字段，直接添加yaml和excl文件，该方法无需修改
返回值为dict，格式：
{'..\\TestCase\\TestData\\case.yaml': 
    {'No.1': 
        {
            'API_Purpose': 'login', 
            'Request_Url': '/api/users', 
            'Request_method': 'POST', 
            'Header': {'Accept': '', 'Accept-Encoding': '', 'Accept-Language': '', 'User-Agent': ''}, 
            'Body_Type': 'Forms', 
            'Request Body': {'name': 'user1', 'password': '123456'}, 
            'Need_Cookie': 'TRUE', 
            'Need_Sign': 'TRUE', 
            'Need_Collection': {'param1': '123', 'param2': '123'}, 
            'Depends': '/api/login,/api/reg', 
            'Response_Type': 'Html', 
            'Checkpoint': {'param1': '123', 'param2': '123'}, 
            'Active': 'TRUE'
        }
    }
}
"""


def load_case_by_path(path):
    file_casedict = {}
    if os.path.isdir(path):
        casefile_list = load_foler_files(path)
        for i in range(len(casefile_list)):
            file_casedict = load_case_by_path(casefile_list[i])

    elif os.path.isfile(path):
        file_suffix = os.path.splitext(path)[1]
        if file_suffix in ['.yaml', '.yml']:
            file_casedict[path] = load_yaml_file(path)
        elif file_suffix in ['.xlsx', '.xls']:
            xlrd_stream = load_excel_file(path)
            for i in range(len(xlrd_stream.sheets())):
                sheetname = xlrd_stream.sheet_by_index(i).name
                taledata = xlrd_stream.sheet_by_index(i)
                case_line_no = {}
                for j in range(1, taledata.nrows):
                    case_line = {}
                    for c in range(1, taledata.ncols):
                        columnname = taledata.cell(0, c).value
                        column_value = taledata.cell(j, c).value.replace('\n', '').replace('\r', '')
                        if '{' in column_value:
                            columnvalue = ast.literal_eval(column_value)
                        else:
                            columnvalue = column_value
                        case_line[columnname] = columnvalue
                    case_line_no['No.' + str(j)] = case_line
                file_casedict[path + '_' + sheetname] = case_line_no
        else:
            LogMsg.logger.error('用例文件格式不正确：' + path)

    else:
        LogMsg.logger.error("传入文件路径异常：" + path)
    return file_casedict
