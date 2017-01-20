from django.http import HttpResponse

#homepage
def index(request):
    return HttpResponse("<h1>Music Home Page</h1>")

