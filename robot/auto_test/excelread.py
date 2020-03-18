# -*- coding: utf-8 -*-
import xlrd
import xlwt
import category
from datetime import date, datetime



def get_cell(a,b):
    # 打开文件
    workbook = xlrd.open_workbook(path)

    # 根据sheet索引或者名称获取sheet内容
    sheet1 = workbook.sheet_by_index(0)  # sheet索引从0开始

    # sheet的名称，行数，列数
    print sheet1.name, sheet1.nrows, sheet1.ncols

    # 获取整行和整列的值（数组）
    rows = sheet1.row_values(1)  # 获取第四行内容
    cols = sheet1.col_values(2)  # 获取第三列内容
    print rows
    # print cols
    for r in rows:
        print r

    print sheet1.cell(1, 3).value
    print xlrd.xldate_as_tuple(sheet1.cell(1, 3).value, 0)
    # 第一种转化为元组形式table.cell(2,1).value是取一个日期单元格的中的值，测试
    print xlrd.xldate.xldate_as_datetime(sheet1.cell(1, 4).value, 0)
    return sheet1(a,b)

def str_date(date,mode=0):
    # print date ,mode
    return str(xlrd.xldate.xldate_as_datetime(date,mode))

def read_auctions(path,excelver=1):
    if excelver==1:
        l = []
        workbook = xlrd.open_workbook(path)
        sheet1 = workbook.sheet_by_index(0)
        # print sheet1.name, sheet1.nrows, sheet1.ncols

        rows = sheet1.row_values(1)
        nrows = sheet1.nrows
        # print nrows
        for i in xrange(1,nrows):
            # auction_title=sheet1.cell(i, 0).value
            auction_description=sheet1.cell(i, 1).value
            cate_id=category.getcate_1(sheet1.cell(i, 2).value)
            # print sheet1.cell(i, 1).value.encode('utf-8')
            cate_id_1=category.getcate_2(sheet1.cell(i, 2).value,sheet1.cell(i, 3).value)
            start_time=str_date(sheet1.cell(i, 4).value,workbook.datemode)
            end_time=str_date(sheet1.cell(i, 5).value,workbook.datemode)
            firstprice=str(sheet1.cell(i, 6).value)
            addprice=str(sheet1.cell(i, 7).value)
            if sheet1.cell(i, 8).value==u"是":
                is_return = 2
            else:
                is_return =1
            if sheet1.cell(i, 9).value==u"是":
                freeship=1
            else:
                freeship=2
            if sheet1.cell(i, 10).value==u"是":
                is_commiss=1
                commissions=3
            else:
                is_commiss = 0
                commissions = 0
            is_outbonus=0
            outbonus=0
            yikoujia=str(sheet1.cell(i, 11).value)
            cankaojia=0
            reserveprice=0
            unionid=sheet1.cell(i, 12).value
            auction_path=sheet1.cell(i, 0).value

            # print auction_description,cate_id, cate_id_1, is_return, freeship, start_time, end_time, firstprice, addprice,is_commiss,commissions,yikoujia,unionid,auction_path,auction_path+"\r\n"+
            a={"auction_title":"auction_title",}
            auction={"auction_description":auction_description,"cate_id":cate_id,"cate_id_1":cate_id_1,
                     "is_return":is_return,"freeship":freeship,"start_time":start_time,"end_time":end_time,
                     "firstprice":firstprice,"addprice":addprice,"is_commiss":is_commiss,"commissions":commissions,
                     "yikoujia":yikoujia,"unionid":unionid,"auction_path":auction_path,"is_outbonus":is_outbonus,
                     "outbonus":outbonus,"cankaojia":cankaojia,"reserveprice":reserveprice,
                     }
            l.append(auction)
        return  l

    # 获取单元格内容
    # print sheet1.cell(1, 0).value.encode('utf-8')
    # print sheet1.cell_value(1, 0).encode('utf-8')
    # print sheet1.row(1)[0].value.encode('utf-8')

    # 获取单元格内容的数据类型
    # print sheet1.cell(1, 0).ctype


if __name__ == '__main__':
    # read_excel()
    path=u'\\test.xlsx'
    l=read_auctions(path)
    for i in l:
        print i
    # get_cell()