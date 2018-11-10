# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-06-27 16:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aSolid_app', '0002_auto_20180627_1508'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='favorites',
        ),
        migrations.AddField(
            model_name='user',
            name='likes',
            field=models.ManyToManyField(default=None, related_name='likes', to='aSolid_app.Quote'),
        ),
    ]