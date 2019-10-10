from django.db import models


# Create your models here.
class Album(models.Model):
    artist = models.CharField(max_length=250)
    album_title = models.CharField(max_length=500)
    genre = models.CharField(max_length=100)
    album_logo = models.CharField(max_length=1000)

    def __str__(self):  #This method returns the string representation of the object. This method is called when print() or str() function is invoked on an object. This method must return the String object. If we don't implement __str__() function for a class, then built-in object implementation is used that actually calls __repr__() function.
        return self.album_title + "-" + self.artist


class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    file_type = models.CharField(max_length=10)
    song_title = models.CharField(max_length=250)

    def __str__(self):  #This method returns the string representation of the object. This method is called when print() or str() function is invoked on an object. This method must return the String object. If we don't implement __str__() function for a class, then built-in object implementation is used that actually calls __repr__() function.
        return self.song_title

