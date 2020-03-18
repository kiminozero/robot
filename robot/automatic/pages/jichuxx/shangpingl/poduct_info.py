# coding=utf-8
import os

from framework.base_page import BasePage


class ProductInfoPage(BasePage):

    # 商品信息页

    file_path = os.path.dirname(os.path.abspath('.')) + '/data/dishLoad.xls'
    # 元素定位

    pldr = "xpath=>html/body/div[1]/div/div/div[4]/div[3]/input"
    # 浏览
    ll = "file"
    qd = "xpath=>.//*[@id='mydiv']/div[3]/input"
    cx = "btn_Search"

    def switch_iframe(self):
            self.switch_iframe_to("myiframe")

    # click 批量导入
    def click_pldr(self):
        self.click(self.pldr)

    def upload_file(self):
        self.find_element(self.ll).send_keys(self.file_path)

    #  click 确定
    def click_qd(self):
        self.click(self.qd)

    def click_cx(self):
        self.click(self.cx)