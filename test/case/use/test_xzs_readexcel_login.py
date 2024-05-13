import requests

import ddt

from lib import read_excel
from lib.db import *
from lib.case_log import *
from config.config import *
# 方法1
# class MyTestCase(unittest.TestCase):
#     @classmethod
#     def setUpClass(cls):
#         cls.r = read_excel.readexcel()
#         cls.l = cls.r.excel_to_list("test_user_data.xlsx", "test_user_login")
#
#     def test_login_ok(self):
#         login1=self.r.get_test_data(self.l,"login_ok")
#
#         url=login1.get("url")
#         # 获取是字符串格式
#
#         args=login1.get("args")
#         print(args)
#         res=login1.get("expect_login")
#         # 将字符串转化字典
#         a=json.loads(args)
#         # 提取提交参数中的username值
#         name=a.get("userName")
#
#         # 测试完成后，还原数据
#         del_user(name)
#
#     def test_login_err1(self):
#         login1=self.r.get_test_data(self.l,"login_err_01")
#         # print(reg1)
#         url=login1.get("url")
#         # 获取字符串格式
#         args=login1.get("args")
#         res=login1.get("expect_login")
#         # 将字符串转化字典
#         a=json.loads(args)
#
#         r=requests.post(url,json=a)
#
#         self.assertIn(res,r.text)
#     def test_login_err2(self):
#         login1=self.r.get_test_data(self.l,"login_err_02")
#         # print(reg1)
#         url=login1.get("url")
#         # 获取字符串格式
#         args=login1.get("args")
#         res=login1.get("expect_login")
#         # 将字符串转化字典
#         a=json.loads(args)
#
#         r=requests.post(url,json=a)
#
#         self.assertIn(res,r.text)
#     def test_login_err3(self):
#         login1=self.r.get_test_data(self.l,"login_err_03")
#         # print(reg1)
#         url=login1.get("url")
#         # 获取字符串格式
#         args=login1.get("args")
#         res=login1.get("expect_login")
#         # 将字符串转化字典
#         a=json.loads(args)
#
#         r=requests.post(url,json=a)
#
#         self.assertIn(res,r.text)
#     def test_login_err4(self):
#         login1=self.r.get_test_data(self.l,"login_err_04")
#         # print(reg1)
#         url=login1.get("url")
#         # 获取字符串格式
#         args=login1.get("args")
#         res=login1.get("expect_login")
#         # 将字符串转化字典
#         a=json.loads(args)
#
#         r=requests.post(url,json=a)
#
#         self.assertIn(res,r.text)
#



# 方法2

# @ddt.ddt
# class MyTestCase(unittest.TestCase):
#     @classmethod
#     def setUpClass(cls):
#         cls.r = read_excel.readexcel()
#         cls.l = cls.r.excel_to_list("test_user_data.xlsx", "test_user_login")
#     @ddt.data("login_ok","login_err_01","login_err_02","login_err_03","login_err_04")
#     def test_login(self,name):
#         login1=self.r.get_test_data(self.l,name)
#         url=login1.get("url")
#         # 获取是字符串格式
#         args=login1.get("args")
#         a = json.loads(args)
#         res=login1.get("expect_login")
#         req=requests.post(url,json=a)
#         self.assertIn(res,req.text)


def read():
    r= read_excel.readexcel()
    l=r.excel_to_list(data_file, "test_user_login")
    t=[]
    for i in range(len(l)):
        t.append(l[i]["case_name"])
    print(t)
    return t
@ddt.ddt()
class MyTestCase(unittest.TestCase):
    @ddt.data(*read())
    def test_login(self, name):
        r= read_excel.readexcel()
        l=r.excel_to_list(data_file, "test_user_login")
        t=r.get_test_data(l,name)
        url=t.get("url")
        data=t.get("args")
        d=json.loads(data)
        exp=t.get("expect_login")
        req=requests.post(url,json=d)
        log_case_info(name,url,d,exp,req.text)
        self.assertIn(exp,req.text)



if __name__ == '__main__':
    unittest.main()

