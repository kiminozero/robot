# coding=utf-8
import ConfigParser
import os
from framework.base_page import BasePage


class LoginPage(BasePage):
    # 定位
    company = "id=>companyName"
    login_name = "id=>loginName"
    password = "id=>password"
    submit_button= "id=>btn"

    # 自动登陆方法
    def login_auto(self):
        config = ConfigParser.ConfigParser()
        file_path = os.path.dirname(os.path.abspath('.')) + '/conf/login.ini'
        config.read(file_path)

        # 读取用户名
        user_name =config.get("companyName", "companyname")

        # 读取密码
        pass_word = config.get("passWord", "password")

        # 登录名
        name = config.get("name", "name")
        # 登陆过程
        self.type_company_name(user_name)
        self.find_element("id=>loginName").click()
        # self.wait(30)
        # self.find_element("id=>loginName").click()
        self.type_name(name)
        self.type_password(pass_word)
        self.send_submit_btn()  # 调用页面对象类中的点击按钮方法
        self.sleep(1)
        try:
            assert u'有美食' == self.get_page_title()  # 调用页面对象继承基类中的获取页面标题方法
            print ('login success.')
        except Exception as e:
            print ('login Fail.', format(e))

    def type_company_name(self, text):  #  输入手机号
        self.type(self.company, text)

    def type_name(self, text):  #  选择登录名
        self.select_xl(self.login_name, "vt", text)

    def type_password(self, text):     #输入密码
        self.type(self.password, text)

    def send_submit_btn(self):
        self.click(self.submit_button)
