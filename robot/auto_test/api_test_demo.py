#coding=utf-8
import unittest
import json
import requests
import random
import re
import time
from sqlalchemy import *
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from commen.my_logger import Logger
from data.auction import *
import threading
import time
from data.auctions_new import auctions
from data.users_205 import *
my_logger=Logger('./logs/producter.log',level='debug')

# host="http://m.atestsite.com"
# api="http://api.atestsite.com"

host="http://m.test.atestsite.com"
api="http://api.test.atestsite.com"
# host="http://m.atestsite.com/bearshop"

base_url=host


headers={"Host": "m.atestsite.com",
"Connection": "keep-alive",
"Accept": "application/json",
"Origin": "http://m.atestsite.com",
"X-Requested-With": "XMLHttpRequest",
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36",
"Content-Type": "application/x-www-form-urlencoded",
"Referer": "http://m.atestsite.com/index.php?act=login&op=pwIndex",
"Accept-Encoding": "gzip, deflate",
"Accept-Language": "zh-CN,zh;q=0.9",
         }

headers_m_205= {"Host": "m.atestsite.com",
"Connection": "keep-alive",
"Content-Length": "6",
"Accept": "application/json, text/javascript, */*; q=0.01",
"Origin": "http://m.atestsite.com",
"X-Requested-With": "XMLHttpRequest",
"User-Agent": "Mozilla/5.0 (Linux; Android 8.0.0; STF-AL10 Build/HUAWEISTF-AL10; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/66.0.3359.126 MQQBrowser/6.2 TBS/044705 Mobile Safari/537.36 MMWEBID/8572 MicroMessenger/6.7.3.1360(0x2607033D) NetType/WIFI Language/zh_CN Process/tools",
"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
"Referer": "http://m.atestsite.com/bearshop/index.php?act=index_home&op=goodsdetail&auction_id=746",
"Accept-Encoding": "gzip, deflate",
"Accept-Language": "zh-CN,ja-JP;q=0.9,en-US;q=0.8",
"Cookie": "user_id=98; token=aac85b55f5d6e7c7bc72777cbbbc8a7a; bearshopkey=e4e86844c2d8d84c16ce440de258e02d; user_subscribe=0; PHPSESSID=03k7hkc6funata18kf1hqjfj13",
}

# s=requests.Session()
# s.headers=headers_m_205
# url=(host+"/index.php?act=login&op=pwIndex","mobile=15100003788&loginPassword=151788")

proxies={'http':'127.0.0.1:8888'}


class Epjh(object):
    max_id_home=0
    max_id_lying=0
    max_id_topic=0
    user_id=0
    random_user=True
    login_status=False

    def __init__(self,random_user=False):
        headers = {"Host": "m.atestsite.com",
                   "Connection": "keep-alive",
                   "Accept": "application/json",
                   "Origin": "http://m.atestsite.com",
                   "X-Requested-With": "XMLHttpRequest",
                   "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36",
                   "Content-Type": "application/x-www-form-urlencoded",
                   "Referer": "http://m.atestsite.com/index.php?act=login&op=pwIndex",
                   "Accept-Encoding": "gzip, deflate",
                   "Accept-Language": "zh-CN,zh;q=0.9",
                   }
        self.host=host
        self.client=requests.Session()
        self.client.headers=headers
        self.client.proxies=proxies

        self.random_user=random_user
        self.login_status=self.login()
        self.a_id=''

    def get_user(self):
        if self.random_user:
            user_id,user,passwd = random.choice(users_info)
        else:
            user_id,user,passwd = users_info.pop()
        return user_id,user,passwd

    def login(self):
        self.user_id,mobile, loginPassword = self.get_user()
        # mobile, loginPassword = '15100003788',''

        with self.client.post(host + "/index.php?act=login&op=pwIndex", "mobile=" + str(mobile) + "&loginPassword=" + str(loginPassword)) as res:
            # print self.client.headers,self.client.cookies,mobile,loginPassword
            # self.s.headers.update({'host': 'm.atestsite.com'})
            if res.status_code==200:
                cookie_dic =requests.utils.dict_from_cookiejar(self.client.cookies)
                # print cookie_dic
                self.client.headers.update({"Authorization": "Bearer " + cookie_dic['token']})

                # self.client.headers=self.headers
                # print("login")
                # my_logger.logger.info(cookie_dic['user_id']+","+mobile+","+loginPassword)  #get user_id
                return True
            else:
                # print("login fail")
                my_logger.logger.error(res.content)
                return False

    def logout(self):
        self.client.close()

    def publish_auction(self, auction):
            url = base_url + "/index.php?act=upload&op=addauction"
            url1 = base_url + "/index.php?act=publish&op=index"
            url2 = base_url + "/index.php?act=publish&op=publishAuction"
            pdata = "pdata=" + auction['auction_img_all'] + "&auction_add_date=" + str(auction['auction_add_date'])
            auction_id = ''
            '''传图'''
            res = self.client.post(url, pdata)
            print url, pdata
            print res, res.content
            if res.json()["state"] == 1:
                auction_id = res.json()["auction_id"]
            else:
                return None

            '''描述'''
            auction["auction_title"]=auction['auction_description'].encode('utf8')
            if len(auction["auction_title"])>20:
                auction["auction_title"]=auction["auction_title"][:20]


            data1 = "auction_id=" + str(auction_id) + "&auction_description=" + auction[
                'auction_description'].encode('utf8') + \
                    "&vedio_link=&vedioid=&asset_id=&auction_title=" + auction["auction_title"]
            res = self.client.post(url1, data1)
            print res.content


            '''传拍品'''
            data2 = "auction_id=" + str(auction_id) + "&starttime=" + str(auction['start_time']) + "&end_time=" + str(
                time.time()+300) + "&cate_id=" + \
                    str(auction['cate_id']) + "&cate_id_1=" + str(auction['cate_id_1']) + "&firstprice=" + str(
                auction['firstprice']) + "&cashprice=0&addprice=" + str(auction['addprice']) + "&freeship=" + str(
                auction['freeship']) + "&cankaojia=NaN&yikoujia=" + str(auction['yikoujia']) + "&auctionreturn=" + str(
                auction['is_return']) + "&reserveprice=NaN&commissions=" + "3%" + "&outbonus=0&is_commiss=" + str(2) + "&is_outbonus=1"

            res = self.client.post(url2, data2)
            print res.content
            if res.json()['state']=='1':
                return auction_id
            else:
                return None


    def bidprice(self,auction_id,price,yikoujia=1):

        if yikoujia==1:
            res=self.client.post(host + "/index.php?act=index_home&op=bidprice",
                         "from_id=0&auction_id=" + str(auction_id) + "&bidprice=" + str(
                             price) + "&is_ykj=1")
            return res
        elif yikoujia==0:
            res=self.client.post(host + "/index.php?act=index_home&op=bidprice",
                             "from_id=0&auction_id=" + str(auction_id) + "&bidprice=" + str(
                                 price) + "&is_ykj=0")
            return res

    def api_bidprice(self,auction_id,price,yikoujia=1,no_add_price=0):

        data={"auction_id":auction_id,"bid_price":price,"is_ykj":yikoujia,"no_add_price":no_add_price}
        if yikoujia==1:
            res=self.client.post(api + "/index.php/goods/bidPrice",
                         json=data)
            return res
        elif yikoujia==0:
            res=self.client.post(api + "/index.php/goods/bidPrice",
                             json=data)
            return res

    def balanceInfo(self):

        res = self.client.post(api + "/index.php/userPay/balanceInfo")
        # print res.content
        return res

    def pay_cash(self,auction_id):
        pass

    def api_baseinfo(self, auction_id):
        url=api+'/index.php/goods/baseInfo'
        data={"auction_id":auction_id,"from_id":0,"type":0}
        res=self.client.post(url,json=data)
        return res

    def get_auction_info(self,auction_id):
        url=host+"/index.php?act=index_home&op=goodsdetail&auction_id="+str(auction_id)
        res=self.client.get(url)
        return res

    def api_bidinfo(self, auction_id):
        url = api + '/index.php/goods/bidinfo'
        data = {"auction_id": auction_id}
        res = self.client.post(url, json=data)
        return res



    def api_shopinfo(self, seller_id, auction_id):
        url = api + '/index.php/goods/shopinfos'
        data = {"seller_id	": seller_id,"auction_id": auction_id}
        res = self.client.post(url, json=data)
        return res

    def api_seller_all_goods(self, seller_id, auction_id):
        url = api + '/index.php/goods/sellerAllGoods'
        data = {"seller_id	": seller_id,"auction_id": auction_id}
        data = "seller_id="+ str(seller_id)+"&auction_id="+str(auction_id)
        res = self.client.post(url, data=data)
        return res

    def get_auction_url(self,auction_id):
        res=self.get_auction_info(auction_id)
        auc_prices = self.find_price(res.content)
        url = host + "/index.php?act=index&op=sendauctionaddr&auction_id="+auction_id+"&seller_id="+auc_prices["seller_id"]+"&from_id=0&auction_sn=EP1906221047223319&type=2"
        res = self.client.get(url)
        return res

    def get_id(self):
        headers=self.client.headers
        cookie_dic = requests.utils.dict_from_cookiejar(self.client.cookies)
        return cookie_dic['user_id']

    def fahuo(self,order_id):
        url=host+"/index.php?act=payment&op=sendout"
        data="order_id="+str(order_id)+"&code=%E3%80%82%E3%80%82%E3%80%82%E3%80%82%E3%80%82&com=+%E9%A1%BA%E4%B8%B0+&is_express=1"
        res=self.client.post(url,data=data)
        return res

    def balancepayment(self,order_id):
        url=host+"/index.php?act=payment&op=balancepayment"
        data="order_id="+str(order_id)+"&paypasswd=111111&coupon_log_id=0"
        res=self.client.post(url,data=data)
        return res

    def api_home_index(self, page=1, first_type=1, second_type=1):
        self.client.headers.update({"Host": "api.atestsite.com"})
        res=self.client.post("http://api.atestsite.com/index.php/list/home",
                             json={"page":page,"first_type":first_type,"second_type":second_type,"max_id":self.max_id_home})
        self.client.headers.update({"Host": "m.atestsite.com"})
        if res.json()['msg'] == "success" and len(res.json()['data']['data'])!=0:
            auctions = res.json()['data']['data']
            self.max_id_home = res.json()['data']['max_id']
            # print auctions,len(auctions)
            return auctions
        else:
            return None

    def api_lyingearnHome(self, page=1):
        url=api+"/index.php/list/lyingearnHome"
        data={"page": page, "first_type": 1, "second_type": 1, "max_id": self.max_id_lying}
        self.client.headers.update({"Host": "api.atestsite.com"})
        res = self.client.post(url,json=data)
        self.client.headers.update({"Host": "m.atestsite.com"})
        if res.json()['msg'] == "success" and len(res.json()['data']['data'])!=0:
            auctions = res.json()['data']['data']
            self.max_id_lying = res.json()['data']['max_id']
            # print auctions,len(auctions)
            return auctions
        else:
            return None

    def api_topic_auctionlist(self, tipic_id=62, page=1):
        url=api+"/index.php/topic/auctionlist"
        data={"topic_id": str(tipic_id), "page": page}
        self.client.headers.update({"Host": "api.atestsite.com"})
        res = self.client.post(url,json=data)
        self.client.headers.update({"Host": "m.atestsite.com"})
        if res.json()['code'] == 0 and len(res.json()['data']['auction'])!=0:
            auctions = res.json()['data']['auction']
            # self.max_id_topic = res.json()['data']['max_id']
            # print auctions,len(auctions)
            return auctions
        else:
            return None

    def get_guanzhu(self,page):

        url=host+"/index.php?act=user&op=participateAuction&page="+str(page)+"&type=3&auction_id_str=2281%2C2281%2C2324%2C2308%2C950%2C2346%2C2263%2C193"
        res = self.client.post(url)
        if res.json()['msg'] == "success" and len(res.json()['data']['data'])!=0:
            auctions = res.json()['data']['data']
            # print auctions,len(auctions)
            return auctions
        else:
            return None

    def get_auction_by_sellerid(self,seller_id=120000,page=1,**kwargs):

        url = host + "/index.php?act=shop&op=alldata_list&nextpage="+str(page)+"&seller_id="+str(seller_id)
        res = self.client.get(url)
        if res.json()['msg'] == "success" and len(res.json()['data']['data']) != 0:
            auctions = res.json()['data']['data']
            # print auctions,len(auctions)
            return auctions
        else:
            return None

    def get_auctions_now(self):
        status=True
        i=1
        l=[]
        file_path='./data/test2.txt'
        with open(file_path, 'w') as f:
            while (status):
                print i
                auctions=self.api_home_index(i)
                if auctions != None:
                    for a in auctions:
                        f.write(json.dumps(a)+"\r\n")
                    l.extend(auctions)
                else:
                    status=False
                i=i+1
                time.sleep(1)
            # print l
            return l

    def get_guanzhu_now(self):
        status=True
        i=1
        l=[]
        file_path='./data/guanzhu2.txt'
        with open(file_path, 'w') as f:
            while (status):
                print i
                sellers=self.get_guanzhu(i)
                if sellers != None:
                    for a in sellers:
                        f.write(json.dumps(a)+"\r\n")
                    l.extend(sellers)
                else:
                    status=False
                i=i+1
                time.sleep(1)
            # print l
            return l



    def find_price(self,response):
        addprice=re.search("addprice = (.*);",response)
        yikoujia=re.search("var yikoujia = (.*);",response)
        firstPrice=re.search("firstPrice = \"(.*)\";",response)
        auction_price=re.search("var auction_price = (.*);",response)
        auction_sn=re.search('var auction_sn ="(.*)";',response)
        seller_id=re.search('var seller_id = "(.*)"',response)
        try:
            d={"addprice":int(addprice.group(1)),"yikoujia":int(yikoujia.group(1)),
               "firstPrice":int(firstPrice.group(1)),"auction_price":int(auction_price.group(1)),
              "auction_sn":auction_sn.group(1),"seller_id":seller_id.group(1)}
            # return int(addprice.group(1)),int(yikoujia.group(1)),int(firstPrice.group(1)),int(auction_price.group(1)),int(endtime.group(1)),auction_sn.group(1),seller_id.group(1)
        except Exception as e:
            # my_logger.logger.error(e)
            my_logger.logger.error("\r\n"+e)
            return None
        return d

    def find_order_id(self,response):

        order_id=re.search('<button order_id="(.*)" class="paymentnow">立即付款</button>',response)

        return order_id.group(1)


    def api_search(self,keyword,page,pageSize,type_of=1):
        url = api + '/index.php/goods/searchAuction'

        data = {"keyword": keyword,"page":page,"pageSize":pageSize,"type_of":type_of}

        res = self.client.post(url, json=data)
        return res

    def api_focusOn(self,seller_id):
        url = api + '/index.php/userInfo/focusOn'
        data = {"seller_id": seller_id}
        res = self.client.post(url, json=data)
        return res
    def api_unfocusOn(self,seller_id):
        url = api + '/index.php/userInfo/unFocusOn'
        data = {"seller_id": seller_id}
        res = self.client.post(url, json=data)
        return res

    def api_categoryData(self):
        url = api + '/index.php/list/categoryData'
        res = self.client.post(url)
        return res

class User(Epjh):

    def get_order_list_dsh(self):
        url = host + "/index.php?act=my&op=userorderdata&nextpage=1&state=2"
        res = self.client.get(url)
        return res


    def get_order_list_dfk(self):
        url = host + "/index.php?act=my&op=userorderdata&nextpage=1&state=0"
        res = self.client.get(url)
        return res

    def find_order_id(self,response):

        order_id=re.search('<button order_id="(.*)" class="paymentnow">立即付款</button>',response)

        return order_id.group(1)

    pass

class Seller(Epjh):

    def get_order_list(self):
        url = host + "/index.php?act=my&op=sellerorderdata&nextpage=1&state=1"
        res = self.client.get(url)
        return res

    def find_order_id(self,response):

        order_id=re.search('<button class="mysendout" order_id="(.*)">立即发货</button>',response)

        return order_id.group(1)
    pass

'''
@unittest.skip("")
class MyTest(unittest.TestCase):  # 继承unittest.TestCase
    def tearDown(self):
                # 每个测试用例执行之后做操作
        print('222222222222222')

    def setUp(self):
        # 每个测试用例执行之前做操作
        print('111111111111111')

    @classmethod
    def tearDownClass(self):
        # 必须使用 @ classmethod装饰器, 所有test运行完后运行一次
        print('444444444444444')

    @classmethod
    def setUpClass(self):
        self.a_id=''
        self.seller=Epjh()
        self.user=Epjh()

    @unittest.skip("")
    def test_publish(self):
        a = auctions[0]
        self.a_id = self.seller.publish_auction(a)
        res = self.user.get_auction_info(self.a_id)
        auc_prices = self.user.find_price(res.content)
        self.assertEqual(auc_prices['firstPrice'], a['firstprice'],"publish pass")

    @unittest.skip("")
    def test_getid(self):
        home = Epjh()
        self.assertEqual(int(home.get_id()),home.user_id,"test_getid fail")

    @unittest.skip("")
    def test_get_auction_url(self):
        home = Epjh()
        res=home.get_auction_url("12219")
        self.assertEqual(int(res.json()["state"]), 1, "test_get_auction_url fail")

    @unittest.skip("")
    def test_topic_auctionlist(self):
        home = Epjh()
        l=[]
        for i in xrange(10):
            res = home.api_topic_auctionlist(68, i)
            if res !=None:
                l.extend(res)
        for i in l:
            print i


    @unittest.skip("")
    def test_baseinfo(self):
        home=Epjh()
        res=home.api_baseinfo(12219)
        print res.json()

    @unittest.skip("")
    def test_bidinfo(self):
        home = Epjh()
        res = home.api_bidinfo(12219)
        print res.json()

    @unittest.skip("")
    def test_shopinfo(self):
        home = Epjh()
        res=home.api_shopinfo(113123, 12219)
        print res.json()

    @unittest.skip("")
    def test_seller_all_goods(self):
        home = Epjh()
        res = home.api_seller_all_goods(113123, 11919)
        print res.json()

    @unittest.skip("")
    def test_auctions(self):
        home = Epjh()
        t_ids = [
            
        ]
        for i in t_ids:
            res=home.api_baseinfo(i['id'])
            i['auction_sn']=res.json()['data']['data']['auction_sn']
            i['rp']= res.json()['data']['data']['yikoujia']
            print i,','
            # print res.json()


@unittest.skip("")
class OrderTest(unittest.TestCase):
    def tearDown(self):

        print('222222222222222')

    def setUp(self):

        print('111111111111111')

    @classmethod
    def tearDownClass(self):

        print('444444444444444')

    @classmethod
    def setUpClass(self):
        self.a_id = ''
        self.seller = Seller()
        self.user = User()


    # @unittest.skip("")
    def test_a_publish(self):
        a = auctions[0]
        self.a_id = self.seller.publish_auction(a)
        self.seller.a_id = self.a_id
        res = self.user.get_auction_info(self.a_id)
        auc_prices = self.user.find_price(res.content)
        self.assertEqual(auc_prices['firstPrice'], a['firstprice'],"publish pass")

    # @unittest.skip("")
    def test_b_chuiia(self):
        auction = self.user.api_baseinfo(self.seller.a_id)
        auction=auction.json()
        print auction
        firstprice=auction['data']['data']['firstprice']
        addprice=auction['data']['data']['addprice']
        seller_id=auction['data']['data']['seller_id']
        leadingprice=auction['data']['data']['leadingprice']
        yikoujia=auction['data']['data']['yikoujia']
        res = self.user.bidprice(self.seller.a_id,yikoujia)
        print res.json()

    # @unittest.skip("")
    def test_c_fukuan(self):
        time.sleep(61)
        res=self.user.get_order_list_dfk()
        print res.content
        order_id=self.user.find_order_id(res.content)
        res=self.user.balancepayment(order_id)
        print res.json()
        self.assertEqual(res.json()['state'],"1","order pay failed")

    def test_d_fahuo(self):
        time.sleep(6)
        res = self.seller.get_order_list()
        print res.content
        order_id = self.seller.find_order_id(res.content)
        res=self.user.fahuo(order_id)
        print res.json()
        self.assertEqual(res.json()['state'],1,"order pay failed")

    def test_e_confirm_shouhuo(self):
        pass

    def test_f_balanceInfo(self):
        res= self.seller.balanceInfo()
        print res.content
        res= self.user.balanceInfo()
        print res.content
'''

# @unittest.skip("")
class APITest(unittest.TestCase):
    def tearDown(self):
        pass

    def setUp(self):
        pass

    @classmethod
    def tearDownClass(self):
        pass

    @classmethod
    def setUpClass(self):
        self.a_id = ''
        self.seller = Seller()
        self.user = User()

    @unittest.skip("")
    def test_api_bidinfo(self):
        home = Epjh()
        res = home.api_bidinfo(12419)
        print res.json()

    @unittest.skip("")
    def test_api_bidprice(self):
        home = Epjh()
        d=[12419,100,0]
        res = home.api_bidprice(d[0],d[1],d[2])
        print res.json()
        print res.json()['data']['data']['msg']
        d = [12419, 160, 0,1]
        res = home.api_bidprice(d[0], d[1], d[2],d[3])
        print res.json()
        print res.json()['data']['data']['msg']
        d = [12419, 1, 0,1]
        res = home.api_bidprice(d[0], d[1], d[2],d[3])
        print res.json()
        print res.json()['data']['data']['msg']

    def test_search(self):
        home = Epjh()
        res =home.api_search(u"日本",1,2000)
        print res.content

    def test_focus(self):
        home = Epjh()
        res = home.api_focusOn(133123)
        print res.content
        time.sleep(1)
        res = home.api_unfocusOn(133123)
        print res.content

    def test_category(self):
        home = Epjh()
        res = home.api_categoryData()
        print res.content

if __name__ == '__main__':
    unittest.main()  # 运行所有的测试用例

