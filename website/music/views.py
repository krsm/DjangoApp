from django.http import HttpResponse
# to work with templates
from django.templates import loader

from .models import Album


#homepage
def index(request):
    # connect to datbase and parse data
    all_albums = Album.objects.all()
    template = loader.get_template('music/index.html')
    context = {
            'all_albums': all_albums,
    }
    return HttpResponse(template.render(context, request))

# details view
def detail(request, album_id):
    return HttpResponse('<h2>Details for Album id: '+ str(album_id)+'</h2>')
