# -*- coding: UTF-8 -*-
#from selenium import webdriver
'''
created on 2017-12-7
@author:Eddie
Project:使用unnitest框架编写测试用例思路
'''
import unittest
import requests
import selenium.common.exceptions
from time import sleep
from selenium import webdriver
from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support import expected_conditions as EC

class Test(unittest.TestCase):
	def setUp(self):
		desired_caps = {}
		desired_caps['platformName'] = 'Android'
		desired_caps['platformVersion'] = '6.0' #6.0 4.4.2
		desired_caps['deviceName'] = 'emulator-5554' #1bf493ad c66d2f78 emulator-555444
		desired_caps['appPackage'] = 'com.kanchufang.privatedoctor'
		desired_caps['appActivity'] = '.activities.start.SplashActivity'
		desired_caps['noReset'] = 'true'
		desired_caps['clearSystemFiles'] = 'true'
		driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

	def findElement(self,element):
		try:
			WebDriverWait(self.driver,20).until(EC.visibility_of_element_located((By.ID,element)))
			return True
		except selenium.common.exceptions.TimeoutException:
			return False
		except selenium.common.exceptions.NoSuchElementException:
			return False

	#@unittest.skip('暂时跳过case1')
	def test_case1(self):#注册
		self.driver.find_element_by_id("com.kanchufang.privatedoctor:id/lrchoose_register_btn").click()
		sleep(5)
		self.driver.find_element_by_id("com.kanchufang.privatedoctor:id/register_hint_dialog_start_btn").click()
		#随机生成手机号
		str = '0123456789'
		top = '210'
		phone = top + "".join(random.choice(str) for i in range(8))
		password = 'qqqqqq'
		name = 'test'

		el1 = self.driver.find_element_by_id("com.kanchufang.privatedoctor:id/et_phone")
		el1.click()
		el1.send_keys(phone)

		el2 = self.driver.find_element_by_id("com.kanchufang.privatedoctor:id/et_password")
		el2.click()
		el2.send_keys(password)

		el3 = self.driver.find_element_by_id("com.kanchufang.privatedoctor:id/et_confirm_password")
		el3.click()
		el3.send_keys(password)

		el4 = self.driver.find_element_by_id("com.kanchufang.privatedoctor:id/et_validation_captcha")
		el4.click()
		el4.send_keys("aaaa")

		el5 = self.driver.find_element_by_id("com.kanchufang.privatedoctor:id/btn_next")
		el5.click()

		self.driver.find_element_by_id("com.kanchufang.privatedoctor:id/warn_dialog_yes_btn").click()

		el4.send_keys("1111")
		el5.click()

		'''
		#调用注册API
		payload = {'phone':phone,'password':password}
		r = requests.post('https://yisheng.aihaisi.com/api/register/test',data = payload)
		
		'''
	#@unittest.skip('暂时跳过case2')
	def test_case2(self):#填写个人信息
		
		WebDriverWait(self.driver,5).until(EC.visibility_of_element_located((By.ID,"com.kanchufang.privatedoctor:id/btn_start_trust_doctor")))	
		name = 'test'
		#sleep(9)
		el6 = self.driver.find_element_by_id("com.kanchufang.privatedoctor:id/et_name")
		el6.click()
		el6.send_keys(name)

		self.driver.find_element_by_id("com.kanchufang.privatedoctor:id/ll_set_hosptial").click()
		sleep(3)
		self.driver.find_element_by_xpath("//*[@text='上海']").click()
		sleep(1)
		self.driver.find_element_by_xpath("//*[@text='上海市']").click()
		sleep(1)
		self.driver.find_element_by_xpath("//*[@text='黄浦区']").click()
		sleep(1)
		self.driver.find_element_by_xpath("//*[@text='上海长征医院']").click()
		self.assertEqual(self.driver.find_element_by_id("com.kanchufang.privatedoctor:id/tv_select_hosptial").text,"上海长征医院","执业点pass")
		
		self.driver.find_element_by_id("com.kanchufang.privatedoctor:id/ll_set_depart").click()
		sleep(1)
		self.driver.find_element_by_xpath("//*[@text='泌尿外科/男科']").click()
		sleep(1)
		self.driver.find_element_by_xpath("//*[@text='男科']").click()
		#self.assertEqual(self.driver.find_element_by_id("com.kanchufang.privatedoctor:id/ll_set_depart").text,"男科","科室lose")

		self.driver.find_element_by_id("com.kanchufang.privatedoctor:id/ll_set_position").click()
		self.driver.find_element_by_xpath("//*[@text='主任医师']").click()
		#self.assertEqual(self.driver.find_element_by_id("com.kanchufang.privatedoctor:id/ll_set_depart").text,"主任医师","职称lose")

		self.driver.find_element_by_id("com.kanchufang.privatedoctor:id/btn_start_trust_doctor").click()

		self.assertIsNone(self.driver.find_element_by_id('com.kanchufang.privatedoctor:id/tab_home_rb'),"登录失败")
		
	@unittest.skip('暂时跳过case3')
	def	test_case3(self):#切换到我tab，退出登录
		WebDriverWait(self.driver,5).until(EC.visibility_of_element_located((By.ID,"com.kanchufang.privatedoctor:id/tv_doctor_name")))
		self.driver.find_element_by_id("com.kanchufang.privatedoctor:id/tab_me_rb").click()
		self.driver.find_element_by_id("com.kanchufang.privatedoctor:id/menu_setting").click()
		el6 = self.driver.find_element_by_id("com.kanchufang.privatedoctor:id/tv_notification_view")
		el7 = self.driver.find_element_by_id("com.kanchufang.privatedoctor:id/layout_flow_mode")
		self.driver.scroll(el7,el6)

		#self.driver.swipe(500,1500,500,500,1000)
		self.driver.find_element_by_id("com.kanchufang.privatedoctor:id/btn_logout").click()
		sleep(1)
		self.driver.find_element_by_id("android:id/button1").click()
		sleep(5)

	@unittest.skip('暂时跳过case4')
	def test_case4(self):#登录
		phone = 43354952
		password = 'qwerty'
		WebDriverWait(self.driver,5).until(EC.visibility_of_element_located((By.ID,"com.kanchufang.privatedoctor:id/lrchoose_login_btn")))
		self.driver.find_element_by_id("com.kanchufang.privatedoctor:id/lrchoose_login_btn").click()
		el8 = self.driver.find_element_by_id("com.kanchufang.privatedoctor:id/login_clear_account_ibtn")
		el9 = self.driver.find_element_by_id("com.kanchufang.privatedoctor:id/account_et")
		if el8.is_displayed():
			el8.click()
			el9.click()
			el9.send_keys(phone)
		else:
			el10.click()
			el9.click()
			el9.send_keys(phone)
		el10 = self.driver.find_element_by_id("com.kanchufang.privatedoctor:id/password_et")
		el10.click()
		el10.send_keys(password)
		self.driver.find_element_by_id("com.kanchufang.privatedoctor:id/login_btn").click()
		WebDriverWait(self.driver,20).until(EC.visibility_of_element_located((By.ID,"com.kanchufang.privatedoctor:id/tab_home_rb")))
		self.assertIsNotNone(self.driver.find_element_by_id("com.kanchufang.privatedoctor:id/tab_home_rb"),'登录失败')
	
	@unittest.skip('暂时跳过case5')
	def test_case5(self):#认证
		WebDriverWait(self.driver,20).until(EC.visibility_of_element_located((By.ID,"com.kanchufang.privatedoctor:id/tab_home_rb")))
		self.driver.find_element_by_id("com.kanchufang.privatedoctor:id/tab_me_rb").click()
		self.driver.find_element_by_id("com.kanchufang.privatedoctor:id/tv_edit_profile").click()
		
		el11 = self.driver.find_element_by_xpath("//*[@text='医生认证']")
		el11.click()
		el12 = self.driver.find_element_by_id("com.kanchufang.privatedoctor:id/btn_upload")
		el12.click()
		el13 = self.driver.find_element_by_xpath("//*[@text='相册']")
		el13.click()
		el14 = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.support.v7.widget.RecyclerView/android.widget.RelativeLayout[1]/android.widget.RelativeLayout/android.widget.CheckBox")
		el15 = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.support.v7.widget.RecyclerView/android.widget.RelativeLayout[2]/android.widget.RelativeLayout/android.widget.CheckBox")
		el14.click()
		el16 = self.driver.find_element_by_id("com.kanchufang.privatedoctor:id/select")
		el16.click()
		WebDriverWait(self.driver,20).until(EC.visibility_of_element_located((By.XPATH,"//*[@text='发送']")))
		self.driver.find_element_by_id("com.kanchufang.privatedoctor:id/btn_upload").click()
		self.driver.find_element_by_id("android:id/button1").click()
		WebDriverWait(self.driver,20).until(EC.visibility_of_element_located((By.ID,"com.kanchufang.privatedoctor:id/btn_auth_verify")))
		#self.assertIsNotNone(self.driver.find_element_by_xpath("//*[@text='您的认证正在审核中…']"),'普通认证提交失败')
		el17 = self.driver.find_element_by_id("com.kanchufang.privatedoctor:id/btn_auth_verify")
		el17.click()
		
		WebDriverWait(self.driver,20).until(EC.visibility_of_element_located((By.ID,"com.kanchufang.privatedoctor:id/btn_upload")))
		el12.click()
		el13 = self.driver.find_element_by_xpath("//*[@text='相册']")
		el13.click()
		el14.click()
		el15.click()
		el16.click()
		WebDriverWait(self.driver,20).until(EC.visibility_of_element_located((By.XPATH,"//*[@text='发送']")))
		el12.click()
		self.driver.find_element_by_id("android:id/button1").click()
		WebDriverWait(self.driver,20).until(EC.visibility_of_element_located((By.ID,"android:id/message")))
		self.assertIsNotNone(self.driver.find_element_by_xpath("//*[@text='上传成功，请耐心等待审核。']"),'权威认证提交失败')

if __name__ == '__main__':
	unittest.main()