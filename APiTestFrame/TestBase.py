# -*- coding: utf-8 -*-
# @Time    : 2017/8/7 17:45
# @Author  : Charles
# @File    : BaseTest.py
# @Software: PyCharm

import CaseInteg
import LogMsg
import unittest
import Utils


class TestBase(unittest.TestCase):

    def casetestBase(self, api_client, configdatadic, udatadic_colle, case_line, usrconfig, config, run_load_list):
        # 用户参数库
        udatadic = {}
        udatadic.update(configdatadic)
        udatadic.update(udatadic_colle)
        LogMsg.logger.info('当前参数库： ' + str(udatadic))
        # 执行请求
        case_result = CaseInteg.case_Prepare(api_client, case_line, udatadic, usrconfig,
                                             config, run_load_list)
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
                if 'Equal' in checkpoint and checkpoint['Equal']:
                    self.assertIn('status_code', checkpoint['Equal'], 'status_code检查内容为空')
                    self.assertEqual(checkpoint['Equal']['status_code'], resptext[0], '检查点比对失败')
                else:
                    LogMsg.logger.info('检查点中不包含equal对比内容！')

                if 'In' in checkpoint and checkpoint['In']:
                    checkin_list = checkpoint['In']
                    for i in range(len(checkin_list)):
                        self.assertIn(checkin_list[i], resptext[1], '检查点比对失败,检查值： ' + checkin_list[i])
                else:
                    LogMsg.logger.error('检查点中不包含In对比内容！')
                    #self.assertIsNone(checkpoint, '检查点内容格式不正确')
                    #self.assertIsNotNone(checkpoint, '检查点内容为空')

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
            else:
                LogMsg.logger.info('检查点中不包含equal对比内容！')

            if 'In' in checkpoint and checkpoint['In']:
                checkin_list = checkpoint['In']
                for i in range(len(checkin_list)):
                    self.assertIn(checkin_list[i], resptext, '检查点比对失败' + ' 检查值： ' + checkin_list[i])
            else:
                LogMsg.logger.error('检查点中不包含In对比内容！')

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
        udatadic_colle.update(collectionparm)

