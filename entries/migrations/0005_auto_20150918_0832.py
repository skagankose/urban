# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('entries', '0004_auto_20150918_0820'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='down_voters',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL, related_name='down_entries', blank=True),
        ),
        migrations.AlterField(
            model_name='entry',
            name='up_voters',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL, related_name='up_entries', blank=True),
        ),
    ]
