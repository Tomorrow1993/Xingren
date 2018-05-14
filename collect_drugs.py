# -*- coding: utf-8 -*-
# @created on 2018/5/11 上午11:49
# @author:Eddie
# from selenium import webdriver
# Project:使用unnitest框架编写测试用例思路

import unittest
from config import *


class Test(unittest.TestCase):
	def test_case1(self):  # 进入西药首页
		WebDriverWait(driver, 20).until(
			EC.visibility_of_element_located((By.ID, "com.kanchufang.privatedoctor:id/tab_home_rb")))
		el1 = driver.find_element_by_id("com.kanchufang.privatedoctor:id/tab_patient_rb")
		el1.click()
		el2 = driver.find_element_by_xpath("//*[@text='test']")
		el2.click()
		el3 = driver.find_element_by_id("com.kanchufang.privatedoctor:id/cib_2")
		el3.click()

	def test_case2(self):  # 点击一项药品进行收藏
		WebDriverWait(driver, 20).until(
			EC.visibility_of_element_located((By.ID, "com.kanchufang.privatedoctor:id/yf_recommend")))
		el4 = driver.find_element_by_xpath("(//android.widget.ImageView[@content-desc='药品'])[1]")
		el4.click()
		el5 = driver.find_element_by_id("com.kanchufang.privatedoctor:id/yf_ll_collect")
		el5.click()

	def test_case3(self):  # 去我的收藏页校验
		el6 = driver.find_element_by_id("com.kanchufang.privatedoctor:id/yf_iv_close")
		el6.click()
		el7 = driver.find_element_by_id("com.kanchufang.privatedoctor:id/yf_fl_my_collect")
		el7.click()
		sleep(2)
		if findelementbyxpath("//*[@text='没有更多了']"):
			print("收藏成功")
		else:
			print("我的收藏内无记录")
