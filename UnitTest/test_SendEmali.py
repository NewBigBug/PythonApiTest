# -*- coding: utf-8 -*-
# @Time    : 2017/8/2 18:00
# @Author  : Charles
# @File    : test_SendEmali.py
# @Software: PyCharm
import unittest
import SendEmail


class TestSendEmail(unittest.TestCase):
    def test_sendemail(self):
        reportPath = '..\output\API_TEST_20170802_17.html'
        logFilePath = '..\output\API_TEST_20170802_17.log'

        SendEmail.post_mail(reportPath, logFilePath)