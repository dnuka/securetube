# securetube engine

from urllib import request
import json
from pprint import pprint
from bs4 import BeautifulSoup
import youtube_dl

base = 'https://www.youtube.com/results/?search_query={}&disable_polymer=1&hl=en-GB&gl=US'


def get_thumbnail(video_id):
	return 'https://img.youtube.com/vi/{}/mqdefault.jpg'.format(video_id)


def fetch_meta(url):
	link = 'https://www.youtube.com/oembed?url={}&format=json'.format(url)
	req = request.Request(link)
	req.add_header("User-Agent", "36438")
	with request.urlopen(req) as youtube:
		data = json.loads(youtube.read().decode())
	#pprint(data)
	return data


def watch(url):
	ydl = youtube_dl.YoutubeDL({'outtmpl': '%(id)s%(ext)s'})
	with ydl:
		result = ydl.extract_info(
			url, download = False
		)
	if 'entries' in result:
		video = result['entries'][0]
	else:
		video = result
		#pprint(video['formats'])
		#print(len(video['formats']))
		for vid in video['formats']:
			if vid['vcodec'] == 'avc1.42001E':
				return vid['url']
		return None


def fetch(query):
	results = []
	if 'channel' in query:
		req = request.Request(query)
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
