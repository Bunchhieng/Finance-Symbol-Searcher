# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('symbolsapp', '0002_auto_20150513_1309'),
    ]

    operations = [
        migrations.AlterField(
            model_name='symbol',
            name='symbol',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='symbol',
            name='ticker',
            field=models.CharField(max_length=100),
        ),
    ]
