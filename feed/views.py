from django.shortcuts import render
from .models import Channels
from securetube.securetube import scrape_url, fetch_meta

def trending(request):
	return render(request, 'feed/trending.html')


def feed(request):
	try:
		urls = []
		channels = Channels.objects.all()
		for channel in channels:
			#print(channel.url)
			urls.append(channel.url)
		video_urls = scrape_url(urls) # len of videos should be 4 by 4

	except Exception as error:
		print(error)
	return render(request, 'feed/feed.html')
