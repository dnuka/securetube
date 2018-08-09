# securetube engine

from urllib import request
from pprint import pprint
from bs4 import BeautifulSoup

base = 'https://www.youtube.com/results/?search_query={}&disable_polymer=1&hl=en-GB&gl=US'


def get_thumbnail(video_id):
	return 'https://img.youtube.com/vi/{}/mqdefault.jpg'.format(video_id)


def fetch(query):
	results = []
	req = request.Request(base.format(query))
	req.add_header("User-Agent", "36438")
	with request.urlopen(req) as youtube:
		raw_data = BeautifulSoup(youtube, 'html.parser')
	#videos = raw_data.find_all('h3', attrs={'class': 'yt-lockup-title'})
	data = raw_data.findAll('a',attrs={'class':'yt-uix-tile-link'})
	for info in data:
		link = 'https://www.youtube.com' + info['href']
		if '/watch?v' in link:
			temp = {}
			temp['url'] = link
			temp['description'] = info['title']
			temp['thumbnail'] = get_thumbnail(info['href'].strip('/watch?v='))
			results.append(temp)
	return results
