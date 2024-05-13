import pickle,logging,time,sys
import unittest
from lib.HTMLTestRunner import HTMLTestRunner
from lib.send_email import send_email
from config.config import *
from test.suit.test_suit import *
from test.case.use.test_user_reg1 import test_user_reg
import time
def discover():
    return unittest.defaultTestLoader.discover(test_path)
def run(suite):
    logging.info("============测试开始=============")
    with open(report_file, 'wb') as f:
        result=HTMLTestRunner(
            stream=f,
            title='接口测试',
            description='测试描述',
            verbosity=2,

        ).run(suite)
    if result.failures:
        # 保存失败用例到文件
        save_failures(result,last_fails_file)
        logging.error("测试失败,失败用例已保存到文件:{}".format(last_fails_file))
    else:
        logging.info("测试成功")
    if send_email_after_run:
        send_email(report_file)
    logging.info("=========================测试结束============================")
def run_all():
        run(discover())
def run_suite(suite_name):
    suite=get_suite(suite_name)
    print(suite)
    if isinstance(suite,unittest.TestSuite):
        run(suite)
    else:
        print("TestSuite不存在")

def collect():
    suite=unittest.TestSuite()
    def _collect(tests):
        if isinstance(tests,unittest.TestSuite): # 如果下级元素还是TestSuite则继续往下找
            if tests.countTestCases() != 0:# 如果TestSuite中有用例则继续往下找
                for i in tests:# 遍历TestSuite
                    _collect(i)# 递归调用
        else:
            suite.addTest(tests)# 如果下级元素是TestCase，则添加到TestSuite中
    _collect(discover())# unittest.defaultTestLoader.discover(tset_case_path)
    return suite
def collect_only():#仅列出所用用例
    t0 = time.time()#开始时间
    i = 0# 用例计数
    for case in collect():# 遍历TestSuite
        i += 1# 计数加1
        print("{}.{}".format(str(i),case.id()))# 输出用例名称
    print("-------------------------------------------------")
    print("Collect {} tests is {:.3f}s".format(str(i), time.time() - t0))# 输出用例总数和用时


def makesuite_by_testlist(testlist_file):
    with open(testlist_file,encoding='utf-8') as f:
        testlist=f.readlines()
    testlist=[i.strip() for i in testlist if not i.startswith("#")]
    print(testlist)
    suite=unittest.TestSuite()
    all_cases=collect()
    for case in all_cases:
        case_name=case.id().split('.')[-1]

        if case_name in testlist:
            suite.addTest(case)
    return suite

# 根据tag来组件suite
def makesuite_by_tag(tag):
    # 声明一个suite
    suite=unittest.TestSuite()
    # 获取当前所有testcase
    for i in collect():
        # tag和标签都包含的时候
        # print(i._testMethodDoc)
        if i._testMethodDoc and tag in i._testMethodDoc:
            # 添加到suite
            suite.addTest(i)
    return suite

# 保存失败用例到文件
# file为序列化保存到的文件名，配置在config/config.py里
def save_failures(result,file):
    suite=unittest.TestSuite()
    for case_result in result.failures:
        # case_result是个元组，第一个元素是用例对象，后面是失败原因等
        suite.addTest(case_result[0])
    with open(file,'wb') as f:
        # 序列化到指定文件
        pickle.dump(suite,f)

#失败用例从跑方法
def rerun_fails():
    # 将用例路径添加到搜索路径,不然反序列化TestSuite会找不到用例
    sys.path.append(test_path)
    with open(last_fails_file,'rb') as f:
        suite=pickle.load(f)
    run(suite)

def main():
    if options.collect_only:
        collect_only()
    elif options.rerun_fails:
        rerun_fails()
    elif options.makesuite_tag:
        makesuite_by_tag(options.makesuite_tag)



if __name__ == '__main__':
    # suite=makesuite_by_testlist(test_list_file)
    # suite=makesuite_by_tag("level1")

   run_all()





