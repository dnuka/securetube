from django.shortcuts import render

def trending(request):
	return render(request, 'feed/trending.html')


def library(request):
	return render(request, 'feed/home.html')
