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
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
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
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
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
                ('thumbnail', models.ImageField(upload_to='img/', blank=True)),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('down_voters', models.ManyToManyField(related_name='down_entries', to=settings.AUTH_USER_MODEL, blank=True)),
                ('up_voters', models.ManyToManyField(related_name='up_entries', to=settings.AUTH_USER_MODEL, blank=True)),
            ],
            options={
                'ordering': ['-rate_total'],
            },
        ),
        migrations.CreateModel(
            name='Subcomment',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('text', models.TextField(max_length=200)),
                ('rate_up', models.IntegerField(default=0)),
                ('rate_down', models.IntegerField(default=0)),
                ('rate_total', models.IntegerField(default=0)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('edited', models.BooleanField(default=False)),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('comment', models.ForeignKey(related_name='subcomments', to='entries.Comment')),
                ('down_voters', models.ManyToManyField(related_name='down_subcomments', to=settings.AUTH_USER_MODEL, blank=True)),
                ('entry', models.ForeignKey(to='entries.Entry')),
                ('up_voters', models.ManyToManyField(related_name='up_subcomments', to=settings.AUTH_USER_MODEL, blank=True)),
            ],
            options={
                'ordering': ['-rate_total'],
            },
        ),
        migrations.CreateModel(
            name='Twosubcomment',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('text', models.TextField(max_length=200)),
                ('rate_up', models.IntegerField(default=0)),
                ('rate_down', models.IntegerField(default=0)),
                ('rate_total', models.IntegerField(default=0)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('edited', models.BooleanField(default=False)),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('comment', models.ForeignKey(to='entries.Comment')),
                ('down_voters', models.ManyToManyField(related_name='down_twosubcomments', to=settings.AUTH_USER_MODEL, blank=True)),
                ('entry', models.ForeignKey(to='entries.Entry')),
                ('subcomment', models.ForeignKey(related_name='twosubcomments', to='entries.Subcomment')),
                ('up_voters', models.ManyToManyField(related_name='up_twosubcomments', to=settings.AUTH_USER_MODEL, blank=True)),
            ],
            options={
                'ordering': ['-rate_total'],
            },
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('website', models.URLField(blank=True)),
                ('avatar', models.ImageField(upload_to='img/', blank=True)),
                ('user', models.OneToOneField(related_name='user_profile', to=settings.AUTH_USER_MODEL)),
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
