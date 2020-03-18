# coding=utf-8
import unittest

from framework.browser_engine import BrowserEngine
from pages.jichuxx.shangpingl.poduct_info import ProductInfoPage
from pages.login_page import LoginPage
from pages.main_page import MainPage


class ProductInfoTest(unittest.TestCase):
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

    def test_product_info(self):

        mainpage = MainPage(self.driver)
        mainpage.click_jcxx()  # 基础信息
        # mainpage.sleep(1)
        mainpage.click_spgl()  # 商品信息
        # mainpage.sleep(1)
        mainpage.click_spxx() #商品管理
        mainpage.sleep(2)
        pdinfo = ProductInfoPage(self.driver)
        pdinfo.switch_iframe()
        pdinfo.click_pldr()
        pdinfo.sleep(2)
        print pdinfo.file_path
        pdinfo.upload_file()
        pdinfo.sleep(2)
        pdinfo.click_qd()
        pdinfo.wait(10)
        # mainpage.clickspxx()
        # pdinfo.switch_iframe()
        pdinfo.wait(5)
        pdinfo.click_cx()
        pdinfo.sleep(5)
