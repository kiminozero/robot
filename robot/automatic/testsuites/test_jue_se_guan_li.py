# coding=utf-8
import unittest
from framework.browser_engine import BrowserEngine
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.quanxiansz.jue_se_guan_li_page import JueSeGuanLiPage

class JueSeGuanLiTest (unittest.TestCase):
    # @classmethod
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

    # @classmethod
    def tearDown(cls):
        """
        测试结束后的操作，这里基本上都是关闭浏览器
        :return:
        """

        cls.driver.quit()

    # 添加
    @unittest.skip("I don't want to run this case.")
    def test_jsgl_xzjs(self):
        mainpage = MainPage(self.driver)
        mainpage.click_qxsz()
        mainpage.click_jsgl()
        jsglpage = JueSeGuanLiPage(self.driver)
        jsglpage.juesemingcheng1 = u"test角色"
        jsglpage.switch_iframe()
        jsglpage.click_xinzengjuese()
        jsglpage.sleep(1)
        jsglpage.click_juesequanxian()
        jsglpage.type_jusemingcheng()
        jsglpage.click_xz_ok()
        jsglpage.sleep(1)
        jsglpage.select_xsts("100")
        jsglpage.get_windows_img()  # 调用基类截图方法
        try:
            assert u"test角色" in jsglpage.find_table_text()
            print ('Test Pass.')
        except Exception as e:
            print ('Test Fail.', format(e))

    # 修改
    @unittest.skip("I don't want to run this case.")
    def test_jsgl_xgjs(self):
        jsglpage = JueSeGuanLiPage(self.driver)
        jsglpage.juesemingcheng1 = u"test角色"
        jsglpage.goto_jsgl()
        jsglpage.sleep(1)
        jsglpage.switch_iframe()
        jsglpage.find_juesemingcheng(jsglpage.juesemingcheng1)
        jsglpage.click_xg_btn()
        jsglpage.click_qx()
        jsglpage.click_xz_ok()
        jsglpage.sleep(1)
        jsglpage.click_xg_btn()
        jsglpage.sleep(2)
        try:
            assert jsglpage.find_element(jsglpage.quanxuan).is_selected()
            print ('Test Pass.')
        except Exception as e:
            print ('Test Fail.', format(e))


    # 删除
    @unittest.skip("I don't want to run this case.")
    def test_jsgl_scjs(self):
        jsglpage = JueSeGuanLiPage(self.driver)
        jsglpage.goto_jsgl()
        jsglpage.juesemingcheng1 = u"test角色"
        jsglpage.switch_iframe()
        jsglpage.type_chaxunjuesemingcheng()
        jsglpage.sleep(1)
        jsglpage.click_chaxun()
        jsglpage.sleep(1)
        jsglpage.click_del_btn()
        jsglpage.sleep(1)
        jsglpage.click_del_ok()
        jsglpage.get_windows_img()

        try:
            assert u"test角色" not in jsglpage.find_table_text()
            print ('Test Pass.')
        except Exception as e:
            print ('Test Fail.', format(e))

    # 删除
    # @unittest.skip("I don't want to run this case.")
    def test_jsgl_scjs_fail(self):
        jsglpage = JueSeGuanLiPage(self.driver)
        jsglpage.goto_jsgl()
        jsglpage.juesemingcheng1 = u"test001"
        jsglpage.switch_iframe()
        jsglpage.type_chaxunjuesemingcheng()
        jsglpage.sleep(1)
        jsglpage.click_chaxun()
        jsglpage.sleep(1)
        jsglpage.click_del_btn()
        jsglpage.sleep(1)
        jsglpage.click_del_ok()
        jsglpage.sleep(1)
        assert u"test001" in jsglpage.find_table_text()
        print ('Test Pass.')
        jsglpage.get_windows_img()
if __name__ == '__main__':
    unittest.main()
