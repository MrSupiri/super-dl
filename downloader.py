import datetime
from common import *

out = " "
err	= " "

def downloader():
	time.sleep(60)
	logger.debug("Starting Downloader")
	while 1:
		if int(datetime.now().strftime('%H')) < 8:
			
			for row in read_from_db("queue"):
				if row[2] == "yt-mp4":
					try:
						run_cmd('youtube-dl '+row[3]+' -o "'+row[6].replace(" ","_")+row[1].replace(" ","-")+'.%(ext)s" -f 22 --max-filesize 250m -c -w --no-progress')
					except Exception as e:
						logger.error(str(type(e).__name__)+" : "+str(e))
					if ("File is larger than max-filesize" in out):
						try:
							run_cmd('youtube-dl '+row[3]+' -o "'+row[6].replace(" ","_")+row[1].replace(" ","-")+'.%(ext)s" -f 18 --max-filesize 250m -c -w --no-progress')
						except Exception as e:
							logger.error(str(type(e).__name__)+" : "+str(e))
				elif row[2] == "yt-mp3":
					try:
						run_cmd('youtube-dl '+row[3]+' -o "'+row[6].replace(" ","_")+row[1].replace(" ","-")+'.%(ext)s" -f 140 -c -w --no-progress')
					except Exception as e:
						logger.error(str(type(e).__name__)+" : "+str(e))
				elif row[2] == "yt-pl":
					try:
						run_cmd('youtube-dl -o "'+row[6].replace(" ","_")+'%(playlist)s/%(playlist_index)s - %(title)s.%(ext)s"  '+row[3]+' -f 22 -c -w --no-progress')
					except Exception as e:
						logger.error(str(type(e).__name__)+" : "+str(e))
				elif row[2] == "wget":
					try:
						run_cmd("wget "+row[3]+" -P "+row[6]+" "+row[4])
					except Exception as e:
						logger.error(str(type(e).__name__)+" : "+str(e))
				logger.debug('Moving the row from queue table to done table')
				movetodone(row[1],row[2],row[3],row[4],row[5],row[6])
			#closedb()
			#logger.debug("Connection Closed")
			logger.info("Waiting 10 mins for next session")
			time.sleep(300)
		else:
			logger.info("Wait till the peek off package is on")
			while int(datetime.now().strftime('%H')) >= 8:
				time.sleep(60)

if __name__=='__main__':
	downloader()
