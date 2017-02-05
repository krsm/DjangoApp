# to raise 404 HTTP Error
from django.http import Http404

# from django.http import HttpResponse # replaced by render
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
   # query database to verify id
    try:
        # pk is primary key, it could be id
        album = Album.objects.get(pk=album_id)
    except Album.DoesNotExist:
        raise Http404("Album does not exist")
    return render(request, 'music/detail.html', {'album': album})

