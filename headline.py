#!/usr/bin/python3
import sqlite3
from datetime import date
from news import crawl

d = date.today()
date = d.isoformat()
day = d.strftime('%Y%m%d')

news = crawl();

con = sqlite3.connect('news.db')
cur = con.cursor()

sqlP = 'insert into PUB values(?, ?)'
sqlT  = 'insert into TITLE values(?, ?, ?, ?)'

#insert data in DB
for i in range(len(news)):
    try:
        url = ('http://news.naver.com/main/list.nhn?mode=LPOD&mid=sec&oid=%s&listYple=paper&date=%s' % (news[i][0], day))
        cur.execute(sqlT, (date, news[i][0], news[i][2], url)); 
    except:
        pass
    #insert PubId & PUB in table PUB
    #cur.execute(sqlP, (news[i][0], news[i][1]));

con.commit()
con.close()
