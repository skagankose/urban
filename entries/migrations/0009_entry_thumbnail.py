# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('entries', '0008_auto_20150922_1846'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='thumbnail',
            field=models.ImageField(upload_to='entries/static/img/', blank=True),
        ),
    ]
