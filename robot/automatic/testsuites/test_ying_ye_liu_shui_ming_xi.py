# coding=utf-8
import unittest

from framework.browser_engine import BrowserEngine
from pages.login_page import LoginPage
from pages.shujuzx.yingyebb.ying_ye_liu_shui_ming_xi_page import YingYeLiuShuiMingXiPage


class YingYeLiuShuiMingXiTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """
        测试固件的setUp()的代码，主要是测试的前提准备工作
        :return:
        """
        browser = BrowserEngine(cls)
        cls.driver = browser.open_browser(cls)
        login_page = LoginPage(cls.driver)
        login_page.login_auto()
    @classmethod
    def tearDownClass(cls):
        """
        测试结束后的操作，这里基本上都是关闭浏览器
        :return:
        """
        cls.driver.quit()

    # 测试营业流水明细 查询
    def test_yylsmx_cx(self):
        """
        这里一定要test开头，把测试逻辑代码封装到一个test开头的方法里。
        :return:
        """
        yylsmxpage = YingYeLiuShuiMingXiPage(self.driver)
        yylsmxpage.goto_yylsmx()
        yylsmxpage.switch_iframe()
        yylsmxpage.sleep(1)
        yylsmxpage.click_cx()
        yylsmxpage.click_ddcx()
        yylsmxpage.sleep(1)
        yylsmxpage.click_chakan()
        yylsmxpage.sleep(5)

        yylsmxpage.get_windows_img()  # 调用基类截图方法
        yylsmxpage.refresh()



if __name__ == '__main__':
    unittest.main()