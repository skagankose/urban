# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('entries', '0012_auto_20150920_1004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='rate_total',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='entry',
            name='rate_up',
            field=models.IntegerField(default=1),
        ),
    ]
