#!/usr/bin/python
from multiprocessing import Process
from yt import monitor
from common import log
from downloader import downloader

log("##########################################################")
log("##########################################################")


if __name__=='__main__':
     p1 = Process(target = downloader)
     p1.start()
     p2 = Process(target = monitor)
     p2.start()
