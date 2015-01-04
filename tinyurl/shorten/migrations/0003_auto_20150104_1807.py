# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shorten', '0002_wordbank'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wordbank',
            name='word',
            field=models.CharField(unique=True, max_length=200),
            preserve_default=True,
        ),
    ]
