# coding=utf-8
import unittest
from framework.browser_engine import BrowserEngine
from pages.login_page import LoginPage
from pages.main_page import MainPage
class Main_Page(unittest.TestCase):
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

        # loginpage = LoginPage(cls.driver)
        # loginpage.type_company_name('13800138000')
        # loginpage.type_password('123456')
        # loginpage.send_submit_btn()  # 调用页面对象类中的点击按钮方法
        # time.sleep(1)
        # try:
        #     assert u'有美食' == loginpage.get_page_title()  # 调用页面对象继承基类中的获取页面标题方法
        #     print ('Test Pass.')
        # except Exception as e:
        #     print ('Test Fail.', format(e))

    @classmethod
    def tearDownClass(cls):
        """
        测试结束后的操作，这里基本上都是关闭浏览器
        :return:
        """
        cls.driver.quit()

    # def test_zgms_login(self):
    #
    #     loginpage = LoginPage(self.driver)
    #     loginpage.type_company_name('13800138000')
    #     loginpage.type_password('123456')
    #     loginpage.send_submit_btn()  # 调用页面对象类中的点击按钮方法
    #     time.sleep(2)
    #     loginpage.get_windows_img()  # 调用基类截图方法
    #     try:
    #         assert u'有美食' == loginpage.get_page_title()  # 调用页面对象继承基类中的获取页面标题方法
    #         print ('Test Pass.')
    #     except Exception as e:
    #         print ('Test Fail.', format(e))

    #@unittest.skip("I don't want to run this case.")
    def test_zgms_jiaoseguanli(self):
        """
        这里一定要test开头，把测试逻辑代码封装到一个test开头的方法里。
        :return:
        """
        mainpage = MainPage(self.driver)
        mainpage.click_qxsz()   # 点击权限管理
        mainpage.click_jsgl()   # 点击角色管理
        mainpage.sleep(2)

        mainpage.get_windows_img()  # 调用基类截图方法
        mainpage.refresh()

            # 测试用户管理页

    def test_zsy_yonghuguanli(self):
        aaa = u"测试003"
        mainpage = MainPage(self.driver)
        mainpage.sleep(1)
        # 点击权限设置
        mainpage.click_qxsz()
        # mainpage.sleep(2)
        # 点击用户管理
        mainpage.click_yhgl()
        mainpage.sleep(1)
        # 切换frame
        mainpage.switch_iframe()
        # 判断是否存在要添加的测试用户
        if not mainpage.assert_has_text(aaa):
            #点击下一页
            mainpage.click_xyy()
            if mainpage.assert_has_text(aaa):
                mainpage.find_yonghumingcheng(aaa)
                mainpage.click_del_btn()  # 点击删除
                # mainpage.sleep(1)
                mainpage.click_del_ok()  # 点击确认删除
                mainpage.sleep(1)

        mainpage.click_xinzengyonghu() #点击新增用户
        mainpage.sleep(1)
        mainpage.type_yhm(aaa)  # 输入用户名
        mainpage.type_js()   # 选择角色
        mainpage.click_qiangzhiyouhui()
        mainpage.click_miandan()
        mainpage.sleep(1)
        mainpage.click_xzok_btn() # 点击ok
        mainpage.sleep(1)
        if not mainpage.assert_has_text(aaa):
            mainpage.click_xyy()
            mainpage.sleep(1)
        mainpage.find_yonghumingcheng(aaa)   #查找定位aaa
        mainpage.click_del_btn()  # 点击删除
        mainpage.sleep(2)
        mainpage.click_del_ok()  # 点击确认删除
        mainpage.sleep(1)
        print mainpage.denglumingcheng
        mainpage.get_windows_img()  # 调用基类截图方法

if __name__ == '__main__':
    unittest.main()