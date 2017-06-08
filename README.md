# Super-DL
Super-DL Linux command line downloader. It help to automatically download videos from your YouTube subscribers daily and it can download any other file in selected time period of a day. <br><br>
This Software is designed to run on Raspberry Pi so You can keep it on 24/7. If Your ISP have split your package to night time package and day time package, You can use the software to make a use of night time date and save your data time data <br><br>
Although although youtube and direct download only torrent support will be added in near future with RSS Automation
# Features
  <ul>
  <li>Donwload youtube videos</li>
  <li>Donwload youtube music vidoes</li>
  <li>Download any direct files</li>
  <li>Automatically download newly released Videos from selected youtubers</li>
  <li>Can Schedule the downloading time</li>
  <li>Record everything in a mysqlite database</li>
  <li>CMD Based (GUID is Coming Soon)</li>
  </ul>
  
# Requirements
<ul>
  <li>Youtube-DL</li>
  <li>Wget</li>
  <li>Python3</li>
  <li>Python-Feedparser</li>
</ul>
# How to Use
This is still in Beta version so there is no GUI<br>
To add the youtubers you want download DB Browser for SQLite and date the super-dl.db<br>
Once you add your favorite youtubers and their <a href="http://dev.zype.com/posts/2014/11/04/finding-youtube-channel-id/">channel id</a>  to youtubers table in the super-dl.db<br>
Save it and Run the start.sh, This will create a screen season named super-dl and run in the background till the Raspberry Pi is turned off<br>
