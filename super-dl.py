#!/usr/bin/python
from multiprocessing import Process
from yt_monitor import monitor
from downloader import downloader
from common import *
import sys

logger.info("##########################################################")
logger.info("##################### Starting ###########################")
logger.info("##########################################################")


if __name__=='__main__':
	logger.info("Waiting 1 mins to Start the Downloader")
	logger.debug("Connecting to Database to get Queue")
	connecttodb()
	try:
		p1 = Process(target = downloader)
		p1.start()
	except Exception as e:
		logger.critical(str(type(e).__name__)+" : "+str(e))
		sys.exit()
		
	logger.info("Starting Youtube YT_Monitor")
	
	try:
		p2 = Process(target = monitor)
		p2.start()
	except Exception as e:
		logger.critical(str(type(e).__name__)+" : "+str(e))
		sys.exit()
		
	# print("Super-DL is successfully Started")
	# print("type !help for get help")
	# inputcmd = input()
	#
	# while(1):
	# 	if inputcmd == "!help":
	# 		print("To add a new Youtuber type !addyoutuber")
	# 		print("To Download a youtube video !yt")
	# 		print("To do a Direct Download type !dl")
	#
	# 	elif inputcmd == "!addyoutuber":
	# 		name = input("Enter the name of the Youtuber :- ")
	# 		id = input("Enter the youtube channel id of the Youtuber :- ")
	# 		vtype = input("Do you want to download content in mp3 or mp4 ? :- ")
	# 		while vtype != "mp3" and vtype != "mp4":
	# 			vtype = input("Invalid Type\nDo you want to download content in mp3 or mp4 ? :- ")
	#
	# 		logger.debug("INSERT INTO youtubers (youtuber, youtube_id, type VALUES (%s, %s, %s)"%(name, id, vtype))
	# 		try:
	# 			addyter(name, id, vtype)
	# 		except Exception as e:
	# 			logger.error(str(type(e).__name__)+" : "+str(e))
	#
	# 	elif inputcmd == "!yt":
	# 		name = input("Enter the name of the Youtube video :- ")
	# 		link = input("Enter the link of the Youtube video :- ")
	# 		vtype = input("Do you want to download content in mp3 or mp4 ? :- ")
	# 		while vtype != "mp3" and vtype != "mp4":
	# 			vtype = input("Invalid Type\nDo you want to download content in mp3 or mp4 ? :- ")
	# 		addtoqueue(name,"yt-"+vtype,link,"/mnt/usb/Youtube/"+row[1]+"/",author)
	#
	# 	elif inputcmd == "!dl":
	# 		name = input("Enter the name of the file :- ")
	# 		link = input("Enter the link for the file :- ")
	# 		path = input("where do you want to save it ? :- ")
	# 		while name == "" and link =="" and path =="":
	# 			print("Invalid input")
	# 			name = input("Enter the name of the file :- ")
	# 			link = input("Enter the link for the file :- ")
	# 			path = input("where do you want to save it ? :- ")
	# 		addtoqueue(name,"wget",link,path+"/"," ")
	# 	else:
	# 		print("Invalid CMD")
	# 		print("type !help for get help")
	# 	inputcmd = input("")