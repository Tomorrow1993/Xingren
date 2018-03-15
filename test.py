from selenium.webdriver.support.ui import WebDriverWait
def findElement(self, element):
    try:
        WebDriverWait(self.wd, 10).until(expected_conditions.presence_of_element_located((By.ID, element)))
        return True
    except selenium.common.exceptions.TimeoutException:
        return False
    except selenium.common.exceptions.NoSuchElementException:
        return False

def test_login(self):
    if self.findElement('cn.dxy.idxyer:id/start_up_welcome_image_iv'):
        for i in range(3):
            self.SwipeLeft(1000)
        self.wd.find_element_by_id('cn.dxy.idxyer:id/start_up_welcome_enter_tv').click()
    else:
        print('欢迎页不存在的')
    self.wd.implicitly_wait(60)
    self.wd.find_element_by_id('cn.dxy.idxyer:id/main_mine_rb').click()
    if self.findElement('cn.dxy.idxyer:id/tab_account'):
        self.wd.find_element_by_id('cn.dxy.idxyer:id/sso_username').set_value('111111111')
        self.wd.find_element_by_id('cn.dxy.idxyer:id/sso_password').set_value('111111111')
        self.wd.find_element_by_id('cn.dxy.idxyer:id/sso_login').click()
    else:
        print('用户已登录')