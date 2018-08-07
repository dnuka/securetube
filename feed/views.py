from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	return render(request, 'securetube/index.html')

def results(request):
	return HttpResponse('results')
