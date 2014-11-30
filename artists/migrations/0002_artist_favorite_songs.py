# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tracks', '0002_auto_20141123_0336'),
        ('artists', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='artist',
            name='favorite_songs',
            field=models.ManyToManyField(related_name='is_favorite_to', blank=True, to='tracks.Track'),
            preserve_default=True,
        ),
    ]
