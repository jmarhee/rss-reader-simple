from parser import buildFeed, buildConfig
from flask import Flask, render_template, send_from_directory
import os
from apscheduler.schedulers.background import BackgroundScheduler
 
app = Flask(__name__)

feed_data = None

@app.before_first_request
def initialize_feeds():
	feeds = buildConfig()
	global feed_data
	feed_data = buildFeed(feeds)
	return feed_data

def update_feeds():
	feeds = buildConfig()
	global feed_data
	feed_data = buildFeed(feeds)
	return feed_data

scheduler = BackgroundScheduler()
job = scheduler.add_job(update_feeds, 'interval', minutes=1)
scheduler.start()

@app.route('/')
def index():
	if os.environ.get("SITE_NAME") == "":
		site_name = "reader.freeipad.internal"
	else:
		site_name = os.environ['SITE_NAME']
	return render_template('index.html', feed_data=feed_data, site_name=site_name)

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

scheduler = BackgroundScheduler()
job = scheduler.add_job(update_feeds, 'interval', minutes=1)
scheduler.start()