# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('albums', '0001_initial'),
        ('artists', '0001_initial'),
        ('tracks', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='track',
            name='album',
            field=models.ForeignKey(to='albums.Album', default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='track',
            name='artist',
            field=models.ForeignKey(to='artists.Artist', default=1),
            preserve_default=False,
        ),
    ]
