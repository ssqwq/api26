import unittest

def setUpModule():
    # 当前模块执行前只执行一次
    print('===setupmodule===')
def tearDownModule():
    # 当前模块执行后只执行一次
    print('===teardownmodule===')
class MyTestCase(unittest.TestCase):
    # 在所有用例执行之前只运行一遍
    @classmethod
    def setUpClass(cls) -> None:
        print("setupclass")
        # 在所有用例执行之后只运行一遍
    @classmethod
    def tearDownClass(cls) -> None:
        print("teardownclass")
    # 在每个用例执行之前都会运行一遍
    def setUp(self) -> None:
        print("setup")
#     在每个用例执行之后都会运行一遍
    def tearDown(self) -> None:
        print("teardown")
#     所有的测试用例都以test开头
    def test_01(self):
        print("test01")
        # 比较值相等
        self.assertEqual(True,True)
    def test_02(self):
        print("test02")
        # 包含   A包含B中
        self.assertIn('h','hello')
    def test_03(self):
        print("test03")
        # 比较内存中的位置
        self.assertIsNot(2,4/2)
    def test_04(self):
        print("test04")
        # 比大小  less<    greater>    lessequal<=     grearerqual>=
        self.assertGreater(7,4)
    def test_05(self):
        print('test05')
        # 判断类型
        self.assertIsInstance({'user':'stu',"ps":'123'},dict)
if __name__ == '__main__':
    unittest.main()
