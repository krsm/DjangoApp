# to raise 404 HTTP Error
# from django.http import Http404 # It will be used a shortcut instead of it

# from django.http import HttpResponse # replaced by render
# # to work with templates
# from django.template import loader
# to combine load and render template
from django.shortcuts import render
from django.shortcuts import get_object_or_404

from .models import Album, Song


# homepage
def index(request):
    # connect to database and parse data
    all_albums = Album.objects.all()
    context = {'all_albums': all_albums}
    return render(request, 'music/index.html', context)


# details view
def detail(request, album_id):
    # query database to verify id
    #  try:
    #      # pk is primary key, it could be id
    #      album = Album.objects.get(pk=album_id)
    #  except Album.DoesNotExist:
    #      raise Http404("Album does not exist")
    album = get_object_or_404(Album, pk=album_id)  # replace try, except statement

    return render(request, 'music/detail.html', {'album': album})


# favorite
def favorite(request, album_id):
    album = get_object_or_404(Album, pk=album_id)  # replace try, except statement
    try:
        select_song = album.song_set.get(pk=request.POST['song'])
    except (KeyError, Song.DoesNotExist):
        return render(request, 'music/detail.html', {

            'album': album,
            'error_message': 'You did not select a valid song',
        })
    else:
        select_song.is_favorite = True
        select_song.save()  # to save changes to database
        return render(request, 'music/detail.html', {'album': album})