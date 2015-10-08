# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='name',
            field=models.CharField(default='name', max_length=10),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='contact',
            name='body',
            field=models.CharField(default='body', max_length=100),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='contact',
            name='code',
            field=models.CharField(default='code', max_length=10),
            preserve_default=True,
        ),
    ]
