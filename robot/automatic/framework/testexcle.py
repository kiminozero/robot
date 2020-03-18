# -*- coding: utf8 -*-
import os
import xlrd


class ExcelRead(object):
    file_path = os.path.dirname(os.path.abspath('.')) + '/data/user.xlsx'  # 表格名称

    bk = xlrd.open_workbook(file_path)
    # shxrange = range(bk.nsheets)
    # print shxrange
    try:
        sh = bk.sheet_by_name("Sheet1")
    except:
        print "no sheet in %s named Sheet1" % file_path

    # 获取行数
    nrows = sh.nrows
    # 获取列数
    ncols = sh.ncols

    def set_excel_path(self, name):
        self.file_path = os.path.dirname(os.path.abspath('.')) + '/data/' + name
        return self.file_path

    def read_excel_sheet(self, name):  # 设定打开表格名称

        self.bk = xlrd.open_workbook(self.set_excel_path(name))
        try:
            self.sh = self.bk.sheet_by_name("Sheet1")
        except:
            print "no sheet in %s named Sheet1" % self.file_path

    def read_excel_cell(self, row, col):  # 读excel单元格数据

        # print "nrows %d, ncols %d" % (self.nrows, self.ncols)
        # 获取第row行第col列数据
        cell_value = self.sh.cell_value(row, col)
        print cell_value
        return cell_value

    def read_excel_rows(self):  # 读取excel rows
        row_list = []
        # 获取各行数据
        for i in range(1, self.nrows):
            row_data = self.sh.row_values(i)
            row_list.append(row_data)
        print row_list
        return row_list


excel = ExcelRead()
# print excel.file_path
excel.read_excel_cell(1, 0)
excel.read_excel_cell(1, 1)
excel.read_excel_rows()
excel.read_excel_sheet(u"user1.xlsx")
excel.read_excel_cell(1, 0)
