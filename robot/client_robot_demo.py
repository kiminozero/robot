#coding=utf-8
import requests
# it's also works well with curl, such as add work or worker stop workers and etc.
s=requests.Session()

do=[{'do':'likenum',"data":{"auction_id":"17032","seller_id":"114149"}},{'do':'likenum',"data":{"auction_id":"17032","seller_id":"114149"}},{'do':'likenum',"data":{"auction_id":"17032","seller_id":"114149"}},{'do':'likenum',"data":{"auction_id":"17032","seller_id":"114149"}},{'do':'likenum',"data":{"auction_id":"17032","seller_id":"114149"}},{'do':'likenum',"data":{"auction_id":"17032","seller_id":"114149"}},{'do':'likenum',"data":{"auction_id":"17032","seller_id":"114149"}},{'do':'likenum',"data":{"auction_id":"17032","seller_id":"114149"}},{'do':'likenum',"data":{"auction_id":"17032","seller_id":"114149"}}]


def work(do):
    pass


def add_works(worknum):
    pass


def start_workers(worknum):
    pass


def stop_workers(worknum):
    pass

def get_status():
    pass

def workcount():
    pass


r=s.post("http://127.0.0.1:5000/work",json={"data":[{'do':'do'}]})


print r.content
