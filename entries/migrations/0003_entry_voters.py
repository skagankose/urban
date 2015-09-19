# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('entries', '0002_auto_20150918_0813'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='voters',
            field=models.ManyToManyField(related_name='liked_stories', to=settings.AUTH_USER_MODEL),
        ),
    ]
