from django.contrib import admin

# Register your models here.

from .models import Album, Song

# registering the class Album to be edited by Admin
admin.site.register(Album)
