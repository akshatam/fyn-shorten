# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shorten', '0004_auto_20150104_1953'),
    ]

    operations = [
        migrations.AddField(
            model_name='wordbank',
            name='taken',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
