# super-dl
Super-DL Linux command line downloader. It help to automatically download videos from your YouTube subscribers daily and it can download any other file in selected time period of a day

# This Version is stop maintaining Check the [New version](https://github.com/mrsupiri/) of this on my Github with much more cool stuff

![status: stop maintaining](https://img.shields.io/badge/Status-Stopped%20Maintaining-red.svg)
[![Codeship](https://img.shields.io/codeship/d6c1ddd0-16a3-0132-5f85-2e35c05e22b1/master.svg?style=flat-square)]()
[![Travis](https://img.shields.io/travis/rust-lang/rust.svg?style=flat-square)]()


# How to USE ?

  - You can use the web interface to add iteams to queue (warning - it has lot of bugs)
  - you can also use database to add iteams to queue.
  - after data is added start the super-dl.py with python3
    ```sh
    screen -S super-dl python3 super-dl.py
    ```

# Dependencies
Install the dependencies run the super-dl.py
```sh
$ apt-get install python3 python3-feedparser
$ apt-get install youtube-dl
$ apt-get install deluge deluge-console
$ apt-get install screen
```
If you still want to use this version and need any help fixing any bug in this make a pullrequest or create a new issue in issue tab
