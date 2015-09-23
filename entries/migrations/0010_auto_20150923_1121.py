# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('entries', '0009_entry_thumbnail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='thumbnail',
            field=models.ImageField(upload_to='/static/img/', blank=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='avatar',
            field=models.ImageField(upload_to='/static/img/', blank=True),
        ),
    ]
