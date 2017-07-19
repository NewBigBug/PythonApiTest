import unittest
import requests
import CaseGoto
import CaseInteg
import UserParam
import FileController
import ddt
import LogMsg
import ResultGenerate
import HTMLTestRunner1
import time

"""
requests库的session对象能够帮我们跨请求保持某些参数，也会在同一个session实例发出的所有请求之间保持cookies。
"""
# 用例通用字典
udatadic = {}
case_result_list = []
# 获取基础用例集合
cago = CaseGoto.case_goto()
usrconfig = cago[0]
configdatadic = cago[1]
case_lines_list = cago[2]
config = cago[3]
# 用户全局变量
udatadic.update(configdatadic)


@ddt.ddt
class ServerTest(unittest.TestCase):
    def setUp(self):
        self.api_client = requests.Session()

    @ddt.data(*case_lines_list)
    def test_api_rq(self, case_line):
        uspa = UserParam.param_generate()
        case_result = CaseInteg.case_Prepare(self.api_client, case_line, udatadic, uspa, usrconfig, config)
        resp = case_result[0]
        respdict = case_result[1]
        case_info = case_result[2]

        collectionparm = {}
        check_diff = {}
        checkpoint = respdict['Checkpoint']
        needcollection = []

        """
        # 先判断返回值resp的内容格式，收集参数只支持json
        """
        #API_Purpose = case_info['CaseName']
        if 'Response_Type' in respdict.keys() and (respdict['Response_Type'] is not None):
            if respdict['Response_Type'] == 'Html':
                if 'Need_Collection' in respdict.keys() and (respdict['Need_Collection'] is not None):
                    LogMsg.logger.info('Response_Type:Html 不支持参数收集')
                else:
                    resptext = [resp.status_code, resp.text]
                    LogMsg.logger.info(resptext)
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
                LogMsg.logger.info(respjson)
                respjson['status_code'] = resp.status_code

                for key, point in checkpoint.items():
                    self.assertTrue(key in respjson, '未找到参数')
                    resppame = respjson[key]
                    self.assertEquals(resppame, point, 'respdata: ' + resppame + 'Checkdata: ' + point + ' 比对失败')
                    check_diff = {
                        'checkresult': 'Pass'
                    }
                for i in range(len(needcollection)):
                    key = needcollection[i]
                    if key in respjson:
                        collectionparm['$' + key + '$'] = respjson[key]
                    else:
                        LogMsg.logger.info('返回值中不存在该参数 ' + key)
        else:
            LogMsg.logger.error('用例中未指定 Response_Type 类型')
        LogMsg.logger.info(collectionparm)
        if check_diff:
            case_rs = ResultGenerate.result_generate(case_info, check_diff)
            LogMsg.logger.info('返回值已处理')

            case_result_list.append(case_rs[0])
            udatadic.update(collectionparm)
            FileController.write_result_to_excel(config['tempfile'], case_result_list)

    def tearDown(self):
        self.api_client.close()


