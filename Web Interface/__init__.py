import sqlite3
from flask import Flask, render_template, flash, request

app = Flask(__name__)

@app.route('/', methods=["GET","POST"])
def homepage():
	try:
		table_type = 'downloads'
		table = request.args.get('table')
		conn = sqlite3.connect('/home/pi/pycharm/super-dl/database/super-dl.db')
		c = conn.cursor()
		if table == "download":
			c.execute('SELECT * FROM downloads where state = "%s"'%(table))
			table_type = 'downloads'
		elif table == "done":
			c.execute('SELECT * FROM downloads where state = "%s"'%(table))
			table_type = 'downloads'
		elif table == "paused":
			c.execute('SELECT * FROM downloads where state = "%s"'%(table))
			table_type = 'downloads'
		elif table == None:
			c.execute('SELECT * FROM downloads')
			table_type = 'downloads'
		elif table == "youtubers":
			c.execute('SELECT * FROM youtubers')
			table_type = 'youtubers'
		items = c.fetchall()
		return render_template("main.html", items=items, table_type=table_type)
	except Exception as e:
		flash(str(e))
		
	return render_template("main.html")
	
if __name__ == "__main__":
    app.run()