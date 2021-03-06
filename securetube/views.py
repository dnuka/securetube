from django.shortcuts import render
from .securetube import fetch, watch, fetch_meta
from feed.models import Channels

def index(request):
    #request.session['proxy'] = anonymous()
    return render(request, 'securetube/index.html')


def results(request):
    if request.method == 'POST':
            query = request.POST.get('query')
            status = request.POST.get('status')
    if 'www.youtube.com' in query:
            query += '/videos'
    #print(query)
    data = fetch(query)
    if status:
            #print(Channels.objects.all())
            channel = Channels(url=query)
            try:
                    search = Channels.objects.get(url=query)
            except Exception as error:
                    print(error)
                    # exception is occured means no mach, just saving is fine. no if
                    channel.save()
    context = {'data': data}
    return render(request, 'securetube/results.html', context)


def play(request):
    if request.method == 'POST':
            url = request.POST.get('url')
    data = watch(url)
    meta = fetch_meta(url)
    context = {'data': data, 'meta': meta}
    return render(request, 'securetube/play.html', context)
