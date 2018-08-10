from django.shortcuts import render
from .securetube import fetch, watch, fetch_meta

def index(request):
	return render(request, 'securetube/index.html')


def results(request):
	if request.method == 'POST':
		query = request.POST.get('query')
	if 'channel' in query:
		data = fetch(query + '/videos')
	data = fetch(query)
	context = {'data': data}
	return render(request, 'securetube/results.html', context)


def play(request):
	if request.method == 'POST':
		url = request.POST.get('url')
	data = watch(url)
	meta = fetch_meta(url)
	context = {'data': data, 'meta': meta}
	return render(request, 'securetube/play.html', context)
