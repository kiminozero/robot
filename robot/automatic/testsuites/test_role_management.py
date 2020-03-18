# coding=utf-8
import unittest
from framework.browser_engine import BrowserEngine
from pages.login_page import LoginPage
from pages.permissionsettings.role_management_page import RoleManagementPage
import sys

from pages.permissionsettings.user_management_page import UserManagementPage

reload(sys)
sys.setdefaultencoding('utf-8')

class RoleManagementTest(unittest.TestCase):
    test_date_role_name = u"总经理"
    test_date_role_used = u"总监"
    test_date_user_used = u"小兵"
    #@staticmethod
    def setUp(cls):
        browser = BrowserEngine(cls)
        cls.driver = browser.open_browser(cls)
        login_page = LoginPage(cls.driver)
        login_page.login_auto()
        login_page.sleep(2)

    # @classmethod
    def tearDown(cls):
        cls.driver.quit()

    # 增删改查
    # @unittest.skip("I don't want to run this case.")
    def test_add_modify_del_role(self):
        role_management_page = RoleManagementPage(self.driver)
        role_management_page.goto_role_management_page()
        role_management_page.switch_iframe()
        role_management_page.select_counts("100")
        # role_management_page.search_role_name(self.test_date_role_name)
        # self.assertIn(self.test_date_role_name,role_management_page.find_table_text())
        role_management_page.sleep(1)
        if self.test_date_role_name in role_management_page.find_table_text():
            print ("列表中有" + self.test_date_role_name + "这个角色")
            role_management_page.delete_role_name(self.test_date_role_name)
            try:
                assert self.test_date_role_name not in role_management_page.find_table_text()
                print ("删除了" + self.test_date_role_name + "这个角色")
            except Exception as e:
                print ('Test Fail.', format(e))
        role_management_page.add_role(self.test_date_role_name)
        try:
            assert self.test_date_role_name in role_management_page.find_table_text()
            print ("增加了" + self.test_date_role_name + "这个角色")
        except Exception as e:
            print ('Test Fail.', format(e))
        role_management_page.select_counts("100")
        role_management_page.modify_role(self.test_date_role_name)
        role_management_page.sleep(1)
        role_management_page.search_role_name(self.test_date_role_name)
        if self.test_date_role_name in role_management_page.find_table_text():
            print ("列表中有" + self.test_date_role_name + "这个角色")
            role_management_page.search_all_role()
            role_management_page.select_counts("100")
            role_management_page.delete_role_name(self.test_date_role_name)
        try:
            assert self.test_date_role_name not in role_management_page.find_table_text()
            print ("最后删除了" + self.test_date_role_name + "这个角色")
        except Exception as e:
            print ('Test Fail.', format(e))


    # 删除被占用的角色
    # @unittest.skip("I don't want to run this case.")
    def test_del_used_role(self):
        role_management_page = RoleManagementPage(self.driver)
        role_management_page.goto_role_management_page()
        role_management_page.switch_iframe()
        role_management_page.select_counts("100")
        role_management_page.sleep(1)
        #新增角色
        if self.test_date_role_used in role_management_page.find_table_text():
            print ("列表中有" + self.test_date_role_used + "这个角色")
        else:
            role_management_page.add_role(self.test_date_role_used)
            try:
                assert self.test_date_role_used in role_management_page.find_table_text()
                print ("增加了" + self.test_date_role_used + "这个角色")
            except Exception as e:
                print ('Test Fail.', format(e))
        #新增用户
        role_management_page.refresh()
        user_management_page = UserManagementPage(self.driver)
        user_management_page.goto_user_management_page()
        user_management_page.switch_iframe()
        user_management_page.select_counts("100")
        user_management_page.sleep(1)
        if self.test_date_user_used in user_management_page.find_table_text():
            print ("列表中有" + self.test_date_user_used + "这个用户")
            user_management_page.delete_user(self.test_date_user_used)
            try:
                assert self.test_date_user_used not in user_management_page.find_table_text()
                print ("删除了" + self.test_date_user_used + "这个用户")
            except Exception as e:
                print ('Test Fail.', format(e))
        user_management_page.add_user(self.test_date_user_used, self.test_date_role_used,u"正常",u"允许登陆美食掌柜APP")
        try:
            assert self.test_date_user_used in user_management_page.find_table_text()
            print ("增加了" + self.test_date_user_used + "这个用户")
        except Exception as e:
            print ('Test Fail.', format(e))
        role_management_page.refresh()
        role_management_page.goto_role_management_page()
        role_management_page.switch_iframe()
        role_management_page.select_counts("100")
        role_management_page.sleep(1)
        role_management_page.delete_role_name(self.test_date_role_used)
        try:
            assert self.test_date_role_used in role_management_page.find_table_text()
            print (self.test_date_role_used+"这个角色被占用,无法删除")
        except Exception as e:
            print ('Test Fail.', format(e))
        role_management_page.refresh()
        user_management_page.goto_user_management_page()
        user_management_page.switch_iframe()
        user_management_page.select_counts("100")
        user_management_page.sleep(1)
        if self.test_date_user_used in user_management_page.find_table_text():
            print ("列表中有" + self.test_date_user_used + "这个用户")
            user_management_page.delete_user(self.test_date_user_used)
            try:
                assert self.test_date_user_used not in user_management_page.find_table_text()
                print ("删除了" + self.test_date_user_used + "这个用户")
            except Exception as e:
                print ('Test Fail.', format(e))
            role_management_page.refresh()
            role_management_page.goto_role_management_page()
            role_management_page.switch_iframe()
            role_management_page.select_counts("100")
            role_management_page.sleep(1)
            if self.test_date_role_used in role_management_page.find_table_text():
                print ("列表中有" + self.test_date_role_used + "这个角色")
                role_management_page.delete_role_name(self.test_date_role_used)
                try:
                    assert self.test_date_role_used not in role_management_page.find_table_text()
                    print ("最后删除了" + self.test_date_role_used + "这个角色")
                except Exception as e:
                    print ('Test Fail.', format(e))

    # 查询有没有角色名称为“总经理”
    @unittest.skip("I don't want to run this case.")
    def test_query_role_name(self):
        role_management_page = RoleManagementPage(self.driver)
        role_management_page.goto_role_management_page()
        role_management_page.switch_iframe()
        role_management_page.query_input_role_name()
        role_management_page.click_query_role_name()
        role_management_page.sleep(1)
        # assert u"总经理" in role_management_page.find_table_text()
        # print ("列表中有‘总经理’这个角色")

    #查询全部角色
    @unittest.skip("I don't want to run this case.")
    def test_query_all_role(self):
        role_management_page = RoleManagementPage(self.driver)
        role_management_page.goto_role_management_page()
        role_management_page.switch_iframe()
        role_management_page.clear_input_role_name()
        role_management_page.sleep(1)
        role_management_page.click_query_role_name()

    #新增角色
    @unittest.skip("I don't want to run this case.")
    def test_add_role(self):
        role_management_page = RoleManagementPage(self.driver)
        role_management_page.goto_role_management_page()
        role_management_page.switch_iframe()
        role_management_page.click_add_role()
        role_management_page.sleep(1)
        role_management_page.input_role_name_pop(self.test_date_role_name)
        role_management_page.select_ji_chu_xin_xi()
        role_management_page.select_hui_yuan_guan_li()
        role_management_page.click_ok()
        role_management_page.sleep(1)
        role_management_page.select_counts("100")
        role_management_page.sleep(1)
        assert u"总经理" in role_management_page.find_table_text()
        print ('Test Pass.')
        role_management_page.get_windows_img()

    #修改角色
    @unittest.skip("I don't want to run this case.")
    def test_modify_role(self):
        role_management_page = RoleManagementPage(self.driver)
        role_management_page.goto_role_management_page()
        role_management_page.sleep(1)
        role_management_page.switch_iframe()
        role_management_page.select_counts("100")
        role_management_page.query_role_name(u"总经理")
        role_management_page.modify_role()
        role_management_page.select_wang_luo_can_ting()
        role_management_page.select_hui_yuan_guan_li()
        role_management_page.get_windows_img()
        role_management_page.click_ok()

    #删除角色
    @unittest.skip("I don't want to run this case.")
    def test_delete_role(self):
        role_management_page = RoleManagementPage(self.driver)
        role_management_page.goto_role_management_page()
        role_management_page.switch_iframe()
        role_management_page.select_counts("100")
        if role_management_page.query_role_name(u"总经理") == 1:
            role_management_page.click_delete_role()
            role_management_page.sleep(1)
            role_management_page.click_ok_del()
            role_management_page.sleep(1)
            role_management_page.get_windows_img()

if __name__ == '__main__':
    # unittest.main(exit=False)
    unittest.main()

