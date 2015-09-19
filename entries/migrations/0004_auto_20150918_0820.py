# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('entries', '0003_entry_voters'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entry',
            name='voters',
        ),
        migrations.AddField(
            model_name='entry',
            name='down_voters',
            field=models.ManyToManyField(related_name='down_entries', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='entry',
            name='up_voters',
            field=models.ManyToManyField(related_name='up_entries', to=settings.AUTH_USER_MODEL),
        ),
    ]
