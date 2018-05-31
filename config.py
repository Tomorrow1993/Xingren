# -*- coding: utf-8 -*-
# @created on 2018/3/14 下午6:47
# @author:Eddie
# Project:使用unnitest框架编写测试用例思路
import sys
import os
import selenium.common.exceptions
from selenium import webdriver
from time import sleep
from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '4.4.2'  # 6.0 4.4.2
desired_caps['deviceName'] = '1bf493ad'  # 1bf493ad c66d2f78 emulator-555444
desired_caps['appPackage'] = 'com.kanchufang.privatedoctor'
desired_caps['appActivity'] = '.activities.start.SplashActivity'
desired_caps['noReset'] = 'true'
desired_caps['clearSystemFiles'] = 'true'
desired_caps['unicodeKeyboard'] = 'true'
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)


def findelementbyid(element):
    try:
        WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, element)))
        return True
    except selenium.common.exceptions.TimeoutException:
        return False
    except selenium.common.exceptions.NoSuchElementException:
        return False


def findelementbyxpath(element):
    try:
        WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, element)))
        return True
    except selenium.common.exceptions.TimeoutException:
        return False
    except selenium.common.exceptions.NoSuchElementException:
        return False
