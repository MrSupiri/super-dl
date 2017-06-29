from datetime import datetime
import sqlite3
import logging
import os
import re
import sys
import time


def read_from_db(name):
    logger.debug("Reading Data from " + name)
    try:
        c.execute('SELECT * FROM ' + name)
        return c.fetchall()
    except Exception as e:
        logger.critical(str(type(e).__name__) + " : " + str(e))


def already_downloaded(author, url):
    c.execute("SELECT last_vid_url FROM youtubers WHERE youtuber = '%s'" % (author))
    last_vid_url = c.fetchone()
    if str(last_vid_url[0]) == str(url):
        return False
    else:
        update_last_vid(url, author)
        return True


def run_cmd(cmd):
    logger.info('executing cmd - ' + cmd)
    try:
        f = os.popen(cmd)
        out = f.read()
        for line in out.split("\n"):
            logger.info("output " + line)
        return out
    except Exception as e:
        logger.critical(str(type(e).__name__) + " : " + str(e))


def clear(s):
    return re.sub('[^A-Za-z0-9 ]+', '', s)


def download(name, method, url, path, by):
    time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    logger.info("INSERT INTO downloads (name, method, url, by, added_time, path) VALUES (%s, %s, %s, %s, %s, %s)" % (
    name, method, url, by, time, path))
    try:
        c.execute("INSERT INTO downloads (name, method, url, by, added_time, path, state) VALUES (?, ?, ?, ?, ?, ?, ?)",
                  (name, method, url, by, time, path, "download"))
        conn.commit()
    except Exception as e:
        logger.critical(str(type(e).__name__) + " : " + str(e))


def add_youtuber(name, id, type):
    c.execute("INSERT INTO youtubers (youtuber, youtube_id, type) VALUES (?, ?, ?)",
              (name, id, type))
    conn.commit()


def connect_db():
    try:
        conn = sqlite3.connect('database/super-dl.db')
        c = conn.cursor()
        return conn, c
    except Exception as e:
        logger.critical(str(type(e).__name__) + " : " + str(e))


def logger():
    # logger = logging.getLogger("Logger")
    # logger.setLevel(logging.DEBUG)
    # ch = logging.StreamHandler(sys.stdout)
    # ch.setLevel(logging.DEBUG)
    # ch = logging.FileHandler('logs/super-dl.log')
    #
    # formatter = logging.Formatter(fmt='%(asctime)-10s %(levelname)-10s: %(module)-10s:  %(message)s',
    #                               datefmt='%Y-%m-%d %H:%M:%S')
    # ch.setFormatter(formatter)
    # logger.addHandler(ch)

    logFormatter = logging.Formatter(fmt='%(asctime)-10s %(levelname)-10s: %(module)-10s:  %(message)s',
                                   datefmt='%Y-%m-%d %H:%M:%S')
    rootLogger = logging.getLogger()
    rootLogger.setLevel(logging.DEBUG)
    fileHandler = logging.FileHandler('logs/super-dl.log')
    fileHandler.setFormatter(logFormatter)
    rootLogger.addHandler(fileHandler)

    consoleHandler = logging.StreamHandler()
    consoleHandler.setFormatter(logFormatter)
    rootLogger.addHandler(consoleHandler)



    return rootLogger


def change_state(url, state):
    logger.info("UPDATE downloads SET state = '%s' WHERE url = '%s';" % (state, url))
    time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    try:
        c.execute("UPDATE downloads SET state = '%s' WHERE url = '%s';" % (state, url))
        if state == "done":
            c.execute("UPDATE downloads SET downloaded_time = '%s' WHERE url = '%s';" % (time, url))
        conn.commit()
    except Exception as e:
        logger.critical(str(type(e).__name__) + " : " + str(e))


def update_last_vid(url, youtuber):
    logger.info("UPDATE youtubers SET last_vid_url = '%s' WHERE youtuber = '%s';" % (url, youtuber))
    try:
        c.execute("UPDATE youtubers SET last_vid_url = '%s' WHERE youtuber = '%s';" % (url, youtuber))
        conn.commit()
    except Exception as e:
        logger.critical(str(type(e).__name__) + " : " + str(e))

file_name = 'logs/super-dl.log'
if os.path.isfile(file_name + ".5"):
    os.remove(file_name + ".5")
if os.path.isfile(file_name + ".4"):
    os.rename(file_name + ".4", file_name + ".5")
if os.path.isfile(file_name + ".3"):
    os.rename(file_name + ".3", file_name + ".4")
if os.path.isfile(file_name + ".2"):
    os.rename(file_name + ".2", file_name + ".3")
if os.path.isfile(file_name + ".1"):
    os.rename(file_name + ".1", file_name + ".2")
if os.path.isfile(file_name):
    os.rename(file_name, file_name + ".1")
    if os.path.isfile(file_name):
        os.remove(file_name)

logger = logger()
conn, c = connect_db()
