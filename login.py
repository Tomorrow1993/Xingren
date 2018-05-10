# -*- coding: UTF-8 -*-
#from selenium import webdriver
'''
created on 2017-12-7
@author:Eddie
Project:使用unnitest框架编写测试用例思路
'''
import unittest
import requests
import random
import selenium.common.exceptions
from Xingren.config import *
from time import sleep
from selenium import webdriver
from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support import expected_conditions as EC


class Test(unittest.TestCase):

	'''//拎到了config里面
	def findelementbyid(self, element):
		try:
			WebDriverWait(driver,20).until(EC.visibility_of_element_located((By.ID,element)))
			return True
		except selenium.common.exceptions.TimeoutException:
			return False
		except selenium.common.exceptions.NoSuchElementException:
			return False
'''
	def test_register(self):#判断是否有欢迎页，然后注册
		if self.findelementbyid('com.kanchufang.privatedoctor:id/lrchoose_register_btn'):
			driver.find_element_by_id("com.kanchufang.privatedoctor:id/lrchoose_register_btn").click()
			driver.find_element_by_id("com.kanchufang.privatedoctor:id/register_hint_dialog_start_btn").click()
		else:
			driver.find_element_by_id("com.kanchufang.privatedoctor:id/login_register_tv").click()
			driver.find_element_by_id("com.kanchufang.privatedoctor:id/register_hint_dialog_start_btn").click()

	def create_phone(self):#随机生成手机号
		str = '0123456789'
		top = '210'
		self.phone = top + "".join(random.choice(str) for i in range(8))
		self.password = 'qqqqqq'
		self.name = 'test'


	def test_case1(self):  # 注册
		self.create_phone()
		el1 = driver.find_element_by_id("com.kanchufang.privatedoctor:id/et_phone")
		el1.click()
		el1.send_keys(self.phone)

		el2 = driver.find_element_by_id("com.kanchufang.privatedoctor:id/et_password")
		el2.click()
		el2.send_keys(self.password)

		el3 = driver.find_element_by_id("com.kanchufang.privatedoctor:id/et_confirm_password")
		el3.click()
		el3.send_keys(self.password)

		el4 = driver.find_element_by_id("com.kanchufang.privatedoctor:id/et_validation_captcha")
		el4.click()
		el4.send_keys("aaaa")

		el5 = driver.find_element_by_id("com.kanchufang.privatedoctor:id/btn_next")
		el5.click()
		'''
		driver.find_element_by_id("com.kanchufang.privatedoctor:id/warn_dialog_yes_btn").click()

		el4.send_keys("1111")
		el5.click()

		#调用注册API
		payload = {'phone':phone,'password':password}
		r = requests.post('https://yisheng.aihaisi.com/api/register/test',data = payload)
		
		'''
	def test_case2(self):#填写个人信息
		self.create_phone()
		WebDriverWait(driver,5).until(EC.visibility_of_element_located((By.ID,"com.kanchufang.privatedoctor:id/btn_start_trust_doctor")))
		name = 'test'
		#sleep(9)
		el6 = driver.find_element_by_id("com.kanchufang.privatedoctor:id/et_name")
		el6.click()
		el6.send_keys(self.name)

		driver.find_element_by_id("com.kanchufang.privatedoctor:id/ll_set_hosptial").click()
		sleep(3)
		driver.find_element_by_xpath("//*[@text='上海']").click()
		sleep(1)
		driver.find_element_by_xpath("//*[@text='上海市']").click()
		sleep(1)
		driver.find_element_by_xpath("//*[@text='黄浦区']").click()
		sleep(1)
		driver.find_element_by_xpath("//*[@text='上海长征医院']").click()

		self.assertEqual(driver.find_element_by_id("com.kanchufang.privatedoctor:id/tv_select_hosptial").text,"上海长征医院","执业点pass")
		
		driver.find_element_by_id("com.kanchufang.privatedoctor:id/ll_set_depart").click()
		sleep(1)
		driver.find_element_by_xpath("//*[@text='泌尿外科/男科']").click()
		sleep(1)
		driver.find_element_by_xpath("//*[@text='男科']").click()
		#assertEqual(driver.find_element_by_id("com.kanchufang.privatedoctor:id/ll_set_depart").text,"男科","科室lose")

		driver.find_element_by_id("com.kanchufang.privatedoctor:id/ll_set_position").click()
		driver.find_element_by_xpath("//*[@text='主任医师']").click()
		#assertEqual(driver.find_element_by_id("com.kanchufang.privatedoctor:id/ll_set_depart").text,"主任医师","职称lose")

		driver.find_element_by_id("com.kanchufang.privatedoctor:id/btn_start_trust_doctor").click()

		#assertIsNone(driver.find_element_by_id('com.kanchufang.privatedoctor:id/tab_home_rb'),"登录失败")
		

	def	test_case3(self):#切换到我tab，退出登录
		WebDriverWait(driver,20).until(EC.visibility_of_element_located((By.ID,"com.kanchufang.privatedoctor:id/tab_me_rb")))
		driver.find_element_by_id("com.kanchufang.privatedoctor:id/tab_me_rb").click()
		driver.find_element_by_id("com.kanchufang.privatedoctor:id/menu_setting").click()
		sleep(2)
		el6 = driver.find_element_by_id("com.kanchufang.privatedoctor:id/tv_modify_password")
		el7 = driver.find_element_by_id("com.kanchufang.privatedoctor:id/layout_flow_mode")
		driver.scroll(el7,el6)

		#driver.swipe(500,1500,500,500,1000)
		driver.find_element_by_id("com.kanchufang.privatedoctor:id/btn_logout").click()
		sleep(1)
		driver.find_element_by_id("android:id/button1").click()
		sleep(5)

	def test_login(self):  # 判断是否有欢迎页，然后登录
			if self.findelementbyid('com.kanchufang.privatedoctor:id/lrchoose_login_btn'):
				driver.find_element_by_id("com.kanchufang.privatedoctor:id/lrchoose_login_btn").click()
			else:
				pass
	def test_case4(self):# 登录
		el10 = driver.find_element_by_id("com.kanchufang.privatedoctor:id/password_et")
		el10.click()
		el10.send_keys('qqqqqq')
		'''
		if el8.is_displayed():
			el8.click()
			el9.click()
			el9.send_keys(phone)
		else:
			el10.click()
			el9.click()
			el9.send_keys(phone)
		el10 = driver.find_element_by_id("com.kanchufang.privatedoctor:id/password_et")
		el10.click()
		el10.send_keys(password)
		'''
		driver.find_element_by_id("com.kanchufang.privatedoctor:id/login_btn").click()
		#WebDriverWait(driver,20).until(EC.visibility_of_element_located((By.ID,"com.kanchufang.privatedoctor:id/tab_home_rb")))
		#assertIsNotNone(driver.find_element_by_id("com.kanchufang.privatedoctor:id/tab_home_rb"),'登录失败')
	

	def test_case5(self):#认证
		WebDriverWait(driver,20).until(EC.visibility_of_element_located((By.ID,"com.kanchufang.privatedoctor:id/tab_home_rb")))
		driver.find_element_by_id("com.kanchufang.privatedoctor:id/tab_me_rb").click()
		driver.find_element_by_id("com.kanchufang.privatedoctor:id/tv_edit_profile").click()
		
		el11 = driver.find_element_by_xpath("//*[@text='医生认证']")
		el11.click()
		el12 = driver.find_element_by_id("com.kanchufang.privatedoctor:id/btn_upload")
		el12.click()
		el13 = driver.find_element_by_xpath("//*[@text='相册']")
		el13.click()
		sleep(1)
		el14 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.support.v7.widget.RecyclerView/android.widget.RelativeLayout[1]/android.widget.RelativeLayout/android.widget.CheckBox")
		el15 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.support.v7.widget.RecyclerView/android.widget.RelativeLayout[2]/android.widget.RelativeLayout/android.widget.CheckBox")
		el14.click()
		el16 = driver.find_element_by_id("com.kanchufang.privatedoctor:id/select")
		el16.click()
		WebDriverWait(driver,20).until(EC.visibility_of_element_located((By.XPATH,"//*[@text='发送']")))
		driver.find_element_by_id("com.kanchufang.privatedoctor:id/btn_upload").click()
		driver.find_element_by_id("android:id/button1").click()
		WebDriverWait(driver,20).until(EC.visibility_of_element_located((By.ID,"com.kanchufang.privatedoctor:id/btn_auth_verify")))
		#assertIsNotNone(driver.find_element_by_xpath("//*[@text='您的认证正在审核中…']"),'普通认证提交失败')
		el17 = driver.find_element_by_id("com.kanchufang.privatedoctor:id/btn_auth_verify")
		el17.click()
		
		WebDriverWait(driver,20).until(EC.visibility_of_element_located((By.ID,"com.kanchufang.privatedoctor:id/btn_upload")))
		el12.click()
		el13 = driver.find_element_by_xpath("//*[@text='相册']")
		el13.click()
		el14.click()
		el15.click()
		el16.click()
		WebDriverWait(driver,20).until(EC.visibility_of_element_located((By.XPATH,"//*[@text='发送']")))
		el12.click()
		driver.find_element_by_id("android:id/button1").click()
		WebDriverWait(driver,20).until(EC.visibility_of_element_located((By.ID,"android:id/message")))
		#assertIsNotNone(driver.find_element_by_xpath("//*[@text='上传成功，请耐心等待审核。']"),'权威认证提交失败')