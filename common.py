import feedparser
import subprocess
from datetime import datetime
import time
import sqlite3

global out
global err

def read_from_db(name):
    c.execute('SELECT * FROM '+name)
    return c.fetchall()
	
def already_downloaded(url):
	for row in read_from_db("done"):
		if url in row:
			return False
			break
	for row in read_from_db("queue"):
		if url in row:
			return False
			break
	return True

	
def log(text):
	with open("log/yt.log", "a") as f:
		f.write(datetime.now().strftime('%X %x')+" - "+text+"\n")
	print(datetime.now().strftime('%X %x')+" - "+text+"\n")
	
def runcmd(cmd):
	p = subprocess.Popen(cmd.split(),stdout=subprocess.PIPE,stderr=subprocess.PIPE)
	out, err = p.communicate()
	log("cmd - "+cmd)
	#log("err - "+err)
	for line in str(out).split("\\n"):
		log("out - "+line)
	for line in str(err).split("\\n"):
		log("err - "+line)	
	
def movetodone(name,method,url,opt,added_time,path):
	time = datetime.now().strftime('%X %x')
	c.execute("INSERT INTO done (name, method, url, opt, added_time, downloaded_time, path) VALUES (?, ?, ?, ?, ?, ?, ?)",
		(name, method, url, opt, added_time, time, path))
	conn.commit()
	c.execute("DELETE FROM queue WHERE url = '"+url+"'")
	conn.commit()
		

	
def addtoqueue(name,method,url,path,opt):
	time = datetime.now().strftime('%X %x')
	c.execute("INSERT INTO queue (name, method, url, opt, added_time, path) VALUES (?, ?, ?, ?, ?, ?)",
		(name, method, url, opt, time, path))
	conn.commit()
	
def connecttodb():
	global conn
	global c
	conn = sqlite3.connect('database/super-dl.db')
	c = conn.cursor()

def closedb():
	c.close
	conn.close()