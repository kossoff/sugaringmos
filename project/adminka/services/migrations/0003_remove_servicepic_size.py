# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0002_service_enabled'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='servicepic',
            name='size',
        ),
    ]
