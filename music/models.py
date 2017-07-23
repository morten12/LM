from django.db import models

class Album(models.Model):
    artist = models.CharField(max_length=250)
    album_title = models.CharField(max_length=500)
    genre = models.CharField(max_length=100)
    album_logo = models.CharField(max_length=1000)

    def __str__(self):
        return self.album_title +' - '+ self.artist

class Song(models.Model):
    # This Song will be linked to the Album with pk 1,2,3 and so on.
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    file_type = models.CharField(max_length=10)
    song_title = models.CharField(max_length=250)
    # When the user press it, it will become True. The favorite one.
    is_favorite = models.BooleanField(default=False)

    def __str__(self):
        return self.song_title

