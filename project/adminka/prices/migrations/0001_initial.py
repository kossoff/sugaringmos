# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import adminka.prices.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PricePic',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', models.FileField(null=True, upload_to=adminka.prices.models.get_pricepic_path, blank=True)),
                ('filename', models.CharField(max_length=250, null=True, blank=True)),
                ('size', models.CharField(default='854x601', max_length=10)),
            ],
            options={
                'db_table': 'price_pic',
            },
            bases=(models.Model,),
        ),
    ]
