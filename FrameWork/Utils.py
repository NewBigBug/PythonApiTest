# -*- coding: utf-8 -*-
# @Time    : 2017/7/12 11:53
# @Author  : Charles
# @File    : Utils.py
# @Software: PyCharm






#比对checkpoint和返回值属性
def generate_checkresult(resp, checkpoint):
    json_diff = {}

    respjson = resp.json()
    for key, point in checkpoint.items():
        if key in respjson:
            resppame = respjson[key]
            if str(resppame) != str(point):
                json_diff[key] = {
                    'respdata': resppame,
                    'checkdata': point,
                    'checkresult': False
                }
            else:
                json_diff[key] = {
                    'respdata': resppame,
                    'checkdata': point,
                    'checkresult': True
                }
        else:
            json_diff[key] = {
                'checkdata': point,
                'checkresult': 'Checkpoint is not exist!'
            }

    return json_diff
