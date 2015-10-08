# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('faq', '0005_auto_20150421_1632'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faqrecord',
            name='changed',
            field=models.DateTimeField(auto_now=True),
            preserve_default=True,
        ),
    ]
