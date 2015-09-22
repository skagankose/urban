# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('entries', '0004_auto_20150922_1120'),
    ]

    operations = [
        migrations.CreateModel(
            name='Twosubcomment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('text', models.TextField(max_length=200)),
                ('rate_up', models.IntegerField(default=0)),
                ('rate_down', models.IntegerField(default=0)),
                ('rate_total', models.IntegerField(default=0)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('edited', models.BooleanField(default=False)),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('comment', models.ForeignKey(to='entries.Comment')),
                ('down_voters', models.ManyToManyField(related_name='down_twosubcomments', blank=True, to=settings.AUTH_USER_MODEL)),
                ('entry', models.ForeignKey(to='entries.Entry')),
            ],
            options={
                'ordering': ['-rate_total'],
            },
        ),
        migrations.AlterModelOptions(
            name='subcomment',
            options={'ordering': ['-rate_total']},
        ),
        migrations.AddField(
            model_name='twosubcomment',
            name='subcomment',
            field=models.ForeignKey(related_name='twosubcomments', to='entries.Subcomment'),
        ),
        migrations.AddField(
            model_name='twosubcomment',
            name='up_voters',
            field=models.ManyToManyField(related_name='up_twosubcomments', blank=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
