# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('artists', '0003_auto_20141130_0139'),
    ]

    operations = [
        migrations.AddField(
            model_name='artist',
            name='slug',
            field=models.SlugField(max_length=140, blank=True, default=''),
            preserve_default=True,
        ),
    ]
