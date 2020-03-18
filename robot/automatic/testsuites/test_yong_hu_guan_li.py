# coding=utf-8
import unittest
from framework.browser_engine import BrowserEngine
from pages.login_page import LoginPage
from pages.quanxiansz.yong_hu_guan_li_page import YongHuGuanLiPage


class YongHuGuanLiTest(unittest.TestCase):
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

            # 测试用户管理页

    def test_zsy_yonghuguanli(self):
        aaa = u"测试003"
        yhglpage = YongHuGuanLiPage(self.driver)
        yhglpage.sleep(1)
        yhglpage.goto_yhgl()
        # 切换frame
        yhglpage.switch_iframe()

        # 判断是否存在要添加的测试用户
        if not yhglpage.assert_has_text(aaa):
            #点击下一页
            yhglpage.click_xyy()

            if yhglpage.assert_has_text(aaa):
                yhglpage.find_yonghumingcheng(aaa)
                yhglpage.click_del_btn()  # 点击删除
                # yhglpage.sleep(1)
                yhglpage.click_del_ok()  # 点击确认删除
                yhglpage.sleep(1)

        yhglpage.click_xinzengyonghu() #点击新增用户
        yhglpage.sleep(1)
        yhglpage.type_yhm(aaa)  # 输入用户名
        yhglpage.type_js()   # 选择角色
        yhglpage.click_qiangzhiyouhui()
        yhglpage.click_miandan()
        yhglpage.sleep(1)
        yhglpage.click_xzok_btn() # 点击ok
        yhglpage.sleep(1)

        if not yhglpage.assert_has_text(aaa):
            yhglpage.click_xyy()
            yhglpage.sleep(1)

        yhglpage.find_yonghumingcheng(aaa)   #查找定位aaa
        yhglpage.click_del_btn()  # 点击删除
        yhglpage.sleep(2)
        yhglpage.click_del_ok()  # 点击确认删除
        yhglpage.sleep(1)
        print yhglpage.denglumingcheng
        yhglpage.get_windows_img()  # 调用基类截图方法

if __name__ == '__main__':
    unittest.main()