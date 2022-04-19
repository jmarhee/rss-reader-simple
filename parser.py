import feedparser
import os
import yaml

def buildConfig():
    with open(os.environ['FEED_YAML_PATH']) as f:
        dict = yaml.load(f, Loader=yaml.FullLoader)
    return dict['feeds']

def buildFeed(feeds):
    feed_body = []
    for url in feeds:
        feed_data = feedparser.parse(url)
        new_feed = {"feed" : url, "data": [feed_data]}
        feed_body.append(new_feed)
    return feed_body