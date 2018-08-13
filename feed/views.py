from django.shortcuts import render

def trending(request):
	return render(request, 'feed/trending.html')


def feed(request):
	return render(request, 'feed/feed.html')
