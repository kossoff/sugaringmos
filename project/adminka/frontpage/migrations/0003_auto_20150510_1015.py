# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import adminka.frontpage.models


class Migration(migrations.Migration):

    dependencies = [
        ('frontpage', '0002_auto_20150510_0407'),
    ]

    operations = [
        migrations.AlterField(
            model_name='frontpageadvert',
            name='image',
            field=models.FileField(null=True, upload_to=adminka.frontpage.models.get_advert_path, blank=True),
            preserve_default=True,
        ),
    ]
