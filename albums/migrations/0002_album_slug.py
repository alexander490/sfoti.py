# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('albums', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='slug',
            field=models.SlugField(max_length=140, blank=True, default=''),
            preserve_default=True,
        ),
    ]
