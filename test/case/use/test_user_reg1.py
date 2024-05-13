#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2024/5/7 9:46
# Author    : weixinlan
# @File     : test_user_reg1.py
# @Software : PyCharm
from test.case.basecase import BaseCase
from lib.db import *
import json

class test_user_reg(BaseCase):
    def test_user_reg_ok(self):
        # 注册用户
        case_data = self.get_case_data("reg_ok")
        username = json.loads(case_data["args"])["userName"]
        #print(username)
        #环境检查
        if check_user(username):
            del_user(username)
        self.send_requset(case_data)
        #数据库断言
        self.assertTrue(check_user(username))
        #数据清理
        del_user(username)

    def test_user_reg_fail(self):
        #注册用户
        case_data = self.get_case_data("reg_err")
        name = json.loads(case_data["args"])["userName"]
        print(name)
        #环境检查
        if not check_user(name):
            add_user(name,"123456")
        #SQL数据库断言
        self.assertTrue(check_user(name))
        self.send_requset(case_data)
