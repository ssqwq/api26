#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2024/4/15 15:28
# Author    : weixinlan
# @File     : post的请求-传统表单.py
# @Software : PyCharm
import requests

url="http://httpbin.org/post"

data = {
    "name":"zhangsan",
    "age":"18"
}

# 传统表单
r=requests.post(url=url,data=data)

print(r.text)