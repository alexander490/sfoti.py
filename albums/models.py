from django.db import models
from sorl.thumbnail import get_thumbnail
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

    def get_cover(self):
        im = get_thumbnail(
            self.cover, '100x100', crop='center', quality=99).url

        return """
        <img src="{img}" alt="{name}">
        """.format(img=im, name=self.name)
    get_cover.allow_tags = True

    def __str__(self):
        return self.name
