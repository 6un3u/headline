import sqlite3
import datetime
from news import crawl

# Connection 객체 만들기
con = sqlite3.connect('news.db')
# 커서 객체 만들기
cur = con.cursor()

# SQL 실행하기
news = crawl();
cur.execute('create table wOffice (office text, title text);')
cur.executemany('insert into wOffice values(?, ?)', news);

now = datetime.datetime.now()
date = now.strftime('%m-%d')

# 저장하기
con.commit()
# 연결 끊기
con.close()

# zetcode.com
