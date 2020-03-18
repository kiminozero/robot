# coding=utf-8
from framework.base_page import BasePage
from pages.main_page import MainPage
import unittest

#角色管理页
class RoleManagementPage(BasePage):

    query_role_name_input = "rolerName"
    query_btn = "btn_Search"
    add_role_btn = "xpath=>/html/body/div[1]/div/div/div[4]/div"
    table = "xpath=>//*[@id='editable-sample']"
    role_name_in_pop = "name"
    select_all_in_pop = "checkAll"
    ok_btn_in_pop = "xpath=>//*[@id='comment']/div[3]/input"
    cancel_btn_in_pop = "xpath=>//*[@id='addTable']/div/div/div[1]/div[3]/a"
    ok_btn_del_pop = "class_name=>layui-layer-btn0"
    cancel_btn_del_pop = "class_name=>layui-layer-btn1"
    cancel_icon_del_pop = "xpath=>//*[@id='layui-layer3']/span/a"
    show_counts = "name=>editable-sample_length"
    #角色权限加减号
    quan_xian_she_zhi = "selfAuthen_1_switch"
    ji_chu_xin_xi = "selfAuthen_4_switch"
    wang_luo_can_ting = "selfAuthen_36_switch"
    hui_yuan_guan_li = "selfAuthen_46_switch"
    shu_ju_zhong_xin ="selfAuthen_48_switch"
    cai_gou_guan_li = "selfAuthen_71_switch"
    ku_cun_guan_li = "selfAuthen_79_switch"
    sheng_chan_jia_gong = "selfAuthen_91_switch"
    #角色权限一级框
    check_quan_xian_she_zhi = "selfAuthen_1_check"
    check_ji_chu_xin_xi = "selfAuthen_4_check"
    check_wang_luo_can_ting = "selfAuthen_36_check"
    check_hui_yuan_guan_li = "selfAuthen_46_check"
    check_shu_ju_zhong_xin = "selfAuthen_48_check"
    check_cai_gou_guan_li = "selfAuthen_71_check"
    check_ku_cun_guan_li = "selfAuthen_79_check"
    check_sheng_chan_jia_gong = "selfAuthen_91_check"
    #角色权限二级框
    check_goto_crm = "selfAuthen_47_check"


    #进入角色管理页
    def goto_role_management_page(self):
        mainpage = MainPage(self.driver)
        mainpage.click_qxsz()
        mainpage.click_jsgl()

    def switch_iframe(self):
            self.switch_iframe_to("myiframe")

    #在列表中查询角色名称存在不存在：
    def query_role_name(self,test_date_role_name):
        table_rows = self.find_element(self.table).find_elements_by_tag_name("tr")
        i = 1
        j = len(table_rows)-1
        while(i<=j):
            i = i+1
            role_name = "xpath=>.//*[@id='editable-sample']/tbody/tr[" + str(i) + "]/td[2]"
            if test_date_role_name == self.get_element_text(role_name):
                print ("find role"+test_date_role_name)
                self.modify_btn = "xpath=>//*[@id='editable-sample']/tbody/tr[" + str(i) + "]/td[4]/span/a[1]"
                self.delete_btn = "xpath=>//*[@id='editable-sample']/tbody/tr[" + str(i) + "]/td[4]/span/a[2]"
                return 1

    #查询输入框输入角色名称
    def query_input_role_name(self,test_date_role_name):
        self.type(self.query_role_name_input,test_date_role_name)

    #点击查询
    def click_query_role_name(self):
        self.click(self.query_btn)

    #清空查询输入框
    def clear_input_role_name(self):
        self.clear(self.query_role_name_input)

    #点击新增角色
    def click_add_role(self):
        self.click(self.add_role_btn)
        print ("新增角色")

    #点击修改角色
    def click_modify_role(self):
        self.click(self.modify_btn)
        print ("修改角色")

    #点击删除角色
    def click_delete_role(self):
        self.click(self.delete_btn)
        print ("删除角色")

    #pop中输入角色名称
    def input_role_name_pop(self,test_date_role_name):
        self.type(self.role_name_in_pop,test_date_role_name)

    #全选
    def select_all(self):
        self.click(self.select_all_in_pop)

    #新增和修改里面的确定
    def click_ok(self):
        self.click(self.ok_btn_in_pop)

    #新增和修改里面的X
    def click_cancel(self):
        self.click(self.cancel_btn_in_pop)

    #删除框里面的确定
    def click_ok_del(self):
        self.click(self.ok_btn_del_pop)

    #删除框里面的取消
    def click_cancel_btn_del(self):
        self.click(self.cancel_btn_del_pop)

    #删除框里面的X
    def click_cancel_icon_del(self):
        self.click(self.cancel_icon_del_pop)

    #选择基础信息
    def select_ji_chu_xin_xi(self):
        self.click(self.check_ji_chu_xin_xi)

    #选择会员管理
    def select_hui_yuan_guan_li(self):
        self.click(self.check_hui_yuan_guan_li)

    #选择网络餐厅
    def select_wang_luo_can_ting(self):
        self.click(self.check_wang_luo_can_ting)

    #选择每页显示条数
    def select_counts(self, length):
        self.select_xl(self.show_counts, "vt", length)

    #查找列表信息
    def find_table_text(self):
        table = self.find_element(self.table)
        return table.text

    #查询角色
    def search_role_name(self, test_date_role_name):
        self.query_input_role_name(test_date_role_name)
        self.click_query_role_name()
        self.sleep(1)

    #查询全部角色
    def search_all_role(self):
        self.clear_input_role_name()
        self.click_query_role_name()

    #删除角色
    def delete_role_name(self, test_date_role_name):
        # self.select_counts("100")
        # self.search_role_name(test_date_role_name)
        if self.query_role_name(test_date_role_name) == 1:
            self.click_delete_role()
            self.sleep(1)
            self.click_ok_del()
            self.sleep(1)
            self.get_windows_img()

    #新增角色
    def add_role(self, test_date_role_name):
        self.click_add_role()
        self.sleep(1)
        self.input_role_name_pop(test_date_role_name)
        self.select_ji_chu_xin_xi()
        self.select_hui_yuan_guan_li()
        self.click_ok()
        self.sleep(1)

    #修改角色
    def modify_role(self, test_date_role_name):
        # self.search_role_name(test_date_role_name)
        self.sleep(1)
        if self.query_role_name(test_date_role_name) == 1:
            self.click_modify_role()
            self.select_wang_luo_can_ting()
            self.select_hui_yuan_guan_li()
            self.get_windows_img()
            self.click_ok()
