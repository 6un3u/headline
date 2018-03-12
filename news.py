from urllib.request import urlopen
import datetime
import re

def find(RE, c):
    p = re.compile(RE)
    m = p.findall(c)

    return m

def dt():
    now = datetime.datetime.now()
    date = now.strftime('%m-%d')
    return date

def crawl():
    url = 'http://news.naver.com/main/home.nhn#'
    f = urlopen(url)
    b = f.read()
    c = b.decode('cp949')
    f.close()

    pubId = find('"officeId" : "(.*)"', c)
    office = find('"officeName" : "(.*)"', c)
    title = find('"title" : "(.*)"', c)

    date = dt()
    num = 0
    news = []

    for i in office:
            if title[num] == "":
                pass
            else: 
                n = [];
                n.append(pubId[num]);
                n.append(i);
                if('\\' in title[num]):
                    title[num] = title[num].replace('\\', '');
                n.append(title[num]);
                news.append(n);
            num+=1
    return news;
