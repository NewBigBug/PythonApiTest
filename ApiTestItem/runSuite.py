# -*- coding: utf-8 -*-
# @Time    : 2017/8/3 9:40
# @Author  : Charles
# @File    : runSuit.py
# @Software: PyCharm
import os
import unittest
import time

import ApiTest_Ufo
import HTMLTestRunner_u
import SendEmail
import ApiTest_Qone


# 组建测试suite
def suite():
    # Test集合
    testlist = ['ApiTest_Qone.QoneApiTest', 'ApiTest_Ufo.UfoApiTest', 'ApiTest_Nauth.NauthApiTest']
    suite = unittest.TestLoader().loadTestsFromNames(testlist)
    return suite


# 执行测试集合，生成报告，发送邮件
if __name__ == '__main__':
    today = time.strftime('%Y%m%d_%H%M', time.localtime(time.time()))
    tempfile = '..\output\\runtemp.yaml'
    reportPath = '..\output\\' + 'API_TEST_' + today + '.html'
    logFilePath = '..\output\\' + 'API_TEST_' + today + '.log'
    fp = open(reportPath, mode='wb')
    runner = HTMLTestRunner_u.HTMLTestRunner(stream=fp, verbosity=2, title='Api Test Report', description='接口测试报告',
                                             tempfile=tempfile)
    runner.run(suite())
    fp.close()
    # 删除临时文件
    os.remove(tempfile)
    # 发送报告邮件
    #SendEmail.post_mail(reportPath, logFilePath)
