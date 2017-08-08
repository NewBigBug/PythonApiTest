# -*- coding: utf-8 -*-
# @Time    : 2017/8/8 9:21
# @Author  : Charles
# @File    : ApiTest_Nauth.py
# @Software: PyCharm

import unittest
import requests
import sys
import CaseGoto
import CaseInteg
import SendEmail
import Utils
import ddt
import LogMsg
import ResultGenerate

"""
requests库的session对象能够帮我们跨请求保持某些参数，也会在同一个session实例发出的所有请求之间保持cookies。
"""


@ddt.ddt
class NauthAPiTest(unittest.TestCase):
    # 配置文件路径
    configpath = '../TestDir/Config/config_nauth.yaml'
    # 获取基础用例集合
    cago = CaseGoto.case_goto(configpath)
    # config中host和header
    usrconfig = cago[0]
    # config中配置的用户参数字典
    configdatadic = cago[1]
    # 用例列表
    case_lines_list = cago[2]
    # config全配置内容
    config = cago[3]
    # 参数收集字典
    udatadic_colle = {}
    # 运行结果临时字典，供检查依赖接口状态
    run_load_list = {}

    def setUp(self):

        self.api_client = requests.Session()

        # self.api_client.verify = False

    @ddt.data(*case_lines_list)
    def test_api_rq_nauth(self, case_line):

        udatadic = {}
        udatadic.update(NauthAPiTest.configdatadic)
        udatadic.update(NauthAPiTest.udatadic_colle)
        LogMsg.logger.info('当前参数库： ' + str(udatadic))
        # 获取用例下标
        self.caseindex = sys._getframe().f_code.co_name + '_' + str(NauthAPiTest.case_lines_list.index(case_line) + 1001)
        LogMsg.logger.info('caseindex: ' + self.caseindex)
        # 执行请求
        case_result = CaseInteg.case_Prepare(self.api_client, case_line, udatadic, NauthAPiTest.usrconfig,
                                             NauthAPiTest.config, NauthAPiTest.run_load_list)
        resp = case_result[0]
        respdict = case_result[1]
        self.case_info = case_result[2]
        collectionparm = {}
        self.check_diff = {}
        checkpoint = respdict['Checkpoint']
        needcollection = []

        """
        # 先判断返回值resp的内容格式，收集参数只支持json
        """
        self.assertIn('Response_Type', respdict, '用例中未指定 Response_Type 类型')
        self.assertTrue(respdict['Response_Type'], '用例中未指定 Response_Type 类型')
        if respdict['Response_Type'] == 'Html':
            if 'Need_Collection' in respdict.keys() and respdict['Need_Collection']:
                LogMsg.logger.info('Response_Type:Html 不支持参数收集')
            else:
                resptext = [str(resp.status_code), resp.text]
                LogMsg.logger.info(resptext)
                if 'status_code' in checkpoint:
                    self.assertEqual(checkpoint['status_code'], resptext[0], '检查点比对失败')
                if 'In' in checkpoint and checkpoint['In']:
                    checkin_list = checkpoint['In']
                    for i in range(len(checkin_list)):
                        self.assertIn(checkin_list[i], resptext[1], '检查点比对失败' + ' 检查值： ' + checkin_list[i])
                self.check_diff = {
                    'caseresult': 'Pass'
                }
        elif respdict['Response_Type'] == 'Json':
            if 'Need_Collection' in respdict and respdict['Need_Collection']:
                needcollection = respdict['Need_Collection'].split(',')
            else:
                LogMsg.logger.info('用例文件中未配置需要收集的参数，若有后续依赖，执行会报错')
            respjson = resp.json()
            resptext = resp.text
            LogMsg.logger.info('返回值Json字符串：' + str(respjson))
            respjson['status_code'] = resp.status_code
            # 开始断言
            checkpoint = Utils.dic_replace(checkpoint, udatadic)
            if 'Equal' in checkpoint and checkpoint['Equal']:
                for key, point in checkpoint['Equal'].items():
                    resppame = Utils.list_all_dict(key, respjson)
                    self.assertEqual(resppame, point, '检查点比对失败: ' + '返回值： ' + str(resppame) + ' 检查值： ' + str(point))
            if 'In' in checkpoint and checkpoint['In']:
                checkin_list = checkpoint['In']
                for i in range(len(checkin_list)):
                    self.assertIn(checkin_list[i], resptext, '检查点比对失败' + ' 检查值： ' + checkin_list[i])
            self.check_diff = {
                'caseresult': 'Pass'
            }
            for i in range(len(needcollection)):
                key = needcollection[i]
                if key in udatadic:
                    collectionparm[key] = udatadic[key]
                else:
                    coll_key = Utils.list_all_dict(key, respjson)
                    if coll_key:
                        collectionparm['$' + key + '$'] = coll_key
                    else:
                        LogMsg.logger.error('参数未收集成功 ' + key)
        LogMsg.logger.info('收集参数： ' + str(collectionparm))
        NauthAPiTest.udatadic_colle.update(collectionparm)

    def tearDown(self):
        case_rs = ResultGenerate.result_generate(self.caseindex, self.case_info, self.check_diff)
        LogMsg.logger.info(case_rs)
        NauthAPiTest.run_load_list.update(case_rs)
        self.api_client.close()
