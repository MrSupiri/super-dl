import feedparser
from datetime import datetime
import time
import sqlite3
import logging
import os

global out
global err

def read_from_db(name):
	logger.debug("Reading Data from "+name)
	try:
		c.execute('SELECT * FROM '+name)
		return c.fetchall()
	except Exception as e:
		logger.critical(str(type(e).__name__)+" : "+str(e))
		
def already_downloaded(url):
	for row in read_from_db("done"):
		if url in row:
			logger.debug(url+"is ready in the downloaded list")
			return False
			break
	for row in read_from_db("queue"):
		if url in row:
			logger.debug(url+"is ready in the queue")
			return False
			break
	return True
	
def run_cmd(cmd):
	logger.info('executing cmd - ' + cmd)
	try:
		f = os.popen(cmd)
		out = f.read()
		for line in out.split("\n"):
			logger.info("output " + line)
	except Exception as e:
		logger.critical(str(type(e).__name__) + " : " + str(e))
	# p = subprocess.Popen(cmd.split(),stdout=subprocess.PIPE,stderr=subprocess.PIPE)
	# out, err = p.communicate()
	# logger.info('executing cmd - '+cmd)
	# for line in str(out).split("\\n"):
	# 	if line != "'":
	# 		logger.info("output - "+line)
	# if err != b'':
	# 	logger.warn("There was a error while running following command\t\t"+cmd)
	# 	for line in str(err).split("\\n"):
	# 		if line != "'":
	# 			logger.error(line)
	
def movetodone(name,method,url,opt,added_time,path):
	time = datetime.now().strftime('%X %x')
	logger.debug('INSERT INTO done (name, method, url, opt, added_time, downloaded_time, path) VALUES (%s, %s, %s, %s, %s, %s, %s)' % (name, method, url, opt, added_time, time, path))
	try:
		c.execute("INSERT INTO done (name, method, url, opt, added_time, downloaded_time, path) VALUES (?, ?, ?, ?, ?, ?, ?)",
			(name, method, url, opt, added_time, time, path))
		conn.commit()
	except Exception as e:
		logger.error(str(type(e).__name__)+" : "+str(e))
	
	logger.debug("DELETE FROM queue WHERE url = '"+url+"'")
	try:	
		c.execute("DELETE FROM queue WHERE url = '"+url+"'")
		conn.commit()	
	except Exception as e:
		logger.error(str(type(e).__name__)+" : "+str(e))

def addtoqueue(name,method,url,path,opt):
	time = datetime.now().strftime('%X %x')
	logger.debug('INSERT INTO queue (name, method, url, opt, added_time, path) VALUES (%s, %s, %s, %s, %s, %s)' % (name, method, url, opt, time, path))
	try:
		c.execute("INSERT INTO queue (name, method, url, opt, added_time, path) VALUES (?, ?, ?, ?, ?, ?)",
			(name, method, url, opt, time, path))
		conn.commit()
	except Exception as e:
		logger.critical(str(type(e).__name__)+" : "+str(e))
	
def addyter(name, id, type):
	c.execute("INSERT INTO youtubers (youtuber, youtube_id, type) VALUES (?, ?, ?)",
		(name, id, type))
	conn.commit()
	
def connecttodb():
	global conn
	global c
	try:
		conn = sqlite3.connect('database/super-dl.db')
		c = conn.cursor()
	except Exception as e:
		logger.critical(str(type(e).__name__)+" : "+str(e))

def closedb():
	try:
		c.close
		conn.close()
	except Exception as e:
		logger.error(str(type(e).__name__)+" : "+str(e))
		
	
global logger
logger = logging.getLogger("Logger")
logger.setLevel(logging.DEBUG)

# create console handler and set level to debug
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

ch = logging.FileHandler('logs/super-dl.log')

# create formatter
formatter = logging.Formatter(fmt='%(asctime)-10s %(levelname)-10s: %(module)-10s:  %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
#%(asctime)s  %(name)s\t
# add formatter to ch
ch.setFormatter(formatter)

# add ch to logger
logger.addHandler(ch)
