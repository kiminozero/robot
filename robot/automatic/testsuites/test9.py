# coding=utf-8
import unittest
from framework.browser_engine import BrowserEngine
from pages.login_page import LoginPage
from pages.main_page import MainPage

class Main_Page(unittest.TestCase):
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

        mainpage = MainPage(cls.driver)
        mainpage.sleep(1)
        mainpage.click_qxsz()  # 点击权限管理
        # mainpage.clickyhgl()  # 点击用户管理
        href = cls.driver.find_element_by_link_text("用户管理").get_attribute("href")
        print  href
        js = "window.open('" + href + "')"
        cls.driver.execute_script(js)

        print cls.driver.current_window_handle  # 输出当前窗口句柄（百度）
        handles = cls.driver.window_handles  # 获取当前窗口句柄集合（列表类型）
        print handles  # 输出句柄集合

        for handle in handles:
            if handle != cls.driver.current_window_handle:
                print 'switch to ', handle
                cls.driver.switch_to_window(handle)
                print cls.driver.current_window_handle
                break
    @classmethod
    def tearDown(cls):
        """
        测试结束后的操作，这里基本上都是关闭浏览器
        :return:
        """
        cls.driver.quit()
    def test_zsy_yonghuguanli(self):
        aaa = u"测试003"
        mainpage = MainPage(self.driver)
        # mainpage.sleep(1)
        # mainpage.clickqxsz()  # 点击权限管理
        #mainpage.clickyhgl()  # 点击用户管理

        mainpage.sleep(1)

        # 判断是否存在要添加的测试用户
        if mainpage.assert_has_text(aaa)!=True:
            mainpage.click_xyy()
            if mainpage.assert_has_text(aaa):
                mainpage.find__yonghumingcheng(aaa)
                mainpage.click_del_btn()  # 点击删除
                mainpage.sleep(1)
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
        while mainpage.assert_has_text(aaa)!= True:
            mainpage.click_xyy()
        mainpage.find__yonghumingcheng(aaa)   #查找定位aaa
        mainpage.click_del_btn()  # 点击删除
        mainpage.sleep(1)
        mainpage.click_del_ok()  # 点击确认删除
        mainpage.sleep(1)
        print mainpage.denglumingcheng
        mainpage.get_windows_img()  # 调用基类截图方法
        mainpage.close()
if __name__ == '__main__':
    unittest.main()
