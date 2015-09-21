# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('entries', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subcomment',
            name='comment',
            field=models.ForeignKey(to='entries.Comment', related_name='subcomments'),
        ),
    ]
