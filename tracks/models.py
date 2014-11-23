from django.db import models

from albums.models import Album
from artists.models import Artist

class Track(models.Model):
	name = models.CharField(max_length=140)
	order = models.PositiveIntegerField()
	track_file = models.FileField(upload_to='tracks')
	artist = models.ForeignKey(Artist)
	album = models.ForeignKey(Album)
