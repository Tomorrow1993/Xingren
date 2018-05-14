 # -*- coding: UTF-8 -*-
#from selenium import webdriver
'''
created on 2018-1-15
@author:Eddie
Project:使用unnitest框架编写测试用例思路
'''
import unittest
import selenium.common.exceptions
from config import *
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
			WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, element)))
			return True
		except selenium.common.exceptions.TimeoutException:
			return False
		except selenium.common.exceptions.NoSuchElementException:
			return False

	def findelementbyxpath(self, element):
		try:
			WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, element)))
			return True
		except selenium.common.exceptions.TimeoutException:
			return False
		except selenium.common.exceptions.NoSuchElementException:
			return False
'''
	def test_case1(self):#开通收费
		WebDriverWait(driver,20).until(EC.visibility_of_element_located((By.ID,"com.kanchufang.privatedoctor:id/tab_home_rb")))
		el1 = driver.find_element_by_id("com.kanchufang.privatedoctor:id/tab_work_site_rb")
		el1.click()
		WebDriverWait(driver,20).until(EC.visibility_of_element_located((By.XPATH,"//*[@text='线下工作室']")))

		el2 = driver.find_element_by_xpath("//*[@text='杏仁门诊']")
		el3 = driver.find_element_by_xpath("//*[@text='新的执业地点']")
		driver.scroll(el3,el2)

		sleep(3)
		el4 = driver.find_element_by_xpath("//*[@text='包月咨询']")
		el4.click()
		WebDriverWait(driver,20).until(EC.visibility_of_element_located((By.XPATH,"//*[@text='99元/月']")))
		el5 = driver.find_element_by_xpath("//*[@text='99元/月']")
		el5.click()
		
		sleep(3)
		el6 = driver.find_element_by_xpath("//*[@text='图文咨询']")
		el6.click()
		WebDriverWait(driver,20).until(EC.visibility_of_element_located((By.XPATH,"//*[@text='19元/次']")))
		el7 = driver.find_element_by_xpath("//*[@text='19元/次']")
		el7.click()

		sleep(3)
		el8 = driver.find_element_by_xpath("//*[@text='电话咨询']")
		el8.click()
		WebDriverWait(driver,20).until(EC.visibility_of_element_located((By.XPATH,"//*[@text='49元/次']")))
		el9 = driver.find_element_by_xpath("//*[@text='49元/次']")
		el9.click()

	'''
	def test_case2(self):#调API添加患者
		test
	'''

	def test_case3(self):#图文咨询
		#购买图文API
		#调用购买图文付费的API
		WebDriverWait(driver,20).until(EC.visibility_of_element_located((By.ID,"com.kanchufang.privatedoctor:id/tab_home_rb")))
		driver.find_element_by_id("com.kanchufang.privatedoctor:id/tab_patient_rb").click()
		#assertIsNotNone(driver.find_element_by_id("id/tab_patient"),'没有找到这个ID')
		if findelementbyxpath("//*[@text='VIP']"):
			pass
		else:
			print('消息列表无图文VIP')
		#assertIsNotNone(driver.find_element_by_xpath("//*[@text='VIP']"),'消息列表无图文VIP')
		el10 = driver.find_element_by_xpath("//*[@text='所有患者']")
		el10.click()
		WebDriverWait(driver,20).until(EC.visibility_of_element_located((By.ID,"com.kanchufang.privatedoctor:id/tv_sort_by_fee")))
		if findelementbyxpath("//*[@text='test']"):
			pass
		else:
			print('VIP患者分组内无患者')
		#assertIsNotNone(driver.find_element_by_xpath("//*[@text='test']"),'VIP患者分组内无患者')
		el11 = driver.find_element_by_id("com.kanchufang.privatedoctor:id/tv_sort_by_fee")
		el11.click()
		if findelementbyxpath("//*[@text='VIP付费：图文咨询  |  1']"):
			pass
		else:
			print('图文咨询分组内无患者')
		'''
		el12 = driver.find_element_by_xpath("//*[@text='VIP付费：图文咨询]")
		el12.click()
		'''
		#assertIsNotNone(driver.find_element_by_xpath("//*[@text='test']"),'图文咨询分组内无患者')
		driver.press_keycode('4')
		sleep(1)
		driver.press_keycode('4')
		sleep(1)

		el13 = driver.find_element_by_xpath("//*[@text='test']")
		el13.click()
		WebDriverWait(driver,20).until(EC.visibility_of_element_located((By.ID,"com.kanchufang.privatedoctor:id/btn_send")))
		if findelementbyxpath("//*[@text='VIP图文']"):
			pass
		else:
			print('聊天页患者名字下面没有VIP图文')
		#assertIsNotNone(driver.find_element_by_xpath("//*[@text='VIP图文']"),'聊天页患者名字下面没有VIP图文')
		driver.swipe(1000,800,100,800)
		WebDriverWait(driver,20).until(EC.visibility_of_element_located((By.XPATH,"//*[@text='咨询订单']")))
		self.assertIn('图文咨询',driver.page_source,'服务套餐tab图文状态未更新')
		driver.press_keycode('4')

		#退款图文API

	def test_case4(self):#包月咨询
		# 购买包月API
		# 调用购买包月付费的API
		if findelementbyxpath("//*[@text='咨询订单']"):
			driver.press_keycode('4')
		else:
			pass
		WebDriverWait(driver, 20).until(
			EC.visibility_of_element_located((By.ID, "com.kanchufang.privatedoctor:id/tab_home_rb")))
		driver.find_element_by_id("com.kanchufang.privatedoctor:id/tab_patient_rb").click()
		# assertIsNotNone(driver.find_element_by_id("id/tab_patient"),'没有找到这个ID')
		if findelementbyxpath("//*[@text='VIP']"):
			pass
		else:
			print('消息列表无包月VIP')
		# assertIsNotNone(driver.find_element_by_xpath("//*[@text='VIP']"),'消息列表无图文VIP')
		el10 = driver.find_element_by_xpath("//*[@text='所有患者']")
		el10.click()
		WebDriverWait(driver, 20).until(
			EC.visibility_of_element_located((By.ID, "com.kanchufang.privatedoctor:id/tv_sort_by_fee")))
		if findelementbyxpath("//*[@text='test']"):
			pass
		else:
			print('VIP患者分组内无患者')
		# assertIsNotNone(driver.find_element_by_xpath("//*[@text='test']"),'VIP患者分组内无患者')
		el11 = driver.find_element_by_id("com.kanchufang.privatedoctor:id/tv_sort_by_fee")
		el11.click()
		if findelementbyxpath("//*[@text='VIP付费：包月咨询  |  1']"):
			pass
		else:
			print('包月咨询分组内无患者')

		# assertIsNotNone(driver.find_element_by_xpath("//*[@text='test']"),'图文咨询分组内无患者')
		driver.press_keycode('4')
		sleep(1)
		driver.press_keycode('4')
		sleep(1)

		el13 = driver.find_element_by_xpath("//*[@text='test']")
		el13.click()
		WebDriverWait(driver, 20).until(
			EC.visibility_of_element_located((By.ID, "com.kanchufang.privatedoctor:id/btn_send")))
		if findelementbyxpath("//*[@text='VIP包月']"):
			pass
		else:
			print('聊天页患者名字下面没有VIP包月')
		# assertIsNotNone(driver.find_element_by_xpath("//*[@text='VIP图文']"),'聊天页患者名字下面没有VIP图文')
		driver.swipe(1000, 800, 100, 800)
		WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//*[@text='咨询订单']")))
		self.assertIn('包月咨询', driver.page_source, '服务套餐tab包月状态未更新')
		driver.press_keycode('4')

	def  test_case5(self):#电话咨询
		#购买电话# API
		if findelementbyxpath("//*[@text='咨询订单']"):
			driver.press_keycode('4')
		else:
			pass

		if findelementbyxpath("//*[@text='VIP']"):
			pass
		else:
			print('消息列表无电话VIP')
		#assertIsNotNone(driver.find_element_by_xpath("//*[@text='VIP']"),'消息列表无电话VIP')
		el10 = driver.find_element_by_xpath("//*[@text='所有患者']")
		el10.click()
		if  findelementbyxpath("//*[@text='test']"):
			pass
		else:
			print('VIP患者分组内无患者')
		#assertIsNotNone(driver.find_element_by_xpath("//*[@text='test']"),'VIP患者分组内无患者')
		el11 = driver.find_element_by_id("com.kanchufang.privatedoctor:id/tv_sort_by_fee")
		el11.click()
		sleep(1)
		if findelementbyxpath("//*[@text='VIP付费：电话咨询  |  1']"):
			pass
		else:
			print('电话咨询分组内无患者')
		#assertIsNotNone(driver.find_element_by_xpath("//*[@text='test']"),'电话咨询分组内无患者')
		driver.press_keycode('4')
		sleep(1)
		driver.press_keycode('4')
		sleep(1)
		el13 = driver.find_element_by_xpath("//*[@text='test']")
		el13.click()
		if findelementbyid("com.kanchufang.privatedoctor:id/iv_goto_call"):
			pass
		else:
			print('聊天页没有电话弹窗')
		#assertIsNotNone(driver.find_element_by_id("com.kanchufang.privatedoctor:id/iv_goto_call",'聊天页没有电话弹窗'))

	if __name__ == '__main__':
		unittest.main()