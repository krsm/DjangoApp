from django.http import HttpResponse

#homepage
def index(request):
    return HttpResponse("<h1>Music Home Page</h1>")

def detail(request, album_id):
    return HttpResponse('<h2>Details for Album id: '+ str(album_id)+'</h2>')


                        )
