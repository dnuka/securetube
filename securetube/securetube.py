# securetube engine

from urllib import request
import json
from pprint import pprint
from bs4 import BeautifulSoup
import youtube_dl

base = """https://www.youtube.com/results/?search_query={}&disable_polymer=1&hl=en-GB&gl=US"""
pure = """https://www.youtube.{}eos?disable_polymer=1&hl=en-GB&gl=US"""


def proxy():
	api = """https://gimmeproxy.com/api/getProxy?protocol=socks5&anonymityLevel=1&supportsHttps=true&minSpeed=500"""
	req = request.Request(api)
	req.add_header('User-Agent', '234564')
	with request.urlopen(req) as data:
		proxy = json.loads(data.read().decode())
	return proxy


def clean_url(url):
	link = url.strip("https://www.youtube.")
	return pure.format(link)


def get_thumbnail(video_id):
	return 'https://img.youtube.com/vi/{}/mqdefault.jpg'.format(video_id)


def fetch_meta(url):
	link = 'https://www.youtube.com/oembed?url={}&format=json'.format(url)
	req = request.Request(link)
	req.add_header('User-Agent', '36438')
	proxy = proxy()
	req.set_proxy(proxy['ip'] + ':' + proxy['port'], proxy['protocol'])
	with request.urlopen(req) as youtube:
		data = json.loads(youtube.read().decode())
	#pprint(data)
	return data


def watch(url):
	data = proxy()
	proxy = data['protocol'] + '://' + data['ip'] + ':' + data['port']
	ydl = youtube_dl.YoutubeDL(
			{'outtmpl': '%(id)s%(ext)s',
			'proxy': proxy()})
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


def scrape_url(urls):
	videos = []
	for url in urls:
		req = request.Request(url)
		req.add_header('User-Agent', '36400')
		proxy = proxy()
		req.set_proxy(proxy['ip'] + ':' + proxy['port'], proxy['protocol'])
		with request.urlopen(req) as channel:
			raw_data = BeautifulSoup(channel, 'html.parser')
		data = raw_data.findAll('a',attrs={'class':'yt-uix-tile-link'})
		vids = []
		for info in data:
			link = 'https://www.youtube.com' + info['href']
			if not len(vids) == 4:
				vids.append(link)
		videos.extend(vids)
	return videos


def simple_fetch(url):
	pass


def fetch(query):
	results = []
	if 'www.youtube.com' in query:
		req = request.Request(clean_url(query))
		#print(clean_url(query))
	else:
		req = request.Request(base.format(query))
	req.add_header('User-Agent', '36438')
	proxy = proxy()
	req.set_proxy(proxy['ip'] + ':' + proxy['port'], proxy['protocol'])
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
			#print(info['href'])
			temp['thumbnail'] = get_thumbnail(
					info['href'].split('/watch?v=', 1)[1])
			results.append(temp)
	return results
