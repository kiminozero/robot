# coding=utf-8
from framework import HTMLTestRunner
import os
import unittest
import time

from testsuites.test2 import Login
from testsuites.test3 import Main_Page
from testsuites.test_jue_se_guan_li import JueSeGuanLiTest
# 设置报告文件保存路径


report_path = os.path.dirname(os.path.abspath('.')) + '/test_report/'
# 获取系统当前时间
now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))

# 设置报告名称格式
HtmlFile = report_path + now + "HTMLtemplate.html"
fp = file(HtmlFile, "wb")

# 构建suite
#suite = unittest.TestLoader().discover("testsuites")
suite = unittest.TestSuite()
suite.addTest(Login('test_zgms_login'))
suite.addTest(Main_Page('test_zsy_yonghuguanli'))
suite.addTest(JueSeGuanLiTest('test_jsgl_xzjs'))
suite.addTest(JueSeGuanLiTest('test_jsgl_xgjs'))
suite.addTest(JueSeGuanLiTest('test_jsgl_scjs'))
suite.addTest(JueSeGuanLiTest('test_jsgl_scjs_fail'))
if __name__ == '__main__':
    # 初始化一个HTMLTestRunner实例对象，用来生成报告
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u"项目测试报告", description=u"用例测试情况")
    # 开始执行测试套件
    runner.run(suite)