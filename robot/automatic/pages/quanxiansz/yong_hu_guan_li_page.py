# coding=utf-8

from framework.base_page import BasePage
from pages.main_page import MainPage


class YongHuGuanLiPage(BasePage):

    denglumingcheng = "xpath=>.//*[@id='editable-sample']/tbody/tr[1]/td[2]"
    del_btn = "xpath=>.//*[@id='editable-sample']/tbody/tr[2]/td[8]/span/a[3]"
    del_ok_btn = "class_name=>layui-layer-btn0"  # "xpath=>.//*[@id='layui-layer1']/div[3]/a[1]"
    del_cancel_btn = "class_name=>layui-layer-btn1"
    xinzengyonghu = "xpath=>html/body/div[1]/div/div/div[4]/div"
    xinzengjuese = "xpath=>html/body/div[1]/div/div/div[4]/div"
    denglumingcheng1 = 'test001'
    dengluming = "loginName1"
    juese = "rid"
    xz_ok_btn = "xpath=>.//*[@id='comment']/div[8]/input"
    table = "xpath=>.//*[@id='editable-sample']"
    miandan ="md"
    qiangzhiyouhui = "qzyh"
    jinyong ="xpath=>.//*[@id='editable-sample']/tbody/tr[4]/td[8]/span/a[2]"
    qiyong = "xpath=>.//*[@id='editable-sample']/tbody/tr[4]/td[8]/span/a[2]"
    xiugai = "xpath=>.//*[@id='editable-sample']/tbody/tr[5]/td[8]/span/a[1]"
    xyy = "link_text=>下一页"
    #  角色管理页
    juesemingcheng = "name"
    jcxxjd = "selfAuthen_4_switch"
    mendianguanli = "selfAuthen_5_check"
    chaxunjuesemingcheng = "rolerName"
    chaxunanniu = "btn_Search"

    def goto_yhgl(self):
        mainpage = MainPage(self.driver)
        mainpage.click_qxsz()
        mainpage.click_yhgl()

    # 切换iframe到myiframe
    def switch_iframe(self):
            self.switch_iframe_to("myiframe")

    # 在table中查找定位某登录名
    def find_yonghumingcheng(self,denglumingcheng1):

        table_rows = self.find_element(self.table).find_elements_by_tag_name('tr')
        i = 1
        j = len(table_rows)-1
        while (i <= j):
            i = i+1
            self.denglumingcheng="xpath=>.//*[@id='editable-sample']/tbody/tr["+str(i)+"]/td[2]"
            if denglumingcheng1 == self.get_element_text(self.denglumingcheng):
                print ('find denglumingcheng.')
                self.del_btn = "xpath=>.//*[@id='editable-sample']/tbody/tr[" + str(i) + "]/td[8]/span/a[3]"
                return 1

    # 确认table 存在text
    def assert_has_text(self,text):

        # self.switch_iframe()

        table = self.find_element(self.table)
        try:
            assert text in  table.text
            print ('find text.')
            return True
        except Exception as e:
            print ("find fail.", format(e))

        # 点击删除按钮

    def click_xinzengyonghu(self):

        self.click(self.xinzengyonghu)


    def click_qiangzhiyouhui(self):
        self.click(self.qiangzhiyouhui)

    def click_miandan(self):
        self.click(self.miandan)


    def click_del_btn(self):
        self.click(self.del_btn)

    def click_del_ok(self):
        self.click(self.del_ok_btn)

    def click_xzok_btn(self):
        self.click(self.xz_ok_btn)

    def type_yhm(self,text):
        self.type(self.dengluming,text)

    # 通过可见文本选择 角色 下拉菜单
    def type_js(self):
        #self.select_xl(self.juese,"value","6593")
        self.select_xl(self.juese, "vt", "test001")

    # 禁用
    def click_jy(self):
        self.click(self.jinyong)
    # 启用
    def click_qi(self):
        self.click(self.qiyong)
    # 修改
    def click_xg(self):
        self.click(self.xiugai)
    # 点击下一页
    def click_xyy(self):
        self.click(self.xyy)

