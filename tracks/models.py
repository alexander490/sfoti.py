from django.db import models

from albums.models import Album
from artists.models import Artist


class Track(models.Model):
    name = models.CharField(max_length=140)
    order = models.PositiveIntegerField()
    track_file = models.FileField(upload_to='tracks')
    artist = models.ForeignKey(Artist)
    album = models.ForeignKey(Album)

    def get_absolute_url(self):
        return '/tracks/{id}/'.format(id=self.id)

    def player(self):
        return """
		<audio controls>
		  <source src="{track}" type="audio/mpeg">
		Your browser does not support the audio element.
		</audio>
    	""".format(track=self.track_file.url)

    player.allow_tags = True
    player.admin_order_field = 'track_file'

    def __str__(self):
        return self.name
