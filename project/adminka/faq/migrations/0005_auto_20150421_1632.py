# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('faq', '0004_auto_20150421_1432'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faqrecord',
            name='changed',
            field=models.DateTimeField(auto_now=True, auto_now_add=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='faqrecord',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
            preserve_default=True,
        ),
    ]
