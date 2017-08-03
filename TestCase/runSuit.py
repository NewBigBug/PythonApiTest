# -*- coding: utf-8 -*-
# @Time    : 2017/8/3 9:40
# @Author  : Charles
# @File    : runSuit.py
# @Software: PyCharm

import unittest
import time
import ApiTest_01
import HTMLTestRunner_u
import SendEmail


# 组建测试suite
def suite():
    suite = unittest.TestLoader().loadTestsFromTestCase(ApiTest_01.ServerTest)
    return suite

# 执行测试集合，生成报告，发送邮件
if __name__ == '__main__':
    today = time.strftime('%Y%m%d_%H', time.localtime(time.time()))
    tempfile = '..\output\\tempyaml.yaml'
    reportPath = '..\output\\' + 'API_TEST_' + today + '.html'
    logFilePath = '..\output\\' + 'API_TEST_' + today + '.log'
    fp = open(reportPath, mode='wb')
    runner = HTMLTestRunner_u.HTMLTestRunner(stream=fp, title='Api Test Report', description='接口测试报告', tempfile=tempfile)
    runner.run(suite())
    fp.close()
    SendEmail.post_mail(reportPath, logFilePath)