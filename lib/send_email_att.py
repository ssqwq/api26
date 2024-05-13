#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2024/4/27 9:32
# Author    : weixinlan
# @File     : send_email_att.py
# @Software : PyCharm
import smtplib
# 邮箱专门的MIME格式
from  email.mime.text import MIMEText
# 支持附件
from email.mime.multipart import MIMEMultipart
# 使用中文邮箱主题
from email.header import Header
# 获取文件 放到变量email_body
with open("../report/report.html", encoding='utf-8')as f:
    # 读取文件
    email_body=f.read()
# 编写邮箱内容   plain是普通文本格式邮箱内容
#
msg=MIMEMultipart()
msg.attach(MIMEText(email_body,'html','utf_8'))
# 组装Email头  发件人  收件人 主题
# 发件人邮箱
msg['From']='3226312891@qq.com'
# 收件人邮箱
msg['To']='3226312891@qq.com'

msg['Subject']=Header('接口测试报告','utf-8')


# 上传附件
# 构造附件1 传送当前目录下的report文件
att1=MIMEText(open('../report/report.html', 'rb').read(), 'base64', 'utf-8')
att1["Content-Type"]='application/octer-stream'
att1["Content-Disposition"]='attachment:filename="report.html"'
msg.attach(att1)


# 连接SMTP服务器发送邮件
# SMTP服务器地址 使用ssl模式
smtp=smtplib.SMTP_SSL('smtp.qq.com')
# 登录邮箱
smtp.login('3226312891@qq.com','ylxlwbqfvqiichdh')
#发送方邮箱和授权码
smtp.sendmail('3226312891@qq.com','3226312891@qq.com',msg.as_string())
smtp.quit()
