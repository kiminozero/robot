# coding=utf-8
import unittest
import sys
from framework.browser_engine import BrowserEngine
from pages.login_page import LoginPage
from pages.permissionsettings.user_management_page import UserManagementPage

reload(sys)
sys.setdefaultencoding('utf-8')

class UserManagementTest(unittest.TestCase):
    test_date_login_name = "tyr"
    test_data_role_name = u"角色"
    test_date_reset_pwd = "111111"
    test_fixed_user = "tao_user"
    def setUp(self):
        browser = BrowserEngine(self)
        self.driver = browser.open_browser(self)
        login_page = LoginPage(self.driver)
        login_page.login_auto()
        login_page.sleep(2)

    def tearDown(self):
        self.driver.quit()

    #增删改查
    # @unittest.skip("I don't want to run this case.")
    def test_add_modify_del_user(self):
        user_management_page = UserManagementPage(self.driver)
        user_management_page.goto_user_management_page()
        user_management_page.switch_iframe()
        user_management_page.select_counts("100")
        user_management_page.sleep(1)
        if self.test_date_login_name in user_management_page.find_table_text():
            print (u"列表中有" + self.test_date_login_name + u"这个用户")
            user_management_page.delete_user(self.test_date_login_name)
            try:
                assert self.test_date_login_name not in user_management_page.find_table_text()
                print (u"删除了" + self.test_date_login_name + u"这个用户")
            except Exception as e:
                print ('Test Fail.', format(e))
        user_management_page.add_user(self.test_date_login_name,self.test_data_role_name, u"正常", u"允许登陆美食掌柜APP")
        try:
            assert self.test_date_login_name in user_management_page.find_table_text()
            print (u"增加了" + self.test_date_login_name + u"这个用户")
        except Exception as e:
            print ('Test Fail.', format(e))
        user_management_page.select_counts("100")
        user_management_page.modify_user(self.test_date_login_name, u"禁用", u"不允许登陆美食掌柜APP")
        # user_management_page.select_counts("100")
        if self.test_date_login_name in user_management_page.find_table_text():
            print (u"列表中有" + self.test_date_login_name + u"这个用户")
            user_management_page.search_all_user()
            user_management_page.select_counts("100")
            user_management_page.delete_user(self.test_date_login_name)
            try:
                assert self.test_date_login_name not in user_management_page.find_table_text()
                print (u"最后删除了" + self.test_date_login_name + u"这个用户")
            except Exception as e:
                print ('Test Fail.', format(e))

    #禁用启用和重置密码
    # @unittest.skip("I don't want to run this case.")
    def test_on_off_reset(self):
        user_management_page = UserManagementPage(self.driver)
        user_management_page.goto_user_management_page()
        user_management_page.switch_iframe()
        user_management_page.select_counts("100")
        user_management_page.turn_on_off(self.test_fixed_user)
        user_management_page.reset_pwd(self.test_fixed_user,self.test_date_reset_pwd)

    #查询有没有登录名称为“tyr”的名称
    @unittest.skip("I don't want to run this case.")
    def test_search_login_name(self):
        user_management_page = UserManagementPage(self.driver)
        user_management_page.goto_user_management_page()
        user_management_page.switch_iframe()
        user_management_page.input_search_login_name()
        user_management_page.click_search_btn()
        user_management_page.get_windows_img()

    #新增用户
    @unittest.skip("I don't want to run this case.")
    def test_add_user(self):
        user_management_page = UserManagementPage(self.driver)
        user_management_page.goto_user_management_page()
        user_management_page.switch_iframe()
        user_management_page.add_user(self.test_date_login_name,self.test_data_role_name, u"禁用",u"允许登陆美食掌柜APP")


    #修改用户
    @unittest.skip("I don't want to run this case.")
    def test_modify_user(self):
        user_management_page = UserManagementPage(self.driver)
        user_management_page.goto_user_management_page()
        user_management_page.switch_iframe()
        user_management_page.select_counts("100")
        user_management_page.modify_user(self.test_date_login_name, u"禁用", u"不允许登陆美食掌柜APP")

    #禁用
    @unittest.skip("I don't want to run this case.")
    def test_disable_user(self):
        user_management_page = UserManagementPage(self.driver)
        user_management_page.goto_user_management_page()
        user_management_page.switch_iframe()
        user_management_page.click_last_page()
        user_management_page.sleep(1)
        user_management_page.find_login_name_in_table(self.test_date_login_name)
        user_management_page.click_disable()
        user_management_page.click_ok_disable_or_delete()
        user_management_page.get_windows_img()

    # 重置密码
    @unittest.skip("I don't want to run this case.")
    def test_reset_user(self):
        user_management_page = UserManagementPage(self.driver)
        user_management_page.goto_user_management_page()
        user_management_page.switch_iframe()
        user_management_page.click_last_page()
        user_management_page.sleep(1)
        user_management_page.find_login_name_in_table(self.test_date_login_name)
        user_management_page.sleep(1)
        user_management_page.click_reset_pwd()
        user_management_page.sleep(1)
        user_management_page.input_new_pwd(self.test_date_reset_pwd)
        user_management_page.input_confirm_pwd(self.test_date_reset_pwd)
        user_management_page.get_windows_img()
        user_management_page.click_ok_btn_reset()

    # 删除
    @unittest.skip("I don't want to run this case.")
    def test_delete_user(self):
        user_management_page = UserManagementPage(self.driver)
        user_management_page.goto_user_management_page()
        user_management_page.switch_iframe()
        user_management_page.click_last_page()
        user_management_page.sleep(1)
        user_management_page.find_login_name_in_table("tyr")
        user_management_page.sleep(1)
        user_management_page.click_delete()
        user_management_page.sleep(1)
        user_management_page.click_ok_disable_or_delete()
        user_management_page.get_windows_img()

if __name__ == '__main__':
    # unittest.main(exit=False)
    unittest.main()