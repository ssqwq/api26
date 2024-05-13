#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2024/4/27 8:47
# Author    : weixinlan
# @File     : send_email_base.py
# @Software : PyCharm
import smtplib
# 邮箱专门的MIME格式
from  email.mime.text import MIMEText
# 编写邮箱内容   plain是普通文本格式邮箱内容
msg=MIMEText('上课好无聊','plain','utf-8')
# 组装Email头  发件人  收件人 主题
# 发件人邮箱
msg['From']='3226312891@qq.com'
# 收件人邮箱
msg['To']='3226312891@qq.com'
msg['Subject']='邮箱标题'
# 连接SMTP服务器发送邮件
# SMTP服务器地址 使用ssl模式
smtp=smtplib.SMTP_SSL('smtp.qq.com')
# 发送方邮箱和授权码
smtp.login('3226312891@qq.com','ylxlwbqfvqiichdh')
#
smtp.sendmail('3226312891@qq.com','2063521091@qq.com',msg.as_string())
smtp.quit()