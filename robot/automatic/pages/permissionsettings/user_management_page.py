# coding=utf-8
from framework.base_page import BasePage
from pages.main_page import MainPage

#用户管理页
class UserManagementPage(BasePage):

    login_name = "loginName"
    search_btn = "btn_Search"
    add_user_btn = "xpath=>/html/body/div[1]/div/div/div[4]/div"
    show_counts = "name=>editable-sample_length"
    login_name_pop = "loginName1"
    status_pop = "status"
    role_pop = "rid"
    allow_msy_pop="cateShopKeepFlag"
    miandan_pop = "md"
    fanjiezhang_pop = "fjz"
    qiang_zhi_you_hui_pop = "qzyh"
    tui_cai_pop = "yxtc"
    login_fen_dian_pop = "yxdlfd"
    ok_btn_pop = "xpath=>//*[@id='comment']/div[8]/input"
    cancel_icon_pop = "xpath=>//*[@id='addTable']/div/div/div[1]/div[3]/a"
    ok_btn_del_or_disable = "class_name=>layui-layer-btn0"
    cancel_btn_del_or_disable = "class_name=>layui-layer-btn1"
    cancel_icon_del_or_disable = "xpath=>//*[@id='layui-layer5']/span/a"
    new_pwd_reset = "newPwd"
    confirm_pwd_reset = "rePwd"
    ok_btn_reset = "xpath=>//*[@id='rePwdCt']/div/div/div[2]/div[3]/input"
    cancel_icon_reset = "xpath=>//*[@id='rePwdCt']/div/div/div[1]/div[3]/a"
    last_page = "xpath=>//*[@id='editable-sample_paginate']/ul/li[6]/a"
    table = "xpath=>.//*[@id='editable-sample']"

    #进入用户管理页
    def goto_user_management_page(self):
        main_page = MainPage(self.driver)
        main_page.click_qxsz()
        main_page.click_yhgl()

    # 切换iframe到myiframe
    def switch_iframe(self):
        self.switch_iframe_to("myiframe")

    #在表格中查找登录名称
    def find_login_name_in_table(self,test_date_login_name):
        table_rows = self.find_element(self.table).find_elements_by_tag_name('tr')
        i = 1
        j = len(table_rows) - 1
        while(i <= j):
            i = i+1
            login_name = "xpath=>.//*[@id='editable-sample']/tbody/tr["+str(i)+"]/td[2]"
            if test_date_login_name == self.get_element_text(login_name):
                print (u"找到登录名称为"+test_date_login_name+u"的用户了")
                self.modify_btn = "xpath=>//*[@id='editable-sample']/tbody/tr["+str(i)+"]/td[8]/span/a[1]"
                self.disable_btn = "xpath=>//*[@id='editable-sample']/tbody/tr["+str(i)+"]/td[8]/span/a[2]"
                self.state = "xpath=>//*[@id='editable-sample']/tbody/tr["+str(i)+"]/td[4]"
                self.delete_btn = "xpath=>//*[@id='editable-sample']/tbody/tr["+str(i)+"]/td[8]/span/a[3]"
                self.reset_pwd_btn = "xpath=>//*[@id='editable-sample']/tbody/tr["+str(i)+"]/td[8]/span/a[4]"
                return 1

    #查询输入框输入登录名称
    def input_search_login_name(self,test_date_login_name):
        self.type(self.login_name,test_date_login_name)

    #点击查询按钮
    def click_search_btn(self):
        self.click(self.search_btn)

    #点击新增用户
    def click_add_user_btn(self):
        self.click(self.add_user_btn)

    #新增用户窗口输入登录名
    def input_login_name_pop(self,test_date_login_name):
        self.type(self.login_name_pop,test_date_login_name)

    #选择状态
    def select_status_pop(self, state):
        self.click(self.status_pop)
        self.select_xl(self.status_pop,"vt", state)

    #选择角色
    def select_role(self,test_date_role_name):
        self.select_xl(self.role_pop,"vt",test_date_role_name)

    #选择允许不允许登录美食掌柜
    def select_allow_msy(self, allow):
        self.click(self.allow_msy_pop)
        self.select_xl(self.allow_msy_pop,"vt", allow)

    #点击免单
    def click_mian_dan(self):
        self.click(self.miandan_pop)

    #点击反结账
    def click_fan_jie_zhang(self):
        self.click(self.fanjiezhang_pop)

    #点击强制优惠
    def click_qiang_zhi_you_hui(self):
        self.click(self.qiang_zhi_you_hui_pop)

    #点击退菜
    def click_tui_cai(self):
        self.click(self.tui_cai_pop)

    #点击登录分店
    def click_login_fen_dian(self):
        self.click(self.login_fen_dian_pop)

    #点击新增或修改的确定
    def click_ok_pop(self):
        self.click(self.ok_btn_pop)

    #点击新增或修改的取消（X)
    def click_cancel_icon_pop(self):
        self.click(self.cancel_icon_pop)

    #点击修改
    def click_modify(self):
        self.click(self.modify_btn)

    #点击禁用
    def click_disable(self):
        self.click(self.disable_btn)

    #点击删除
    def click_delete(self):
        self.click(self.delete_btn)

    #点击重置密码
    def click_reset_pwd(self):
        self.click(self.reset_pwd_btn)

    #点击禁用或者删除的确定
    def click_ok_disable_or_delete(self):
        self.click(self.ok_btn_del_or_disable)

    #点击禁用或者删除的取消
    def click_cancel_btn_disable_or_delete(self):
        self.click(self.cancel_btn_del_or_disable)

    #点击禁用或者删除的叉号（X)
    def click_cancel_icon_disable_or_delete(self):
        self.click(self.cancel_icon_del_or_disable)

    #重置密码-输入新密码
    def input_new_pwd(self,test_date_new_pwd):
        self.type(self.new_pwd_reset,test_date_new_pwd)

    #重置密码-输入确认密码
    def input_confirm_pwd(self,test_date_new_pwd):
        self.type(self.confirm_pwd_reset,test_date_new_pwd)

    #重置密码-确定
    def click_ok_btn_reset(self):
        self.click(self.ok_btn_reset)

    #重置密码-叉号（X)
    def click_cancel_icon_reset(self):
        self.click(self.cancel_icon_reset)

    #点击尾页
    def click_last_page(self):
        self.click(self.last_page)

    # 选择每页显示条数
    def select_counts(self, length):
        self.select_xl(self.show_counts, "vt", length)

    #查找列表信息
    def find_table_text(self):
        table = self.find_element(self.table)
        return table.text

    #删除用户
    def delete_user(self, test_date_login_name):
        if self.find_login_name_in_table(test_date_login_name) == 1:
            self.sleep(1)
            self.click_delete()
            self.sleep(1)
            self.click_ok_disable_or_delete()
            self.get_windows_img()

    #增加用户
    def add_user(self, test_date_login_name, test_data_role_name, state,allow):
        self.sleep(1)
        self.click_add_user_btn()
        self.sleep(1)
        self.input_login_name_pop(test_date_login_name)
        self.select_status_pop(state)
        self.select_role(test_data_role_name)
        self.select_allow_msy(allow)
        self.click_mian_dan()
        self.click_fan_jie_zhang()
        self.click_ok_pop()
        self.sleep(1)

    #修改用户
    def modify_user(self,test_date_login_name, state, allow):
        self.sleep(1)
        if self.find_login_name_in_table(test_date_login_name) == 1:
            self.click_modify()
            self.sleep(1)
            self.select_status_pop(state)
            self.select_allow_msy(allow)
            self.click_mian_dan()
            self.click_qiang_zhi_you_hui()
            self.get_windows_img()
            self.click_ok_pop()
            self.sleep(1)

    #查询所有的用户
    def search_all_user(self):
        self.clear(self.login_name)
        self.click(self.search_btn)

    #启用禁用
    def turn_on_off(self,test_fixed_user):
        self.sleep(1)
        if self.find_login_name_in_table(test_fixed_user) == 1:
            print (u"当前状态是" + self.get_element_text(self.state))
            try:
                self.click_disable()
                self.click_ok_disable_or_delete()
                self.sleep(1)
                print (u"启用禁用成功")
                print (u"状态改为" + self.get_element_text(self.state))
            except Exception as e:
                print ('Test Fail.', format(e))
                print (u"启用禁用发生错误")

    #重置密码
    def reset_pwd(self,test_fixed_user,test_date_reset_pwd):
        self.sleep(1)
        if self.find_login_name_in_table(test_fixed_user) == 1:
            self.sleep(1)
            self.click_reset_pwd()
            self.sleep(1)
            try:
                self.input_new_pwd(test_date_reset_pwd)
                self.input_confirm_pwd(test_date_reset_pwd)
                self.click_ok_btn_reset
                print (u"重置密码成功")
            except Exception as e:
                print ('Test Fail.', format(e))
                print (u"重置密码发生错误")