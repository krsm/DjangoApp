"""website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from .import views

# variable to store app name - related to namespace

app_name = 'music'  # has to receive the name of app

# regular expression
# start with ^
# ends with $
urlpatterns = [
    # route related music
    url(r'^$', views.index, name='index'),

    # /music/<alum_id>/
    # /music/71/
    # () to create a group, to see 71 as a group, for instance
    url(r'^(?P<album_id>[0-9]+)/$', views.detail, name='detail'),

    # /music/<alum_id>/favorite
    url(r'^(?P<album_id>[0-9]+)/favorite/$', views.favorite, name='favorite'),

]
