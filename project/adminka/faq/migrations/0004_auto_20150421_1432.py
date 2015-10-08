# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('faq', '0003_faqrecord_resolution'),
    ]

    operations = [
        migrations.RenameField(
            model_name='faqrecord',
            old_name='resolution',
            new_name='size',
        ),
    ]
