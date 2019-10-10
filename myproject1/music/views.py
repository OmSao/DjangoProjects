#from django.shortcuts import render
from django.http import Http404
from .models import Album
from django.template import loader
from django.shortcuts import  render
# Create your views here.

from django.http import HttpResponse

'''
def index(request):
    return HttpResponse("<h1>This is Music app homepage. Awesome !!. </h1>")
'''


def index(request):
    all_albums = Album.objects.all()
    template = loader.get_template('music/index.html')
    context = {'all_albums': all_albums}
    '''
    html = ''
    for album in all_albums:
        #url = '/music/555'
        url = '/music/' + str(album.id)+''
        html += '<a href="'+url+'">' + album.album_title + '</a><br>'
    '''
    return render(request, 'music/index.html', context)
    #return HttpResponse(template.render(context, request))
    #return HttpResponse(html)


def detail(request, album_id):
    #return HttpResponse("<h2>Details for the Album id: "+str(album_id)+"</h2>")
    try:
        album = Album.objects.get(pk=album_id)
    except Album.DoesNotExist:
        raise Http404("404 Error: Album doesn't exist.[Om Sao]")
    return render(request, 'music/detail.html', {'album': album})
