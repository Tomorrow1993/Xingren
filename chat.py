# -*- coding: UTF-8 -*-
# from selenium import webdriver
'''
created on 2018-1-15
@author:Eddie
Project:使用unnitest框架编写测试用例思路
'''
import unittest
import HTMLReport
import selenium.common.exceptions
from time import sleep
from selenium import webdriver
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Test(unittest.TestCase):

    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '4.4.2'  # 6.0 4.4.2
        desired_caps['deviceName'] = '1bf493ad'  # 1bf493ad c66d2f78#
        desired_caps['appPackage'] = 'com.kanchufang.privatedoctor'
        desired_caps['appActivity'] = '.activities.start.SplashActivity'
        desired_caps['noReset'] = 'true'
        desired_caps['clearSystemFiles'] = 'true'
        driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def findElement(self,element):
        try :
            WebDriverWait(self.driver,20).until(EC.visibility_of_element_located((By.ID,element)))
            return True
        except selenium.common.exceptions.TimeoutException:
            return False
        except selenium.common.exceptions.NoSuchElementException:
            return False

    def test_case1(self):
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.ID, "com.kanchufang.privatedoctor:id/tab_home_rb")))
        el1 = self.driver.find_element_by_id("com.kanchufang.privatedoctor:id/tab_patient_rb")
        el1.click()

        # TouchAction(self.driver).tap([(124,1259)],500)
        # TouchAction(self.driver).tap([(356, 999)], 500).perform()
        name = "test"

        el2 = self.driver.find_element_by_xpath("//*[@text='test']")
        el2.click()

        el3 = self.driver.find_element_by_id("com.kanchufang.privatedoctor:id/et_input")
        el3.click()
        el3.send_keys("hello")

        el4 = self.driver.find_element_by_id("com.kanchufang.privatedoctor:id/btn_send")
        el4.click()
        sleep(3)
        #self.assertIsNotNone(self.driver.find_element_by_xpath("//*[@text='hello']"), '文本发送失败')

        el5 = self.driver.find_element_by_id("com.kanchufang.privatedoctor:id/cib_0")
        el5.click()

        # 长按发送语音
        el6 = self.driver.find_element_by_id("com.kanchufang.privatedoctor:id/tv_press_speak")
        elx = el6.location.get('x')
        ely = el6.location.get('y')
        self.driver.swipe(elx, ely, elx, ely, 5000)
        sleep(3)
        self.assertIsNotNone(self.driver.find_element_by_id("com.kanchufang.privatedoctor:id/layout_content"), '语音发送失败')

        el7 = self.driver.find_element_by_id("com.kanchufang.privatedoctor:id/cib_1")
        el7.click()
        el8 = self.driver.find_element_by_id("com.kanchufang.privatedoctor:id/chk_photo")
        el8.click()
        el9 = self.driver.find_element_by_xpath("//*[@text='发送(1)']")
        el9.click()

        el10 = self.driver.find_element_by_id("com.kanchufang.privatedoctor:id/btn_send")
        el11 = self.driver.find_element_by_id("com.kanchufang.privatedoctor:id/cib_4")
        el11.click()
        el12 = self.driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.support.v4.view.ViewPager/android.widget.FrameLayout/android.widget.LinearLayout[2]/android.widget.ViewSwitcher/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.ViewSwitcher/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.support.v4.view.ViewPager/android.widget.GridView/android.widget.ImageView[1]")
        el12.click()
        el10.click()


if __name__ == '__main__':

    # 测试套件
    suite = unittest.TestSuite()
    # 测试用例加载器
    loader = unittest.TestLoader()
    # 把测试用例加载到测试套件中
    suite.addTests(loader.loadTestsFromTestCase(Test))

    # 测试用例执行器
    runner = HTMLReport.TestRunner(report_file_name='test',  # 报告文件名，默认“test”
                                   output_path='/Users/liuchang/Desktop/report',  # 保存文件夹名，默认“report”
                                   verbosity=2,  # 控制台输出详细程度，默认 2
                                   title='测试报告',  # 报告标题，默认“测试报告”
                                   description='无测试描述',  # 报告描述，默认“无测试描述”
                                   thread_count=1,  # 并发线程数量（无序执行测试），默认数量 1
                                   sequential_execution=True  # 是否按照套件添加(addTests)顺序执行，
                                   # 会等待一个addTests执行完成，再执行下一个，默认 False
                                   )
    # 执行测试用例套件
    runner.run(suite)
    unittest.main()