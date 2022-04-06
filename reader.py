from bs4 import BeautifulSoup
import requests
import yaml
import os
import time
import yaml

headers = {'User-Agent': 'freeipad-reader'}

# with open(os.environ['FEED_YAML_PATH']) as f:
# 	dict = yaml.load(f, Loader=yaml.FullLoader)
# 	feeds = dict['feeds']
 
class ReadRss:
 
    def __init__(self, rss_url, headers):
 
        self.url = rss_url
        self.headers = headers
        try:
            self.r = requests.get(rss_url, headers=self.headers)
            self.status_code = self.r.status_code
        except Exception as e:
            print('Error fetching the URL: ', rss_url)
            print(e)
        try:    
            self.soup = BeautifulSoup(self.r.text, 'lxml')
        except Exception as e:
            print('Could not parse the xml: ', self.url)
            print(e)
        self.articles = self.soup.findAll('item')
        self.articles_dicts = [{'title':a.find('title').text,'link':a.link.next_sibling.replace('\n','').replace('\t',''),'description':a.find('description').text,'pubdate':a.find('pubdate').text} for a in self.articles]
        self.urls = [d['link'] for d in self.articles_dicts if 'link' in d]
        self.titles = [d['title'] for d in self.articles_dicts if 'title' in d]
        self.descriptions = [d['description'] for d in self.articles_dicts if 'description' in d]
        self.pub_dates = [d['pubdate'] for d in self.articles_dicts if 'pubdate' in d]

def buildConfig():
	with open(os.environ['FEED_YAML_PATH']) as f:
		dict = yaml.load(f, Loader=yaml.FullLoader)
		return dict['feeds']
 
def buildFeed(feeds):
	feed_body = []
	for url in feeds:
		new_feed = {"feed" : url, "data": []}
		feed = ReadRss(url, headers)
		end = len(feed.pub_dates) -1 
		feed_urls = feed.urls
		feed_dates = feed.pub_dates
		feed_titles = feed.titles
		feed_descriptions = feed.descriptions
		for e in range(0,end):
			feed_body_item = {}
			feed_body_item['urls'] = feed_urls[int(e)].replace("<![CDATA[","").replace("]]>","")
			feed_body_item['dates'] = feed_dates[int(e)].replace("<![CDATA[","").replace("]]>","")
			feed_body_item['titles'] = feed_titles[int(e)].replace("<![CDATA[","").replace("]]>","")
			feed_body_item['descriptions'] = feed_descriptions[int(e)].replace("<![CDATA[","").replace("]]>","")
			feed_body_item['article_body'] = feed.articles[int(e)]
			new_feed['data'].append(feed_body_item)
		feed_body.append(new_feed)
	print(feed_body[1])
	return feed_body