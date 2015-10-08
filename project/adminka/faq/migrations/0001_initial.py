# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import adminka.faq.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FAQRecord',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('question', models.CharField(max_length=250)),
                ('answer', models.CharField(max_length=1000)),
                ('image', models.FileField(null=True, upload_to=adminka.faq.models.get_faqpic_path, blank=True)),
                ('filename', models.CharField(max_length=250, null=True, blank=True)),
                ('align_left', models.BooleanField(default=True)),
                ('enabled', models.BooleanField(default=False)),
                ('created', models.DateField(auto_now_add=True)),
                ('changed', models.DateField(auto_now=True)),
                ('position', models.IntegerField(default=0)),
            ],
            options={
                'ordering': ['position'],
                'db_table': 'faq_records',
            },
            bases=(models.Model,),
        ),
    ]
