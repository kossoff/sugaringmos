# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0004_servicepic_position'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='servicepic',
            options={'ordering': ['position']},
        ),
    ]
