# coding=utf-8

from framework.base_page import BasePage

from pages.main_page import MainPage


class JueSeGuanLiPage(BasePage):

    juesemingcheng1 = u"角色"
    #  角色管理页
    juesemingcheng = "name"
    jcxxjd = "selfAuthen_4_switch"
    mendianguanli = "selfAuthen_5_check"
    chaxunjuesemingcheng = "rolerName"
    quanxuan = "checkAll"
    chaxun = "btn_Search"
    xg_btn = "xpath=>.//*[@id='editable-sample']/tbody/tr[2]/td[4]/span/a[1]"
    del_btn = "xpath=>.//*[@id='editable-sample']/tbody/tr[1]/td[4]/span/a[2]"
    ok_btn = "class_name=>layui-layer-btn0"
    cancel_btn = "l=>取消"
    jueseming = "xpath=>.//*[@id='editable-sample']/tbody/tr[1]/td[2]"
    table = "xpath=>.//*[@id='editable-sample']"
    xzjs_ok = "xpath=>.//*[@id='comment']/div[3]/input"
    xgjs_ok = "xpath=>.//*[@id='comment']/div[3]/input"
    xinzengjuese = "xpath=>html/body/div[1]/div/div/div[4]/div"
    xsts = "name=>editable-sample_length"
    
    # 转到角色管理页
    def goto_jsgl(self):
        mainpage = MainPage(self.driver)
        mainpage.click_qxsz()
        mainpage.click_jsgl()


    def switch_iframe(self):
            self.switch_iframe_to("myiframe")

    # 查找角色名称
    # 在table中查找定位某登录名
    def find_juesemingcheng(self,juesemingchen1):

        table_rows = self.find_element(self.table).find_elements_by_tag_name('tr')
        i = 1
        j = len(table_rows)-1
        print j

        while (i <= j):
            # print ("++++++++++++++++++++",table_rows[i].text)
            i = i+1
            self.juesemingcheng="xpath=>.//*[@id='editable-sample']/tbody/tr["+str(i)+"]/td[2]"
            if juesemingchen1 == self.get_element_text(self.juesemingcheng):
                print ('find denglumingcheng.')
                self.del_btn = "xpath=>.//*[@id='editable-sample']/tbody/tr[" + str(i) + "]/td[4]/span/a[2]"
                self.xg_btn = "xpath=>.//*[@id='editable-sample']/tbody/tr[" + str(i) + "]/td[4]/span/a[1]"

                return 1

    #  点击新增角色
    def click_xinzengjuese(self):
        self.click(self.xinzengjuese)

    # 点击删除按钮
    def click_del_btn(self):
        self.click(self.del_btn)
    # 修改
    def click_xg_btn(self):
        self.click(self.xg_btn)

    # 权限 全选
    def click_qx(self):
        self.click(self.quanxuan)

    def click_xg_ok(self):
        self.click(self.xgjs_ok)

    def click_del_ok(self):
        self.click(self.ok_btn)

    def click_del_cancel(self):
        self.click(self.cancel_btn)

    def click_chaxun(self):
        self.click(self.chaxun)

    def type_chaxunjuesemingcheng(self):
        self.type(self.chaxunjuesemingcheng,self.juesemingcheng1)

    def type_jusemingcheng(self):
        self.type(self.juesemingcheng,self.juesemingcheng1)

    def click_juesequanxian(self):
        self.click(self.jcxxjd)
        self.click(self.mendianguanli)
        # 修改角色ok
    def click_xz_ok(self):
        self.click(self.xzjs_ok)

    def select_xsts(self,len="100"):
        self.select_xl(self.xsts, "vt", len)

    def find_table_text(self):
        table = self.find_element(self.table)
        return table.text
