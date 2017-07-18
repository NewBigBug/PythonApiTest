# -*- coding: utf-8 -*-
# @Time    : 2017/7/18 9:16
# @Author  : Charles
# @File    : SendMail.py
# @Software: PyCharm

# 发送通知邮件
import smtplib
from email.mime.text import MIMEText

"""
def sendMail(text):
    sender = 'shuangshuangwei@quarkfinance.com'
    receiver = ['@myhost.cn']
    mailToCc = ['@myhost.cn']
    subject = '[AutomantionTest]接口自动化测试报告通知'
    smtpserver = 'smtp.exmail.qq.com'
    username = '@.cn'
    password = 'password'

    msg = MIMEText(text, 'html', 'utf-8')
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = ';'.join(receiver)
    msg['Cc'] = ';'.join(mailToCc)
    smtp = smtplib.SMTP()
    smtp.connect(smtpserver)
    smtp.login(username, password)
    smtp.sendmail(sender, receiver + mailToCc, msg.as_string())
    smtp.quit()


def main():
    errorTest = runTest('TestCase/TestCasePre.xlsx')
    if len(errorTest) > 0:
        html = '<html><body>接口自动化定期扫描，共有 ' + str(len(
            errorTest)) + ' 个异常接口，列表如下：' + '</p><table><tr><th style="width:100px;">接口</th><th style="width:50px;">状态</th><th style="width:200px;">接口地址</th><th>接口返回值</th></tr>'
        for test in errorTest:
            html = html + '<tr><td>' + test[0] + '</td><td>' + test[1] + '</td><td>' + test[2] + '</td><td>' + test[
                3] + '</td></tr>'
        html = html + '</table></body></html>'
        # sendMail(html)

"""