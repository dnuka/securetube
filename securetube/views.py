from django.shortcuts import render
from .securetube import fetch, watch

def index(request):
	return render(request, 'securetube/index.html')


def results(request):
	if request.method == 'POST':
		data = fetch(request.POST.get('query'))
		context = {'data': data}
	return render(request, 'securetube/results.html', context)


def play(request):
	if request.method == 'POST':
		data = watch(request.POST.get('url'))
		context = {'data': data}
	return render(request, 'securetube/play.html', context)
