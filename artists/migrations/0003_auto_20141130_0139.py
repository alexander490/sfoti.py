# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('artists', '0002_artist_favorite_songs'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artist',
            name='favorite_songs',
            field=models.ManyToManyField(related_name='is_favorite_of', blank=True, to='tracks.Track'),
            preserve_default=True,
        ),
    ]
