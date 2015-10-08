# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import adminka.sugarwaxing.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PageType1',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.TextField()),
                ('section', models.CharField(default='default', max_length=20)),
                ('image', models.FileField(null=True, upload_to=adminka.sugarwaxing.models.get_pagetype1pic_path, blank=True)),
                ('filename', models.CharField(max_length=250, null=True, blank=True)),
            ],
            options={
                'db_table': 'pages_type_1',
            },
            bases=(models.Model,),
        ),
    ]
