from django.http import HttpResponse
# # to work with templates
# from django.template import loader
# to combine load and render template
from django.shortcuts import render

from .models import Album


# homepage
def index(request):
    # connect to database and parse data
    all_albums = Album.objects.all()
    context = {'all_albums': all_albums}
    return render(request, 'music/index.html', context)


# details view
def detail(request, album_id):
    return HttpResponse('<h2>Details for Album id: ' + str(album_id) + '</h2>')
