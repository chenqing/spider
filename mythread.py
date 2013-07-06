#!/usr/bin/python
#coding=utf-8
import threading
from Queue import Queue
from dytt8.dytt8 import dytt8
from xunbo.xunbo import xunbo
#下面的dy 就是dytt8的这个class的一个引用，
dy = dytt8(10)
xunbo = xunbo(3)

ftp_urls = []

class ThreadUrl(threading.Thread):
	'''
	封装多线程库，用来多线程跑啊
	'''

	def __init__(self,queue,site):
        	threading.Thread.__init__(self)
        	self.queue = queue
		self.site = site  #传递的是一个class的实例或者引用

	def run(self):

		while True:
			try:
				url = self.queue.get()
				t = self.site.ftp_url(url)
				if len(t) > 1:
					ftp_urls.append(t)
			except:
				pass
			self.queue.task_done()



def mythread(site,num=20):
	'''
	num: 结合队列，跑多线程的抓取，默认线程数是20个
	site: 这是一个关于某个站点的引用，比如 t = dytt8() 
	'''
	queue = Queue()

	for i in range(num):

		t= ThreadUrl(queue,site)

		t.setDaemon(True)

		t.start()


	for url in site.http_url():

		queue.put(url)

        	queue.join()

	for ftp_url in ftp_urls:
        	print ftp_url
if __name__ == '__main__':
	mythread(xunbo)
