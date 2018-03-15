# -*- coding: utf-8 -*-
# @created on 2018/3/14 下午6:47
# @author:Eddie
# from selenium import webdriver
# Project:使用unnitest框架编写测试用例思路
import unittest
from login import Test

if __name__=='__main__':
    suite = unittest.TestSuite()

    tests = [Test("test_case1"),Test("test_case2")]
    suite.addTests(tests)

    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)