# coding=utf-8

from framework.base_page import BasePage


class MainPage(BasePage):

    # 权限设置
    qunxianshezhi = "link_text=>权限设置"
    jiaoseguanli = "link_text=>角色管理"
    yonghuguanli = "link_text=>用户管理"

    # 基础信息
    jichuxinxi = "link_text=>基础信息"
    mendianguanli = "link_text=>门店管理"
    shangpinguanli = "link_text=>商品管理"
    shangpinfenlei = "link_text=>商品分类"
    shangpinxinxi = "link_text=>商品信息"
    taocanshezhi = "link_text=>套餐设置"
    kouweishezhi = "link_text=>口味设置"
    shangpinchengzhong = "link_text=>商品称重"
    zhuozhangguanli = "link_text=>卓账管理"
    zhuozhangfenlei = "link_text=>桌账分类"
    zhuozhangmingxi = "link_text=>桌账明细"
    shouyinguanli = "link_text=>收银管理"
    fukuanfangshishezhi = "link_text=>付款方式设置"
    weixinzhifushezhi = "link_text=>微信支付设置"
    zhifubaozhifushezhi = "link_text=>支付宝支付设置"
    jiashouxiangmushezhi = "link_text=>加收项目设置"
    tuicailiyoushezhi = "link_text=>退菜理由设置"
    zhekoufanganshezhi = "link_text=>折扣方案设置"
    yingjianguanli = "link_text=>硬件管理"
    gongzuozhanshezhi = "link_text=>工作站设置"
    dayinjishezhi = "link_text=>打印机设置"
    diancaibaoshezhi = "link_text=>点菜宝设置"
    renyuanguanli = "link_text=>人员管理"
    shoukuanyuan = "link_text=>收款员"
    fuwuyuan = "link_text=>服务员"
    yewuyuan = "link_text=>业务员"
    kehushezhi = "link_text=>客户设置"
    zhichuguanli = "link_text=>支出管理"
    zhichuleixing = "link_text=>指出类型"
    zhichumingxi = "link_text=>支出明细"
    cangshushezhi = "link_text=>参数设置"
    fupingkongzhi ="link_text=>副屏控制"

    # 网络餐厅
    # 会员管理

    # 数据中心
    shujuzhongxin = "link_text=>数据中心"
    yingyebaobiao = "link_text=>营业报表"
    zongdianshujuhuizong = "link_text=>总店数据汇总"
    yingyeliushuimingxi = "link_text=>营业流水明细"
    yueduyingyebaobiao = "link_text=>月度营业报表"
    yingyeshiduanbaobiao = "link_text=>营业时段报表"
    wuliaoyongliangxiangqing = "link_text=>物料用量详情"
    shoukuanbaobiao = "link_text=>收款报表"
    yueduyingyeshoukuanbaobiao = "link_text=>月度营业收款报表"
    yuedushouzhibiao = "link_text=>月度收支表"
    yingyeshoukuanmingxi = "link_text=>营业收款明细"
    fanjiezhangjilu = "link_text=>反结账记录"
    jiaojiebaojilu = "link_text=>交接班记录"
    xiaofeimingxi_meishiguanchang = "link_text=>消费明细(美食广场)"
    # 采购管理
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

    # 切换iframe到myiframe
    def switch_iframe(self):
            self.switch_iframe_to("myiframe")

    # 在table中查找定位某登录名
    def find_yonghumingcheng(self,denglumingcheng1):

        # self.switch_iframe()

        table_rows = self.find_element(self.table).find_elements_by_tag_name('tr')
        i = 1
        j = len(table_rows)-1
        print j

        while (i <= j):
            # print ("++++++++++++++++++++",table_rows[i].text)
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

    # 权限设置
    def click_qxsz(self):
        self.click(self.qunxianshezhi)

    # 角色管理
    def click_jsgl(self):
        self.click(self.jiaoseguanli)

    # 用户管理
    def click_yhgl(self):
        self.click(self.yonghuguanli)

    # 基础信息
    def click_jcxx(self):
        self.click(self.jichuxinxi)

    # 商品管理
    def click_spgl(self):
        self.click(self.shangpinguanli)

    # 商品信息
    def click_spxx(self):
        self.click(self.shangpinxinxi)
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

    def click_sjzx(self):
        self.click(self.shujuzhongxin)

    def click_yybb(self):
        self.click(self.yingyebaobiao)

    def click_yylsmx(self):
        self.click(self.yingyeliushuimingxi)