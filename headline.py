import sqlite3
from bottle import route, run, template, static_file
from datetime import date

d = date.today()
date = d.isoformat()
date = d.strftime('%Y-%m-%d')

@route('/')
def index():
    con = sqlite3.connect('news.db')
    c = con.cursor()
    c.execute("select * from headline where day='%s'" % date)
    result = c.fetchall()
    c.close()
    output = template('index', rows=result)
    return output 

@route('/static/<filename:path>')
def giveCss(filename):
    return static_file(filename, root='static/')

run(host='0.0.0.0', debug=True)
#run(port=8080)



