from django.db import models


class Artist(models.Model):
    first_name = models.CharField(max_length=140)
    last_name = models.CharField(max_length=140, blank=True)
    biography = models.TextField(blank=True)
    favorite_songs = models.ManyToManyField('tracks.Track', blank=True, related_name='is_favorite_of')

    def natural_key(self):
        data = {
            'first_name': self.first_name,
            'last_name': self.last_name,
            'biography': self.biography
        }

        return data

    def __str__(self):
        return self.first_name + ' ' + self.last_name
