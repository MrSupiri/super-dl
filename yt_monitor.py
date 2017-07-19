from common import *
import feedparser

def monitor():
	while 1:
		logger.debug("Connecting to Database to Update Youtubers")
		logger.debug("Connected to Database")
		try:
			for row in read_from_db("youtubers"):
				logger.debug("Getting Info about "+row[1])
				d = feedparser.parse('https://www.youtube.com/feeds/videos.xml?channel_id='+row[2])
				link = d['entries'][0]['link']
				title = d['entries'][0]['title']
				published = int(d['entries'][0]['published'].split("-")[2].split("T")[0])
				if (int(datetime.utcnow().strftime('%d')) == published) and already_downloaded(d['entries'][0]['author'],link):
					logger.debug("Adding Data to DB ")
					if row[3] == "mp4":
						download(title,"yt-mp4",link,"/mnt/usb/Youtube/"+row[1]+"/",d['entries'][0]['author'])
					if row[3] == "mp3":
						download(title,"yt-mp3",link,"/mnt/usb/Music/super-dl/"+row[1]+"/",d['entries'][0]['author'])
				else:
					logger.debug("Info is already added or not released withing today")
		except Exception as e:
			logger.critical(str(type(e).__name__) + " : " + str(e))

		try:
			for row in read_from_db("torrent"):
				logger.debug("Getting Info about "+row[2])
				d = feedparser.parse(row[2])
				for entry in d['entries']:
					link = entry['link']
					title = row[1]
					if title in str(entry['title']):
						if (already_torrented(title,link)):
							logger.debug("Adding Data to DB ")
							download(entry['title'],"torrent",link,row[3],' ')
							break
						else:
							logger.debug("Info is already added")
							break
		except Exception as e:
			logger.critical(str(type(e).__name__) + " : " + str(e))


		logger.debug("Connection Closed to Database")
		logger.info("Going for 1 Hour Sleep")
		time.sleep(3600)
if __name__=='__main__':
	monitor()
