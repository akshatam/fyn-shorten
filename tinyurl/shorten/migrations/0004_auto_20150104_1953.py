# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shorten', '0003_auto_20150104_1807'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='generatedurl',
            name='id',
        ),
        migrations.AlterField(
            model_name='generatedurl',
            name='generated_alias',
            field=models.OneToOneField(primary_key=True, serialize=False, to='shorten.WordBank'),
            preserve_default=True,
        ),
    ]
