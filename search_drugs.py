# -*- coding: utf-8 -*-
# @created on 2018/3/14 下午6:47
# @author:Eddie
# Project:使用unnitest框架编写测试用例思路
import unittest
from config import *
from HTMLReport import logger


class SearchDrugs(unittest.TestCase):
	def test_case1(self):  # 进入西药首页
		WebDriverWait(driver, 20).until(
			EC.visibility_of_element_located((By.ID, "com.kanchufang.privatedoctor:id/tab_home_rb")))
		el1 = driver.find_element_by_id("com.kanchufang.privatedoctor:id/tab_patient_rb")
		el1.click()
		el2 = driver.find_element_by_xpath("//*[@text='test']")
		el2.click()
		el3 = driver.find_element_by_id("com.kanchufang.privatedoctor:id/cib_2")
		el3.click()

	def test_case2(self):  # 点击搜索框搜索
		el4 = driver.find_element_by_id("com.kanchufang.privatedoctor:id/yf_act_search")
		el4.click()
		el4.send_keys('汤臣倍健')
		os.system('adb shell ime set com.sohu.inputmethod.sogou/.SogouIME')
		sleep(2)
		driver.press_keycode(66)
		sleep(2)
		el5 = driver.find_element_by_xpath("(//android.widget.ImageView[@content-desc='药品'])[1]")
		el5.click()

	def test_case3(self):  # 设置用法用量
		if findelementbyid("com.kanchufang.privatedoctor:id/yf_tv_custom"):
			el6 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout[3]/android.widget.LinearLayout[1]/android.widget.LinearLayout/android.view.View/android.widget.TextView")
			el6.click()
		else:
			sleep(2)
			el7 = driver.find_elements_by_id("com.kanchufang.privatedoctor:id/yf_increment")
			for i in el7:
				i.click()
			el8 = driver.find_element_by_xpath("//*[@text='片']")
			el8.click()
			el9 = driver.find_element_by_xpath("//*[@text='口服']")
			el9.click()
			el10 = driver.find_element_by_xpath("//*[@text='qd']")
			el10.click()
			if findelementbyxpath("//*[@text='饭前服药']"):
				el12 = driver.find_element_by_id("com.kanchufang.privatedoctor:id/yf_route_more")
				el13 = driver.find_element_by_id("com.kanchufang.privatedoctor:id/yf_tv_tips")
				driver.scroll(el12, el13)
				el11 = driver.find_element_by_xpath("//*[@text='饭前服药']")
				el11.click()
			else:
				el12 = driver.find_element_by_id("com.kanchufang.privatedoctor:id/yf_tv_tips")
				el13 = driver.find_element_by_id("com.kanchufang.privatedoctor:id/yf_route_more")
				driver.scroll(el12, el13)
				el11 = driver.find_element_by_xpath("//*[@text='饭前服药']")
				el11.click()

	def test_case4(self):  # 加入推荐单
		if findelementbyid("com.kanchufang.privatedoctor:id/yf_btn_update"):
			el11 = driver.find_element_by_id("com.kanchufang.privatedoctor:id/yf_btn_update")
			el11.click()
		else:
			el12 = driver.find_element_by_id("com.kanchufang.privatedoctor:id/yf_btn_add_recommend")
			el12.click()

	def test_case5(self):  # 去推荐
		sleep(2)
		el13 = driver.find_element_by_id("com.kanchufang.privatedoctor:id/yf_recommend")
		el13.click()

	def test_case6(self):  # 填写诊断
		el14 = driver.find_element_by_id("com.kanchufang.privatedoctor:id/yf_tv_diagnosis")
		el14.click()
		WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, "com.kanchufang.privatedoctor:id/yf_title")))
		os.system('adb shell ime set io.appium.android.ime/.UnicodeIME')
		el15 = driver.find_element_by_id("com.kanchufang.privatedoctor:id/yf_actv_search")
		el15.send_keys("痤疮")
		os.system('adb shell ime set com.sohu.inputmethod.sogou/.SogouIME')
		sleep(2)
		driver.press_keycode(66)
		el16 = driver.find_element_by_id("com.kanchufang.privatedoctor:id/yf_tv_recommend")
		el16.click()
		sleep(2)
		self.assertIsNotNone(driver.find_element_by_id("com.kanchufang.privatedoctor:id/btn_send"), '药品推荐成功')

