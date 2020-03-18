# coding=utf-8
import unittest
from framework.browser_engine import BrowserEngine
from pages.login_page import LoginPage

class Login(unittest.TestCase):
    def setUp(self):
        """
        测试固件的setUp()的代码，主要是测试的前提准备工作
        :return:
        """
        browser = BrowserEngine(self)
        self.driver = browser.open_browser(self)

    def tearDown(self):
        """
        测试结束后的操作，这里基本上都是关闭浏览器
        :return:
        """
        self.driver.quit()

    def test_zgms_login(self):
        """
        这里一定要test开头，把测试逻辑代码封装到一个test开头的方法里。
        :return:
        """
        loginpage = LoginPage(self.driver)
        loginpage.type_company_name('13800138000')
        loginpage.type_password('123456')
        loginpage.send_submit_btn() # 调用页面对象类中的点击按钮方法
        loginpage.sleep(2)
        loginpage.get_windows_img()  # 调用基类截图方法
        try:
            assert u'有美食' == loginpage.get_page_title()  # 调用页面对象继承基类中的获取页面标题方法
            print ('Test Pass.')
        except Exception as e:
            print ('Test Fail.', format(e))


if __name__ == '__main__':
    unittest.main()