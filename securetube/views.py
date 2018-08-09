from django.shortcuts import render
from .securetube import fetch

def index(request):
	return render(request, 'securetube/index.html')


def results(request):
	if request.method == 'POST':
		data = fetch(request.POST.get('query'))
		context = {'data': data}
	return render(request, 'securetube/results.html', context)
