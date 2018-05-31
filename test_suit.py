# -*- coding: utf-8 -*-
# @created on 2018/3/14 下午6:47
# @author:Eddie
# Project:使用unnitest框架编写测试用例思路
import HTMLReport
from HTMLReport import logger
import unittest
#from Xingren.chat import *
#from demo.test import *
#from Xingren.login import *
#from Xingren.payment import *
from collect_drugs import *
from add_Taoc import *
from search_drugs import *


# 测试报告
if __name__ == '__main__':

    suite = unittest.TestSuite()

    # tests = [Test("test_register"), Test("create_phone"), Test("test_case1"), Test("test_case2"),Test("test_case3"), Test("test_login"), Test("test_case4"), Test("test_case5")]
    # tests = [Test("test_case2"), Test("test_case3"), Test("test_case4"), Test("test_case5")]
    # tests = [Test("findElement"), Test("test_register"), Test("create_phone"), Test("test_case1"), Test("test_case2"), Test("test_case3"), Test("test_login"), Test("test_case4"), Test("test_case5")
    tests = [SearchDrugs("test_case1"), SearchDrugs("test_case5"), SearchDrugs("test_case6")]
    # tests = [Test("test_case1"), Test("test_case2"), Test("test_case3"), Test("test_case4"), Test("test_case5")]
    suite.addTests(tests)

    runner = HTMLReport.TestRunner(report_file_name='test',  # 报告文件名，默认“test”
                                   output_path='/Users/liuchang/Desktop/report',  # 保存文件夹名，默认“report”
                                   #verbosity=2,  # 控制台输出详细程度，默认 2
                                   title='测试报告',  # 报告标题，默认“测试报告”
                                   description='app登陆等一系列功能回归测试',  # 报告描述，默认“无测试描述”
                                   thread_count=1,  # 并发线程数量（无序执行测试），默认数量 1
                                   sequential_execution=True  # 是否按照套件添加(addTests)顺序执行，会等待一个addTests执行完成，再执行下一个，默认 False
                                   )
    runner.run(suite)
