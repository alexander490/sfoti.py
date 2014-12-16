# from django.core.cache import cache
# from django.db.models.signals import post_save
# from django.contrib.sessions.models import Session
# from django.dispatch import receiver
from django.db import models
from slugify import slugify, Slugify, UniqueSlugify, slugify_unicode


class Artist(models.Model):
    first_name = models.CharField(max_length=140)
    last_name = models.CharField(max_length=140, blank=True)
    biography = models.TextField(blank=True)
    slug = models.SlugField(max_length=140, blank=True, default='')
    favorite_songs = models.ManyToManyField(
        'tracks.Track', blank=True, related_name='is_favorite_of')

    def natural_key(self):
        data = {
            'first_name': self.first_name,
            'last_name': self.last_name,
            'biography': self.biography
        }

        return data

    def __str__(self):
        return self.first_name + ' ' + self.last_name

    def save(self, *args, **kwargs):
        custom_slugify = UniqueSlugify(to_lower=True)
        self.slug = custom_slugify(str(self))
        super(Artist, self).save(*args, **kwargs)


# @receiver(post_save)
# def clear_cache(sender, **kwargs):
#     if sender != Session:
#         cache._cache.flush_all()
