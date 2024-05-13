#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2024/4/15 15:32
# Author    : weixinlan
# @File     : post-json.py
# @Software : PyCharm
import requests

url="http://httpbin.org/post"
data = '''{
    "name":"zhangsan",
    "age":"18"
}'''
'{"name:"zhangsan","age":"18"}'

r=requests.post(url=url,data=data)

print(r.text)