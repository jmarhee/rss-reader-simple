from reader import buildFeed, buildConfig
from flask import Flask, render_template
import os
 
app = Flask(__name__)

@app.route('/')
def index():
	feeds = buildConfig()
	feeds_data = buildFeed(feeds)
	if os.environ.get("SITE_NAME") == "":
		site_name = "reader.freeipad.internal"
	else:
		site_name = os.environ['SITE_NAME']
	return render_template('index.html', feeds=feeds_data, site_name=site_name)
