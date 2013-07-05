#!/usr/bin/python
#coding=utf-8
import threading
from Queue import Queue
import  sqlite3

from dytt8.dytt8 import dytt8

dy = dytt8(10)

db = sqlite3.connect("/Users/chenqing/hellopy/spider/spider.db")

link = db.cursor()

ftp_urls = []


class ThreadUrl(threading.Thread):


    def __init__(self,queue):
        threading.Thread.__init__(self)
        self.queue = queue

    def run(self):

        while True:
            url = self.queue.get()

            t = dy.ftp_url(url)
            if len(t) > 1:
                ftp_urls.append(t)
            self.queue.task_done()



if __name__ == '__main__':

    queue = Queue()

    for i in range(20):

        t= ThreadUrl(queue)

        t.setDaemon(True)

        t.start()


    for url in dy.http_url():

        queue.put(url)

        queue.join()

    for ftp_url in ftp_urls:
        print ftp_url


    db.close()