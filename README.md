spider
======

功能：
-----
    爬取常见电影网站的电影链接，然后，你懂得
    
    当然你也可以把连接写入数据库，这里使用的数据库是python自带的sqllite3
    目前支持的网站有：电影天堂（www.dyt8.net）迅播影院（www.2tu.cc）
    后续也会增加一些其它的网站，不仅限于电影类网站
    
用法：
-----
    [ chenqing@qing ~/hellopy/spider ] python spider.py 
    开始抓取迅播前三页的电影链接。。。
    ftp://dy:dy@xlj.2tu.cc:30358/[迅雷下载www.2tu.cc]分手合约.HD1024高清国语中字.rmvb
    ftp://dy:dy@xlj.2tu.cc:20345/[迅雷下载www.2tu.cc]速度与激情6.BD1024高清英语中字.rmvb
    ftp://dy:dy@xlj.2tu.cc:10305/[迅雷下载www.2tu.cc]同谋.HD1024高清国语中字.rmvb
    ftp://dy:dy@xlj.2tu.cc:20346/[迅雷下载www.2tu.cc]守门人.BD1024高清中英双字.rmvb
    ftp://dy:dy@xlj.2tu.cc:30275/[迅雷下载www.2tu.cc]松林外.DVD英语中字.rmvb
    ftp://dy:dy@xla.xunbo.cc:20395/[迅雷下载www.XunBo.Cc]亲密敌人.DVDsrc国语中字.rmvb
    .......
sqlite3:
------
    [ chenqing@Qing ~/hellopy/spider  ] sqlite3 spider.db
    SQLite version 3.7.12 2012-04-03 19:43:07
    Enter ".help" for instructions
    Enter SQL statements terminated with a ";"
    sqlite> select * from sqlite_master where type="table" and name="ftp_url";
    table|ftp_url|ftp_url|4|CREATE TABLE `ftp_url` ( `id` INTEGER PRIMARY KEY  NOT NULL , `url` varchar(120) DEFAULT NULL)
