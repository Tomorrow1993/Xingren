# -*- coding: utf-8 -*-
# @created on 2018/5/7 上午11:18
# @author:Eddie
# from selenium import webdriver
# Project:使用unnitest框架编写测试用例思路

import unittest
from Xingren.config import *


class Test(unittest.TestCase):
    def test_case1(self):#进入西药首页
        WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, "com.kanchufang.privatedoctor:id/tab_home_rb")))
        el1 = driver.find_element_by_id("com.kanchufang.privatedoctor:id/tab_patient_rb")
        el1.click()
        el2 = driver.find_element_by_xpath("//*[@text='test']")
        el2.click()
        el3 = driver.find_element_by_id("com.kanchufang.privatedoctor:id/cib_2")
        el3.click()
        WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, "com.kanchufang.privatedoctor:id/yf_recommend")))
        el4 = driver.find_element_by_id("com.kanchufang.privatedoctor:id/yf_fl_drug_set")
        el4.click()
        if findelementbyid("com.kanchufang.privatedoctor:id/yf_tv_add_template"):
            driver.find_element_by_id("com.kanchufang.privatedoctor:id/yf_tv_add_template").click()
        else:
            driver.find_element_by_xpath("//*[@text='添加用药套餐']").click()

    def test_case2(self):#搜索药品
        el6 = driver.find_element_by_id("com.kanchufang.privatedoctor:id/yf_et_template_input")
        el6.send_keys("test")
        driver.hide_keyboard()
        el7 = driver.find_element_by_id("com.kanchufang.privatedoctor:id/yf_tv_add_now")
        el7.click()
        sleep(2)
        driver.hide_keyboard()
        el8 = driver.find_element_by_id("com.kanchufang.privatedoctor:id/yf_act_search")
        el8.send_keys("感冒灵")
        #切换回第三方键盘
        os.system('adb shell ime set com.sohu.inputmethod.sogou/.SogouIME')

        #点击键盘上回车键
        sleep(2)
        driver.press_keycode(66)
        sleep(2)
        el9 = driver.find_element_by_xpath("(//android.widget.ImageView[@content-desc='药品'])[1]")
        el9.click()

    def test_case3(self):  #加入用药套餐
        WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, "com.kanchufang.privatedoctor:id/yf_btn_add_recommend")))
        el10 = driver.find_element_by_id("com.kanchufang.privatedoctor:id/yf_btn_add_recommend")
        el10.click()
        driver.press_keycode('4')
        el11 = driver.find_element_by_id("com.kanchufang.privatedoctor:id/menu_save")
        el11.click()

    def test_case4(self):  #加入推荐单
        WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, "com.kanchufang.privatedoctor:id/yf_tv_save_to_set")))
        el12 = driver.find_element_by_id("com.kanchufang.privatedoctor:id/yf_tv_save_to_set")
        el12.click()






