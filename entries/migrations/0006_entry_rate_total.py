# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('entries', '0005_auto_20150918_0832'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='rate_total',
            field=models.IntegerField(default=0),
        ),
    ]
