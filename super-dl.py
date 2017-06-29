#!/usr/bin/python3
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