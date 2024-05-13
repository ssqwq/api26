#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2024/5/6 17:23
# Author    : weixinlan
# @File     : test_user_login.py
# @Software : PyCharm
from test.case.basecase import BaseCase
class test_user_login(BaseCase):
    def test_login_success(self):
        """"level1登陆成功"""
        case_data=self.get_case_data("login_ok")
        print(case_data)
        self.send_requset(case_data)
    def test_login_fail(self):
        """"level2登录失败"""
        case_data=self.get_case_data("login_err_01")
        self.send_requset(case_data)


        