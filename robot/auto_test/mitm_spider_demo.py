# -*- coding: utf-8 -*-
import json
import os
import random
import threading
import datetime
import queue
import sys
import re
import time
from bs4 import BeautifulSoup
import requests
import mitmproxy.flow
from future.backports.urllib import parse

from mitmproxy import ctx

import json
import datetime

headers = {

    "Connection", "keep-alive",
    "Cache-Control", "max-age=0",
    "Upgrade-Insecure-Requests", "1",
    "User-Agent",
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36",
    "Accept",
"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
    "Accept-Encoding", "gzip, deflate",
    "Accept-Language", "zh-CN,zh;q=0.9",
    
}
headers1 = {"Host": "api.testsite.com",
            "Connection": "keep-alive",
            "Content-Length": "51",
            "Accept": "*/*",
            "Origin": "http://api.testsite.com",
            "X-Requested-With": "XMLHttpRequest",
            "User-Agent": "Mozilla/5.0 (Linux; Android 9; STF-AL10 Build/HUAWEISTF-AL10; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/66.0.3359.126 MQQBrowser/6.2 TBS/044813 Mobile Safari/537.36 MMWEBID/8572 MicroMessenger/6.7.3.1360(0x2607033D) NetType/WIFI Language/zh_CN Process/tools",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN,zh-CN;q=0.9,ja-JP;q=0.8,en-US;q=0.7",
              }
headers2 = {
    "Host": "newapi.testsite.cn",
    "Origin": "https://www.testsite.cn",
    "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
    "Accept-Language": "zh-cn",
    "Accept-Encoding": "br, gzip, deflate",
    "Connection": "keep-alive",
    "Accept": "application/json, text/plain, */*",
    "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/7.0.5(0x17000523) NetType/WIFI Language/zh_CN",
     "Referer": "https://www.testsite.cn/content/2.0/dist/",
}

headers3={
  "Host":"www.testsite.com",
  "Connection":"keep-alive",
   "Pragma":"no-cache",
  "Cache-Control":"no-cache",
   "Accept":"application/json, text/javascript, */*; q=0.01",
  "X-Requested-With":"XMLHttpRequest",
  "User-Agent":"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3    809.100 Mobile Safari/537.36",
  "Content-Type":"application/x-www-form-urlencoded; charset=UTF-8",
   "Origin":"http://www.testsite.com",
   "Referer":"http://www.testsite.com/jsp/ecp/item/manage/auctroomitemquerylist.jsp?saleroomid=2147486517&h=778",
   "Accept-Encoding":"gzip, deflate",
     "Accept-Language":"zh-CN,zh;q=0.9",
   }


s = requests.Session()
s.headers = headers
urls = []

s1 = requests.Session()
s1.headers = headers1

s2 = requests.Session()
s2.headers = headers2

s3=requests.Session()
s3.headers=headers3

def find_id(
        url="http://appapi.testsite.com/api/ydAuction/findYdAuction?activeStatus=0&businessCategory=1068588&hasSearch=3&pageNum=1&pageSize=2&userId=0"):
    topic_ids = []
    r = s.get(url)
    topic_ids = r.json()['data']['result']
    return topic_ids


# print(find_id())

def get_auction(topic_id=''):
    data = "hasSearch=3&id=65595627&pageNum=1&pageSize=100&sortKey=1&sortType=1"
    r = s.get("http://appapi.testsite.com/api/ydAuction/findTaregtInstances?hasSearch=3&id=" + str(
        topic_id) + "&pageNum=1&pageSize=100&sortKey=1&sortType=1")
    print(r.content)
    auction_ids = r.json()['data']['result']
    return auction_ids


def get_auction_yes(topic_id=''):
    # ctx.log.info(topic_id)
    data = "order=desc&orderby=sn&limit=200&auctionSessionId=" + str(topic_id)
    r = s1.post("http://api.testsite.com/api.php?do=auction&act=list", data=data)
    print(r.content)
    auction_ids = r.json()['auctions']
    return auction_ids


def find_auction(auction_ids):
    urls = []
    for a in auction_ids:
        aid = str(a['targetInsatnceId'])
        data = aid + "?id=" + aid + "&delay=1"
        r = s.get("http://appapi.testsite.com/api/ydAuction/getNetInstanceById/" + data)
        print(r.content)
        auction = [re.sub(r'[,. -!?:/\\]', '', r.json()['data']['name']), r.json()['data']['bigImage']]
        urls.append(auction)
    return urls


def find_auction_yes(auction_ids):
    urls = []
    for a in auction_ids:
        aid = str(a['auctionId'])
        data = "auctionId=" + aid
        r = s1.post("http://api.testsite.com/api.php?do=auction&act=details_PC", data=data)
        print(r.content)
        auction = [re.sub(r'[,. -!?:/\\]', '', r.json()['title']), r.json()['images_b']]
        urls.append(auction)
    return urls


# find_auction(auction_ids=get_auction())

# print(urls)

# zhuanchang=u"臻品和田玉专场"
def save(title, urls):
    # print urls
    # print title
    # print type(title)
    print("./images/", fenlei, zhuanchang)
    # pathdir=u"./images/"+fenlei+zhuanchang
    pathdir = u"/home/develop/" + fenlei + zhuanchang
    if not os.path.exists(pathdir):
        # os.mkdir(pathdir)
        os.makedirs(pathdir)

    dir_name = pathdir + '/' + title
    dir_name = dir_name.strip()
    if not os.path.exists(dir_name):
        try:
            os.mkdir(dir_name)
            i = 1
            for url in urls:
                image = requests.get(url).content
                with open(dir_name + "/" + str(i) + '.jpg', 'wb') as file:
                    file.write(image)
                i = i + 1
        except Exception as e:
            print(e)
    else:
        pass


def save_by_topic(topic_ids):
    global zhuanchang
    for t in topic_ids:

        zhuanchang = re.sub(r'[,. -!?:/\\]', '', t['name'])
        topic_id = t['id']
        auction_ids = get_auction(topic_id)
        urls1 = find_auction(auction_ids)
        for u in urls1:
            save(u[0], u[1])


def net_save(title, urls):
    # print urls
    # print title
    # print type(title)
    print("./images/", fenlei, zhuanchang)
    # pathdir=u"./images/"+fenlei+zhuanchang
    pathdir = u"f:/workspace/" + fenlei + zhuanchang
    if not os.path.exists(pathdir):
        # os.mkdir(pathdir)
        os.makedirs(pathdir)

    dir_name = pathdir + '/' + title
    dir_name = dir_name.strip()
    if not os.path.exists(dir_name):
        try:
            os.mkdir(dir_name)
            js = {"urls": urls, "dir_name": dir_name}
            # r=s.post("http://127.0.0.1:1323/save",json=js)
            # r = s.post("http://127.0.0.1:1323/save_limit", json=js)
            r = s.post("http://127.0.0.1:1323/save_limit", json=js)
            print(r.content)
        except Exception as e:
            print(e)
    else:
        pass


def net_save_by_topic(topic_ids):
    global zhuanchang
    for t in topic_ids:

        zhuanchang = re.sub(r'[,. -!?:/\\]', '', t['name'])
        topic_id = t['id']
        auction_ids = get_auction(topic_id)
        urls1 = find_auction(auction_ids)
        for u in urls1:
            net_save(u[0], u[1])


def find_auction_xing(auction_ids):
    urls = []
    for a in auction_ids:
        aid = str(a['id'])
        data = "ProductId=" + str(aid) + "&UserId=dd63e2dfe6d14fce88c00706ecb309e5"
        r = s2.post("https://newapi.testsite.cn/WebApi/Details/GetEPDetails", data=data)
        print(r.content)
        images = []
        for i in r.json()['data']['product_imgs']:
            images.append(i['photo2'])
        auction = [re.sub(r'[,. -!?:/\\]', '', r.json()['data']['product_name']), images]
        urls.append(auction)
    return urls


def get_auction_xing(topic_id=''):
    # ctx.log.info(topic_id)
    data = "SpecialId=" + str(topic_id) + "&PageIndex=1&PageSize=100"
    r = s2.post("https://newapi.testsite.cn/WebApi/Special/GetSpecialDetailById", data=data)
    print(r.content)
    auction_ids = r.json()['data']['data']['productlist']
    return auction_ids


def net_save_by_topic_yes(topic_ids):
    global zhuanchang
    for t in topic_ids:

        zhuanchang = re.sub(r'[,. -!?:/\\]', '', t['title'])
        topic_id = t['auctionSessionId']
        auction_ids = get_auction_yes(topic_id)
        urls1 = find_auction_yes(auction_ids)
        for u in urls1:
            net_save(u[0], u[1])


def net_save_by_topic_xing(topic_ids):
    global zhuanchang
    for t in topic_ids:

        zhuanchang = re.sub(r'[,. · -!?:/\\]', '', t['special_name'])
        topic_id = t['id']
        auction_ids = get_auction_xing(topic_id)
        urls1 = find_auction_xing(auction_ids)
        for u in urls1:
            net_save(u[0], u[1])

def find_auction_rade(auction_ids):
    urls = []
    for a in auction_ids:
        aid = str(a['LOT_ID'])
        js = {"lotId": aid, "saleRoomId": "", "showRoom": ""}
        data = 'dataStr=' + parse.quote(json.dumps(js))
        r = s3.post("http://www.testsite.com/ecp/catalogueinfo/getcatalogueinfobylotid.action", data=data)
        # print(r.headers)
        # print(r.content)
        try:
            images = []
            images.append(r.json()['data']['majorItemPic']['filepath'] + ".jpg")
            for i in r.json()['data']['otherItemPicList']:
                images.append(i['filepath'] + ".jpg")

            auction = [re.sub(r'[,. -!?:/\\]', '', r.json()['data']['itemInfo']['itemName']), images]
            urls.append(auction)
        except:
            print(data)
            print(r.headers)
    return urls

def get_auction_rade(topic_id=''):
    # ctx.log.info(topic_id)
    js = {"queryId": "itemSaleRoomListsQuery", "filterMap": {"saleRoomId": topic_id, "timeFlag": "all"},
          "pageInfo": {"currentPage": 1, "pageCount": 0, "recordCount": 0, "pageSize": "200"}}
    data = 'queryData=' + parse.quote(json.dumps(js))
    r = s3.post("http://www.testsite.com/ecp/item/input/iteminput/querysriteminfo.action", data=data)

    auction_ids = r.json()['data']['data']
    print len(auction_ids)
    print data
    print auction_ids
    return auction_ids

def net_save_by_topic_rade(topic_ids):
    global zhuanchang
    for t in topic_ids:

        zhuanchang = re.sub(r'[,. -!?:/\\]', '', t['SRNAME'])
        topic_id = t['SALEROOMID']
        auction_ids = get_auction_rade(topic_id)
        urls1 = find_auction_rade(auction_ids)
        for u in urls1:
            net_save(u[0], u[1])


# fenlei=u"testpath/0806/"

# zhuanchang="0801"


topic_ids = []


def get_str_day(days=0):
    return (datetime.date.today() + datetime.timedelta(days=days)).strftime('%Y%m%d')


# fenlei=u"testpath/"+tomorrow+"/"




dir_name1 = "/root/mitm/logs"
# today = datetime.date.today().strftime('%Y%m%d')
today = get_str_day(0)
tomorrow = get_str_day(1)
fenlei = u"testpath/" + tomorrow + "/"


def response(flow):
    today = get_str_day(0)
    tomorrow = get_str_day(1)
    # ctx.log.info(flow.request.url)

    # if "/api/ydAuction/" in flow.request.path:
    if re.match('/api/ydAuction/\d+', flow.request.path):
        # ctx.log.info(flow.response.text)
        data = json.loads(flow.response.text)
        ctx.log.info(flow.request.path)
        auc = json.dumps(data['data'])
        topic_ids = []
        topic_ids.append(data['data'])

        # save_by_topic(topic_ids)
        net_save_by_topic(topic_ids)

        with open(dir_name1 + '/' + today + ".log", 'a+') as f:
            f.write(auc + '\n')
    elif re.match('/api/auction/\d+', flow.request.path):
        # ctx.log.info(flow.response.text)
        auction_id = flow.request.path.split("/")[-1]
        data = json.loads(flow.response.text)
        data['data']['id'] = auction_id
        data['data']['name'] = data['data']['auctionName']
        ctx.log.info(flow.request.path)
        auc = json.dumps(data['data'])
        topic_ids = []
        topic_ids.append(data['data'])

        # save_by_topic(topic_ids)
        net_save_by_topic(topic_ids)

        with open(dir_name1 + '/' + today + ".log", 'a+') as f:
            f.write(auc + '\n')

    if 'http://api.testsite.com/api.php?do=auction_session&act=details_PC' == flow.request.url:
        # ctx.log.info(flow.response.text)
        data = json.loads(flow.response.text)
        ctx.log.info(flow.request.path)
        auc = json.dumps(data)
        topic_ids = []
        topic_ids.append(data)

        # save_by_topic(topic_ids)
        net_save_by_topic_yes(topic_ids)

        with open(dir_name1 + '/' + today + "new.log", 'a+') as f:
            f.write(auc + '\n')

    if 'https://newapi.testsite.cn/WebApi/Special/GetSpecialDetailById' == flow.request.url:
        # ctx.log.info(flow.response.text)
        data = json.loads(flow.response.text)
        ctx.log.info(flow.request.path)
        auc = json.dumps(data['data']['data'])
        topic_ids = []
        topic_ids.append(data['data']['data']['special'])

        # save_by_topic(topic_ids)
        net_save_by_topic_xing(topic_ids)

        with open(dir_name1 + '/' + today + "new.log", 'a+') as f:
            f.write(auc + '\n')


if __name__ == "__main__":

    today = get_str_day(0)
    tomorrow = get_str_day(1)
    # today = datetime.date.today().strftime('%Y%m%d')
    # tomorrow=(datetime.date.today()+datetime.timedelta(days=1)).strftime('%Y%m%d')

    pt = u"f:/workspace/testpath" + tomorrow

    # if not os.path.exists(pt):
    #     os.mkdir(pt)

    # fenlei = u"testpath/" + tomorrow + "/"
    # js={"data":{"data":{"special":{"id":"6a32e5e966014f039e11c435ea2bf3c6","special_name":u"匠心 · 当代瓷器精品合辑（五）","product_count":13,"look_count":1180,"price_count":146,"start_date":"2019/8/16 9:00:00","end_date":"2019/8/17 21:40:00","order_num":2625,"remark":"","rectangle":"https://cdns.testsite.cn/uploadimages/20190814/eb4b934f41e54c57a823a6f890146b53.jpg","square":"","special_type":0,"special_state_name":"已结束"},"productlist":[{"id":"106fbd6b8f474ebe89018c650d4e4df3","old_id":0,"prefix1":None,"suffix1":None,"suffix2":None,"artist_id":None,"product_name":"阳士琦《苹果绿梅花胆瓶 阳士琦 官窑粉彩传承人》","product_count":0,"standard_width":None,"standard_height":None,"standard_length":None,"quality":None,"phase":None,"start_price":0.0,"increase_price":0.0,"max_price":0.0,"maxprice":4600.0,"create_year":None,"order_num":2625,"start_date":"2019/8/16 9:00:00","end_date":"2019/8/17 21:40:00","product_type":None,"remark":None,"product_state":0,"product_state_name":"已结束","sale_type":2,"SaleTypeName":None,"flat_scale":None,"look_count":59,"price_count":11,"photo":"https://cdns.testsite.cn/uploadimages/20190814/1a3c6f9613f64377a3f147768cf7caf6.min.jpg?imageView2/1/w/370/h/370","price":None,"seckillprice":None,"sale_object_id":"6a32e5e966014f039e11c435ea2bf3c6","release_state":0,"artist_name":None},{"id":"30882d3d6ffa49678a9286688e651264","old_id":0,"prefix1":None,"suffix1":None,"suffix2":None,"artist_id":None,"product_name":"阳士琦《皇家气派款 黄地珐琅彩万寿延年赏瓶 官窑粉彩传承人》","product_count":0,"standard_width":None,"standard_height":None,"standard_length":None,"quality":None,"phase":None,"start_price":0.0,"increase_price":0.0,"max_price":0.0,"maxprice":4700.0,"create_year":None,"order_num":2625,"start_date":"2019/8/16 9:00:00","end_date":"2019/8/17 21:40:00","product_type":None,"remark":None,"product_state":0,"product_state_name":"已结束","sale_type":2,"SaleTypeName":None,"flat_scale":None,"look_count":41,"price_count":11,"photo":"https://cdns.testsite.cn/uploadimages/20190814/2590c81ab66144898e0a4f72f817341e.min.jpg?imageView2/1/w/370/h/370","price":None,"seckillprice":None,"sale_object_id":"6a32e5e966014f039e11c435ea2bf3c6","release_state":0,"artist_name":None},{"id":"30b2fc125b1a4472b104b2b0ec4cdd3f","old_id":0,"prefix1":None,"suffix1":None,"suffix2":None,"artist_id":None,"product_name":"阳士琦《黄地开光粉彩山水人物纹四方茶壶》","product_count":0,"standard_width":None,"standard_height":None,"standard_length":None,"quality":None,"phase":None,"start_price":0.0,"increase_price":0.0,"max_price":0.0,"maxprice":8100.0,"create_year":None,"order_num":2625,"start_date":"2019/8/16 9:00:00","end_date":"2019/8/17 21:40:00","product_type":None,"remark":None,"product_state":0,"product_state_name":"已结束","sale_type":2,"SaleTypeName":None,"flat_scale":None,"look_count":32,"price_count":21,"photo":"https://cdns.testsite.cn/uploadimages/20190814/1a4390d20754488892756873482012c6.min.jpg?imageView2/1/w/370/h/370","price":None,"seckillprice":None,"sale_object_id":"6a32e5e966014f039e11c435ea2bf3c6","release_state":0,"artist_name":None},{"id":"816ce80845154081bfc996d4a5c34958","old_id":0,"prefix1":None,"suffix1":None,"suffix2":None,"artist_id":None,"product_name":"阳士琦《珐琅彩芍药雉鸡玉壶春瓶》","product_count":0,"standard_width":None,"standard_height":None,"standard_length":None,"quality":None,"phase":None,"start_price":0.0,"increase_price":0.0,"max_price":0.0,"maxprice":6500.0,"create_year":None,"order_num":2625,"start_date":"2019/8/16 9:00:00","end_date":"2019/8/17 21:40:00","product_type":None,"remark":None,"product_state":0,"product_state_name":"已结束","sale_type":2,"SaleTypeName":None,"flat_scale":None,"look_count":26,"price_count":10,"photo":"https://cdns.testsite.cn/uploadimages/20190814/80df9bf2587e43d7b7939386e6f90ee3.min.jpg?imageView2/1/w/370/h/370","price":None,"seckillprice":None,"sale_object_id":"6a32e5e966014f039e11c435ea2bf3c6","release_state":0,"artist_name":None},{"id":"82f6f10347b44002879c09569b35f8d7","old_id":0,"prefix1":None,"suffix1":None,"suffix2":None,"artist_id":None,"product_name":"俞小平《青花冰梅将军盖罐 艺术瓷厂老画师》","product_count":0,"standard_width":None,"standard_height":None,"standard_length":None,"quality":None,"phase":None,"start_price":0.0,"increase_price":0.0,"max_price":0.0,"maxprice":1668.0,"create_year":None,"order_num":2625,"start_date":"2019/8/16 9:00:00","end_date":"2019/8/17 21:40:00","product_type":None,"remark":None,"product_state":0,"product_state_name":"已结束","sale_type":2,"SaleTypeName":None,"flat_scale":None,"look_count":46,"price_count":8,"photo":"https://cdns.testsite.cn/uploadimages/20190814/3b4c9b0af2444a5aa1d83032c4e2b39d.min.jpg?imageView2/1/w/370/h/370","price":None,"seckillprice":None,"sale_object_id":"6a32e5e966014f039e11c435ea2bf3c6","release_state":0,"artist_name":None},{"id":"8f4819b41437460e80e2e20e853c05a7","old_id":0,"prefix1":None,"suffix1":None,"suffix2":None,"artist_id":None,"product_name":"俞小平《《天蓝釉双鹤对杯》 艺术瓷厂老画师》","product_count":0,"standard_width":None,"standard_height":None,"standard_length":None,"quality":None,"phase":None,"start_price":0.0,"increase_price":0.0,"max_price":0.0,"maxprice":601.0,"create_year":None,"order_num":2625,"start_date":"2019/8/16 9:00:00","end_date":"2019/8/17 21:35:00","product_type":None,"remark":None,"product_state":0,"product_state_name":"已结束","sale_type":2,"SaleTypeName":None,"flat_scale":None,"look_count":49,"price_count":5,"photo":"https://cdns.testsite.cn/uploadimages/20190814/b136ee02a8d94912a0bb5d65b6b12b54.min.jpg?imageView2/1/w/370/h/370","price":None,"seckillprice":None,"sale_object_id":"6a32e5e966014f039e11c435ea2bf3c6","release_state":0,"artist_name":None},{"id":"91e0f07720414586865d3f9cc1dad786","old_id":0,"prefix1":None,"suffix1":None,"suffix2":None,"artist_id":None,"product_name":"俞小平《青花硕果梅瓶 艺术瓷厂老画师》","product_count":0,"standard_width":None,"standard_height":None,"standard_length":None,"quality":None,"phase":None,"start_price":0.0,"increase_price":0.0,"max_price":0.0,"maxprice":900.0,"create_year":None,"order_num":2625,"start_date":"2019/8/16 9:00:00","end_date":"2019/8/17 21:40:00","product_type":None,"remark":None,"product_state":0,"product_state_name":"已结束","sale_type":2,"SaleTypeName":None,"flat_scale":None,"look_count":18,"price_count":7,"photo":"https://cdns.testsite.cn/uploadimages/20190814/e1131b16513e4cc5bdd43caef46219cd.min.jpg?imageView2/1/w/370/h/370","price":None,"seckillprice":None,"sale_object_id":"6a32e5e966014f039e11c435ea2bf3c6","release_state":0,"artist_name":None},{"id":"95f09d15867444ad959cbf1458b816e2","old_id":0,"prefix1":None,"suffix1":None,"suffix2":None,"artist_id":None,"product_name":"阳士琦《五彩鱼澡纹杯 官窑粉彩传承人》","product_count":0,"standard_width":None,"standard_height":None,"standard_length":None,"quality":None,"phase":None,"start_price":0.0,"increase_price":0.0,"max_price":0.0,"maxprice":688.0,"create_year":None,"order_num":2625,"start_date":"2019/8/16 9:00:00","end_date":"2019/8/17 21:40:00","product_type":None,"remark":None,"product_state":0,"product_state_name":"已结束","sale_type":2,"SaleTypeName":None,"flat_scale":None,"look_count":31,"price_count":7,"photo":"https://cdns.testsite.cn/uploadimages/20190814/eeda35bea9754ca5a51ae1d50c88f2e1.min.jpg?imageView2/1/w/370/h/370","price":None,"seckillprice":None,"sale_object_id":"6a32e5e966014f039e11c435ea2bf3c6","release_state":0,"artist_name":None},{"id":"97bbb427a11b424c9c0f1276a93b29a4","old_id":0,"prefix1":None,"suffix1":None,"suffix2":None,"artist_id":None,"product_name":"俞小平《粉彩观音佛像瓷板 艺术瓷厂老画师》","product_count":0,"standard_width":None,"standard_height":None,"standard_length":None,"quality":None,"phase":None,"start_price":0.0,"increase_price":0.0,"max_price":0.0,"maxprice":7000.0,"create_year":None,"order_num":2625,"start_date":"2019/8/16 9:00:00","end_date":"2019/8/17 21:35:00","product_type":None,"remark":None,"product_state":0,"product_state_name":"已结束","sale_type":2,"SaleTypeName":None,"flat_scale":None,"look_count":23,"price_count":12,"photo":"https://cdns.testsite.cn/uploadimages/20190814/3c65415f9c574281be62cc4a07fddbe0.min.jpg?imageView2/1/w/370/h/370","price":None,"seckillprice":None,"sale_object_id":"6a32e5e966014f039e11c435ea2bf3c6","release_state":0,"artist_name":None},{"id":"ae5cc3778c1f463f90a93604383a11ef","old_id":0,"prefix1":None,"suffix1":None,"suffix2":None,"artist_id":None,"product_name":"俞小平《粉彩扎道六鹤同春梅瓶 艺术瓷厂老画师》","product_count":0,"standard_width":None,"standard_height":None,"standard_length":None,"quality":None,"phase":None,"start_price":0.0,"increase_price":0.0,"max_price":0.0,"maxprice":1968.0,"create_year":None,"order_num":2625,"start_date":"2019/8/16 9:00:00","end_date":"2019/8/17 21:35:00","product_type":None,"remark":None,"product_state":0,"product_state_name":"已结束","sale_type":2,"SaleTypeName":None,"flat_scale":None,"look_count":36,"price_count":10,"photo":"https://cdns.testsite.cn/uploadimages/20190814/cb7ec9dd9e7a4281937e1854746c8724.min.jpg?imageView2/1/w/370/h/370","price":None,"seckillprice":None,"sale_object_id":"6a32e5e966014f039e11c435ea2bf3c6","release_state":0,"artist_name":None},{"id":"c7d84c0b1e4d4f238616bd884d0f1017","old_id":0,"prefix1":None,"suffix1":None,"suffix2":None,"artist_id":None,"product_name":"阳士琦《官窑粉彩传承人 《洋彩山水观音瓶》》","product_count":0,"standard_width":None,"standard_height":None,"standard_length":None,"quality":None,"phase":None,"start_price":0.0,"increase_price":0.0,"max_price":0.0,"maxprice":4000.0,"create_year":None,"order_num":2625,"start_date":"2019/8/16 9:00:00","end_date":"2019/8/17 21:35:00","product_type":None,"remark":None,"product_state":0,"product_state_name":"已结束","sale_type":2,"SaleTypeName":None,"flat_scale":None,"look_count":29,"price_count":9,"photo":"https://cdns.testsite.cn/uploadimages/20190814/9ee97524d98c4838bfd37dda0e1d5722.min.jpg?imageView2/1/w/370/h/370","price":None,"seckillprice":None,"sale_object_id":"6a32e5e966014f039e11c435ea2bf3c6","release_state":0,"artist_name":None},{"id":"cafb472c66704cba8299a313991debc4","old_id":0,"prefix1":None,"suffix1":None,"suffix2":None,"artist_id":None,"product_name":"阳士琦《官窑粉彩传承人 《粉彩描金春荷茶壶》》","product_count":0,"standard_width":None,"standard_height":None,"standard_length":None,"quality":None,"phase":None,"start_price":0.0,"increase_price":0.0,"max_price":0.0,"maxprice":1200.0,"create_year":None,"order_num":2625,"start_date":"2019/8/16 9:00:00","end_date":"2019/8/17 21:35:00","product_type":None,"remark":None,"product_state":0,"product_state_name":"已结束","sale_type":2,"SaleTypeName":None,"flat_scale":None,"look_count":37,"price_count":6,"photo":"https://cdns.testsite.cn/uploadimages/20190814/40b7d8b38ffa4eefb3a011a2e451f0ea.min.jpg?imageView2/1/w/370/h/370","price":None,"seckillprice":None,"sale_object_id":"6a32e5e966014f039e11c435ea2bf3c6","release_state":0,"artist_name":None},{"id":"d898090a96164b85b893fdc4c0f7f645","old_id":0,"prefix1":None,"suffix1":None,"suffix2":None,"artist_id":None,"product_name":"阳士琦《纯金刻画珊瑚红龙纹梅瓶  故宫博物院乾隆花园延趣楼陶瓷修复人》","product_count":0,"standard_width":None,"standard_height":None,"standard_length":None,"quality":None,"phase":None,"start_price":0.0,"increase_price":0.0,"max_price":0.0,"maxprice":36000.0,"create_year":None,"order_num":2625,"start_date":"2019/8/16 9:00:00","end_date":"2019/8/17 21:40:00","product_type":None,"remark":None,"product_state":0,"product_state_name":"已结束","sale_type":2,"SaleTypeName":None,"flat_scale":None,"look_count":78,"price_count":29,"photo":"https://cdns.testsite.cn/uploadimages/20190814/dea8c1eb052c46e7b18506517725f9b2.min.jpg?imageView2/1/w/370/h/370","price":None,"seckillprice":None,"sale_object_id":"6a32e5e966014f039e11c435ea2bf3c6","release_state":0,"artist_name":None}]},"page":2,"IsEnd":True,"NowTime":"2019/8/19 17:42:08"},"success":True,"errorMessage":None,"StatusCode":200,"CurrentTime":"2019-08-19 17:42:08"}
    # topic_ids = []
    # topic_ids.append(js['data']['data']['special'])
    # net_save_by_topic_xing(topic_ids)
    
    fenlei = u"testpath/" + tomorrow + "/"
    js={"result":True,"data":{"SRNAME":u"文房雅珍专场","SRENDTIME":1625029278000,"SRTYPE":"0001","AUCTNAME":u"瓷杂精品专场","AUCTIONID":2147483657,"SRSTARTTIME":1560488478000,"SALESID":100055362,"CONTENT":"瓷杂部","SALESNAME":"汪颖","SALEROOMID":2147486338}}

    topic_ids = []
    topic_ids.append(js['data'])
    net_save_by_topic_rade(topic_ids)
    
    # with open(r"./logs/" + today + ".log", 'r') as f:

