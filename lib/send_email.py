#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2024/4/28 14:37
# Author    : weixinlan
# @File     : send_email.py
# @Software : PyCharm

import smtplib
# 邮箱专门的MIME格式
from  email.mime.text import MIMEText
# 支持附件
from email.mime.multipart import MIMEMultipart
# 使用中文邮箱主题
from email.header import Header
from config.config import *

def send_email(report_file):

    # 获取文件 放到变量email_body
    with open(report_file, encoding='utf-8') as f:
        # 读取文件
        email_body = f.read()
    # 编写邮箱内容   plain是普通文本格式邮箱内容
    #
    msg = MIMEMultipart()
    msg.attach(MIMEText(email_body, 'html', 'utf_8'))
    # 组装Email头  发件人  收件人 主题
    # 发件人邮箱
    msg['From'] = smtp_user
    # 收件人邮箱
    msg['To'] = receive

    msg['Subject'] = Header(subject, 'utf-8')

    # 上传附件
    # 构造附件1 传送当前目录下的report文件
    att1 = MIMEText(open(report_file, 'rb').read(), 'base64', 'utf-8')
    att1["Content-Type"] = 'application/octer-stream'
    att1["Content-Disposition"] = 'attachment:filename="report.html"'
    msg.attach(att1)

    # 连接SMTP服务器发送邮件
    # SMTP服务器地址 使用ssl模式
    smtp = smtplib.SMTP_SSL(smtp_server)
    # 登录邮箱
    smtp.login(smtp_user, smtp_ps)
    # 发送方邮箱和授权码
    smtp.sendmail(sender, receive, msg.as_string())
    smtp.quit()


if __name__ == '__main__':
    send_email("../report/report.html")