import datetime
import time
import sqlite3
from common import *

out = " "
err	= " "


	
def downloader():
	log("Info - Waiting 1 mins to Start the Downloader")
	time.sleep(60)
	log("Info - Starting Downloader")
	while 1:
		if int(datetime.now().strftime('%H')) < 8:
			log("Downloader - Connecting to Database to get Queue")
			connecttodb()
			for row in read_from_db("queue"):
				if row[2] == "yt-mp4":
					runcmd('youtube-dl '+row[3]+' -o '+row[6].replace(" ","_")+row[1].replace(" ","-")+'.%(ext)s -f 22 --max-filesize 250m -c -w --no-progress')
					if ("File is larger than max-filesize" in out):
						runcmd('youtube-dl '+row[3]+' -o "'+row[6].replace(" ","_")+row[1].replace(" ","-")+'.%(ext)s -f 18 --max-filesize 250m -c -w --no-progress')
				elif row[2] == "yt-mp3":
					runcmd('youtube-dl '+row[3]+' -o '+row[6].replace(" ","_")+row[1].replace(" ","-")+'.%(ext)s -f 140 -c -w --no-progress')
				elif row[2] == "wget":
					runcmd("wget "+row[3]+" -P "+row[6]+" "+row[4])
				movetodone(row[1],row[2],row[3],row[4],row[5],row[6])
			closedb()
			log("Downloader - Connection Closed")
			log("Downloader - Going for 10 Mins Sleep")
			time.sleep(300)
		else:
			log("Downloader - Wait till the peek off package is on")
			while int(datetime.now().strftime('%H')) >= 8:
				time.sleep(60)
				