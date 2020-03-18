#coding=utf-8
import threading
import Queue
import time
import random
import flask
from gevent import pywsgi

from attack import *
l=[
["produce one cup!", 1],
["produce one desk!", 2],
["produce one apple!", 3],
["produce one banana!", 4],
["produce one bag!", 5],
]

works=[]

class Producter(threading.Thread):
    def __init__(self, queue):
        threading.Thread.__init__(self)
        self.queue = queue
        self.thread_stop = False
    def run(self):
        while not self.thread_stop:
            print("thread%d %s: producting  tast" % (self.ident, self.name))
            res = q.qsize()
            if res < 3:
                try:
                    q.put(random.choice(l), block=True, timeout=None)
                except Queue.Empty:
                    print("product fail!")
                    # self.thread_stop = True
                    break
            # print("task recv:%s ,task No:%d" % (task[0], task[1]))
                print("i am producting")
                time.sleep(1)
                print("product finished!")
            # q.task_done()  # 完成一个任务
            res = q.qsize()  # 判断消息队列大小


    def stop(self):
        self.thread_stop = True


class Worker(threading.Thread):
    def __init__(self, queue):
        threading.Thread.__init__(self)
        self.queue = queue
        self.thread_stop = False

    def run(self):
        while not self.thread_stop:
            print("thread%d %s: waiting for tast" % (self.ident, self.name))
            try:
                task = q.get(block=True, timeout=20)  # 接收消息
                print("task recv:%s ,task No:%d" % (task[0], task[1]))
                print("i am working")
                time.sleep(3)
                print("work finished!")
            except Queue.Empty:
                print("Nothing to do!")
                print("Nothing to do!")
                print("Nothing to do!")
                # self.thread_stop = True
                # break

            # q.task_done()  # 完成一个任务
            res = q.qsize()  # 判断消息队列大小
            if res > 0:
                print("fuck!There are still %d tasks to do" % (res))
            else:
                time.sleep(5)
    def stop(self):
        self.thread_stop = True

# if __name__ == "__main__":
    # q = Queue.Queue(5)
    # producter=Producter(q)
    # producter.start()
    # worker = worker(q)
    # worker.start()

    # q.put(["produce one cup!", 1], block=True, timeout=None)  # 产生任务消息
    # q.put(["produce one desk!", 2], block=True, timeout=None)
    # q.put(["produce one apple!", 3], block=True, timeout=None)
    # q.put(["produce one banana!", 4], block=True, timeout=None)
    # q.put(["produce one bag!", 5], block=True, timeout=None)
    print("***************leader:wait for finish!")
    # q.join()  # 等待所有任务完成
    print("***************leader:all task finished!")


class MyWorker(threading.Thread):

    def __init__(self, queue):
        threading.Thread.__init__(self)
        self.queue = queue
        self.thread_stop = False
        self.attack=Attack()
        if self.attack.login_status==False:
            my_logger.logger.error(self.attack.login_status)
            time.sleep(1)
            self.attack=Attack()
        elif self.attack.login_status==True:
            print "login"
        else:
            my_logger.logger.error(self.attack.client.headers)

    def change_worker(self):
        self.attack.client.close()
        self.attack=Attack()

    def do(self,task):
        pass
        if task['do']:
            if task['do']== "do":
                print 'do'
                print self.attack.client.headers
                print self.attack.client.cookies

            elif task['do']=="viewnum":
                print "viewnum"
                auction_id=task['data']['auction_id']
                self.attack.add_viewnum(auction_id)

            elif task['do']=="likenum":
                print "likeinfo"
                auction_id=task['data']['auction_id']
                self.attack.add_likenum(auction_id)

            elif task['do']=="share_num":
                print "share_num"
                auction_id=task['data']['auction_id']
                self.attack.add_share_num(auction_id)

            elif task['do']=="guanzhu":
                print "guanzhu"
                seller_id=task['data']['seller_id']
                self.attack.add_guanzhu(seller_id)

            elif task['do']=="dabaojian":
                print "dabaojian"
                auction_id = task['data']['auction_id']
                seller_id = task['data']['seller_id']
                for i in xrange(5):
                    self.attack.add_viewnum(auction_id)
                    time.sleep(0.3)
                self.attack.add_likenum(auction_id)
                self.attack.add_guanzhu(seller_id)
                self.attack.add_share_num(auction_id)

            elif task['do']=="chujia":
                print "chujia"
                auction_id=task['data']['auction_id']
                rp=task['data']['rp']
                self.attack.seesee_auction_attack(auction_id,rp)

            elif task['do']=="geturl":
                print "geturl"
                url=task['data']['url']
                self.attack.get_url(url)

            elif task['do']=="nextworker":
                print "nextworker"
                self.change_worker()
                print "newworker"

            elif task['do']=="stop":
                print "stop"
                self.stop()
                print "stop"


    def run(self):
        while not self.thread_stop:
            print("thread%d %s: waiting for tast" % (self.ident, self.name))
            try:
                task = q.get(block=True, timeout=20)  # 接收消息
                print("task recv:%s ,task No:%d" % (task['do'], 111))
                print("i am working")

                self.do(task)

                time.sleep(3)
                print("work finished!")
            except Queue.Empty:
                print("Nothing to do!")
                # self.thread_stop = True
                # break

            # q.task_done()  # 完成一个任务
            res = q.qsize()  # 判断消息队列大小
            if res > 0:
                print("fuck!There are still %d tasks to do" % (res))
            else:
                time.sleep(5)



    def stop(self):
        self.thread_stop = True


# if __name__ == "__main__":
    # q = Queue.Queue(5)
    # producter=Producter(q)
    # producter.start()
    # worker = worker(q)
    # worker.start()

    # q.put(["produce one cup!", 1], block=True, timeout=None)  # 产生任务消息
    # q.put(["produce one desk!", 2], block=True, timeout=None)
    # q.put(["produce one apple!", 3], block=True, timeout=None)
    # q.put(["produce one banana!", 4], block=True, timeout=None)
    # q.put(["produce one bag!", 5], block=True, timeout=None)
    print("***************leader:wait for finish!")
    # q.join()  # 等待所有任务完成
    print("***************leader:all task finished!")


from flask import Flask, request

app = Flask(__name__)

workhandler=[]

@app.route('/')
def gello_world():
    return 'Hello World'


q = Queue.Queue(500)
@app.route('/work', methods=['POST'])
def work():
    works=request.json['data']
    # print works
    works=list(works)
    t = threading.Thread(target=add_works, args=(works,))
    t.start()
    # for w in works:
    #     print w
    #     q.put(w, block=True, timeout=None)
    return flask.jsonify({'status': '0', 'errmsg': 'OK','counts':len(works)})

@app.route('/status')
def get_status():
    res = q.qsize()
    if res > 0:
        return "%d workers working.......... " % (len(workhandler))+"fuck!There are still %d tasks to do\n" % (res)
    else:
        return "There %d workers and.......... " % (len(workhandler))+"nothing to do\n"

def start(web_host,port):
    pywsgi.WSGIServer((web_host, port),
                      app, log=None).serve_forever()


@app.route('/start')
def start_work(worknum=100):
    if (request.args.get('count')):
        worknum = int(request.args.get('count'))
    print worknum
    # return str(worknum)
    works = []
    for i in xrange(worknum):
        works.append(MyWorker(q))
    for w in works:
        w.start()
    # for w in works:
    #     w.join()
    workhandler.extend(works)
    return str(len(workhandler))

@app.route('/workcount')
def get_workhandler():
    return str(len(workhandler))

@app.route('/stop')
def stop_worker():
    worknum=len(workhandler)
    if (request.args.get('count')):
        if int(request.args.get('count'))<=worknum:
            worknum=int(request.args.get('count'))
    print "will stop "+str(worknum)+"workers"
    for i in xrange(worknum):
        try:
            workhandler[i].stop()
        except Exception as e:
            print e
        global workhandler
    workhandler=workhandler[worknum:]
    return "still have "+str(len(workhandler))+" workers\n"

def add_works(works):
    for w in works:
        print w
        q.put(w, block=True, timeout=None)


if __name__ == '__main__':
    # worker = Worker(q)
    # worker.start()
    web_host="0.0.0.0"
    port=5000

    # works=[]
    # for i in xrange(10):
    #     works.append(MyWorker(q))
    # for w in works:
    #     w.start()

    start(web_host, port)