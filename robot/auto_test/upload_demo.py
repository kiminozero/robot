#!/usr/bin/python
# -*- coding:utf-8 -*-
import json
import xlrd
import re
from collections import OrderedDict
import requests,random
import time
import os
import random
import string
import glob

# a demo a php server side upload through post
headers = {
    "Host": "api.test.testsite.com",
    "Connection": "keep-alive",
    "Accept": "*/*",
    "Origin": "http://m.test.testsite.com",
    "User-Agent": "Mozilla/5.0 (iPhone; U; CPU iPhone OS 5_1_1 like Mac OS X; en-us) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9B206 Safari/7534.48.3 XiaoMi/MiuiBrowser/10.9.2",
    # "Content-Type": "multipart/form-data",
    "Referer": "http://m.test.testsite.com",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,en-US;q=0.9",
}


s=requests.session()
s.headers=headers
proxy = {"http": "http://127.0.0.1:8888"}
s.proxies=proxy

url="http://api.test.testsite.com/index.php/adminTreasure/uploadFile"
auction_img_path=u"\images\\20190906104925clp2bs3sq9n_w_508_h_640.jpg"
multiple_files = OrderedDict([
    ('file', ("20190711103807.jpg",open(auction_img_path,"rb"),'image/jpeg')),
    ('filename', (None, 'shop/auction/20190906/20190906180708eaj2evt2oya_w_4032_h_3024.jpg')),
    ('filetype', (None, 'image')),
    ('relation', (None, 'auction')),
])

print multiple_files


r = s.post(url,files=multiple_files)
print r.content
