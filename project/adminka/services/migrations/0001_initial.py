# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import adminka.services.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=250, null=True, blank=True)),
                ('link', models.CharField(max_length=250, null=True, blank=True)),
                ('text', models.TextField(null=True, blank=True)),
                ('has_gallery', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'services',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ServicePic',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', models.FileField(null=True, upload_to=adminka.services.models.get_service_pic_path, blank=True)),
                ('filename', models.CharField(max_length=250, null=True, blank=True)),
                ('size', models.CharField(default='854x601', max_length=10)),
                ('service', models.ForeignKey(to='services.Service')),
            ],
            options={
                'db_table': 'service_pics',
            },
            bases=(models.Model,),
        ),
    ]
