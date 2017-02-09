from django.db import models

# Create your models here.
class Album(models.Model):
    artist = models.CharField(max_length=250)
    album_title = models.CharField(max_length=100)
    genre = models.CharField(max_length=150)
    album_logo = models.CharField(max_length=1000)

    def __str__(self):
        return self.album_title + ' - ' + self.artist


class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    file_type = models.CharField(max_length=20)
    song_tile = models.CharField(max_length=200)
    is_favorite = models.BooleanField(default=False)

    # string representation of a song

    def __str__(self):
        return self.song_tile


# python manage.py makemigrations nameofproject -> Make changes
# python manage. py migrate -> Apply changes
