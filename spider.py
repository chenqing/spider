#!/usr/bin/python
#coding=utf-8
from dytt8.dytt8 import dytt8
from xunbo.xunbo import xunbo
from mythread    import mythread

#dytt8 = dytt8(5)

print "开始抓取迅播前三页的电影链接。。。"
xunbo = xunbo(3)

mythread(xunbo)
