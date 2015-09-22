# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('entries', '0003_subcomment_created_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='subcomment',
            name='down_voters',
            field=models.ManyToManyField(related_name='down_subcomments', blank=True, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='subcomment',
            name='edited',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='subcomment',
            name='rate_down',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='subcomment',
            name='rate_total',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='subcomment',
            name='rate_up',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='subcomment',
            name='up_voters',
            field=models.ManyToManyField(related_name='up_subcomments', blank=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
