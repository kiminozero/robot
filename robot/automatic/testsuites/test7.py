# coding=utf-8
import unittest

from framework.browser_engine import BrowserEngine
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.quanxiansz.jue_se_guan_li_page import JueSeGuanLiPage


class JueSeGuanLiTest (unittest.TestCase):
    @classmethod
    def setUp(cls):
        """
        测试固件的setUp()的代码，主要是测试的前提准备工作
        :return:
        """
        browser = BrowserEngine(cls)
        cls.driver = browser.open_browser(cls)
        login_page = LoginPage(cls.driver)
        login_page.login_auto()
        login_page.sleep(2)

    @classmethod
    def tearDown(cls):
        """
        测试结束后的操作，这里基本上都是关闭浏览器
        :return:
        """
        cls.driver.quit()



    def test_zgms_jiaoseguanli(self):
        """
        这里一定要test开头，把测试逻辑代码封装到一个test开头的方法里。
        :return:
        """
        mainpage = MainPage(self.driver)
        mainpage.click_qxsz()   # 点击权限管理
        mainpage.click_jsgl()   # 点击角色管理
        mainpage.sleep(2)
        jueseguanli =JueSeGuanLiPage(self.driver)
        jueseguanli.juesemingcheng1 = u"角色1"
        jueseguanli.switch_iframe()
        jueseguanli.type_chaxunjuesemingcheng()
        jueseguanli.sleep(1)
        jueseguanli.click_chaxun()
        jueseguanli.sleep(1)
        jueseguanli.click_del_btn()
        jueseguanli.sleep(1)
        print jueseguanli.get_element_text(jueseguanli.cancel_btn)
        jueseguanli.sleep(1)
        jueseguanli.click_del_cancel()
        jueseguanli.sleep(1)
        jueseguanli.click_del_btn()
        jueseguanli.sleep(1)
        print jueseguanli.get_element_text(jueseguanli.ok_btn)
        jueseguanli.click_del_ok()
        jueseguanli.sleep(1)
        jueseguanli.click_xinzengjuese()
        jueseguanli.sleep(1)
        jueseguanli.click_juesequanxian()
        jueseguanli.type_jusemingcheng()
        jueseguanli.click_xz_ok()
        jueseguanli.sleep(1)
        jueseguanli.get_windows_img()  # 调用基类截图方法


if __name__ == '__main__':
    unittest.main()