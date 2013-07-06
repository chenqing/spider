#!/usr/bin/python
#coding=utf-8
from dytt8.dytt8 import dytt8
from xunbo.xunbo import xunbo
from mythread    import mythread
import sqlite3
'''
	本文件是将抓取到的链接写入sqlite 数据库的版本
'''

db = sqlite3.connect('./spider.db')

link = db.cursor()

link.execute('select * from sqlite_master where type="table" and name="ftp_url";')
if not link.fetchone():

    link.execute("""CREATE TABLE `ftp_url` ( `id` INTEGER PRIMARY KEY  NOT NULL , `url` varchar(120) DEFAULT NULL)""")
    db.commit()

print "开始抓取迅播前三页的电影链接。。。"
xunbo = xunbo(3)

urls = mythread(xunbo)
for url in urls:
    sql = """INSERT INTO `ftp_url` values(NULL,'%s' );""" %(url)
    link.execute(sql)

db.commit()

db.close()
