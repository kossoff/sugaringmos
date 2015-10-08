# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('faq', '0002_auto_20150420_0002'),
    ]

    operations = [
        migrations.AddField(
            model_name='faqrecord',
            name='resolution',
            field=models.CharField(default='170x120', max_length=10),
            preserve_default=True,
        ),
    ]
