# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('symbolsapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Symbols',
            new_name='Symbol',
        ),
    ]
