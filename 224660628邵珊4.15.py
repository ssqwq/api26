#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2024/4/15 16:31
# Author    : weixinlan
# @File     : 224660628邵珊4.15.py
# @Software : PyCharm
import requests

# 方法一
# url="http://192.168.55.42/Home/Goods/search.html?q=%E6%89%8B%E6%9C%BA"

# 方法二
url="http://192.168.55.42/Home/Goods/search.html"

pana={
    "q":"手机",

}




r=requests.get(url,params=pana)

print(r.text)