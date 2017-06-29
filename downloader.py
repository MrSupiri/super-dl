from common import *

def downloader():
    time.sleep(60)
    logger.debug("Starting Downloader")
    while 1:
        try:
            if int(datetime.now().strftime('%H')) < 8:
                for row in read_from_db("downloads"):
                    if row[11] == "download":
                        if row[2] == "yt-mp4":
                            out = run_cmd('youtube-dl -o "{}{} [%(id)s].%(ext)s" {} -f 18 --max-filesize 250m -c -w --no-progress'.format(row[7],clear(row[1]),row[3]))
                        if ("File is larger than max-filesize" in out):
                            logger.info("Lowering Quality Due to Large File Size")
                            run_cmd('youtube-dl -o "{}{} [%(id)s].%(ext)s" {} -f 18 --max-filesize 250m -c -w --no-progress'.format(row[7], clear(row[1]), row[3]))
                        elif row[2] == "yt-mp3":
                            run_cmd('youtube-dl -o "{}{} [%(id)s].%(ext)s" {} -f 140 --max-filesize 250m -c -w --no-progress'.format(row[7], clear(row[1]), row[3]))
                        elif row[2] == "yt-pl":
                            run_cmd('youtube-dl -o "{}%(playlist)s/%(playlist_index)s-%(title)s_[%(id)s].%(ext)s" {} -f 22 -c -w --no-progress'.format(row[7], row[3]))
                        elif row[2] == "wget":
                            run_cmd("wget "+row[3]+" -P "+row[6]+" "+row[9])
                        logger.debug('Moving the row from queue table to done table')
                        change_state(row[3],"done")
                logger.info("Waiting 10 mins for next session")
                time.sleep(300)
            else:
                logger.info("Wait till the peek off package is on")
                w_time = 0
                while int(datetime.now().strftime('%H')) >= 8:
                    w_time += 1
                    time.sleep(60)
                    if w_time > 120:
                        logger.debug("Wait till the peek off package is on")
                        w_time = 0
        except Exception as e:
            logger.critical(str(type(e).__name__) + " : " + str(e))

if __name__=='__main__':
    downloader()
