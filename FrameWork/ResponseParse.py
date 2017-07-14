# -*- coding: utf-8 -*-
# @Time    : 2017/7/13 14:04
# @Author  : Charles
# @File    : ResponseParse.py
# @Software: PyCharm

"""
resp为结果返回值
respdict该参数应为示例字典格式
respdict={
    'Need_Collection':'param1,param2'
    'Response_Type': 'Html'
    'Checkpoint':
        param1: '123'
        param2: '123'
}
"""
import LogMsg


def response_parse(resp, respdict):
    collectionparm = {}
    check_diff = {}

    checkpoint = respdict['Checkpoint']
    needcollection = []


    """
    # 先判断返回值resp的内容格式，收集参数只支持json
    """
    if 'Response_Type' in respdict.keys() and (respdict['Response_Type'] is not None):
        if respdict['Response_Type'] == 'Html':
            resptext = [resp.status_code, resp.text]
            if 'status_code' in checkpoint.keys():
                if checkpoint['status_code'] == resptext[0]:
                    check_diff['status_code'] = {
                        'respdata': resptext[0],
                        'checkdata': checkpoint['status_code'],
                        'checkresult': True
                    }
                else:
                    check_diff['status_code'] = {
                        'respdata': resptext[0],
                        'checkdata': checkpoint['status_code'],
                        'checkresult': False
                    }
                del check_diff['status_code']
                for key, point in checkpoint.items():
                    if point in resptext[1]:
                        stindex = resptext[1].index(point)
                        cutslice = resptext[1][stindex - 15:stindex + 15]
                        check_diff[key] = {
                            'respdata': cutslice,
                            'checkdata': checkpoint[key],
                            'checkresult': True
                        }
                    else:
                        check_diff[key] = {
                            'respdata': '字符串未找到',
                            'checkdata': checkpoint[key],
                            'checkresult': False
                        }
            else:
                for key, point in checkpoint.items():
                    if point in resptext[1]:
                        stindex = resptext[1].index(point)
                        cutslice = resptext[1][stindex - 15:stindex + 15]
                        check_diff[key] = {
                            'respdata': cutslice,
                            'checkdata': checkpoint[key],
                            'checkresult': True
                        }
                    else:
                        check_diff[key] = {
                            'respdata': '字符串未找到',
                            'checkdata': checkpoint[key],
                            'checkresult': False
                        }


        elif respdict['Response_Type'] == 'Json':

            if 'Need_Collection' in respdict.keys() and (respdict['Need_Collection'] is not None):
                needcollection = respdict['Need_Collection'].split(',')
            else:
                LogMsg.logger.info('用例文件中未配置需要收集的参数，若有后续依赖，执行会报错')

            respjson = resp.json()
            respjson['status_code'] = resp.status_code

            for key, point in checkpoint.items():
                if key in respjson:
                    resppame = respjson[key]
                    if str(resppame) != str(point):
                        check_diff[key] = {
                            'respdata': resppame,
                            'checkdata': point,
                            'checkresult': False
                        }
                    else:
                        check_diff[key] = {
                            'respdata': resppame,
                            'checkdata': point,
                            'checkresult': True
                        }
                else:
                    check_diff[key] = {
                        'respdata': 'Checkpoint is not exist in respdata',
                        'checkdata': point,
                        'checkresult': False
                    }
            for i in range(len(needcollection)):
                key = needcollection[i]
                if key in respjson:
                    collectionparm['$'+key] = respjson[key]
                else:
                    LogMsg.logger.info('返回值中不存在该参数 ' + key)

    else:
        LogMsg.logger.error('用例中未指定 Response_Type 类型')

    LogMsg.logger.info(collectionparm)
    responseparse = [collectionparm, check_diff]
    return responseparse
