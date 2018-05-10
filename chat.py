# -*- coding: UTF-8 -*-
# from selenium import webdriver
'''
created on 2018-1-15
@author:Eddie
Project:使用unnitest框架编写测试用例思路
'''
import unittest
import selenium.common.exceptions
from Xingren.config import *
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Test(unittest.TestCase):

    def findElement(self, element):
        try:
            WebDriverWait(driver,20).until(EC.visibility_of_element_located((By.ID, element)))
            return True
        except selenium.common.exceptions.TimeoutException:
            return False
        except selenium.common.exceptions.NoSuchElementException:
            return False

    def test_case1(self):
        WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.ID, "com.kanchufang.privatedoctor:id/tab_home_rb")))
        el1 = driver.find_element_by_id("com.kanchufang.privatedoctor:id/tab_patient_rb")
        el1.click()

        # TouchAction(self.driver).tap([(124,1259)],500)
        # TouchAction(self.driver).tap([(356, 999)], 500).perform()
        name = "test"

        el2 = driver.find_element_by_xpath("//*[@text='test']")
        WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.ID, "com.kanchufang.privatedoctor:id/ib_add_patient")))
        el2.click()

    def test_case2(self):
        # 发送文本
        el3 = driver.find_element_by_id("com.kanchufang.privatedoctor:id/et_input")
        el3.click()
        el3.send_keys("hello")

        el4 = driver.find_element_by_id("com.kanchufang.privatedoctor:id/btn_send")
        el4.click()
        sleep(3)
        #self.assertIsNotNone(self.driver.find_element_by_xpath("//*[@text='hello']"), '文本发送失败')

        el5 = driver.find_element_by_id("com.kanchufang.privatedoctor:id/cib_0")
        el5.click()

    def test_case3(self):
        # 长按发送语音
        el6 = driver.find_element_by_id("com.kanchufang.privatedoctor:id/tv_press_speak")
        elx = el6.location.get('x')
        ely = el6.location.get('y')
        driver.swipe(elx, ely, elx, ely, 5000)
        sleep(3)
        self.assertIsNotNone(driver.find_element_by_id("com.kanchufang.privatedoctor:id/layout_content"), '语音发送失败')

    def test_case4(self):
        # 发送图片
        el7 = driver.find_element_by_id("com.kanchufang.privatedoctor:id/cib_1")
        el7.click()
        el8 = driver.find_element_by_id("com.kanchufang.privatedoctor:id/chk_photo")
        el8.click()
        el9 = driver.find_element_by_xpath("//*[@text='发送(1)']")
        el9.click()

    def test_case5(self):
        # 发送表情
        el10 = driver.find_element_by_id("com.kanchufang.privatedoctor:id/btn_send")
        el11 = driver.find_element_by_id("com.kanchufang.privatedoctor:id/cib_4")
        el11.click()
        el12 = driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.support.v4.view.ViewPager/android.widget.FrameLayout/android.widget.LinearLayout[2]/android.widget.ViewSwitcher/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.ViewSwitcher/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.support.v4.view.ViewPager/android.widget.GridView/android.widget.ImageView[1]")
        el12.click()
        el10.click()
