import feedparser
from datetime import datetime
import time
import sqlite3
from common import *


def monitor():
	log("Info - Starting Youtube YT_Monitor")
	while 1:
		log("YT_Monitor - Connecting to Database to Update Youtubers")
		connecttodb()
		log("YT_Monitor - Connected")
		for row in read_from_db("youtubers"):
			log("YT_Monitor - Getting Info about "+row[1])
			d = feedparser.parse('https://www.youtube.com/feeds/videos.xml?channel_id='+row[2])
			link = d['entries'][0]['link']
			title = d['entries'][0]['title']
			published = int(d['entries'][0]['published'].split("-")[2].split("T")[0])
			if (int(datetime.utcnow().strftime('%d')) == published) and already_downloaded(link):
				log("YT_Monitor - Adding Data to DB ")
				if row[3] == "mp4":
					log("YT_Monitor - INSERT INTO queue (name, method, url, opt, added_time, path) VALUES ("+title+", yt-mp4, "+link+", /mnt/usb/Youtube, "+d['entries'][0]['author']+")")
					addtoqueue(title,"yt-mp4",link,"/mnt/usb/Youtube/"+row[1]+"/",d['entries'][0]['author'])
				if row[3] == "mp3":
					log("YT_Monitor - INSERT INTO queue (name, method, url, opt, added_time, path) VALUES ("+title+", yt-mp3, "+link+", /mnt/usb/Music/super-dl, "+d['entries'][0]['author']+")")
					addtoqueue(title,"yt-mp3",link,"/mnt/usb/Music/super-dl/"+row[1]+"/",d['entries'][0]['author'])
			else:
				log("YT_Monitor - Info is already added or not released withing today")
		closedb()
		log("YT_Monitor - Connection Closed")
		log("YT_Monitor - Going for 1 Hour Sleep")
		time.sleep(3600)