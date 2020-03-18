# -*- coding: utf-8 -*-
import threading
import urllib2
import urllib
import random
import math
import urlparse
import time
import cookielib

########################################################################


class Baidu:
    """"""
    Referer='http://*.*.com'
    TargetPage='*.*.com'
    BaiduID=''
    Hjs="http://hm.baidu.com/h.js?"
    Hgif="http://hm.baidu.com/hm.gif?"
    UserAgent='Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)' #IE9
    MyData={'cc':'1','ck':'1','cl':'32-bit','ds':'1024x768','et':'0','ep':'0','ja':'1','ln':'zh-cn','lo':'0','nv':'1','st':'3','v':'1.2.51','lv':'3'}
    #----------------------------------------------------------------------
    def __init__(self,baiduID,targetPage=None,refererPage=None):
        """Constructor"""
        self.TargetPage=targetPage or  self.TargetPage
        self.Referer=refererPage or self.Referer
        self.BaiduID=baiduID
        self.MyData['si']=self.BaiduID
        self.MyData['su']=urllib.quote(self.Referer)
        pass
    def run(self,timeout=5):
        cj=cookielib.CookieJar()
        opener=urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
        opener.addheaders=[("Referer",self.TargetPage),("User-Agent",self.UserAgent)]
        t=random.randint(1, 100)
        time.sleep(t)
        print "start" ,t

        try:
            response=opener.open(self.Hjs+self.BaiduID).info()
            self.MyData['rnd']=int(random.random()*2147483647 )
            self.MyData['lt']=int(time.time())
            self.MyData['sn'] = int(random.randint(9500, 11000))
            fullurl=self.Hgif+urllib.urlencode(self.MyData)
            response2=opener.open(fullurl,timeout=timeout).info()
            self.MyData['rnd']=int(random.random()*2147483647 )
            self.MyData['et']='3'
            self.MyData['ep']='2000,100'
            # self.MyData['sn'] = int(random.randint(9500,11000))
            response3=opener.open(self.Hgif+urllib.urlencode(self.MyData),timeout=timeout).info()
            pass
            print "ok"
        except urllib2.HTTPError ,ex:
            print ex.code
            pass
        except urllib2.URLError,ex:
            print ex.reason
            pass
        pass



if  __name__ =="__main__":
    # a=Baidu('bb03731dc2284bf3282795b6719579b9','http://bead.*.com/index.php?act=index','www.*.com')
    # a.run()

    urls=[
        "http://bead.*.com/index.php?act=index",
        "http://bead.*.com/index.php?act=fen",
        "http://bead.*.com/index.php?act=category",
        "http://bead.*.com/index.php?act=lyingearn",
        "http://bead.*.com/index.php?act=lyingearn",
        "http://bead.*.com/index.php?act=index_home&op=goodsdetail&auction_id=3003",
        "http://bead.*.com/index.php?act=index_home&op=goodsdetail&auction_id=3002",
        "http://bead.*.com/index.php?act=index_home&op=goodsdetail&auction_id=3001",
        "http://bead.*.com/index.php?act=index_home&op=goodsdetail&auction_id=3000",
        "http://bead.*.com/index.php?act=index_home&op=goodsdetail&auction_id=2999",
        "http://bead.*.com/index.php?act=index_home&op=goodsdetail&auction_id=2888",
    ]
    def js_baidu(user=1000):
        tt=[]
        for i in xrange(user):
            u=random.choice(urls)
            a = Baidu('bb03731dc2284bf3282795b6719579b9', u, '*.com')
            t = threading.Thread(target=a.run, args=(5,))  # 创建线程
            # t.setDaemon(True)  # 设置为后台线程，这里默认是False，设置为True之后则主线程不用等待子线程
            tt.append(t)
        for t in tt:
            t.start()
        for t in tt:
            t.join()

    for i in xrange(10):
        js_baidu()
        time.sleep(60)
