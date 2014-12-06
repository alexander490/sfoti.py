from django.db import models
from django.core.cache import cache
from django.db.models.signals import post_save
from django.contrib.sessions.models import Session

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


# @receiver(post_save)
# def clear_cache(sender, **kwargs):
#     if sender != Session:
#         cache._cache.flush_all()