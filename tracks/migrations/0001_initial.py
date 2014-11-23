# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Track',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=140)),
                ('order', models.PositiveIntegerField()),
                ('track_file', models.FileField(upload_to='tracks')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
