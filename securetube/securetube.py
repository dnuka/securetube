# securetube engine

from urllib import request
from pprint import pprint
from bs4 import BeautifulSoup

base = 'https://www.youtube.com/results/?search_query={}&disable_polymer=1&hl=en-GB&gl=US'


def fetch(query):
	req = request.Request(base.format(query))
	req.add_header("User-Agent", "36435")
	with request.urlopen(req) as youtube:
		raw_data = BeautifulSoup(youtube, 'html.parser')
	videos = raw_data.find_all('h3', attrs={'class': 'yt-lockup-title'})
	return videos


