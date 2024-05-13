#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2024/4/15 14:55
# Author    : weixinlan
# @File     : get请求.py
# @Software : PyCharm
import requests

url="http://httpbin.org/get"

# 发送一个get请求
r=requests.get(url)


# 解析响应对象

# 响应的文本信息
print(r.text)
# 响应二进制格式
print(r.content)
# 响应编码格式
print(r.encoding)
# 响应头部信息
print(r.headers)
# 响应状态码
print(r.status_code)
# 响应cookies
print(r.cookies)