# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('text', models.TextField(max_length=300)),
                ('rate_up', models.IntegerField(default=0)),
                ('rate_down', models.IntegerField(default=0)),
                ('rate_total', models.IntegerField(default=0)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('edited', models.BooleanField(default=False)),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('down_voters', models.ManyToManyField(related_name='down_comments', to=settings.AUTH_USER_MODEL, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=150)),
                ('text', models.TextField()),
                ('rate_up', models.IntegerField(default=0)),
                ('rate_down', models.IntegerField(default=0)),
                ('rate_total', models.IntegerField(default=0)),
                ('views', models.IntegerField(default=0)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('edited', models.BooleanField(default=False)),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('down_voters', models.ManyToManyField(related_name='down_entries', to=settings.AUTH_USER_MODEL, blank=True)),
                ('up_voters', models.ManyToManyField(related_name='up_entries', to=settings.AUTH_USER_MODEL, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Subcomment',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('text', models.TextField(max_length=200)),
                ('updated_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('comment', models.ForeignKey(to='entries.Comment')),
                ('entry', models.ForeignKey(to='entries.Entry')),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('website', models.URLField(blank=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='entry',
            field=models.ForeignKey(to='entries.Entry'),
        ),
        migrations.AddField(
            model_name='comment',
            name='up_voters',
            field=models.ManyToManyField(related_name='up_comments', to=settings.AUTH_USER_MODEL, blank=True),
        ),
    ]
