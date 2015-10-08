# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0003_remove_servicepic_size'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicepic',
            name='position',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
