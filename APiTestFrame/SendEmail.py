# -*- coding: UTF-8 -*-
# @Time    : 2017/8/2 16:21
# @Author  : Charles
# @File    : SendEmail.py
# @Software: PyCharm

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import FileController


def post_mail(reportFile, logFile):
    subject = 'ApiTest-接口自动化测试报告'
    sender = 'BigBug@quarkfinance.com'
    receiver = ['shuangshuangwei@quarkfinance.com']
    mailToCc = ['V-YunLiu@quarkfinance.com']

    smtpserver = 'mail.quarkfinance.com'
    smtpserver_port = '25'

    username = ''
    password = ''

    # 创建一个带附件的邮件实例
    msg = MIMEMultipart()
    # 创建邮件内容
    log_stream = FileController.load_text_file(logFile)
    report_stream = FileController.load_html_file(reportFile)
    # 邮件正文
    report_stream = report_stream.replace("class=\'hiddenRow\'", "class=\''")
    msgzw = MIMEText(report_stream, 'html', 'utf-8')
    msg.attach(msgzw)
    # 邮件附件
    msg_logfile = MIMEText(log_stream)
    msg_logfile.add_header('Content-Disposition', 'attachment', filename='APITest执行日志.log')
    msg_report = MIMEText(report_stream)
    msg_report.add_header('Content-Disposition', 'attachment', filename='APITest执行报告.html')
    msg.attach(msg_logfile)
    msg.attach(msg_report)

    # 构造邮件
    msg['Subject'] = subject
    msg['From'] = 'ApiTest'
    msg['To'] = ';'.join(receiver)
    msg['Cc'] = ';'.join(mailToCc)
    smtp = smtplib.SMTP()
    smtp.connect(smtpserver, smtpserver_port)
    # smtp.login(username, password)
    smtp.sendmail(sender, receiver + mailToCc, msg.as_string())

    smtp.quit()







