# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0003_auto_20150425_2109'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='body',
            field=models.CharField(default='body', max_length=1000),
            preserve_default=True,
        ),
    ]
