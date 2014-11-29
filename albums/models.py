from django.db import models

from artists.models import Artist


class Album(models.Model):
    name = models.CharField(max_length=140)
    cover = models.ImageField(upload_to='albums')
    artist = models.ForeignKey(Artist)

    def natural_key(self):
        data = {
            'name': self.name,
            'cover': self.cover.url
        }

        return data

    def __str__(self):
        return self.name
