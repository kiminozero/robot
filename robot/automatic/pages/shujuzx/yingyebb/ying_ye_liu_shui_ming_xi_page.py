# coding=utf-8

from framework.base_page import BasePage
from pages.main_page import MainPage


class YingYeLiuShuiMingXiPage(BasePage):


    # 元素定位
    dqmd = "companyNo_nameId"
    ksss = "bTime"
    jsss = "eTime"
    cx = "btn_Search"
    cpcx = "one1"
    ddcx = "one2"
    yt = "lastDay"
    yz = "lastWeek"
    yy = "lastMonth"
    gjcx = "seniorSearch"
    chakan = "xpath=>.//*[@id='editable-sample2']/tbody/tr[1]/td[18]/span/a"

    def goto_yylsmx(self):
        mainpage = MainPage(self.driver)
        mainpage.click_sjzx()
        mainpage.click_yybb()
        mainpage.click_yylsmx()


    def switch_iframe(self):
            self.switch_iframe_to("myiframe")

    # click 订单查询
    def click_ddcx(self):
        self.click(self.ddcx)

    #  click 查看
    def click_chakan(self):
        self.click(self.chakan)

    def click_cx(self):
        self.click(self.cx)