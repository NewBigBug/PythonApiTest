import unittest
import requests
import sys
import CaseGoto
import CaseInteg
import UserParam
import Utils
import ddt
import LogMsg
import ResultGenerate
import HTMLTestRunner_u
import time

"""
requests库的session对象能够帮我们跨请求保持某些参数，也会在同一个session实例发出的所有请求之间保持cookies。
"""


@ddt.ddt
class ServerTest(unittest.TestCase):

    # 获取基础用例集合
    cago = CaseGoto.case_goto()
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

        self.api_client.verify = False

    @ddt.data(*case_lines_list)
    def test_api_rq(self, case_line):

        udatadic = {}
        udatadic.update(ServerTest.configdatadic)
        udatadic.update(ServerTest.udatadic_colle)
        LogMsg.logger.info('当前参数库： ' + str(udatadic))
        # 获取用例下标
        self.caseindex = sys._getframe().f_code.co_name + '_' + str(ServerTest.case_lines_list.index(case_line) + 1001)
        LogMsg.logger.info('caseindex: ' + self.caseindex)
        # 执行请求
        case_result = CaseInteg.case_Prepare(self.api_client, case_line, udatadic, ServerTest.usrconfig,
                                             ServerTest.config, ServerTest.run_load_list)
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
                if 'status_code' in checkpoint.keys():
                    self.assertEqual(checkpoint['status_code'], resptext[0], '检查点比对失败')
                    del checkpoint['status_code']
                    for key, point in checkpoint.items():
                        self.assertIn(point, resptext[1], '检查点比对失败')
                        self.check_diff = {
                            'caseresult': 'Pass'
                        }
                else:
                    for key, point in checkpoint.items():
                        self.assertIn(point, resptext[1], '检查点比对失败')
                        self.check_diff = {
                            'caseresult': 'Pass'
                        }
        elif respdict['Response_Type'] == 'Json':
            if 'Need_Collection' in respdict and respdict['Need_Collection']:
                needcollection = respdict['Need_Collection'].split(',')
            else:
                LogMsg.logger.info('用例文件中未配置需要收集的参数，若有后续依赖，执行会报错')
            respjson = resp.json()
            LogMsg.logger.info('返回值Json字符串：' + str(respjson))
            respjson['status_code'] = resp.status_code
            # 开始断言
            checkpoint = Utils.dic_replace(checkpoint, udatadic)
            for key, point in checkpoint.items():
                resppame = Utils.list_all_dict(key, respjson)
                self.assertEqual(resppame, point, '检查点比对失败' + str(resppame) + str(point))
            self.check_diff = {
                'caseresult': 'Pass'
            }
            for i in range(len(needcollection)):
                key = needcollection[i]
                coll_key = Utils.list_all_dict(key, respjson)
                if coll_key:
                    collectionparm['$' + key + '$'] = coll_key
                else:
                    LogMsg.logger.info('返回值中不存在该参数 ' + key)
        LogMsg.logger.info('收集参数： ' + str(collectionparm))
        ServerTest.udatadic_colle.update(collectionparm)

    def tearDown(self):
        case_rs = ResultGenerate.result_generate(self.caseindex, self.case_info, self.check_diff)
        LogMsg.logger.info(case_rs)
        ServerTest.run_load_list.update(case_rs)
        #print(ServerTest.run_load_list)
        self.api_client.close()


def suite():
    suite = unittest.TestLoader().loadTestsFromTestCase(ServerTest)
    return suite


if __name__ == '__main__':
    today = time.strftime('%Y%m%d_%H_%M_%S', time.localtime(time.time()))
    tempfile = 'D:\GitPro\Python\PythonApiTest\output\\tempyaml.yaml'
    reportPath = 'D:\GitPro\Python\PythonApiTest\output\\' + 'API_TEST_' + today + '.html'
    fp = open(reportPath, mode='wb')
    runner = HTMLTestRunner_u.HTMLTestRunner(stream=fp, title='Api Test Report', description='接口测试报告',
                                             tempfile=tempfile)
    runner.run(suite())
    fp.close()
