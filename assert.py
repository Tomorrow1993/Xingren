# -*- coding: utf-8 -*-
# @created on 2018/3/13 下午4:55
# @author:Eddie
# from selenium import webdriver
# Project:使用unnitest框架编写测试用例思路

import unittest
class  Test(unittest.TestCase):
    def test1(self):
        a = "hello"
        b = "world"
        self.assertEqual(a,b,"ab不相等")
    def test2(self):
        c = "1"
        d = "r"
        self.assertEqual(c,d,"cd不相等")
    def test3(self):
        e = "1"
        f = "1"
        self.assertEqual(e,f,"ef相等")

if __name__ == '__main__':
    unittest.main()

