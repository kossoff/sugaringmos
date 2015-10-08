# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import adminka.frontpage.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FrontpageAdvert',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=30)),
                ('link', models.CharField(max_length=250)),
                ('text', models.CharField(max_length=250)),
                ('image', models.FileField(null=True, upload_to=adminka.frontpage.models.get_slide_path, blank=True)),
                ('filename', models.CharField(max_length=250, null=True, blank=True)),
                ('enabled', models.BooleanField(default=False)),
                ('created', models.DateField(auto_now_add=True)),
                ('changed', models.DateField(auto_now=True)),
                ('position', models.IntegerField(default=0)),
            ],
            options={
                'ordering': ['position'],
                'db_table': 'frontpage_advert',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='FrontpageBanner',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', models.FileField(null=True, upload_to=adminka.frontpage.models.get_banner_path, blank=True)),
                ('filename', models.CharField(max_length=250, null=True, blank=True)),
                ('created', models.DateField(auto_now_add=True)),
                ('changed', models.DateField(auto_now=True)),
            ],
            options={
                'db_table': 'frontpage_banners',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='FrontpageSlide',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=20)),
                ('image', models.FileField(null=True, upload_to=adminka.frontpage.models.get_slide_path, blank=True)),
                ('filename', models.CharField(max_length=250, null=True, blank=True)),
                ('enabled', models.BooleanField(default=False)),
                ('created', models.DateField(auto_now_add=True)),
                ('changed', models.DateField(auto_now=True)),
                ('position', models.IntegerField(default=0)),
            ],
            options={
                'ordering': ['position'],
                'db_table': 'frontpage_slides',
            },
            bases=(models.Model,),
        ),
    ]
